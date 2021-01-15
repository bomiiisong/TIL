# 모듈

- 어떤 대상의 부분 또는 조각

  e.g. 레고 블록, 자동차 부품

- 프로그램에서는 **작은 프로그램 조각**

- 프로그램 모듈화 장점 : 다른 프로그램/다른 사용자가 이용하기 쉬움

  - e.g. 카카오 게임을 위한 카카오톡 접속 모듈

- Python에서 모듈 == `.py`

  - 같은 폴더 내에 있는 `.py` 파일(모듈)은 다른 파이썬 파일에서 `import`로 호출 가능



### (1) Built-in Module

- Python이 제공하는 기본 모듈 -> 추가 조치없이 바로 사용 가능
- 대표적인 `Built-in Module`
  - `random` : 난수
  - `time` : 시간
  - `urllib.request` : 웹



### (2) Namespace 사용

- `Alias` 설정

  ```python
  import numpy as np #np라는 별칭 설정
  ```

- 모듈에서 특정 함수 또는 클래스만 호출

  ```python
  from sklearn import train_test_split
  ```

- 모듈에서 모든 함수 또는 클래스 호출

  ```python
  from sklearn import * # '*'문자는 모듈의 전체 함수를 호출
  ```

  

# 패키지(라이브러리)

> 참고 도서 : *점프 투 파이썬*

- 하나의 대형 프로젝트를 만드는 코드의 묶음

- 모듈을 계층적 구조로 관리할 수 있음

  e.g. 모듈 이름 : A.b -> A는 패키지, b는 모듈

- 다양한 오픈소스들이 패키지로 관리되고 있음

- 패키지 만들기

  (1) 세부 기능을 나눠 폴더로 만듦

  ```python
  # 가상의 game 패키지 (점프투파이썬 예시 자료)
  
  game/ # root 디렉터리
  		__init__.py
    	sound/  #서브 디렉터리
      		__init__.py
        	echo.py
          wav.py
      graphic/  #서브 디렉터리
      		__init__.py
        	screen.py
          render.py
      play/  #서브 디렉터리
      		__init.py
        	run.py
          test.py
  ```

  

  (2) 기능 폴더 별 모듈 (`.py`) 구현(함수 등)

  ```python
  #echo.py (예시)
  def echo_test():
      print("echo")
  ```

  - 함수 실행 방법

    ```python
    # 1.
    import game.sound.echo
    game.sound.echo.echo_test()
    
    #2.
    from game.sound import echo
    echo.echo_test
    
    #3.
    from game.sound.echo import echo_test
    echo_test() #어떤 패키지의 함수인지 알 수 없음. 비직관적
    ```

    

  (3)  폴더 별로 `__init__.py` 구성하기

  - `__init__.py`파일이 없으면 패키지로 인식되지 않음

    > python 3.3버전부터 `__init__.py`파일이 없어도 패키지로 인식
    >
    > 그러나 버전 호환을 위해 생성하도록 하자

   - `__init__.py` 파일에는 `import`와 `__all__ = [함수1, 함수2, ...]` 로 구성

   - `__init__.py` 생성 후에는 `import *`로 원하는 결과를 출력할 수 있음

     

  (4) `__main__.py` 파일 만들기

   - 패키지를 실행 파일로 만들기 위해 반드시 필요함

   - `.exe` 파일과 비슷하다고 생각하자

     

  #### 🔸상대경로 (중요) 

  - 다음과 같이 `__init__.py`를 작성한 후 `game`패키지를 실행하면 오류가 발생

  ```python
  #game/__init__.py
  
  import graphic
  import play
  import sound
  
  __all__ = ['graphic', 'play', 'sound']
  ```

  ```python
  from game.graphic.render import render_test
  
  ImportError: No module named 'graphic'
  ```

  오류가 발생하는 이유는 `__init__.py`에서 graphic을 import 할 때 **현재 디렉터리를 기준**으로 작성했기 때문이다. 즉, 최상위 폴더 `package`디렉터리 기준으로 graphic을 실행하려고 했기 때문에 graphic 모듈이 없다고 판단한 것이다. 

  이를 해결하기 위해 `__init__.py`파일을 다음과 같이 수정해야한다.

  ```python
  #game/__init__.py
  
  from . import graphic # `__init__.py`있는 현재 폴더 기준으로 graphic을 호출
  from . import play
  from . import sound
  
  __all__ = ['graphic', 'play', 'sound']
  ```

  버릇처럼 `__init__.py`파일 작성 시에는 `from . `을 붙이도록 하자

  

