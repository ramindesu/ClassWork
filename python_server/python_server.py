from http.server import BaseHTTPRequestHandler, HTTPServer
import json
class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('context_type' , 'text/html')
            self.end_headers()
            self.wfile.write(b'hello world')

        elif self.path == '/info':
            self.send_response(200)
            self.send_header('context_type' , 'text/html')
            self.end_headers()
            response = {"message": "Server is running"}
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('context_type' , 'text/html')
            self.end_headers()
            self.wfile.write(b'404 NOT FOUND')


httpd = HTTPServer(('localhost',8080),Handler)
httpd.serve_forever()