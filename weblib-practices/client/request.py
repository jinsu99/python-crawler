from urllib.parse import urlencode
from urllib.request import urlopen, Request

# GET
http_response = urlopen('https://www.example.com')
body = http_response.read()     # url의 html읽어오기
body = body.decode('utf-8')     # utf-8로 인코딩 되어있으니, decoding해주기
# print(body)


# POST : 딕셔너리로 데이터 전달
data = {
    'id': 'seafood',
    'name': '동해물',
    'pw': '1234'
}


data = urlencode(data).encode('utf-8')  # 인코딩

request = Request('https://www.example.com', data)
request.add_header('Contente-Type', 'text/html')

http_response = urlopen(request)
print(http_response.status)
body = http_response.read()
html = body.decode('utf-8')

print(html)

