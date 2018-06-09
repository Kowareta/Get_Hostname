#!/usr/bin/env python
from http.server import BaseHTTPRequestHandler, HTTPServer
import socket

class HTTPServer_RequestHandler(BaseHTTPRequestHandler):
    #GET
    def do_GET(self):
        #Send response status code
        self.send_response(200)

        #Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        #Send message back to client
        message = (socket.gethostname())
        #Write contens as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

    def run():
      print('Starting server...')

      #Server settings
      server_address = ('', 80)
      httpd = HTTPServer(server_address, HTTPServer_RequestHandler)
      print('Running server...')
      httpd.serve_forever()

    run()
