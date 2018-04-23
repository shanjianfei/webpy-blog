import web
import json

users = {}

urls = (
	'/', 'Index',
	'/login', 'Login',
	'/register', 'Register',
	'/getUser', 'GetUser'
)

web.config.debug = False
app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore('sessions'), {'username': None, 'login': 0})


class Index(object):
	def GET(self):
		if session.get('login') == 1:
			raise web.seeother('/static/html/index_login.html')
		else:
			raise web.seeother('/static/html/index_not_login.html')

class Login(object):
	def GET(self):
		raise web.seeother('/static/html/login.html')

	def POST(self):
		data = web.input()
		user = data['usr']
		password = data['psd']
		if user in users.keys() and users[user] == password:
			session.login = 1
			session.username = user
			web.setcookie('username', user, 3600)
			return json.dumps({'status': 'success'})
		else:
			return json.dumps({'status': 'fail'})

class Register(object):
	def POST(self):
		data = web.input()
		if 'usr' in data and 'psd' in data:
			users[data['usr']] = data['psd']
			return json.dumps({'status': 'success'})
		else:
			return json.dumps({'status': 'fail'})

class GetUser(object):
	def GET(self):
		if session.get('username', None) is not None and session.get('login', 0) == 1:
			return json.dumps({'username': session.get('username')})


if __name__ == '__main__':
	app.run()