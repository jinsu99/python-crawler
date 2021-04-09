from itertools import count

import pandas as pd
from bs4 import BeautifulSoup
from collection import crawler

import time
from datetime import datetime
from selenium import webdriver


def crawling_pelicana():
    # 가져온 데이터 담아줄 list
    results = []

    # 점포가 늘어나서 페이지가 늘어났다면 for문의 직접 정해준 반복횟수는 의미가 없다.
    # ※ 마지막 페이지를 검출하도록 해보자
    # 1. 마지막 페이지로 가서 html을 확인한다.
    # 2. 페리카나의 경우 tbody에 내용이 없다.
    # 3. 즉, tr의 개수가 0일 때 마지막 페이지.
    for index in count(start=1, step=1):
        url = f'https://pelicana.co.kr/store/stroe_search.html?page={index}&branch_name=&gu=&si'
        html = crawler.crawling(url)

        bs = BeautifulSoup(html, 'html.parser')
        tag_table = bs.find('table', attrs={'class': ['table', 'mt20']})
        tag_tbody = tag_table.find('tbody')
        tags_tr = tag_tbody.findAll('tr')

        # ※ 마지막 페이지 검출
        # print(len(tags_tr))
        if len(tags_tr) == 0:
            # print('마지막 페이지 :', index)
            break

        for tag_tr in tags_tr:
            datas = list(tag_tr.strings)
            name = datas[1]
            address = datas[3]
            sidogugun = address.split()[:2]
            results.append((name, address) + tuple(sidogugun))

    # print(results)

    # pandas를 사용해 csv파일로 저장하기
    # pandas = 데이터를 테이블로 저장
    # pandas 설치 : pip install pandas

    # store
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gugun'])
    table.to_csv('results/pelicana.csv', encoding='utf-8', mode='w', index=True)


def crawling_nene():
    pass


def crawling_kyochon():
    pass


def crawling_goobne():
    # dom형태의 웹을 크롤링하는 방법
    # googledriver를 통해 js를 사용할 수 있다.

    # Chrome 브라우저 시작
    url = 'http://goobne.co.kr/store/search_store.jsp'
    wd = webdriver.Chrome('C:\\Users\\pc\\Desktop\\Pycharm-project\\chromedriver_win32\\chromedriver.exe')

    # 페이지 이동
    wd.get(url)
    time.sleep(3)

    # 끝 검출방법 : javascriptstore.getList('108')

    results = []
    for index in count(start=1, step=1):
        # 자바 스크립트 실행
        script = f'store.getList({index})'
        wd.execute_script(script)
        print(f'{datetime.now()}: success for request[{script}]')
        time.sleep(3)

        # 자바스크립트 실행된 html(동적으로 랜더링된 html)가져오기
        html = wd.page_source

        # 파싱하기(bs4)
        bs = BeautifulSoup(html, 'html.parser')
        tag_tbody = bs.find('tbody', attrs={'id': 'store_list'})
        tags_tr = tag_tbody.findAll('tr')

        # 끝 검출
        if tags_tr[0].get('class') is None:
            break

        for tag_tr in tags_tr:
            datas = list(tag_tr.strings)
            name = datas[1]
            address = datas[6]
            sidogugun = address.split()[:2]
            results.append((name, address)+tuple(sidogugun))

    # Chrome 브라우저 닫기
    wd.close()

    # store
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gugun'])
    table.to_csv('results/goobne.csv', encoding='utf-8', mode='w', index=True)


if __name__ == '__main__':
    # crawling_pelicana()
    # crawling_nene()
    # crawling_kyochon()
    crawling_goobne()