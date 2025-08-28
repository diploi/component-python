import http.server
import socketserver
from http import HTTPStatus
import numpy as np

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        random_value = np.random.default_rng().random()
        response = f'Hello world!\nRandom value: {random_value}\n'
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))

class Server(socketserver.TCPServer):
    allow_reuse_address = True

httpd = Server(('0.0.0.0', 8000), Handler)
httpd.serve_forever()