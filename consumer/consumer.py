from suds.client import Client
from suds.cache import NoCache

class Consumer:

	def __init__(self, url):
		self.url = url
		self.client = Client(self.url, cache=NoCache())

	def execute(self, method, args=None):
		return getattr(self.client.service, method)(args)
