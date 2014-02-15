import BaseHTTPServer
from json_conversion import *
import re
import stat
import os

path_to_vomiting = './vomiting-lat-long.csv'

#data = ConvertToJSON(path_to_vomiting, 'F')

class ApiHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    def api_endpoint(s, path):
        s.send_response(200)
        s.send_header("Content-type", "application/json")
        s.end_headers()

        s.wfile.write(ConvertToJSON(path_to_vomiting, 'F'))

    def static_file(s, path):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()

        if stat.S_ISDIR(os.stat(s.path).st_mode):
            path = os.path.join(os.getcwd(), 'public', 'index.html')
        else:
            path = os.getcwd() + '/public' + path

        f = open(path, 'r')
        s.wfile.write(f.read());

    def do_GET(s):

        api_matcher = re.compile('/api(/|$)', re.IGNORECASE)
        if api_matcher.match(s.path):
            s.api_endpoint(s.path)
        else:
            s.static_file(s.path)

server_class = BaseHTTPServer.HTTPServer
httpd = server_class(("localhost", 6080), ApiHandler)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass

print time.asctime(), "Server Started"
httpd.server_close()
print time.asctime(), "Server stopped"
