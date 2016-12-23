import requests

MAIN_URL = 'https://api.telegra.ph/'

class telegraphApi():
	def __init__(self):
		self.http = requests.Session()
		self.auth = None

	def callMethod(self, n_method=None, a_method=None):
		method = MAIN_URL + n_method.__name__+'?'
		for x,y in a_method:
			if x!='self' and y!=None: method+=x+'='+str(y)+'&'
		response = self.http.get(method[:-1])
		method = eval(response.text.replace('\/','/').replace('true','True').replace('false','False'))
		return method


	def createAccount(self, short_name=None, author_name=None, author_url=None):
		'''Use this method to create a new Telegraph account. 
		
		short_name (String, 1-32 characters):
			Required. Account name, helps users with several accounts remember which they are currently using. 
		author_name (String, 0-128 characters):
			Default author name used when creating new articles.
		author_url (String, 0-512 characters):
			Default profile link, opened when users click on the author's name below the title. 
			Can be any link, not necessarily to a Telegram profile or channel.'''

		resp = self.callMethod(n_method=self.createAccount, a_method=locals().items())
		self.auth = resp['result']['access_token']
		return resp

	def editAccountInfo(self, access_token=None, short_name=None, author_name=None, author_url=None):
		'''Use this method to update information about a Telegraph account.

		access_token (String):
			Required. Access token of the Telegraph account.
		short_name (String, 1-32 characters):
			New account name.
		author_name (String, 0-128 characters):
			New default author name used when creating new articles.
		author_url (String, 0-512 characters):
			New default profile link, opened when users click on the author's name below the title. 
			Can be any link, not necessarily to a Telegram profile or channel.'''

		return self.callMethod(n_method=self.editAccountInfo, a_method=locals().items())

	def getAccountInfo(self, access_token=None, field=None):
		'''Use this method to get information about a Telegraph account. Returns an Account object on success.

		access_token (String):
			Required. Access token of the Telegraph account.
		fields (Array of String, default = [“short_name”,“author_name”,“author_url”]):
		List of account fields to return. 
		Available fields: short_name, author_name, author_url, auth_url, page_count.'''

		return self.callMethod(n_method=self.getAccountInfo, a_method=locals().items())

	def revokeAccessToken(self, access_token=self.auth):
		'''Use this method to revoke access_token and generate a new one, 
		for example, if the user would like to reset all connected sessions.

		access_token (String):
			Required. Access token of the Telegraph account.'''

		resp = self.callMethod(n_method=self.revokeAccessToken, a_method=locals().items())
		self.auth = resp['result']['access_token']
		return resp

	def createPage(self, access_token=self.auth, title=None, author_name=None, author_url=None,
		content=None, return_content=False):

		'''Use this method to create a new Telegraph page. On success, returns a Page object.

		access_token (String):
			Required. Access token of the Telegraph account.
		title (String, 1-256 characters):
			Required. Page title.
		author_name (String, 0-128 characters):
			Author name, displayed below the article's title.
		author_url (String, 0-512 characters):
			Profile link, opened when users click on the author's name below the title. 
			Can be any link, not necessarily to a Telegram profile or channel.
		content (Array of Node, up to 64 KB):
			Required. Content of the page. 
		return_content (Boolean, default = false):
			If true, a content field will be returned in the Page object.'''
		
		return self.callMethod(n_method=self.createPage, a_method=locals().items())

	def editPage(self, access_token=self.auth, path=None, title=None, content=None, 
		author_name=None, author_url=None, return_content=False):

		'''Use this method to edit an existing Telegraph page.

		access_token (String):
			Required. Access token of the Telegraph account.
		path (String):
			Required. Path to the page.
		title (String, 1-256 characters):
			Required. Page title.
		content (Array of Node, up to 64 KB):
			Required. Content of the page.
		author_name (String, 0-128 characters):
			Author name, displayed below the article's title.
		author_url (String, 0-512 characters):
			Profile link, opened when users click on the author's name below the title. 
			Can be any link, not necessarily to a Telegram profile or channel.
		return_content (Boolean, default = false):
			If true, a content field will be returned in the Page object.'''

		return self.callMethod(n_method=self.editPage, a_method=locals().items())

	def getPage(self, path=None, return_content=False):

		'''Use this method to get a Telegraph page. Returns a Page object on success.

		path (String):
			Required. Path to the Telegraph page (everything that comes after http://telegra.ph/).
		return_content (Boolean, default = false):
			If true, content field will be returned in Page object.'''

		return self.callMethod(n_method=self.getPage, a_method=locals().items())

	def getPageList(self, access_token=self.auth, offset=0, limit=50):

		'''Use this method to get a list of pages belonging to a Telegraph account. 
		Returns a PageList object, sorted by most recently created pages first.

		access_token (String):
			Required. Access token of the Telegraph account.
		offset (Integer, default = 0):
			Sequential number of the first page to be returned.
		limit (Integer, 0-200, default = 50):
			Limits the number of pages to be retrieved.'''

		return self.callMethod(n_method=self.getPageList, a_method=locals().items())

	def getViews(self, path=None, year=None, month=None, day=None, hour=None):

		'''Use this method to get the number of views for a Telegraph article. 
		Returns a PageViews object on success.

		path (String):
			Required. Path to the Telegraph page (in the format Title-12-31).
		year (Integer, 2000-2100):
			Required if month is passed. If passed, the number of page views for the requested year will be returned.
		month (Integer, 1-12):
			Required if day is passed. If passed, the number of page views for the requested month will be returned.
		day (Integer, 1-31):
			Required if hour is passed. If passed, the number of page views for the requested day will be returned.
		hour (Integer, 0-24):
			If passed, the number of page views for the requested hour will be returned.'''

		return self.callMethod(n_method=self.getViews, a_method=locals().items())
