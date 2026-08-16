from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models import AuthToken, User
from backend.security import hash_token

bearer = HTTPBearer(auto_error=False)


def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer),
    db: Session = Depends(get_db),
) -> User:
    if credentials is None or credentials.scheme.lower() != "bearer":
        raise HTTPException(status_code=401, detail="Authentication required")

    token_hash = hash_token(credentials.credentials)
    token_row = db.query(AuthToken).filter(AuthToken.token_hash == token_hash).first()
    if token_row is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    return token_row.user
