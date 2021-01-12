# Python 정복(파일)

> *개발환경 : jupyter notebook*
>
> 참고 : 파이썬 정복(한빛미디어, 14장)



## 1. 파일 쓰기

```python
open(파일경로, 모드)
write() #저장할 내용 작성
close() #파일 닫기
```

| 모드 |       설명       |
| :--: | :--------------: |
|  r   | 파일 읽기 (read) |
| w	|	파일 기록 (write) , 동일 파일이 이미 있는 경우 덮어씀 |
| a | 파일에 데이터 추가 (add) |
| x | 파일에 기록, 동일 파일이 이미 있는 경우 저장 취소됨 |

- 모드는 **모드+파일 종류 문자**로 사용됨
  - 파일 종류 문자 : t [텍스트 파일], b [이진 파일]
  - Default 모드 : `rt` -> 텍스트 읽기 모드

- Example

  ```python
  f = open("poem.txt", "wt") #파일 열기 (기록 모드 + 텍스트 파일)
  f.write("""죽는 날까지 하늘을 우러러, 
  한 점 부끄럼이 없기를 
  잎새에 이는 바람에도 나는 괴로워 했다.""") #텍스트 작성
  f.close() #파일 닫기
  ```

  - `open` 함수에 경로 입력 X -> 코드 실행한 경로에 자동 저장되어짐

## 2. 파일 읽기

 - `read` : 파일 전체 한 번에 읽는 함수 

    -  *대용량 파일인 경우 많은 메모리 소모* -> `read` 함수 인수 지정하여 일정 부분 읽어오기

   ```python
   try:
       f = open("poem.txt", "rt") #파일 열기 (읽기 모드 + 텍스트 파일)
       text = f.read() #read(10) -> 10 문자씩 출력
       print(text)
   except FileNotFoundError:
       print("파일이 없습니다.") #파일이 없는 경우 메시지 출력
   finally:
       f.close() #파일 오류 발생하더라도 "닫기"가 실행될 수 있도록
     
     >> 죽는 날까지 하늘을 우러러 
     	 한 점 부끄럼이 없기를 
   		 잎새에 이는 바람에도 나는 괴로워 했다.
   ```



- `readline` : 파일을 한 줄씩 읽어오는 함수

  ```python
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
  
  >> 1 : 죽는 날까지 하늘을 우러러, 
     2 : 한 점 부끄럼이 없기를 
     3 : 잎새에 이는 바람에도 나는 괴로워 했다.
  ```

- `readlines` : 파일 전체를 읽고 문자열 한 줄씩 **리스트**로 반환

  ```python
  f = open("poem.txt", "rt") #파일 열기 (읽기 모드 + 텍스트 파일)
  rows = f.readlines() #type(row) -> list
  for row in rows:
      print(row, end = "")
  f.close()
  
  >> 죽는 날까지 하늘을 우러러, #rows[0]
  	 한 점 부끄럼이 없기를 #rows[1]
  	 잎새에 이는 바람에도 나는 괴로워 했다. #rows[2]
  ```



## 3. 입출력 위치

- 순차 접근 : 파일을 순서대로 읽음

- 임의 접근 : 입출력 위치를 바꿔가며 원하는 부분을 자유롭게 읽음

- `tell` : 입출력 위치 조사

  ```python
  
  ```

  

- `seek` : 입출력 위치 지정

  ```python
  seek(위치, 기준)
  ```

  - Example

  ```python
  f = open("poem.txt", "rt")
  f.seek(12,0)
  text = f.read()
  f.close()
  print(text)
  ```



## 4. 내용 추가

 - `a` 모드 : 기존 내용 유지하고 뒤에 덧붙임 (=append)

   ```python
   f = open("poem.txt", "at") #파일 열기 (append모드 + 텍스트 파일)
   f.write("\n\n윤동주-서시")
   f.close()
   
   #저장한 내용 확인
   f = open("poem.txt", "rt") #파일 열기 (읽기 모드 + 텍스트 파일)
   text = f.read()
   f.close()
   print(text)
   
   >> 죽는 날까지 하늘을 우러러, 
      한 점 부끄럼이 없기를 
      잎새에 이는 바람에도 나는 괴로워 했다.
   
      윤동주 - 서시
   ```

   

 - `w` 모드 : 파일이 이미 있는 경우, 덮어쓰기

   ```python
   f = open("poem.txt", "wt") #파일 열기 (append모드 + 텍스트 파일)
   f.write("윤동주 - 서시")
   f.close()
   
   #저장한 내용 확인
   f = open("poem.txt", "rt") #파일 열기 (읽기 모드 + 텍스트 파일)
   text = f.read()
   f.close()
   print(text)
   
   >> 윤동주 - 서시
   ```

- `with~as` : 자동으로 `close`실행

  ```python
  with open("poem.txt", "rt") as f:
      text = f.read()
  print(text)
  ```

   