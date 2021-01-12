# Python 정복 (문자열)

> *개발환경 : jupyter notebook*
>
> 참고 : 파이썬 정복(한빛미디어, 10장)



## (1) 슬라이스

- `[begin : end : step]`

- `end` : 지정한 숫자 - 1 번째 인자까지 출력

- `step` : 출력 간격을 의미

  ```python
  yoil = "월화수목금토일"
  print(yoin[: : 2]) #1
  print(yoil[: : -1]) #2
  
  월수금일 #1
  일토금목수화월 #2
  ```



## (2) 문자열 메서드

 ### 1. 검색

    ```python
    s = "python programming"
    print(len(s)) #내장함수
    print(s.find('o')) #변수 s에서 'o'를 검색 -> 'o' 위치 return
    print(s.rfind('o')) #변수 s에서 'o'를 뒤에서부터 검색 -> 'o' 위치 return
    print(s.index('r')) #변수 s에서 'r'의 위치 return
    print(s.count('n')) #변수 s에서 'n'의 개수 return
    
    18 #len(s)
    4 #s.find
    9 #s.rfind (rear find)
    8 #s.index
    2 #s.count
    ```
    
    - 내장함수와 객체 소속의 메서드는 호출 방식이 다름
      - `len()` : len(변수)
      - `find` : 변수.find
      
    - `find, rfind` : 검색한 문자가 존재하지 않으면  -1 반환
    
    - `index` : 검색한 문자가 존재하지 않으면 예외 발생 -> 예외 처리 필요
    
    - `count` : `count('sub')` 식의 부분 문자열도 검색 가능


​      

### 2. 조사

   - `in` : 특정 문자의 존재 여부만 파악해주는 메서드 *(True or False 반환)*
   - `startswith` : 특정 문자열로 시작되는지 조사, 앞부분의 일부만 비교
   - `endswith` : 특정 문자열로 끝나는지 뒷부분만 비교


   ```python
   word = apple
   if word.startswith("a"):
     print("a")
   if word.startswith("c"):
     print("c")
   
   file = "carrot.jpg"
   if file.endswith(".jpg"):
     print("jpg file")
   ```

   - `startswith, endswith` : 문자열 중간까지 검색하는 `find, count`와 달리, 앞부분/뒷부분의 문자열만 검색 

   - 기타 조사 메서드

     | 함수      | 설명                        |
     | --------- | --------------------------- |
     | `isalpha` | 모든 문자가 알파벳인지 조사 |
     | `islower` |	모든 문자가 소문자인지 조사 |
     | `isupper` | 모든 문자가 대문자인지 조사 |
     | `isspace` | 모든 문자가 공백인지 조사 |
     | `isalnum` | 모든 문자가 알파벳 또는 숫자인지 조사 |
     | `isdecimal`| 모든 문자가 숫자인지 조사 |
     | `isdigit` | 모든 문자가 숫자인지 조사 : 유니코드 '/u00B2' (== sqaure)값 인식 |
     | `isnumeric` | 모든 문자가 숫자인지 조사 : 유니코드 '/u00BD'(==1/2) 값 인식 |
     | `isidentifier` | 명칭으로 쓸 수 있는 문자 구성인지 조사 |
     | `isprintable` | 인쇄 가능한 문자 구성인지 조사 |

     

### 3. 변경

   - **메서드를 적용하여도, original 변수의 값은 변하지 않음**

   ```python
   s = "Good night. sweet dreams"
   print(s.lower()) #전체 문자열 소문자로 변경
   print(s.upper()) #전체 문자열 대문자로 변경
   print(s)
   
   print(s.swapcase()) #대문자는 소문자로, 소문자는 대문자로 변경
   print(s.capitalize()) #맨 첫 문자만 대문자로 변경
   print(s.title()) #문장 별 첫 문자를 대문자로 변경
   ```

   - `strip`
     - `lstrip()` : 왼쪽 공백 제거
     - `rstrip()` : 오른쪽 공백 제거
     - `strip()` : 양쪽 공백 제거

### 4. 분할
   - `split()` : 공백/지정 구문자를 기준으로 문자열 분할
   - `splitlines()` : 행별로 문자열 분할
   - `join` : 문자 사이 구분자 추가

### 5. 대체
   - `replace(a, b)` : a를 b로 대체 -> 문자열 전체에서 a를 찾아 b로 대체
   -   `just`
     - `ljust()` : 왼쪽 정렬 (정렬 폭 지정)
     - `rjust()` : 오른쪽 정렬 (정렬 폭 지정)
     - `center()` : 중앙 정렬 (정렬 폭 지정)

