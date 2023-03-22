from flask import Flask, render_template, request, redirect
from repositories import author_repositories
from repositories import book_repositories
from models.book import Book

from flask import Blueprint

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def books():
    books = book_repositories.select_all() 
    return render_template("books/index.html", all_books = books)

@books_blueprint.route('/books/<id>')
def show_id(id):
    book = book_repositories.select(id)
    return render_template('books/show.html', solo_book = book)