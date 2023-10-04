import http.server
import json
import os
import socketserver
from dotenv import load_dotenv

load_dotenv()

simpler = http.server.SimpleHTTPRequestHandler


class RequestHandler(simpler):
    def do_GET(self):
        if self.path == '/api':
            data = {
                'title': 'Python Micro Start',
                'description': 'Simple microservice with native Python'
            }
            output_json = json.dumps(data, indent=2)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.wfile.write(output_json.encode('utf-8'))
            return

        file = "/index.html" if self.path == '/' else self.path
        self.path = './public' + file

        if not os.path.isfile(self.path):
            self.path = './public/404.html'

        return simpler.do_GET(self)


pin = int(os.environ.get('PORT_INTERNAL'))
pex = int(os.environ.get('PORT_EXTERNAL'))

try:
    with socketserver.TCPServer(("", pin), RequestHandler) as httpd:
        print("Server Ports: %s:%s" % (pex, pin))
        httpd.serve_forever()
except KeyboardInterrupt:
    httpd.server_close()
