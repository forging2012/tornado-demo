#�����Ǿ���� ��Hello, world�� ʾ����

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()



#�����������������
#Tornado �� Web ����Ὣ URL ���� URL ��ʽӳ�䵽 tornado.web.RequestHandler ��������ȥ��
# ���������ж����� get() �� post() ���������Դ���ͬ�� HTTP ����
#����Ĵ��뽫 URL ��Ŀ¼ / ӳ�䵽 MainHandler������һ�� URL ��ʽ /story/([0-9]+) ӳ�䵽 StoryHandler��
# ������ʽƥ��ķ������Ϊ�������� ����Ӧ�����У�

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("You requested the main page")

class StoryHandler(tornado.web.RequestHandler):
    def get(self, story_id):
        self.write("You requested the story " + story_id)

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/story/([0-9]+)", StoryHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


#����ʹ�� get_argument() ��������ȡ��ѯ�ַ����������Լ����� POST �����ݣ�

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body><form action="/" method="post">'
                   '<input type="text" name="message">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')

    def post(self):
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + self.get_argument("message"))

class StoryHandler(tornado.web.RequestHandler):
    def get(self, story_id):
        self.write("You requested the story " + story_id)

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/story/([0-9]+)", StoryHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


#post/get������ҳ�滥��
import tornado.ioloop
import tornado.web

class PostHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body><form action="/article" method="post">'
                   '<input type="text" name="message" value="Article">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')
class ArticleHandler(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Content-Type", "text/plain")
        self.write("This is a " + self.get_argument("message"))

application = tornado.web.Application([
    (r"/post", PostHandler),
    (r"/article", ArticleHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


#tornado.web.HTTPError �쳣
import tornado.ioloop
import tornado.web

class PostHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body><form action="/article" method="post">'
                   '<input type="text" name="message" value="Article">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')
class ArticleHandler(tornado.web.RequestHandler):
    def post(self):
        #self.set_header("Content-Type", "text/plain")
        #self.write("This is a " + self.get_argument("message"))
        raise tornado.web.HTTPError(403)

application = tornado.web.Application([
    (r"/post", PostHandler),
    (r"/article", ArticleHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


#tornadoģ��
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items = ["Item 1", "Item 2", "Item 3"]
        self.render("template.html", title="My title", items=items)

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

#Item 1
#Item 2
#Item 3


#escape: tornado.escape.xhtml_escape �Ąe��
#xhtml_escape: tornado.escape.xhtml_escape �Ąe��
#url_escape: tornado.escape.url_escape �Ąe��
#json_encode: tornado.escape.json_encode �Ąe��
#squeeze: tornado.escape.squeeze �Ąe��
#linkify: tornado.escape.linkify �Ąe��
#datetime: Python �� datetime ģ��
#handler: ��ǰ�� RequestHandler ����
#request: handler.request �Ąe��
#current_user: handler.current_user �Ąe��
#locale: handler.locale �Ąe��
#_: handler.locale.translate �Ąe��
#static_url: for handler.static_url �Ąe��
#xsrf_form_html: handler.xsrf_form_html �Ąe��
#reverse_url: Application.reverse_url �Ąe��
#Application ������ ui_methods �� ui_modules �����������Ŀ
#�κδ��ݸ� render ���� render_string �Ĺؼ��ֲ���


#Cookie �Ͱ�ȫ Cookie
#����ʹ�� set_cookie �������û������������ cookie��

import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        if not self.get_cookie("mycookie"):
            self.write("Your cookie was not set yet! I will set it now.")
            self.set_cookie("mycookie", "myvalue")
        else:
            self.write("Your cookie was set!")

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()


#��ȫ Cookie
#Cookie �����ױ�����Ŀͻ���α�졣
# ���������� cookie �б��浱ǰ��½�û��� id ֮�����Ϣ������Ҫ�� cookie ��ǩ���Է�ֹα�졣
# Tornado ͨ�� set_secure_cookie �� get_secure_cookie ����ֱ��֧�������ֹ��ܡ� Ҫʹ����Щ����������Ҫ�ڴ���Ӧ��ʱ�ṩһ����Կ������Ϊ cookie_secret��
# ����԰�����Ϊһ���ؼ��ʲ�������Ӧ�õ������У�

#ǩ������ cookie �а����˱������ cookie ֵ�����⻹��һ��ʱ�����һ�� HMAC ǩ����
# ��� cookie �Ѿ����ڻ��� ǩ����ƥ�䣬get_secure_cookie ������ None�����û������ cookie ʱ�� ����ֵ��һ���ġ�
# �������ӵİ�ȫ cookie �汾���£�

import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        if not self.get_secure_cookie("mycookie"):
            self.set_secure_cookie("mycookie", "myvalue")
            self.write("Your cookie was not set yet!")
        else:
            self.write("Your cookie was set!")

application = tornado.web.Application([
        (r"/", MainHandler),
    ], cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo="
)

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()


#�û���֤
#��ǰ�Ѿ���֤���û���Ϣ��������ÿһ������������ self.current_user ���У� ͬʱ��ģ��� current_user ��Ҳ�ǡ�
# Ĭ������£�current_user Ϊ None��
#Ҫ��Ӧ�ó���ʵ���û���֤�Ĺ��ܣ�����Ҫ��д�������� get_current_user() �� ���������������ж���ǰ�û���״̬������ͨ�� cookie��
#������������û��򵥵�ʹ��һ�� nickname ��½Ӧ�ã��õ�½��Ϣ�������浽 cookie �У�

#�����ʹ�� authenticated װ������װ�� post() ��������ô���û�û�е�½��״̬�£� �������᷵�� 403 ����
#Tornado �ڲ������˶Ե�������֤��ʽ��֧�֣����� Google �� OAuth ��
# ���� auth ģ�� �Ĵ����ĵ����˽������Ϣ�� for more details. Checkauth ģ�����˽�����ϸ�ڡ�
# �� Tornado ��Դ������һ�� Blog �����ӣ���Ҳ���Դ����￴�� �û���֤�ķ������Լ������ MySQL ���ݿ��б����û����ݣ���

import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class MainHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return
        name = tornado.escape.xhtml_escape(self.current_user)
        #self.redirect("/admin")
        self.write("Hello, " + name)

class LoginHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.write('<html><body><form action="/login" method="post">'
                       'Name: <input type="text" name="name">'
                       '<input type="submit" value="Sign in">'
                       '</form></body></html>')
        else:
            self.redirect("/admin")

    def post(self):
        self.set_secure_cookie("user", self.get_argument("name"))
        self.redirect("/")

class AdminHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return
        name = tornado.escape.xhtml_escape(self.current_user)
        #self.redirect("/admin")
        self.write("Hello, " + name)

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/login", LoginHandler),
    (r"/admin", AdminHandler),
], cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=")

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()



#��վα������ķ���
#��վα������(Cross-site request forgery)�� ���Ϊ XSRF���Ǹ��Ի� Web Ӧ���г�����һ����ȫ���⡣
# ǰ�������Ҳ��ϸ������ XSRF ������ʵ�ַ�ʽ��
#��ǰ���� XSRF ��һ��ͨ�õķ������Ƕ�ÿһ���û�����¼һ���޷�Ԥ֪�� cookie ���ݣ�Ȼ��Ҫ�������ύ�������ж����������� cookie ���ݡ�
# ��������ݲ�ƥ�� ����ô�������Ϳ����Ǳ�α��ġ�
#Tornado ���ڽ��� XSRF �ķ������ƣ�Ҫʹ�ô˻��ƣ�����Ҫ��Ӧ�������м��� xsrf_cookies �趨��
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        self.write("Hello, " + name)

class LoginHandler(BaseHandler):
    def get(self):
        self.write('<html><body><form action="/" method="post">'
                   'Name: <input type="text" name="name">'
                   '<input type="submit" value="Sign in">'
                   '</form></body></html>')

    def post(self):
        self.set_secure_cookie("user", self.get_argument("name"))
        self.redirect("/")

settings = {
    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    "login_url": "/login",
    "xsrf_cookies": True,
}

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/login", LoginHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()

"""
��������� xsrf_cookies����ô Tornado �� Web Ӧ�ý��������û�����һ�� _xsrf �� cookie ֵ����� POST PUT DELET ������û���� �� cookie ֵ����ô�������ᱻֱ�Ӿܾ�������㿪����������ƣ���ô������ ���ύ�ı��У��㶼��Ҫ����һ�������ṩ���ֵ�������ͨ����ģ����ʹ�� ר�ŵĺ��� xsrf_form_html() ��������һ�㣺

<form action="/new_message" method="post">
  {{ xsrf_form_html() }}
  <input type="text" name="message"/>
  <input type="submit" value="Post"/>
</form>
������ύ���� AJAX �� POST �����㻹����Ҫ��ÿһ��������ͨ���ű������ _xsrf ���ֵ���������� FriendFeed �е� AJAX �� POST ����ʹ���� jQuery ������Ϊ���������鶫��� _xsrf ֵ��

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

jQuery.postJSON = function(url, args, callback) {
    args._xsrf = getCookie("_xsrf");
    $.ajax({url: url, data: $.param(args), dataType: "text", type: "POST",
        success: function(response) {
        callback(eval("(" + response + ")"));
    }});
};
���� PUT �� DELETE �����Լ���ʹ�ý� form ������Ϊ������ POST ���� ��˵����Ҳ������ HTTP ͷ���� X-XSRFToken ����������� XSRF token��

�������Ҫ���ÿһ�������������� XSRF ��Ϊ���������д RequestHandler.check_xsrf_cookie()����������Ҫʹ��һ����֧�� cookie �� API�� �����ͨ���� check_xsrf_cookie() ������������� XSRF �������ơ�Ȼ����� ����Ҫͬʱ֧�� cookie �ͷ� cookie ��֤��ʽ����ôֻҪ��ǰ������ͨ�� cookie ������֤�ģ����Ӧ�ö���ʹ�� XSRF �������ƣ���һ��������Ҫ��
"""


