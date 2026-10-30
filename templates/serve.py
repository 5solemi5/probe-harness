"""표준 라이브러리만 쓰는 웹 서버 골격. 필요할 때 복사해서 쓴다: cp ~/.h/templates/serve.py app.py

- 0.0.0.0 에 바인딩해야 미리보기 탭에서 보인다.
- 기능 로직은 별도 모듈(예: core.py)에 두고 여기서는 화면·API만 다룬다.
"""
import csv
import html
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

PORT = int(os.environ.get("PORT", "3000"))
DATA = os.environ.get("DATA", "out/result.csv")  # 화면에 보여 줄 결과 파일


def load_rows(path):
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def table(rows):
    if not rows:
        return "<p>결과가 없습니다.</p>"
    cols = list(rows[0])
    head = "".join(f"<th>{html.escape(c)}</th>" for c in cols)
    body = "".join(
        "<tr>" + "".join(f"<td>{html.escape(str(r[c]))}</td>" for c in cols) + "</tr>" for r in rows
    )
    return f"<table border=1 cellpadding=4><tr>{head}</tr>{body}</table>"


class Handler(BaseHTTPRequestHandler):
    def send(self, code, body, ctype):
        data = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        path = urlparse(self.path).path
        try:
            if path == "/health":
                self.send(200, json.dumps({"ok": True}), "application/json")
            elif path == "/api/rows":
                self.send(200, json.dumps(load_rows(DATA), ensure_ascii=False), "application/json; charset=utf-8")
            elif path == "/":
                rows = load_rows(DATA)
                page = f"<!doctype html><meta charset=utf-8><title>결과</title><h1>결과 {len(rows)}건</h1>{table(rows)}"
                self.send(200, page, "text/html; charset=utf-8")
            else:
                self.send(404, "not found", "text/plain; charset=utf-8")
        except Exception as e:  # 한 요청의 오류로 서버 전체가 죽지 않게 한다
            self.send(500, f"error: {e}", "text/plain; charset=utf-8")


if __name__ == "__main__":
    print(f"http://0.0.0.0:{PORT}  (data: {DATA})")
    ThreadingHTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
