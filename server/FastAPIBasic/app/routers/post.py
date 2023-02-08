from typing import List, Optional

from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session

from .. import models, schemas, oauth2
from ..database import get_db

# from sqlalchemy import func

# from fastapi.params import Body

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


@router.get("/", response_model=List[schemas.PostResponse])
def get_posts(
        db: Session = Depends(get_db),
        current_user: models.User = Depends(oauth2.get_current_user),
        limit: int = 10,
        offset: int = 0,
        search: Optional[str] = ""
):
    # cursor.execute(""" SELECT * FROM posts """)
    # conn.commit()
    # posts = cursor.fetchall()

    # authored posts
    # posts = db.query(models.Post).filter(models.Post.author_id == current_user.id).all()

    posts = db.query(models.Post) \
        .filter(models.Post.title.contains(search)) \
        .limit(limit) \
        .offset(offset) \
        .all()

    # performing joins on sqlalchemy creates nested data, raw query does not
    #
    # SELECT posts.*, COUNT(votes.post_id) AS votes
    # FROM posts
    # LEFT JOIN votes ON posts.id = votes.post_id
    # GROUP BY posts.id;
    #
    # db.query(models.Post, func.count(models.Vote.post_id).label("votes")) \
    #     .join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True) \
    #     .group_by(models.Post.id) \
    #     .filter(models.Post.title.contains(search)) \
    #     .limit(limit) \
    #     .offset(offset) \
    #     .all()

    return posts


# def create_post(payload: dict = Body(...)):
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def create_post(
        post: schemas.PostCreate,
        db: Session = Depends(get_db),
        current_user: models.User = Depends(oauth2.get_current_user)
):
    # cursor.execute(
    #     """ INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,
    #     (post.title, post.content, post.published,)
    # )
    # conn.commit()
    #
    # created_post = cursor.fetchone()

    # created_post = models.Post(title=post.title, content=post.content, published=post.published)

    # NOTE: **post.dict() is the same as title=post.title, content=post.content, published=post.published
    created_post = models.Post(author_id=current_user.id, **post.dict())

    db.add(created_post)
    db.commit()

    db.refresh(created_post)

    return created_post


def find_post_query(post_id, db: Session = Depends(get_db)):
    return db.query(models.Post).filter(models.Post.id == post_id)


def find_post(post_id, db: Session = Depends(get_db)):
    # cursor.execute(
    #     """ SELECT * from posts WHERE id = %s """,
    #     (str(post_id),)
    # )
    # conn.commit()
    #
    # return cursor.fetchone()

    return db.query(models.Post).filter(models.Post.id == post_id).first()


@router.get("/latest", response_model=schemas.PostResponse)
def get_recent_post(db: Session = Depends(get_db)):
    # cursor.execute(""" SELECT * from posts ORDER BY created_at DESC """)
    # conn.commit()
    #
    # post = cursor.fetchone()
    # return {"data": post}

    post = db.query(models.Post).order_by(models.Post.created_at.desc()).first()

    return post


@router.get("/{post_id}", response_model=schemas.PostResponse)
def get_post(
        post_id: int,
        response: Response,
        db: Session = Depends(get_db),
        current_user: models.User = Depends(oauth2.get_current_user)
):
    # authored post
    # post = db.query(models.Post).filter(models.Post.author_id == current_user.id).first()

    post = find_post(post_id, db)

    if not post:
        # response.status_code = status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post {post_id} not found")

    return post


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(
        post_id: int,
        db: Session = Depends(get_db),
        current_user: models.User = Depends(oauth2.get_current_user)
):
    # cursor.execute(
    #     """ DELETE FROM posts WHERE id = %s RETURNING * """,
    #     (str(post_id),)
    # )
    # conn.commit()
    #
    # deleted_post = cursor.fetchone()

    delete_query = find_post_query(post_id, db)

    post = delete_query.first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post {post_id} not found")

    if not post.author_id == current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"cannot delete post {post_id}")

    delete_query.delete()

    db.commit()


@router.put("/{post_id}", response_model=schemas.PostResponse)
def update_post(
        post_id: int,
        post: schemas.PostUpdate,
        db: Session = Depends(get_db),
        current_user: models.User = Depends(oauth2.get_current_user)
):
    # cursor.execute(
    #     """ UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """,
    #     (post.title, post.content, post.published, post_id,)
    # )
    # conn.commit()
    #
    # updated_post = cursor.fetchone()

    update_query = find_post_query(post_id, db)

    db_post = update_query.first()

    if not db_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post {post_id} not found")

    if not db_post.author_id == current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"cannot delete post {post_id}")

    update_query.update(post.dict())

    db.commit()

    updated_post = update_query.first()

    return updated_post
