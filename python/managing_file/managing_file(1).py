#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##파일 열기, 기록, 닫기

f = open("poem.txt", "wt") #파일 열기 (기록 모드 + 텍스트 파일)
f.write("""죽는 날까지 하늘을 우러러, 
한 점 부끄럼이 없기를 
잎새에 이는 바람에도 나는 괴로워 했다.""") #텍스트 작성
f.close() #파일 닫기


# In[ ]:


##read()

try:
    f = open("poem.txt", "rt") #파일 열기 (읽기 모드 + 텍스트 파일)
    text = f.read() #read(10) -> 10 문자씩 출력
    print(text)
except FileNotFoundError:
    print("파일이 없습니다.") #파일이 없는 경우 메시지 출력
finally:
    f.close() #파일 오류 발생하더라도 "닫기"가 실행될 수 있도록


# In[ ]:


##readline()

f = open("poem.txt", "rt") #파일 열기 (읽기 모드 + 텍스트 파일)
text = ""
line = 1
while True:
    row = f.readline() #poem.txt 의 내용을 한 줄씩 저장
    if not row: #더 이상 내용이 없으면 종료
        break
    text += str(line) + " : " + row #각 줄의 index + 내용 출력
    line += 1 #index 숫자 1씩 증가 
f.close()
print(text)


# In[ ]:


##readlines

f = open("poem.txt", "rt") #파일 열기 (읽기 모드 + 텍스트 파일)
rows = f.readlines() #type(row) -> list
for row in rows:
    print(row, end = "")
f.close()


# In[ ]:


##tell


# In[ ]:


##seek(위치, 기준)

f = open("poem.txt", "rt")
f.seek(12,0)
text = f.read()
f.close()
print(text)


# In[ ]:


##a(=append)모드

f = open("poem.txt", "at") #파일 열기 (append모드 + 텍스트 파일)
f.write("\n\n윤동주 - 서시") #\n : 줄 바꿈
f.close()

#저장한 내용 확인
f = open("poem.txt", "rt") #파일 열기 (읽기 모드 + 텍스트 파일)
text = f.read()
f.close()
print(text)


# In[ ]:


##w모드 : 덮어쓰기

f = open("poem.txt", "wt") #파일 열기 (append모드 + 텍스트 파일)
f.write("윤동주 - 서시")
f.close()

#저장한 내용 확인
f = open("poem.txt", "rt") #파일 열기 (읽기 모드 + 텍스트 파일)
text = f.read()
f.close()
print(text)


# In[ ]:


##with ~ as : 자동으로 close 실행

with open("poem.txt", "rt") as f:
    text = f.read()
print(text)

