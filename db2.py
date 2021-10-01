# db2.py

import sqlite3

# 먼저 메모리에만 저장(파일엔 저장안하고 메모리에만 임시 저장 -> 연습할때 많이쓴다)
# con = sqlite3.connect(":memory:")

# test.db 파일에 저장
con = sqlite3.connect("c:\\work\\sample.db")

# 커서 객체를 생성
cur = con.cursor()

# 테이블 구조 만들기(테이블 스키마 생성)
cur.execute("create table PhoneBook (Name text, PhoneNum text);")

# 1건 데이터 입력
cur.execute("insert into PhoneBook values ('derick', '010-222');")

# 입력 데이터 파라미터 처리
name = "gildong"
phoneNum = "010-123"
# 파라미터가 여러개니까 튜플()로 처리
cur.execute("insert into PhoneBook values (?,?);", (name, phoneNum))

# 한번에 여러개의 레코드(row) 입력
datalist = (("tom", "010-333"), ("dsp", "010-567"))
cur.executemany("insert into PhoneBook values (?,?);", datalist)

# 검색 해서 결과 보기
cur.execute("select * from PhoneBook;")
# 다중 라인 주석처리 : ctrl + /
# for row in cur:
#     print(row)

print("---1건---")
print( cur.fetchone() )
# select 한번 하면 버퍼에 한번만 적재되고 fetch할때마다 다음 row로 버퍼 넘어간다
print("---2건---")
print( cur.fetchmany(2) )
print("---전체---")
# 따라서 전체 조회하려면 select 다시 해서 전체 데이터를 버퍼에 채워줘야한다
cur.execute("select * from PhoneBook;")
print( cur.fetchall() )

# 정상적으로 종료하기
con.commit()
# 연결 끊고 나가기
con.close()