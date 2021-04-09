from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

from collection import crawler


def ex01():
    # url open
    request = Request("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")
    response = urlopen(request)
    html = response.read().decode('cp949')  # 인코딩방법 확인하고 decoding하기 : euc-kr은 cp949로 decoding하자
    # print(html)

    bs = BeautifulSoup(html, 'html.parser')

    # find는 하나의 태그만 찾는다
    divs = bs.find('div', attrs={'class': 'tit3'})
    print(divs)

    # findAll는 해당하는 태그 중 첫번째만 반환
    divs = bs.findAll('div', attrs={'class': 'tit3'})

    # 리스트가 아닌 element
    # print(type(divs))

    # 순회는 가능하다
    # for div in divs:
    #     # print(div)
    #     print(div.a.text)   # div>a>text의 값만 출력

    # enumerate로 형변환하고 언패킹
    for index, div in enumerate(divs):
        print(index + 1, div.a.text, div.a['href'], sep='\t')


def ex02():
    # collection 폴더의 crawler 모듈 함수 사용 예정

    html = crawler.crawling(
        url="https://movie.naver.com/movie/sdb/rank/rmovie.nhn",
        encoding='cp949')
    # print(html)

    bs = BeautifulSoup(html, 'html.parser')
    divs = bs.findAll('div', attrs={'class': 'tit3'})

    for index, div in enumerate(divs):
        print(index + 1, div.a.text, div.a['href'], sep='\t')


if __name__ == '__main__':
    ex02()
