# Django #1. 애플리케이션 생성(2)

프로젝트 및 애플리케이션 개발하기 (2) 

-> Model 코딩 (`models.py` & `admin.py`)



*참고 도서 : Django로 배우는 쉽고 빠른 웹 개발 파이썬 웹 프로그래밍*



## Model 코딩

**데이터베이스에 테이블 관련 사항 개발 (`admin.py`, `models.py`)**

- 테이블 정의
- 정의된 테이블 `Admin` 페이지에 적용
- 데이터베이스 변경 사항 확인
- 데이터베이스에 변경 사항 반영
- 작업 결과 확인



#### 1) 테이블 정의 (`Models.py`)

- `polls`(애플리케이션)의 `models.py` 파일 열어 작업

```shell
polls> atom models.py
```

- 필요한 테이블 `class`로 생성
- `PK` 는 Django에서 자동으로 생성

```python
from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
```



#### 2) `Admin` 페이지에 적용 (`admin.py`)

- `polls`의 `admin.py` 파일 열어 작업

```shell
polls> atom admin.py
```

- 앞서 생성한 테이블 정보 추가

```python
from django.contrib import admin
from polls.models import Question, Choice

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
```



***새로운 테이블 생성 시, `models.py` 와 `admin.py` 두 개의 파일 모두 수정해야함**



#### 3) 데이터베이스 변경 사항 확인

```shell
polls> python manage.py makemigrations
```

- 생성한 테이블 정보 및 추가 수정 정보 목록 확인 가능



#### 4) 데이터베이스에 변경 사항 적용

```shell
polls> python manage.py migrate
```

- 참고 : migrate 명령 시, Django가 사용하는 SQL문 확인 명령

  ```shell
  python manage.py sqlmigrate polls 0001
  ```



#### 5) 작업 결과 확인

- 생성한 테이블이 `admin` 페이지에 추가된 것 확인

```shell
#runserver 실행 중인 상태여야 함
http://127.0.0.1:8000/admin
```

