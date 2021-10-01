# Try1.py

def divide(a,b):
    return a/b

# 함수 호출
try :
    result = divide(5,"aaa")
    result2 = divide(5,0)
    
except ZeroDivisionError:
    print("0으로 나누면 안됩니다.")
except TypeError:
    print("숫자만 입력 가능합니다.")
else:
    print("결과1 : {0}".format(result))
    print("결과2 : {0}".format(result2))
finally:
    print("한번 더 체크")


print("전체 코드 실행 종료")

