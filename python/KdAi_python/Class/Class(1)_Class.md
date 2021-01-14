# Class

> 도서 : 파이썬 정복(한빛미디어, 15장)
>
> 개발 환경 : *Jupiter notebook*

- 객체지향의 가장 기본적인 개념
- 파이썬은 스크립트 언어이므로, `Class`를 배우기에 적합하지는 않음
- 객체 지향의 특징 
  - 캡슐화
  - 추상화
  - 다형성
  - 상속



## 1. 캡슐화

- 모델링 결과를 `Class`로 포장하는 것

  *모델링 : 사물을 분석하여 속성과 동작을 추출*

```python
## capsule 1

balance = 8000 # 예금 잔액 

def deposit(money): # 입출금 동작 수행
    global balance
    balance += money
  
def inquire(): # 잔액 조회 & 출력
    print("잔액은 %d원 입니다." % balance)
    
deposit(1000)
inquire()    
```

```python
# 실행 결과
잔액은 9000원 입니다.
```

- 캡슐화하면, 여러 객체를 만들기 쉬워짐

```python
## capsule 2

class Account:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, money):
        self.balance += money
    def inquire(self):
        print("잔액은 %d원 입니다." % self.balance)

# 객체 1
sinhan = Account(8000)
sinhan.deposit(1000)
sinhan.inquire()

# 객체 2
kb = Account(120000)
kb.inquire()
```

```python
# 실행 결과
잔액은 9000원 입니다.
잔액은 120000원 입니다.
```



## 2. 생성자

- 객체를 초기화하는 `__init__` 생성자

- `Class` 호출하여 객체를 생성하기 위한 가장 먼저 선언하는 값

- 초기값을 선언해야 추가 메서드를 사용할 수 있음 

  ```python
  class 이름:
      def __init__(self, 초기값):
          멤버 초기화
      추가 메서드 정의
  ```



## 3. 상속

- 부모 클래스의 메서드 기능을 사용할 때 **'상속'**을 통해 메서드를 활용할 수 있음
- 부모 클래스 : 참조하고자하는 메서드 기능을 정의한 클래스(상위 클래스)

```python
class 이름(부모 클래스):
    ....
```

- Example

  ```python
  ## 부모 클래스
  
  class Human:
      def __init__(self, age, name):
          self.age = age
          self.name = name
          
      def intro(self):
          print(str(self.age) + "살 " + self.name + "입니다.")
  ```

  ```python
  ## Inheritance & Overriding
  
  class Student(Human):
      def __init__(self, age, name, stunum):
          super().__init__(age, name) #부모 Class(Human)에서 정의한 age, name 사용
          self.stunum = stunum
          
      def intro(self):
          super().intro() #부모 Class(=Human)의 intro 함수 기능을 포함
          print("학번 : " + str(self.stunum)) #추가 기능 => 재정의, 오버라이딩(override)
          
      def study(self):
          print("하늘천 땅지 검을현 누를황")
  ```

  ```python
  # 부모 클래스(Human) 실행 결과
  
  bom = Human(20, '보미')
  bom.intro()
  
  >> 20살 보미입니다.
  ```

  ```python
  # 자식 클래스(Student) 실행 결과
  
  bomi = Student(20, '보미', 1234567)
  bomi.intro()
  
  >> 20살 보미입니다.  #부모 클래스의 기능을 그대로 물려받음
     학번 : 1234567
  ```

  



