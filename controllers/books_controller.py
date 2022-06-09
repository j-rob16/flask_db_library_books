from flask import Flask, redirect, render_template, request
from repositories import book_repository, author_repository
from models.book import Book

from flask import Blueprint

books_blueprint = Blueprint("tasks", __name__)

# INDEX
# GET '/books'
@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books=books)

# NEW
# GET '/books/new'
@books_blueprint.route('/books/new', methods=['GET'])
def new_book():
    authors = author_repository.select_all()
    return render_template('books/new.html', all_authors=authors)

# CREATE
# POST '/books'
@books_blueprint.route('/books', methods=['POST'])
def create_book():
    title = request.form['title']
    author_id = request.form['author_id']
    read = request.form['read']
    blurb = request.form['blurb']
    author = author_repository.select(author_id)
    book = Book(title, author, blurb, read)
    book_repository.save(book)
    return redirect('/books')

@books_blueprint.route('/books/<id>')
def show_book(id):
    found_book = book_repository.select(id)
    return render_template('/books/show.html', book=found_book)

# DELETE
# POST '/books/<id>/delete'
@books_blueprint.route('/books/<id>/delete')
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')