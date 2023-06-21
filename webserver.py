from http.server import HTTPServer, BaseHTTPRequestHandler

class helloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write('Hello World!'.encode())

def main():
    PORT = 8000
    server = HTTPServer(('', PORT), helloHandler)
    print('Server Running on Port %s' % PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()