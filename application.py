import os
from book import Book
from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import *
from flask import render_template

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

db.init_app(app)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return "Project 1: TODO"
    # books = Book.query.all()
    # return render_template("index.html", books=books)

@app.route("/books")
def books():
    """List all books."""
    books=Book.query.all()
    return render_template("books.html", books=books)

@app.route("/login")
def login():
    """login in the web page."""

    return render_template("login.html")

@app.route("/books/<int:ISBN>")
def book(ISBN):
    """List details about a book."""

    # Make sure book exists.
    book = Book.query.get(ISBN)
    if book is None:
        return render_template("error.html", message="No such flight.")

