from models.book import Book
from models.author import Author

import repositories.book_repositories as book_repository
import repositories.author_repositories as author_repository

author1 = Author("Jack")
author_repository.save(author1)

book1 = Book("Shadow Company", "shooter", author1)
book_repository.save(book1)