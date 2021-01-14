# 액세서

> 객체의 안정성 확보를 위해 사용하는 은폐 기능이 있어야 하지만,
>
> 파이썬은 공식적인 은폐 기능이 없음 -> 외부 누구나 접근 가능
>
> 이를 해결하기 위한 액세서
>
> 도서 : 파이썬 정복(한빛미디어, 15장)
>
> 개발 환경 : *jupyter notebook*



## 1. getter/setter

- `getter` : 클래스 멤버 값을 읽어주는 Method

- `setter` : 클래스 멤버 값을 변경하는 Method

  ```python
  ## getter/setter Method
  
  class Date:
      def __init__(self, month):
          self.month = month
      def getmonth(self):
          return self.month
      def setmonth(self, month):
          if 1 <= month <= 12:
              self.month = month
              
  today = Date(8)
  print(today.getmonth()) # return 8
  
  today.setmonth(15) # return 8
  print(today.getmonth())
  ```

- 문제점 : 여전히 클래스 멤버의 이름을 알고 있기 때문에 아무 값이나 대입 가능

- 해결방법 : (1)`property` 데코레이터 사용

  ​				(2) 멤버 이름 복잡하게 설정



## 2. Property

```python
## Property (1)

class Date:
    def __init__(self, month):
        self.inner_month = month
    def getmonth(self):
        return self.inner_month
    def setmonth(self, month):
        if 1 <= month <= 12:
            self.inner_month = month
    month = property(getmonth, setmonth)
    
## Property (2)

class Date:
    def __init__(self, month):
        self.inner_month = month
        
    @property #decorator -> getter
    def month(self):
        return self.inner_month
    
    @month.setter #setter
    def month(self, month):
        if 1 <= month <= 12:
            self.inner_month = month
```

- 문제점 : 숨겨진 멤버 이름도 알 수 있고, 이를 임의로 변경 가능

  ​			객체이름.`tab` key를 누르면 모든 클래스의 모든 멤버 조회 가능

- 해결방법 : 숨겨진 멤버 이름을 '__'로 시작 -> 바로 참조하지 못하게 방지



## 3. __변수

```python
## hidden

class Date:
    def __init__(self, month):
        self.__month = month
        
    def getmonth(self):
        return self.__month
    
    def setmonth(self, month):
        if 1 <= month <= 12:
            self.__month = month
            
    month = property(getmonth, setmonth)
```

- 참고 : __가 붙으면 내부의 실제 이름은 '`_클래스명__멤버명`'으로 변경됨
  - e.g. `_Date__month`