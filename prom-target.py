#!/usr/bin/env python3
import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"#Mock Prometheus metrics\n")
        a_range = int(args.metrics/2)
        i = 0
        for m in range(0, args.metrics):
            for la in range(0, args.labels):
                i = i+1
                self.wfile.write(f"mock_metric_{m}{{labelA=\"{la}\",labelB=\"0\"}} {i}\n".encode())

parser = argparse.ArgumentParser(
                    prog='prom-target',
                    description='Serves a prometheus endpoint with a specified number of metrics and label cardinality')
parser.add_argument('-p', '--port', type=int, default=8000)
parser.add_argument('-m', '--metrics', type=int, default=1000)
parser.add_argument('-l', '--labels', type=int, default=10)
args = parser.parse_args()

print(f'Listening on port {args.port} to serve {args.metrics * args.labels} total metrics')

httpd = HTTPServer(('0.0.0.0', args.port), SimpleHTTPRequestHandler)
httpd.serve_forever()
