# MariaDB 설치 및 사용 방법

> Homebrew로 MariaDB 설치하고 사용하기

## 1. Homebrew update

```shell
$ brew update
```

## 2. MariaDB 설치

```shell
$ brew install mariadb
```

## 3. MariaDB server 실행

- **brew**로 설치한 경우

```shell
#MariaDB 서버 실행
$ brew services start mariadb
#MariaDB 접속
$ sudo mysql -u root

###참고 명령어###
#MariaDB 서버 상태 확인
$ brew services list
#MariaDB 서버 중지
$ brew services stop mariadb

```

- 홈페이지 Download인 경우

  ```sh
  #MariaDB 서버 실행
  $ mysql.server start
  #MariaDB 접속
  $ mysql -u root
  
  ###참고 명령어###
  #MariaDB 서버 상태 확인
  $ mysql.server status
  #MariaDB 서버 중지
  $ mysql.server stop
  ```

  

### MariaDB 설치 및 실행 과정 중 오류들

 	1. 기존에 설치되어 있던 `Mysql`로 인해 *Conflict error*가 발생함
     - 해결 방법 : `Mysql`을 완벽히 삭제한 후 `MariaDB`를 설치해야 한다.

2. `Brew`를 이용하여 설치하면 DB 구동 및 접속 명령어가 따로 있다.
   - 일반 명령어를 사용하였더니, 접속 error 발생



