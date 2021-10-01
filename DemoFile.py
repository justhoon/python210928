# DemoFile.py

for x in range(1,6):
    print(x, "*", x, "=", x*x)

for x in range(1,6):
    print(x, "*", x, "=", str(x*x).rjust(3))

print("--서식문자--")
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:,}".format(1500000))

# 텍스트 파일 읽기 쓰기
f = open("c:\\work\\demo.txt", "wt")
f.write("첫번째\n두번째\n세번째\n")
f.close()

f = open("c:\\work\\demo.txt", "rt")
result = f.read()
print( result )
f.close()

f = open("c:\\work\\demo.txt", "rt")
print("어디쯤 읽고있니 : ", f.tell() )

# 처음으로 돌아가
f.seek(0)
print(f.readline())
print(f.readline())

print("어디쯤 읽고있니 : ", f.tell() )

# 리스트에 리턴
f.seek(0)
lst = f.readlines()
print( lst )
f.close()