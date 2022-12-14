import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository


author1 = Author("Nagib Mahfoz")
author_repository.save(author1)

book1 = Book("Pyramids", author1)
book_repository.save(book1)

print(book_repository.select_all())

