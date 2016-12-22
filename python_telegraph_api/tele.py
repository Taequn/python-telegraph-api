import requests

MAIN_URL = 'https://api.telegra.ph/'

class telegraphApi():
	def __init__(self):
		self.http = requests.Session()

	def callMethod(self, n_method=None, a_method=None):
		method = MAIN_URL + n_method.__name__+'?'
		for x,y in a_method:
			if x!='self' and y!=None: method+=x+'='+str(y)+'&'
		response = self.http.get(method[:-1])
		method = eval(response.text.replace('\/','/').replace('true','True').replace('false','False'))
		return method


		#and here we go with methods
	def createAccount(self, short_name=None, author_name=None, author_url=None):
		return self.callMethod(n_method=self.createAccount, a_method=locals().items())

	def editAccountInfo(self, access_token=None, short_name=None, author_name=None, author_url=None):
		return self.callMethod(n_method=self.editAccountInfo, a_method=locals().items())

	def getAccountInfo(self, access_token=None, field=None):
		return self.callMethod(n_method=self.getAccountInfo, a_method=locals().items())

	def revokeAccessToken(self, access_token=None):
		return self.callMethod(n_method=self.revokeAccessToken, a_method=locals().items())

	def createPage(self, access_token=None, title=None, author_name=None, author_url=None,
		content=None, return_content=False):
		return self.callMethod(n_method=self.createPage, a_method=locals().items())

	def editPage(self, access_token=None, path=None, title=None, content=None, 
		author_name=None, author_url=None, return_content=False):
		return self.callMethod(n_method=self.editPage, a_method=locals().items())

	def getPage(self, path=None, return_content=False):
		return self.callMethod(n_method=self.getPage, a_method=locals().items())

	def getPageList(self, access_token=None, offset=0, limit=50):
		return self.callMethod(n_method=self.getPageList, a_method=locals().items())

	def getViews(self, path=None, year=None, month=None, day=None, hour=None):
		return self.callMethod(n_method=self.getPageList, a_method=locals().items())