# 객체지향(OOP) (1)

> **O**bjective-**O**riented **P**rogramming 개념 정리



## 1. 클래스(Class) 와 인스턴스(instance)

- `클래스(Class)` : 속성을 가진 설계도
- `Instance(or object)` : 설계도를 이용하여 만든 객체
- Example - 붕어빵
  - `Class` : 붕어빵틀
  -  `Instance` : 고구마맛 붕어빵, 말차맛 붕어빵, 크림치즈 붕어빵 (속성 : 맛)



## 2. Objects in Python

- 축구 선수 정보 `Class`로 구현하기

  - `Class` 는 **속성(Variable)** 과 **행동(Function)** 으로 이루어짐

  - `self` : `Class`로 생성한 `instance`를 의미 **(Class를 의미하는 것이 아님)**

    ```python
    son = SoccerPalyer("HeungMin", "FW", 7)
    
    class SoccerPlayer(object):
        def __init__(self, name, position, back_number):
            self.name = name # son(instance 명).name = "HeungMin" -> son.name에 "HeungMin"을 할당
            self.position = position # son(instance 명).position = "FW" -> son.position에 "FW"를 할당
            self.back_number = back_number # son(instance 명).back_number = 7 -> son.back_number에 7 할당
    ```

    

  (1) Variable

  - Varialbe 추가는 `__init__`, `self` 로 가능

    - `__init__`은 객체 초기화 예약 함수
    - _ 는 특수한 예약 함수, 변수에 사용됨

    e.g. `__main__`, `__add__`, `__str__`

    ```python
    class SoccerPlayer(object):
        def __init__(self, name, position, back_number):
            self.name = name
            self.position = position
            self.back_number = back_number
        def __str__(self): #print(son) 실행 시 출력 
            return "I play in %s in center." %
            (self.name, self.position) # '__str__'함수의 return값은 반드시 "str" type 이어야 함
            
    son = SoccerPlayer("Son", "MF", 10) # __init__함수 초기 값
    print(son)
    ```

  (2) Function

  - `self`를 추가해야만 `Class` 함수로 인정됨

    ```python
    class SoccerPlayer(object):
        def change_back_number(self, new_number):
            print("선수의 등번호를 변경합니다 : From %d to %d" % (self.back_number, new_number))
            self.back_number = new_number # 새로운 번호 할당
    ```

  (3) object(Instance) 

  - `SoccerPlayer`라는 `Class` 로 **각기 다른 이름, 포지션, 등 번호 (속성)**을 가진 여러 명의 선수(player)를 생성

    ```python
    class SoccerPlayer(object): #CamelCase naming (하단에 설명)
           def __init__(self, name, position, back_number):
              self.name = name # 선수 이름
              self.position = position # 선수 포지션
              self.back_number = back_number # 선수 등 번호
    ```

    

---

#### [Naming 상식]

- 변수, Class 명, 함수명 짓는 방식
  - `snake_case` : 띄워쓰기 부분에 "_" 추가 -> **함수명, 변수명**에 사용
  - `CamelCase` : 띄워쓰기 부분에 대문자 -> **Class 명**에 사용