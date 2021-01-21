# MongoDB 설치

> Homebrew 이용하여 MongoDB 설치하기

## 1. Homebrew update

```sh
$ brew update
```

## 2. brew로 설치하기

```shell
#nodejs 설치
$ brew install node
#MongoDB 설치
$ brew install mongodb
```

## 3. MongoDB server 실행

```shell
$ brew services start mongodb/brew/mongodb-community
$ mongod
```

## 4. 새로운 터미널 열고 MongoDB 사용

```shell
#새로운 Terminal
$ mongo
```



## # Error & Solution

- `brew install mongodb` 를 실행하였으나 다음과 같은 오류가 발생했다.

```shell
==> Searching for similarly named formulae...
Error: No similarly named formulae found.
Error: No available formula or cask with the name "mongodb".
==> Searching for a previously deleted formula (in the last month)...
Error: No previously deleted formula found.
==> Searching taps on GitHub...
Error: No formulae found in taps.
```

- 이럴 땐 `brew tap` 명령어로 설치해야 한다.

  ```shell
  #brew tap ~~
  brew tap mongodb/brew
  #MongoDB community version 설치
  brew install mongodb-community@4.4
  ```

- 순조롭게 설치되는 듯 했으나, 다른 오류 발생

  ```sh
  #CLT(Command Line Tool error)
  Error: Your CLT does not support macOS 11.
  It is either outdated or was modified.
  Please update your CLT or delete it if no updates are available.
  Update them from Software Update in System Preferences or run:
    softwareupdate --all --install --force
  
  If that doesn't show you an update run:
    sudo rm -rf /Library/Developer/CommandLineTools
    sudo xcode-select --install
  
  Alternatively, manually download them from:
    https://developer.apple.com/download/more/.
  
  Error: An exception occurred within a child process:
    SystemExit: exit
  ```

- 해결 방법 : 기존 `CLT`삭제 후 새로운 버전으로 설치

  ```sh
  #기존 CLT 삭제
  sudo rm -rf /Library/Developer/CommandLineTools
  #새로운 버전 설치
  sudo xcode-select --install
  ```

  

