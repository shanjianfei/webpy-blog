import web

urls = (
	'/', 'Index',
	'/login', 'Login'
)

app = web.application(urls, globals())

class Index(object):
	def GET(self):
		return 'hello'

class Login(object):
	def GET(self):
		web.seeother('/static/html/login.html')

	def POST(self):
		return 'login success'

if __name__ == '__main__':
	app.run()