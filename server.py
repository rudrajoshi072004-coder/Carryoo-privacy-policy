"""Serve static privacy policy HTML (Railway / local). Binds to $PORT on 0.0.0.0."""
import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PORT = int(os.environ.get("PORT", "8080"))


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def log_message(self, format, *args):
        print(f"{self.address_string()} - {format % args}")


def main():
    server = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Serving Carryoo privacy policy on http://0.0.0.0:{PORT}")
    server.serve_forever()


if __name__ == "__main__":
    main()
