# DemoRE.py

# 정규표현식(re)
import re

# re내부 함수 match()
result = re.match("[0-9]*th", "35th")
print( result )

result2 = result.group()
print( result2 )

# search() 함수와 match() 함수의 차이점
# search는 시작, 중간, 종료 아무데나 포함만되면 true
# match는 정확하게 전체가 일치
print( bool(re.match("[0-9]*th", "  35th")) )
print( bool(re.search("[0-9]*th", "  35th")) )

# 우편번호를 포함(5자리 digit)
print( bool(re.search("\d{5}", "우리 동네는 52000")) )

result = re.search("\d{4}", "올해는 2021년")
print( result.group() )

# apple이란 단어
print( bool( re.match("apple", "this is apple")) )
print( bool( re.search("apple", "this is apple")) )
