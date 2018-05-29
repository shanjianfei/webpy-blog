# --*-- coding: utf-8 --*--
import web
import json

users = {'admin': '123456'}

urls = (
	'/', 'Index',
	'/login', 'Login',
	'/register', 'Register',
	'/user', 'User',
	'/comment', 'Comment',
)


app = web.application(urls, globals())

"""
sessoin对象用来保存用户状态,目前只有两种状态。
1，login的值为0时表示此次发起请求的用户是处于未登录的状态
2，login的值为1时表示此次发起请求的用户是处于登录的状态
"""
if '_session' not in web.config: #将session加入到webpy全局变量中
    session = web.session.Session(app, web.session.DiskStore('sessions'), {'username': None, 'login': 0})
    web.config._session = session
else:
    session = web.config._session

def connect():
	try:
		db = web.database(dbn='mysql',host='localhost',port=3306, db='test')
		return db
	except Exception,e:
		print e
		return -1


class Index(object):
	def GET(self):
		if session.get('login') == 1:
			try:
				f = open('index/index_login.html', 'r')
				return f.read()
			except Exception,e:
				print e
				return web.notfound('页面不存在')
			# raise web.seeother('/static/html/index_login.html')
		else:
			try:
				f = open('index/index_not_login.html', 'r')
				return f.read()
			except Exception,e:
				print e
				return web.notfound('页面不存在')
			# raise web.seeother('/static/html/index_not_login.html')

class Login(object):
	def GET(self):
		raise web.seeother('/static/html/login.html')

	def POST(self):
		data = eval(web.data())
		user = data.get('usr', '')
		password = data.get('psd', '')
		global users
		if user in users.keys() and users.get(user) == password:
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

class User(object):
	def GET(self):
		if session.get('username', None) is not None and session.get('login', 0) == 1:
			return json.dumps({'username': session.get('username')})

class Comment(object):
	def GET(self):
		pass

	def POST(self):
		data = web.input(comment='')
		if session.login == 1 and data.comment != '':
			user = session.get('username', '匿名用户')
			db = connect()
			if db != -1:
				re = db.insert('comment', content=data.comment, user=user)
			return json.dumps({'status': 'success'})
		else:
			return json.dumps({'status': 'fail'})
		


if __name__ == '__main__':
	app.run()
