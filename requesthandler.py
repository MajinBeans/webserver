from http.server import HTTPServer, BaseHTTPRequestHandler

tasklist = ['Task 1', 'Task 2', 'Task 3']

class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('/tasklist'):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            
            output = ''
            output += '<html><body>'
            output += '<h1>Task List</h1>'
            output += '<h3><a href="/tasklist/new">Add New Task</a></h3>'
            for task in tasklist:
                output += task
                output += '<br>'
            
            output += '</body></html>'
            self.wfile.write(output.encode())

def main():
    PORT = 9000
    server = HTTPServer(('', PORT), requestHandler)
    print('Server Running on Port %s' % PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()