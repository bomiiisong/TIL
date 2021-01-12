# Python 정복(표준 모듈)

> 함수의 모음으로, **패키지, 라이브러리** 라고도 불림
>
> *개발환경 : jupyter notebook*
>
> 참고 : 파이썬 정복(한빛미디어, 12장)

- 모듈 내 실행가능 함수 목록 확인 방법

  : `dir(모듈이름)`



## 1. 수학

	- `math`

## 2. 시간

- `time`	

  - `time.localtime()` : 현재 시간을 struct로 반환

    ```python
    import time
    
    now = time.localtime()
    print(now)
    
    >> time.struct_time(tm_year=2021, tm_mon=1, tm_mday=12, tm_hour=10, tm_min=43, tm_sec=25, tm_wday=1, tm_yday=12, tm_isdst=0)
    
    #활용
    print("%d년 %d월 %d일" % (now.tm_year, now.tm_mon, now.tm_mday))
    >> 2021년 1월 12일
    ```

- `datetime`

  - `timezone` : 위치 기반 시간대 설정(e.g. 한국시간, 미국시간 등)

- `sleep` : 실행동안 일정 시간차를 두어 실행

- 소요 시간 측정

  ```python
  import time
  
  start = time.time()
  for i in range(1000): 
    print(n)
  end = time.time()
  print(end - start)
  ```

 

 - `calendar` : 달력 객체 리턴

    - `calendar(year)` : 인수로 받은 년도의 달력 객체 반환

    - `month(year, month)` : 년도, 달을 인수로 받아 해당 월의 달력 객체 반환

    - `weekday(year, month, day)` : 해당 일자의 요일을 `index`로 반환

      ```python
      day = calendar.weekday(2021,8,15)
      print(day)
      
      >> 6   #일요일
      ```



## 3. 난수

	- `rand`  : 실수형 난수 반환
	- `randint(begin, end)` : 정수형 난수
	- `choice` : 리스트에서 임의의 요소 하나를 반환
	- `shuffle` : 리스트 요소 무작위 섞기
	- `sample(리스트, 뽑을 개수)` : 리스트에서 지정 개수만큼 sample 추출

