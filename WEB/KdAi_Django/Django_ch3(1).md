# Django #1. 애플리케이션 생성(1)

프로젝트 및 애플리케이션 개발하기 (1)

-> 프로젝트 디렉토리 생성부터 데이터베이스 파일 생성까지



*참고 도서 : Django로 배우는 쉽고 빠른 웹 개발 파이썬 웹 프로그래밍*



## 프로젝트 뼈대 만들기

**프로젝트 및 앱 개발에 필요한 디렉토리와 파일 생성**

- 모델 코딩 : 테이블 관련 사항을 개발 (models.py , admin.py 파일)

- urlconfig 코딩 : url 및 뷰 매핑 관계를 정의  (urls.py 파일 2개 : \mysite\urls.py , \polls\urls.py)

- 템플릿 코딩 : 화면 UI 개발(template\ 디렉토리 하위의 *.html 파일)
- 뷰 코딩 : 애플리케이션 로직 개발 (views.py 파일)



#### 1) 프로젝트 생성
   - 프로젝트를 생성할 디렉토리에 다음의 명령어를 입력

```shell
> django-admin startproject 프로젝트 이름

# 실습 예제에서 사용한 프로젝트 이름 [mysite]
> django-admin startproject mysite
```

- `mysite`의 이름은 **프로젝트 루트 디렉토리**이자 **프로젝트명** -> 원하는데로 변경 가능

- 최상위의 `mysite` 디렉토리와 하위 `mysite` 디렉토리가 **동일한 이름**으로 생성됨

  -> 혼동할 수 있으므로 **루트 디렉토리**의 이름을 변경해도 무방함(변경 권장)

```shell
# 디렉토리 이름 변경 명령어(window)
> move mysite ch3
# 디렉토리 이름 변경 명령어 (Linux, Mac)
$ mv mysite ch3
```



#### 2) 애플리케이션 생성
   - **루트 디렉토리** 밑에 새로운 애플리케이션을 생성

```shell
> python manage.py startapp 애플리케이션이름

# 실습 예제에서 사용한 애플리케이션 이름 [polls]
> python manage.py startapp polls
```

* 참고 : 프로젝트는 여러 개의 애플리케이션을 포함할 수 있음



#### 3) 프로젝트 설정 파일 변경 (`settings.py` : 프로젝트의 전반적 사항을 설정)

   - `atom settings.py` : 루트 디렉토리의 `settings.py` 파일 열기

     

   (1) `ALLOWED_HOSTS` 지정

- `DEBUG=Ture` : 개발모드 (서버 IP 값 지정하지 않아도 무방)
  
- `DEBUG=False` : 운영 모드 (서버의 IP, 도메인 지정 필수) 
  
```python
ALLOWED_HOSTS = ['개인 IP address 입력', 'localhost', '127.0.0.1']
```



   (2) `INSTALLED_APPS` : 애플리케이션 등록

   - `polls` 디렉토리의 `app.py` 파일의 `PollsConfig` Class 입력

   ```python
   INSTALLED_APPS = [
   	...생략...
   	'polls.apps.PollsConfig', #polls 디렉토리의 app.py파일의 PollsConfig Class
   ]
   ```

 

  (3) `DATABASES` : 데이터베이스 엔진 설정

- `Django`의 디폴트 데이터베이스는 `SQLite`
- `SQLite`를 사용할 것이라면, 별도의 수정 혹은 설정없이 그대로 사용

```python
DATABASES = {
	'default':{
	...생략...
	}
}
```



(4) `TIME_ZONE`: 시간 지정

```python
TIME_ZONE = 'Asia/Seoul'
```



#### 4) 기본 데이터베이스 파일 생성

- 테이블 생성 전, 개발 시작 시 명령 실행 -> `db.sqlite3`파일 생성하기

```shell
ch3> python manage.py migrate
```



#### 5) 작업 결과 확인 (`runserver`)

```shell
ch3> python manage.py runserver 0.0.0.:8000
```



#### 6) `Admin` 설정

- Django에서는 기본적으로  `Admin` 기능을 제공

```sh
# Admin 페이지 접속
http://127.0.0.1:8000/admin
```

- 관리자(super-user) 생성

```shell
ch3> python manage.py createsuperuser
# Username / Email / PassWord 차례로 입력
```



