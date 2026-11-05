#!/usr/bin/env python3
"""Servidor local de prueba que declara UTF-8 (http.server no lo hace por sí solo)."""
import http.server, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
class H(http.server.SimpleHTTPRequestHandler):
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map,
                      ".html": "text/html; charset=utf-8", ".mp3": "audio/mpeg", ".webp": "image/webp"}
http.server.ThreadingHTTPServer(("", int(sys.argv[1])), H).serve_forever()
