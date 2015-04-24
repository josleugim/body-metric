# -*- coding: utf-8 -*-
__author__ = 'jramirez'

import os
import cherrypy
from src.controllers import StringGenerator
from src.controllers import StringGeneratorWebService


if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/metrics': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    webapp = StringGenerator()
    webapp.metrics = StringGeneratorWebService()
    cherrypy.quickstart(webapp, '/', conf)