# --*-- coding: utf-8 --*--
import web
import json
import uuid
from datetime import datetime

users = {'admin': '123456'}

urls = (
    '/', 'Index',
    '/login', 'Login',
    '/register', 'Register',
    '/user', 'User',
    '/article', 'Article',
    '/articledetail', 'ArticleDetail'
)


app = web.application(urls, globals())

"""
sessoin对象用来保存用户状态,目前只有两种状态。
1，login的值为0时表示此次发起请求的用户是处于未登录的状态
2，login的值为1时表示此次发起请求的用户是处于登录的状态
"""
if '_session' not in web.config: # 将session加入到webpy全局变量中
    session = web.session.Session(app, web.session.DiskStore('sessions'), {'username': None, 'login': 0})
    web.config._session = session
else:
    session = web.config._session


def connect():
    try:
        db = web.database(dbn='mysql', host='localhost', port=3306, db='myblog', user='root', pw='1102121672')
        return db
    except Exception, e:
        print e
        return -1


class Index(object):
    def GET(self):
        if session.get('login') == 1:
            try:
                f = open('index/index_login.html', 'r')
                return f.read()
            except Exception, e:
                print e
                return web.notfound('页面不存在')
            # raise web.seeother('/static/html/index_login.html')
        else:
            try:
                f = open('index/index_not_login.html', 'r')
                return f.read()
            except Exception, e:
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


class ArticleDetail(object):
    def GET(self):
        data = web.input()
        print(data)
        db = connect()
        if 'id' in data:
            res = db.select('articles',
                            where={'article_id': data['id']})
        else:
            res = db.select('articles')

        _res = []
        for _ in res:
            _['create_time'] = str(_['create_time'])
            _['last_modified_time'] = str(_['last_modified_time'])
            _res.append(_)
        print(_res)
        return json.dumps({'status': 'success', 'data': _res})


class Article(object):
    def GET(self):
        data = web.input()
        db = connect()
        if 'id' in data:
            res = db.select('articles',
                            what='title,create_time,article_type',
                            where={'article_id': data['id']})
        else:
            res = db.select('articles',
                            what='article_id,title,create_time,article_type, click_rate')
        _res = []
        for _ in res:
            _['create_time'] = str(_['create_time'])
            _res.append(_)
        return json.dumps({'status': 'success', 'data': _res})

    def _check(self, data):
        if 'title' in data and 'content' in data and 'type' in data:
            title = data['title']
            content = data['content']
            _type = data['type']
            if title != '' and 0 < len(title) < 85 and len(content) > 0 \
                    and _type != '':
                return True
        return False

    def POST(self):
        data = eval(web.data())
        if session.login == 1 and self._check(data):
            # user = session.get('username', '匿名用户')
            db = connect()
            if db != -1:
                _d = {
                    'article_id': uuid.uuid1(),
                    'title': data['title'],
                    'article': data['content'],
                    'article_type': data['type'],
                    'create_time': datetime.now(),
                    'last_modified_time': datetime.now()
                }
                db.insert('articles', **_d)
            return json.dumps({'status': 'success'})
        else:
            return json.dumps({'status': 'fail'})

    def DELETE(self):
        data = web.input()
        if 'id' in data:
            id = data['id']
            db = connect()
            if db != -1:
                try:
                    db.delete('articles',
                              where='article_id = $id', vars=locals())
                    return json.dumps({'status': 'success'})
                except Exception, e:
                    print e
        return json.dumps({'status': 'fail'})


if __name__ == '__main__':
    app.run()
