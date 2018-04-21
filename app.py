import web
import json

users = {}

urls = (
	'/', 'Index',
	'/login', 'Login',
	'/register', 'Register'
)

app = web.application(urls, globals())

class Index(object):
	def GET(self):
		return 'hello'

class Login(object):
	def GET(self):
		web.seeother('/static/html/login.html')

	def POST(self):
		data = web.input()
		user = data['usr']
		password = data['psd']
		if user in users.keys() and users[user] == password:
			web.seeother('/')
		else:
			return json.dumps({'status': 'fail'})

		return 'login success'

class Register(object):
	def POST(self):
		data = web.input()
		if 'usr' in data and 'psd' in data:
			users[data['usr']] = data['psd']
			return json.dumps({'status': 'success'})
		else:
			return json.dumps({'status': 'fail'})

if __name__ == '__main__':
	app.run()