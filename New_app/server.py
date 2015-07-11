import tornado.ioloop
import tornado.web
import tornado.template
loader = tornado.template.Loader("./templates")
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(loader.load("main.html").generate())

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()