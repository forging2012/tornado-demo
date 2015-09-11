#以下是经典的 “Hello, world” 示例：

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



#请求处理程序和请求参数
#Tornado 的 Web 程序会将 URL 或者 URL 范式映射到 tornado.web.RequestHandler 的子类上去。
# 在其子类中定义了 get() 或 post() 方法，用以处理不同的 HTTP 请求。
#下面的代码将 URL 根目录 / 映射到 MainHandler，还将一个 URL 范式 /story/([0-9]+) 映射到 StoryHandler。
# 正则表达式匹配的分组会作为参数引入 的相应方法中：

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


#可以使用 get_argument() 方法来获取查询字符串参数，以及解析 POST 的内容：

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


#post/get方法多页面互动
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


#tornado.web.HTTPError 异常
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


#tornado模板
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


#escape: tornado.escape.xhtml_escape 的別名
#xhtml_escape: tornado.escape.xhtml_escape 的別名
#url_escape: tornado.escape.url_escape 的別名
#json_encode: tornado.escape.json_encode 的別名
#squeeze: tornado.escape.squeeze 的別名
#linkify: tornado.escape.linkify 的別名
#datetime: Python 的 datetime 模组
#handler: 当前的 RequestHandler 对象
#request: handler.request 的別名
#current_user: handler.current_user 的別名
#locale: handler.locale 的別名
#_: handler.locale.translate 的別名
#static_url: for handler.static_url 的別名
#xsrf_form_html: handler.xsrf_form_html 的別名
#reverse_url: Application.reverse_url 的別名
#Application 设置中 ui_methods 和 ui_modules 下面的所有项目
#任何传递给 render 或者 render_string 的关键字参数


#Cookie 和安全 Cookie
#可以使用 set_cookie 方法在用户的浏览中设置 cookie：

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


#安全 Cookie
#Cookie 很容易被恶意的客户端伪造。
# 加入你想在 cookie 中保存当前登陆用户的 id 之类的信息，你需要对 cookie 作签名以防止伪造。
# Tornado 通过 set_secure_cookie 和 get_secure_cookie 方法直接支持了这种功能。 要使用这些方法，你需要在创建应用时提供一个密钥，名字为 cookie_secret。
# 你可以把它作为一个关键词参数传入应用的设置中：

#签名过的 cookie 中包含了编码过的 cookie 值，另外还有一个时间戳和一个 HMAC 签名。
# 如果 cookie 已经过期或者 签名不匹配，get_secure_cookie 将返回 None，这和没有设置 cookie 时的 返回值是一样的。
# 上面例子的安全 cookie 版本如下：

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


#用户认证
#当前已经认证的用户信息被保存在每一个请求处理器的 self.current_user 当中， 同时在模板的 current_user 中也是。
# 默认情况下，current_user 为 None。
#要在应用程序实现用户认证的功能，你需要复写请求处理中 get_current_user() 这 个方法，在其中判定当前用户的状态，比如通过 cookie。
#下面的例子让用户简单地使用一个 nickname 登陆应用，该登陆信息将被保存到 cookie 中：

#如果你使用 authenticated 装饰器来装饰 post() 方法，那么在用户没有登陆的状态下， 服务器会返回 403 错误。
#Tornado 内部集成了对第三方认证形式的支持，比如 Google 的 OAuth 。
# 参阅 auth 模块 的代码文档以了解更多信息。 for more details. Checkauth 模块以了解更多的细节。
# 在 Tornado 的源码中有一个 Blog 的例子，你也可以从那里看到 用户认证的方法（以及如何在 MySQL 数据库中保存用户数据）。

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



#跨站伪造请求的防范
#跨站伪造请求(Cross-site request forgery)， 简称为 XSRF，是个性化 Web 应用中常见的一个安全问题。
# 前面的链接也详细讲述了 XSRF 攻击的实现方式。
#当前防范 XSRF 的一种通用的方法，是对每一个用户都记录一个无法预知的 cookie 数据，然后要求所有提交的请求中都必须带有这个 cookie 数据。
# 如果此数据不匹配 ，那么这个请求就可能是被伪造的。
#Tornado 有内建的 XSRF 的防范机制，要使用此机制，你需要在应用配置中加上 xsrf_cookies 设定：
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
如果设置了 xsrf_cookies，那么 Tornado 的 Web 应用将对所有用户设置一个 _xsrf 的 cookie 值，如果 POST PUT DELET 请求中没有这 个 cookie 值，那么这个请求会被直接拒绝。如果你开启了这个机制，那么在所有 被提交的表单中，你都需要加上一个域来提供这个值。你可以通过在模板中使用 专门的函数 xsrf_form_html() 来做到这一点：

<form action="/new_message" method="post">
  {{ xsrf_form_html() }}
  <input type="text" name="message"/>
  <input type="submit" value="Post"/>
</form>
如果你提交的是 AJAX 的 POST 请求，你还是需要在每一个请求中通过脚本添加上 _xsrf 这个值。下面是在 FriendFeed 中的 AJAX 的 POST 请求，使用了 jQuery 函数来为所有请求组东添加 _xsrf 值：

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
对于 PUT 和 DELETE 请求（以及不使用将 form 内容作为参数的 POST 请求） 来说，你也可以在 HTTP 头中以 X-XSRFToken 这个参数传递 XSRF token。

如果你需要针对每一个请求处理器定制 XSRF 行为，你可以重写 RequestHandler.check_xsrf_cookie()。例如你需要使用一个不支持 cookie 的 API， 你可以通过将 check_xsrf_cookie() 函数设空来禁用 XSRF 保护机制。然而如果 你需要同时支持 cookie 和非 cookie 认证方式，那么只要当前请求是通过 cookie 进行认证的，你就应该对其使用 XSRF 保护机制，这一点至关重要。
"""


