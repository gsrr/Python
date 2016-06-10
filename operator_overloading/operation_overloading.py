class Book:
		title = ''
		pages = 0

		def __init__(self, title='', pages=0):
				self.title = title
				self.pages = pages

		def __str__(self):
				B
				return self.title

		def __radd__(self, other):
				return self.pages + other

		def __lt__(self, other):
				return self.pages < other

		def ___le__(self, other):
				return self.pages <= other

		def __eq__(self, other):
				return self.pages == other

		def __ne__(self, other):
				return self.pages != other

		def __gt__(self, other):
				return self.pages > other

		def __ge__(self, other):
				return self.pages >= other

book1 = Book('Fluency', 381)
book2 = Book('The Martian', 385)
book3 = Book('Ready Player One', 386)

print book1 + book2
print sum([book1, book2, book3])


