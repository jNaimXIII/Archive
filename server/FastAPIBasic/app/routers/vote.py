from fastapi import status, Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from .. import schemas, oauth2, models
from ..database import get_db

router = APIRouter(
    prefix="/vote",
    tags=["Vote"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_vote(
        vote: schemas.VoteCreate,
        db: Session = Depends(get_db),
        current_user: models.User = Depends(oauth2.get_current_user)
):
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post {vote.post_id} not found")

    vote_query = db.query(models.Vote) \
        .filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)

    vote_result = vote_query.first()

    if vote_result:
        vote_query.delete()

        message = "vote removed"
    else:
        created_vote = models.Vote(user_id=current_user.id, post_id=vote.post_id)
        db.add(created_vote)

        message = "vote added"

    db.commit()

    return {"message": message}
