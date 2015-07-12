import os
import tornado.ioloop
import tornado.web
import tornado.template
import github

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "debug":True
}
loader = tornado.template.Loader("./templates")


class ProjectExtractor(tornado.web.RequestHandler):
  def get(self):
    githubUrl =  self.get_argument("github-url", None, True)
    if not github:
      self.write("No url submitted")
    Contributors = github.Github().returnContributors(githubUrl)
    self.write(loader.load("contributors_list.html").generate(Contributors=Contributors, project=githubUrl))

class DiversityInformation(tornado.web.RequestHandler):
  def post(self):
    #data_json = tornado.escape.json_decode(self.request.body)
    print self.request.body
    self.write("hi")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(loader.load("main.html").generate())

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/submitproject", ProjectExtractor),
    (r"/diversityinfo", DiversityInformation)
],**settings )

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()