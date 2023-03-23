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

@books_blueprint.route("/books/<id>")
def show_id(id):
    book = book_repositories.select(id)
    return render_template("books/show.html", solo_book = book)

@books_blueprint.route('/books/<id>/delete', methods=['POST'])
def delete_task(id):
    book_repositories.delete(id)
    return(redirect('/books'))

@books_blueprint.route("/books/new")
def new_book():
    author = author_repositories.select_all()
    return render_template("/books/new.html",  all_authors = author )

@books_blueprint.route("/books", methods=['POST'])
def create_book():
    title = request.form['title']
    genre = request.form['genre']
    author_id = request.form['author_id']
    author = author_repositories.select(author_id)
    book = Book(title, genre, author)
    book_repositories.save(book)
    return redirect('/books')