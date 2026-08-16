from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.dependencies import get_current_user
from backend.models import Post, User
from backend.schemas import PostCreate, PostUpdate

router = APIRouter(prefix="/api/posts", tags=["posts"])


def serialize(post: Post) -> dict:
    return {
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "author": post.author.username,
        "author_id": post.user_id,
        "created_at": post.created_at,
        "updated_at": post.updated_at,
    }


@router.get("")
def list_posts(db: Session = Depends(get_db)):
    posts = db.query(Post).order_by(Post.id.desc()).all()
    return [serialize(post) for post in posts]


@router.get("/{post_id}")
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return serialize(post)


@router.post("", status_code=201)
def create_post(
    payload: PostCreate,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    post = Post(user_id=user.id, title=payload.title.strip(), content=payload.content.strip())
    db.add(post)
    db.commit()
    db.refresh(post)
    return serialize(post)


def owned_post(db: Session, user_id: int, post_id: int) -> Post:
    post = db.query(Post).filter(Post.id == post_id).first()
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    if post.user_id != user_id:
        raise HTTPException(status_code=403, detail="Only the author may modify this post")
    return post


@router.put("/{post_id}")
def update_post(
    post_id: int,
    payload: PostUpdate,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    post = owned_post(db, user.id, post_id)
    post.title = payload.title.strip()
    post.content = payload.content.strip()
    db.commit()
    db.refresh(post)
    return serialize(post)


@router.delete("/{post_id}", status_code=204)
def delete_post(
    post_id: int,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    post = owned_post(db, user.id, post_id)
    db.delete(post)
    db.commit()
    return Response(status_code=204)
