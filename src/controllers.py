# -*- coding: utf-8 -*-
__author__ = 'jramirez'

import cherrypy
from cherrypy import tools


class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return open('src/static/templates/index.html')


class StringGeneratorWebService(object):
    exposed = True

    @cherrypy.tools.accept(media='text/plain')
    @tools.json_out()
    def GET(self):
        return {"string": cherrypy.session['mystring']}

    def POST(self, length=8):
        import random
        import string

        some_string = ''.join(random.sample(string.hexdigits, int(length)))
        cherrypy.session['mystring'] = some_string
        return some_string

    def PUT(self, another_string):
        cherrypy.session['mystring'] = another_string

    def DELETE(self):
        cherrypy.session.pop('mystring', None)