# DemoSTR

# 앞뒤에 공백문자 제거
strB = "<<  spam and ham  >>"
print(strB)

# 문자열 전처리
result = strB.strip("<> ")
result = result.replace("spam", "spam egg")
print(result)
print("---리스트---")
lst = result.split()

print(lst)
print("---하나의 문자열---")
print( ":) ".join(lst) )

