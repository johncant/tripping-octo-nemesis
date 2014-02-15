import BaseHTTPServer
from json_conversion import *

path_to_vomiting = '../data/ASB Noise Cleansing Waste Washing/vomiting-lat-long.csv'

#data = ConvertToJSON(path_to_vomiting, 'F')

class ApiHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(s):
        s.send_response(200)
        s.send_header("Content-type", "application/json")
        s.end_headers()


        s.wfile.write(ConvertToJSON(path_to_vomiting, 'F'))


server_class = BaseHTTPServer.HTTPServer
httpd = server_class(("localhost", 6080), ApiHandler)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass

print time.asctime(), "Server Started"
httpd.server_close()
print time.asctime(), "Server stopped"
