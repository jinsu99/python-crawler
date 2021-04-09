from http.client import HTTPConnection


conn = HTTPConnection('www.naver.com')  # 연결
conn.request('GET', '/')                # 요청
resp = conn.getresponse()               # 응답

# 응답 확인
print(resp.status, resp.reason)

# 성공 (200 OK)
if resp.status == 200:
    body = resp.read()  # body 읽어오기
    print(type(body), body)

# 실패 (404 not Found)
conn.request('GET', '/hello.html')
resp = conn.getresponse()               # 응답
print(resp.status, resp.reason)



