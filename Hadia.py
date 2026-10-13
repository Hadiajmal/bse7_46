from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Hello from bse7_46 - Hadia Ajmal</h1>")

HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()