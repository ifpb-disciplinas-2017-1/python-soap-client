
from consumer.consumer import Consumer

class AuthorConsumer:

	def __init__(self):
		url = "http://10.3.186.68:8080/soap-biblioteca/AutorServiceService?wsdl"
		self.consumer = Consumer(url)


	def listAll(self):
		return self.consumer.execute('listAllAutores');

class BookConsumer:

	def __init__(self):
		url = "http://10.3.186.68:8080/soap-biblioteca/LivroServiceService?wsdl"
		self.consumer = Consumer(url)

	def listAll(self):
		return self.consumer.execute('listAllLivros', None)

	def add(self, book):
		self.consumer.execute('addLivro', book)

	def remove(self, bookIsbn):
		self.consumer.execute('removeLivro', bookIsbn)

	def bindAuthor(self, bookIsbn, authorEmail):
		self.consumer.execute('bindAutor', [bookIsbn, authorEmail])

#authorConsumer = AuthorConsumer()

#bookConsumer
bookConsumer = BookConsumer()

#In case you want to list authors
#authors = authorConsumer.listAll()

#new book dictionary
newBook = {
   'descricao': "About the most import things in Go",
   'edicao': "2017",
   'isbn': "51231-400-2000",
   'titulo': "Go, the important things"
}

#adding a new book
bookConsumer.add(newBook)

#getting books from the webservice
books = bookConsumer.listAll()

for book in books:
	print book
