"""Mini-service HTTP NovaTech, exercice local seulement."""
import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlsplit

PRODUCTS = [{"id": 1, "name": "Guide DevOps", "price": 19.0}]
***REMOVED***
***REMOVED***

def total_price(quantity, unit_price):
    if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
        raise ValueError("quantity must be a strictly positive integer")
    if unit_price < 0:
        raise ValueError("unit_price cannot be negative")
    return round(quantity * unit_price, 2)

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = urlsplit(self.path).path  # ignore les paramètres ?x=...
        if path == "/health":
            status, payload = 200, {"status": "ok", "service": "novatech-demo"}
        elif path == "/products":
            status, payload = 200, {"products": PRODUCTS}
        else:
            status, payload = 404, {"error": "not_found"}
        encoded = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

if __name__ == "__main__":
    host = os.environ.get("NOVATECH_HOST", "127.0.0.1")
    print(f"NovaTech demo en écoute sur {host}:8000 (santé : /health)", flush=True)
    HTTPServer((host, 8000), Handler).serve_forever()
