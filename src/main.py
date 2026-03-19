import http.server
import socketserver
from http import HTTPStatus
import logging
logging.basicConfig(level=logging.INFO)


logging.info("initializing Python server")
class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Python</title>
            <meta name="viewport" content="width=device-width, initial-scale=1" />

            <style>
            * {
                font-family: sans-serif;
                font-size: 16px;
            }

            html,
            body {
                margin: 0;
                min-height: 100vh;
                background: #202328;
                color: #fff;
            }

            body {
                display: flex;
                flex-direction: column;
                gap: 8px;
                padding: 32px;
                align-items: center;
                justify-content: center;
                box-sizing: border-box;
            }

            h1 {
                font-size: 24px;
            }

            p,
            form,
            hr {
                max-width: min(400px, 100%);
            }

            p {
                text-align: center;
                opacity: 0.8;
                line-height: 1.5;
            }

            button,
            .button {
                padding: 10px 18px;
                align-self: center;
                text-decoration: none;
                background: #6650fa;
                border-radius: 64px;
                border: none;
                color: #fff;
                cursor: pointer;
            }

            a {
                font-size: inherit;
                color: inherit;
            }

            hr {
                display: block;
                margin: 32px 0;
                width: 100%;
                height: 2px;
                background: #31363f;
                border: none;
            }

            a:last-child {
                margin-top: 32px;
            }

            code {
                font-family: monospace;
                font-size: 14px;
                background: #31363f;
                padding: 2px 4px;
                border-radius: 4px;
            }
            </style>
            
        </head>
        <body>
            <img
                alt="Python logo"
                src="https://github.com/diploi/component-python/raw/main/.diploi/icon.svg"
                width="64"
                height="64"
            />

            <h1>Python</h1>

            <p>
                Your Python application is up and running! You can start editing the code. 
                In development stage, Python will automatically reload as you make changes.
                <br><br>
                <b> Install dependencies: </b><br> 
                Please use <code>uv add package_name</code> to add Python packages to your environment.
            </p>

            <hr />

            <a href="https://diploi.com/"
            ><img width="54" height="16" src="https://diploi.com/logo-white.svg"
            /></a>
        </body>
        </html>
        """
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

class Server(socketserver.TCPServer):
    allow_reuse_address = True

httpd = Server(('0.0.0.0', 8000), Handler)
httpd.serve_forever()