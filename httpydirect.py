#!/usr/bin/env python3

""" Made by SpeerSec - free for use, credit if modified or reused """

import argparse
import http.server
import socketserver
import sys

class RedirectHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Forward the request to the target URL
        self.send_response(307)
        self.send_header("Location", self.server.target_url)
        self.end_headers()

# Parse the command line arguments
parser = argparse.ArgumentParser(description="A simple HTTP server that redirects incoming requests to a specified URL")
parser.add_argument("--port", "-p", type=int, default=8000, help="the port to listen on (default: 8000)")
parser.add_argument("--ip", "-i", default="127.0.0.1", help="the IP address to listen on (default: 127.0.0.1)")
parser.add_argument("--url", "-u", required=True, help="the URL to redirect to")
args = parser.parse_args()

# If no arguments were provided, print the help menu and exit
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit()

# Create the server and run it
with socketserver.TCPServer((args.ip, args.port), RedirectHandler) as httpd:
    httpd.target_url = args.url
    print("Redirecting incoming requests to {}".format(args.url))
    httpd.serve_forever()
