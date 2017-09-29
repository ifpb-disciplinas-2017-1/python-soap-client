from suds.client import Client
from suds.cache import NoCache

class AutorConsumer:

	def __init__(self):
		self.url = "http://kieckegard-pc:8080/soap-biblioteca/AutorServiceService?wsdl"
		self.client = Client(self.url, cache=NoCache())

	def add(self, autor):
		self.client.service.addAutor(autor)

	def listAll(self):
		return self.client.service.listAllAutores()

class LivroConsumer:

	def __init__(self):
		self.url = "http://kieckegard-pc:8080/soap-biblioteca/LivroServiceService?wsdl"
		self.client = Client(self.url, cache=NoCache())

	def add(self, livro):
		#print "[LivroConsumer] adding livro... {}".format(livro)
		self.client.service.addLivro(livro)

	def remove(self, livro):
		self.client.service.removeLivro(livro)

	def listAll(self):
		return self.client.service.listAllLivros()

	def addAuthor(self, livroIsbn, autorEmail):
		self.client.service.bindAutor(livroIsbn, autorEmail);

livro = {
	'isbn': '123124123',
	'titulo': 'Java 8: News',
	'descricao': 'Livro sobre as novidades do Java 8',
	'edicao': '2014',
	'autores': []
}

class Program:

	def __init__(self):
		self.bookConsumer = LivroConsumer()
		self.authorConsumer = AutorConsumer()

	def newBook(self):
		#getting data from device input
		isbn = raw_input("ISBN: ")
		title = raw_input("Title: ")
		description = raw_input("Description: ")
		edition = raw_input('Edition: ')
		#returning dictionary containing the obtained data
		return {
			'isbn': isbn,
			'titulo': title,
			'descricao': description,
			'edicao': description,
			'autores': []
		}

	def newAuthor(self):

		email = raw_input("E-mail: ")
		name = raw_input("Name: ")
		abrev = raw_input("Abreviation: ")

		return {
			'email': email,
			'nome': name,
			'abreviacao': abrev
		}

	def printMenu(self):
		print "+-----------------------------------+"
		print "| 1 - list all authors              |"
		print "| 2 - list all books                |"
		print "| 3 - add a new book                |"
		print "| 4 - remove an existent book       |"
		print "| 5 - add a new author              |"
		print "| 6 - bind an author to a book      |"
		print "| 7 - unbind an author from a book  |"
		print "| 8 - remove an author              |"
		print "| 9 - exit                          |"
		print "+-----------------------------------+"
		return int(raw_input(">> "))

	def printBooks(self):
		print self.bookConsumer.listAll()

	def printAuthors(self):
		print self.authorConsumer.listAll()

	def handle(self, option):
		if(option == 9):
			return 1
		else:
			if(option == 1):
				self.printAuthors()
			elif(option == 2):
				self.printBooks()
			elif(option == 3):
				print "Fill the following book fields: "
				book = self.newBook()
				self.bookConsumer.add(book)
				print "The book {} was successfully added!".format(book["isbn"])
			return 0

	def start(self):

		while(True):
			option = self.printMenu()
			result = self.handle(option)
			if(result == 1):
				return


program = Program()
program.start()

	

