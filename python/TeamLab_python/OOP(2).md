# 객체지향(OOP) (2)

> **O**bjective-**O**riented **P**rogramming 특징 정리



## Characteristics 1. Inheritance(상속)

​	: 부모 클래스로부터 속성과 Method를 물려받은 자식 클래스 생성

- 상속 Example

```python
Class Person(object): # Person -> 부모클래스
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def about_me(self): # Method 선언
        print("이름은", self.name, "이며, 나이는", str(self.age), "살 입니다.")
        
 Class Employee(Person):
     def __init__(self, name, age, gender, salary, hire_date):
         super().__init__(name, age, gender) #부모 객체의 변수를 사용해라
         self.salay = salary #속성 추가
         self.hire_date = hire_date
     
     def do_work(self): #새로운 Method 추가
         print("Work hard")
         
     def about_me(self):  #부모 클래스 함수 재정의
         super().about_me() #부모 클래스의 about_me 함수 사용
         print("급여는 ", self.salary, "원 이고, 입사일은 ", self.hire_date, "입니다.") #추가로 출력할 내용
```



## Characteristics 2. Polymorphism(다형성)

- 같은 이름의 Method의 **내부 로직을 다르게 작성**

  - Method의 역할은 같지만 입력 값이 다를 경우 

- Python에서는 같은 부모 클래스를 상속받는 경우 주로 발생

  - Example

    ```python
    class Person(object):
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def do_work(self):
            print("행복하게 생활하기")
            
    class Employee(Person):
    		(생략)
        def do_work(self): 
             print("일 열심히 하기")
             
    class Student(Person):
        (생략)
        def do_work(self):
            print("공부 열심히 하기")
    ```

  

## Characteristics 3. Visibility(가시성)

- 객체 정보를 볼 수 있는 레벨을 조절

  (1) 객체 사용자가 임의로 수정하는 것을 방지

  (2) 필요 없는 정보 접근 제어

  (3) 소스의 보호

  

---

#### [추가 상식]

- Encapsulation

  - 캡슐화 or 정보 은닉
  - Class 설계 시, Class 간 간섭/정보 공유 최소화 해야 한다는 개념
  - Class의 Interface(Input, parameter, return 등)만 알아도 원활히 활용 가능

  

  