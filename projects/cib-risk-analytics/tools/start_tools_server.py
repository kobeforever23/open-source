#!/usr/bin/env python3
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import argparse
import os

parser = argparse.ArgumentParser(description='Serve CIB risk tools locally.')
parser.add_argument('--port', type=int, default=8090, help='Port to bind (default: 8090)')
args = parser.parse_args()

root = Path(__file__).resolve().parent
os.chdir(root)
server = ThreadingHTTPServer(('127.0.0.1', args.port), SimpleHTTPRequestHandler)
print(f'Serving {root} on http://127.0.0.1:{args.port}')
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
finally:
    server.server_close()
    print('Server stopped.')
