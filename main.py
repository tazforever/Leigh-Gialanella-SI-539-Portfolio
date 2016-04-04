import webapp2
import os
import logging
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class IndexHandler(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('templates/index.html')
    	self.response.write(template.render({'title': 'HOME'}))

class ResumeHandler(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('templates/resume.html')
    	self.response.write(template.render({'title' : 'Resume'}))

class ProjectsHandler(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('templates/projects.html')
    	self.response.write(template.render({'title' : 'Projects'}))

class PhotosHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/photos.html')
        self.response.write(template.render({'title' : 'Photos'}))


class ContactHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/contact.html')
        self.response.write(template.render({'title' : 'Contact'}))


app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/index.html', IndexHandler),
    ('/resume.html', ResumeHandler),
    ('/projects.html', ProjectsHandler),
    ('/photos.html', PhotosHandler),
    ('/contact.html', ContactHandler),
], debug=True)





