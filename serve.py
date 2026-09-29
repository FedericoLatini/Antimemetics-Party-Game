import http.server
import socketserver
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
PORT = 8080

class ReusableServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    '.pdf': 'application/pdf',
    '.html': 'text/html',
    '.js': 'application/javascript',
    '.css': 'text/css',
})

if __name__ == '__main__':
    with ReusableServer(('127.0.0.1', PORT), Handler) as httpd:
        print(f"Serving at http://127.0.0.1:{PORT}")
        httpd.serve_forever()
