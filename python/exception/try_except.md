# Python 정복(예외 처리)

> 예외 상황을 다루기 위한 **예외 처리** 
>
> *개발환경 : jupyter notebook*
>
> 참고 : 파이썬정복(한빛미디어, 13장)



## 1. 예외 처리

```python
try:
  실행할 명령
except 예외 as 변수:
  오류 처리문
else:
  예외가 발생하지 않을 때의 처리
```

- Example

  ```python
  str = "89점"
  try:
    score = int(str)
    print(score)
  except:
    print("예외가 발생했습니다")
  else:
    print(score)
    
  print("작업 완료")
  ```

  

- 예외의 종류

  - `NameError` : 정의된 변수가 없는 경우

    ```python
    str = "당근"
    print(std)
    
    >> NameError: name 'std' is not defined
    ```

    

  - `ValueError` : 값의 형식 오류

    ```python
    str = "당근 77개"
    print(int(str))
    
    >> ValueError: invalid literal for int() with base 10: '당근 77개'
    ```

    

  - `ZeroDivisionError` : 0으로 나눈 경우

    ```python
    str = 7
    print(str/0)
    
    >> ZeroDivisionError: division by zero
    ```

    

  - IndexError : 첨자 범위를 이탈한 경우

    ```python
    str = "당근"
    print(str[5])
    
    >> IndexError: string index out of range
    ```

    

  - `TypeError` : 타입이 맞지 않은 경우

    ```python
    str = 5
    num = "15"
    print(num/str)
    
    >> TypeError: unsupported operand type(s) for /: 'str' and 'int'
    ```



## 2. raise

>  고의로 예외를 발생시키는 명령어

```python
#1부터 지정 범위까지의 정수 합계 구하기

def calcsum(n):
  if (n < 0): #음수 입력 시 예외 발생시킴
    raise ValueError
  sum = 0
  for i in range(n+1):
    sum += i
 	return sum

try:
  print("~10 = ", calcsum(10))
  print("~-5 = ", calcsum(-5))
except ValueError:
  print("입력값이 잘못되었습니다.")
```

- `get` : `dictionary`에 찾는 `key`가 없으면 `None`을 반환

  - `dictionary` 타입의 예외를 처리할 때 사용 가능

  ```python
  dic = {'boy':'소년', 'book':'책', 'apple':'사과'}
  check = dic.get('carrot')
  print(check)
  
  >> None
  ```

  

## 3. funally

> 예외 발생 여부에 상관없이 반드시 실행해야 할 명령 지정

 - Example

   ```python
   try:
   	print("네트워크 접속")
   	a = 2 / 0 #ZeroDivisionError 발생
   	print("네트워크 통신 수행")
   finally:
     print("접속 해제") #예외 발생 시에도 접속 해제 되었음을 알려줌
   print("작업 완료")
   ```



## 4. assert

> 프로그램 현재 상태가 맞는지 확인

```python
assert 조건, 메시지
```

- Example

  ```python
  score = 130
  assert score<=100, "점수는 100 이하여야 합니다"
  print(score)
  
  >> AssertionError: 점수는 100 이하여야 합니다
  ```

  