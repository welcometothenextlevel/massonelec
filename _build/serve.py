import http.server, os, sys
ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'docs')
class H(http.server.SimpleHTTPRequestHandler):
    def __init__(s, *a, **k): super().__init__(*a, directory=ROOT, **k)
    def translate_path(s, path):
        p = super().translate_path(path)
        if not os.path.exists(p) and os.path.exists(p + '.html'): return p + '.html'
        return p
    def end_headers(s): s.send_header('Cache-Control', 'no-store'); super().end_headers()
http.server.ThreadingHTTPServer(('127.0.0.1', int(sys.argv[1]) if len(sys.argv) > 1 else 4471), H).serve_forever()
