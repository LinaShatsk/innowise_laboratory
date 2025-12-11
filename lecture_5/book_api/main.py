from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel, ConfigDict
from typing import Optional, List

SQLALCHEMY_DATABASE_URL = "sqlite:///./books.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class BookDB(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=True)


Base.metadata.create_all(bind=engine)


class BookCreate(BaseModel):
    title: str
    author: str
    year: Optional[int] = None


class BookResponse(BookCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI(title="Book Collection API")


@app.post("/books/", response_model=BookResponse, status_code=201)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    """Add a new book"""
    db_book = BookDB(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


@app.get("/books/", response_model=List[BookResponse])
def get_all_books(db: Session = Depends(get_db)):
    """Get all books"""
    books = db.query(BookDB).all()
    return books


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """Delete a book by ID"""
    book = db.query(BookDB).filter(BookDB.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="The book was not founded")

    db.delete(book)
    db.commit()
    return None


@app.put("/books/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book_update: BookCreate, db: Session = Depends(get_db)):
    """Update book details"""
    book = db.query(BookDB).filter(BookDB.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="The book was not founded")

    for field, value in book_update.model_dump().items():
        setattr(book, field, value)

    db.commit()
    db.refresh(book)
    return book


@app.get("/books/search/", response_model=List[BookResponse])
def search_books(
    title: Optional[str] = Query(None),
    author: Optional[str] = Query(None),
    year: Optional[int] = Query(None),
    db: Session = Depends(get_db)
):
    """Search books by title, author, or year"""
    query = db.query(BookDB)

    if title:
        query = query.filter(BookDB.title.contains(title))
    if author:
        query = query.filter(BookDB.author.contains(author))
    if year:
        query = query.filter(BookDB.year == year)

    books = query.all()
    return books


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080, reload=True)
