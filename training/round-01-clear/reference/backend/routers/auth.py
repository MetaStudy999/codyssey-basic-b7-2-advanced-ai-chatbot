from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.dependencies import bearer, get_current_user
from backend.models import AuthToken, User
from backend.schemas import LoginIn, SignupIn, TokenOut
from backend.security import hash_password, hash_token, new_access_token, verify_password

router = APIRouter(prefix="/api/auth", tags=["auth"])


def issue_token(db: Session, user: User) -> str:
    raw = new_access_token()
    db.add(AuthToken(user_id=user.id, token_hash=hash_token(raw)))
    db.commit()
    return raw


@router.post("/signup", status_code=201)
def signup(payload: SignupIn, db: Session = Depends(get_db)):
    email = payload.email.strip().lower()
    username = payload.username.strip()
    if "@" not in email:
        raise HTTPException(status_code=422, detail="Valid email is required")
    if db.query(User).filter(User.email == email).first():
        raise HTTPException(status_code=409, detail="Email already exists")
    if db.query(User).filter(User.username == username).first():
        raise HTTPException(status_code=409, detail="Username already exists")

    user = User(email=email, username=username, password_hash=hash_password(payload.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"id": user.id, "email": user.email, "username": user.username}


@router.post("/login", response_model=TokenOut)
def login(payload: LoginIn, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email.strip().lower()).first()
    if user is None or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return TokenOut(access_token=issue_token(db, user))


@router.post("/logout", status_code=204)
def logout(
    user: User = Depends(get_current_user),
    credentials=Depends(bearer),
    db: Session = Depends(get_db),
):
    token_hash = hash_token(credentials.credentials)
    row = db.query(AuthToken).filter(AuthToken.user_id == user.id, AuthToken.token_hash == token_hash).first()
    if row is not None:
        db.delete(row)
        db.commit()
    return None


@router.get("/me")
def me(user: User = Depends(get_current_user)):
    return {"id": user.id, "email": user.email, "username": user.username}
