from bs4 import BeautifulSoup

html = '''
<td class ="title black">
    <div class ="tit3" data-no="10">        
        <a href="/movie/bi/mi/basic.nhn?code=191637"title = "고질라 VS. 콩"> 고질라VS.콩 </a>
    </div>
</td>
'''


# 1. tag 조회
def ex01():
    bs = BeautifulSoup(html, 'html.parser')
    # print(bs)

    tag_td = bs.td
    # print(tag_td)

    tag_div = bs.div

    # tag_a = bs.a          # 방법 1. 전체 html 안에서 a 찾기
    tag_a = tag_div.a       # 방법 2. div태그 안에서 a 찾기 : 범위를 줄였으니 당연히 더 빠르다.

    print(type(tag_a))      # string type이 아니라 element
    print(tag_a)            # print함수가 가져와서 string 형태로 출력해준다. (__str__구현되어있나봄)

    # 태그의 속성까지 사용해서 데이터를 가져오는 편이 더 정확하다.


# 2. attribute로 조회하기
def ex02():
    bs = BeautifulSoup(html, 'html.parser')
    # tag_td = bs.find('td', attrs={'class': 'title'})              # class가 title인 td태그
    # 여러 class를 갖는 태그를 찾을 때에는 검색 조건에 list 사용
    tag_td = bs.find('td', attrs={'class': ['title', 'black']})
    # print(tag_td)

    tag_div = bs.find('div', attrs={'class': 'tit3'})
    print(tag_div)


if __name__ == '__main__':
    # ex01()
    ex02()