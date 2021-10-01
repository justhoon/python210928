# web1.py

# from 패키지명 import 모듈명
from bs4 import BeautifulSoup

# 페이지 로딩
page = open("c:\\work\\test01.html", "rt", encoding = "utf-8").read()

# 검색이 용이한 객체(soup) 생성
soup = BeautifulSoup(page, "html.parser")

# 전체 페이지 보기(순수하게 전체 페이지 보여줌)
print( soup.prettify() )

print( "---------------------" )

# 문서 내부에 <p> 검색
print( soup.find_all("p") )

print( "---------------------" )

# 첫번재 <p> 가져오기
print( soup.find("p") )

print( "---------------------" )

# 조건이 있는 경우 : <p class="outer-text">
# 파이썬의 키워드로 class가 제공되므로 충돌 피하고자 class_ 사용
print( soup.find_all("p", class_="outer-text") )

print( "---------------------" )

# 태그 안쪽에 문자열 검색 : .text 속성 사용
# <p> 문자열 </p>
for tag in soup.find_all("p"):
    title = tag.text
    title2 = title.replace("\n", "")
    title2 = title2.replace("\t", "")
    print( title2.strip() )