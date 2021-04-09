import sys
from datetime import datetime
from urllib.request import Request, urlopen


# def print_error(e):
#     print(e)
# 두번째 인자에 file을 넣어서 file에 출력할수도 있다.
# sys.stdout : module sys의 standard output(console)
# 시스템 구동시 기본적으로 3개 사용된다 : stdin(키보드), stdout(콘솔), stderror
# print(f'{e} : {datetime.now()}', file=sys.stdout)
# 람다 함수 : 이름이 없는 함수 (화살표 프로그래밍)
# (예) lambda e -> 함수내용):
# 따로 return문을 작성하지않아도 return된다

def crawling(
        url='',
        encoding='utf-8',
        err=lambda e: print(f'{e} : {datetime.now()}', file=sys.stderr)):
    try:
        request = Request(url)
        response = urlopen(request)
        print(f'{datetime.now()}: success for request[{url}]')

        receive = response.read()
        return receive.decode(encoding, errors='replace')

    except Exception as e:
        if err is not None:
            err(e)

