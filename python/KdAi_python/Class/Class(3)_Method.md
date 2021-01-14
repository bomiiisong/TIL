# Method

- Class Method
- 연산자 Method
- 특수 Method



## 1. Class Method



## 2. 연산자 Method



## 3. 특수 Method

| Method  | 설명 |
| ------- | ---- |
| __str__ | 객체를 문자열화     |
| __repr__ |  객체 표현식 생성 |
| __len__ | 객체의 길이 조사 |

- `__str__` 사용 시 결과

```python
## __str__

class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    
    def __str__(self):
        return "이름 %s, 나이 %d" % (self.name, self.age)
      
song = Human(20, 'bomi')
print(song)
```

```python
# 실행 결과
이름 송보미, 나이 20
```



* `__str__` 사용 안 했을 때 결과

  ```python
  class Human:
      def __init__(self, age, name):
          self.age = age
          self.name = name
          
      def intro(self):
          print("이름 %s, 나이 %d" % (self.name, self.age))
          
  song = Human(20, 'bomi')
  print(song)
  ```

  ```python
  # 실행 결과
  <__main__.Human object at 0x7fc382da4250>
  ```

  