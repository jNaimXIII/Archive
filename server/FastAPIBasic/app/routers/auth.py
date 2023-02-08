from fastapi import APIRouter, Depends, status, HTTPException
# from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import models
from .. import oauth2
from .. import schemas
from .. import utils
from ..database import get_db

router = APIRouter(
    tags=["Authentication"],
    prefix="/auth"
)


# def login(credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
@router.post("/login", status_code=status.HTTP_200_OK, response_model=schemas.AuthResponse)
def login(credentials: schemas.AuthLogin, db: Session = Depends(get_db)):
    # user = db.query(models.User).filter(models.User.email == credentials.username).first()
    user = db.query(models.User).filter(models.User.email == credentials.email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="invalid credentials")

    valid_password = utils.verify_hash_password(credentials.password, user.password)

    if not valid_password:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="invalid credentials")

    access_token = oauth2.create_access_token(data={"user_id": user.id})

    return {"access_token": access_token}
