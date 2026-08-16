from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.ai_client import AIClientError, generate_reply
from backend.database import get_db
from backend.dependencies import get_current_user
from backend.models import ChatSession, Message, User
from backend.schemas import ChatSessionCreate, MessageCreate

router = APIRouter(prefix="/api/chat", tags=["chat"])


def owned_session(db: Session, user_id: int, session_id: int) -> ChatSession:
    session = (
        db.query(ChatSession)
        .filter(ChatSession.id == session_id, ChatSession.user_id == user_id)
        .first()
    )
    if session is None:
        # 404 avoids exposing whether another user's session exists.
        raise HTTPException(status_code=404, detail="Chat session not found")
    return session


@router.get("/sessions")
def list_sessions(user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    rows = (
        db.query(ChatSession)
        .filter(ChatSession.user_id == user.id)
        .order_by(ChatSession.id.desc())
        .all()
    )
    return [{"id": row.id, "title": row.title, "created_at": row.created_at} for row in rows]


@router.post("/sessions", status_code=201)
def create_session(
    payload: ChatSessionCreate,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    row = ChatSession(user_id=user.id, title=payload.title.strip())
    db.add(row)
    db.commit()
    db.refresh(row)
    return {"id": row.id, "title": row.title, "created_at": row.created_at}


@router.get("/sessions/{session_id}/messages")
def list_messages(
    session_id: int,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    session = owned_session(db, user.id, session_id)
    return [
        {"id": msg.id, "role": msg.role, "content": msg.content, "created_at": msg.created_at}
        for msg in session.messages
    ]


@router.post("/sessions/{session_id}/messages", status_code=201)
def send_message(
    session_id: int,
    payload: MessageCreate,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    session = owned_session(db, user.id, session_id)
    user_message = Message(session_id=session.id, role="user", content=payload.content.strip())
    db.add(user_message)
    db.commit()

    recent = (
        db.query(Message)
        .filter(Message.session_id == session.id)
        .order_by(Message.id.desc())
        .limit(12)
        .all()
    )
    prompt_messages = [
        {"role": msg.role, "content": msg.content}
        for msg in reversed(recent)
    ]

    try:
        answer = generate_reply(prompt_messages)
    except AIClientError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc

    ai_message = Message(session_id=session.id, role="assistant", content=answer)
    db.add(ai_message)
    db.commit()
    db.refresh(ai_message)
    return {"id": ai_message.id, "role": ai_message.role, "content": ai_message.content}
