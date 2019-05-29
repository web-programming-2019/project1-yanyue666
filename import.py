import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from book import Book
from flask import Flask, render_template, request
from models import *

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))
# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db.init_app(app)

def main():
    f = open("books.csv")
    reader = csv.reader(f)
    for ISBN, title, author, year in reader:
        db.execute("INSERT INTO Book(title,author,year,ISBN) VALUES (:title, :author, :year,:ISBN)",
                   {"title": title, "author": author, "year": year,"ISBN": ISBN})
    #     book = Book(title=title, author= author, year= year,ISBN= ISBN)
    #     db.session.add(book)#将CSV数据全部写入数据库
    # db.session.commit()
    db.commit()

if __name__ == "__main__":
    main()

