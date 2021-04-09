from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

port = 8888


class MyHttpRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        # http://localhost:8888/ 의 요청이 출력됨
        # (예) http://localhost:8888/test/joinform 이면 /joinform 출력
        # print(self.path)

        # http://localhost:8888/ 의 요청을 파라미터별로 구분
        result = urlparse(self.path)
        print(result)

        #
        if result.path == '/':
            self.send_response(200)  # 응답보내기
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write('<h1>Main Page</h1>'.encode('utf-8'))
        elif result.path == '/board':
            params = parse_qs(result.query)
            print(params)

            self.send_response(200)  # 응답보내기
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h3>게시판</h3>
    <ol>
        <li>안녕하세요</li>
        <li>가입인사합니다</li>
        <li>반가워요</li>
    </ol>
</body>
</html>'''.encode('utf-8')) # 실제 사용할때 이런식으로 html태그를 넣지는 않아


http = HTTPServer(('0.0.0.0', port), MyHttpRequestHandler)
print(f'Server Runningg on Port{port}')
http.serve_forever()  # 서버를 끝내지마라!


