# Git .DS_Store file 제거하기

> Mac OS의 경우, `.DS_Store`라는 불필요한 파일이 생성되어 git repository에 자동 push 됨



## 해결 방법 (1)

- 이미 git repository에 push 된 경우

  ```sh
  find . -name .DS_Store -print0 | xargs -0 git rm --ignore-unmatch
  ```

  

