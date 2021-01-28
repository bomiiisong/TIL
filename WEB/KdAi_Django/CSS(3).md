# CSS #3

CSS 선택자 & HTML 속성 활용하기 

*참고 도서: 생활코딩! HTML + CSS + Javascript*

### 1. HTML 속성 :`Class`

- 목표 

  1. 방문한 적 없는 링크 : `black`

  2. 방문한 적 있는 링크 : `gray`

  3. 현재 방문하고 있는 링크 : `red`

     

- **목표 2** 적용 코드

```html
<style>
    a {
        color: black;
        text-decoration: none;
    }
</style>

....생략

<ol>
    <li><a href="index2.html" style="color:gray;"> HTML </a></li>
    <li><a href="index2.html" style="color:gray;"> CSS </a></li>
    <li><a href="index2.html"> Javascript </a></li>
</ol>
```

But, 이 경우 **중복 발생**

- 중복 처리 방법 : `Class` 속성 사용 (*`Class`는 `HTML`속성, No CSS*)

  ```html
  <ol>
      <li><a href="index2.html" class="saw"> HTML </a></li>
      <li><a href="index2.html" class="saw"> CSS </a></li>
      <li><a href="index2.html"> Javascript </a></li>
  </ol>
  ```

  

- `Class="saw"`의 태그가 있는 링크를 `grey` 색상으로 적용하기 위해 `<style>` 태그에 추가

  ```css
  <style>
      a {
          color: black;
          text-decoration: none;
      }
      .saw {
          color: grey;
      }
  </style>
  ```

  - `saw`만 작성하면 `Class` 속성의 `saw`가 아니라, `saw`라는 선택자를 찾기 때문에 적용 안됨
  - 따라서 `.saw`로 표시해야함

- **목표 3** 적용 코드

  - `active` 클래스 추가

  ```html
  <style>
      a {
          color: black;
          text-decoration: none;
      }
      .saw {
          color: grey;
      }
      .active{
          color: red;
      }
  </style>
  
  ...
  
  <ol>
      <li><a href="index2.html" class="saw"> HTML </a></li>
      <li><a href="index2.html" class="saw active"> CSS </a></li>
      <li><a href="index2.html"> Javascript </a></li>
  </ol>
  ```

  - `class` 속성 값은 여러 개가 올 수 있고, 띄어쓰기로 구분함

    ```html
    class="saw active"  */saw, active 두 가지 값 사용*/
    ```

    

### 2. `<style>` tag 적용 순서

- 여러 클래스 값에게 영향을 받는다면, 가장 마지막 `<style>` tag가 적용됨

```html
#1. .active가 마지막 tag인 경우 => <a> tag는 red 적용

<style>
    a {
        color: black;
        text-decoration: none;
    }
    .saw {
        color: grey;
    }
    .active{
        color: red;
    }
</style>

...

<ol>
    <li><a href="index2.html" class="saw"> HTML </a></li>
    <li><a href="index2.html" class="saw active"> CSS </a></li>
    <li><a href="index2.html"> Javascript </a></li>
</ol>
```



```html
# 2. .saw가 마지막 tag인 경우 -> <a> tag에 grey 적용
    
<style>
    a {
        color: black;
        text-decoration: none;
    }
    .active{
        color: red;
    }
    .saw {
        color: grey;
    }
</style>

...

<ol>
    <li><a href="index2.html" class="saw"> HTML </a></li>
    <li><a href="index2.html" class="saw active"> CSS </a></li>
    <li><a href="index2.html"> Javascript </a></li>
</ol>
```



- 영향력에 대한 우선순위를 고려하기 위해 `ID 선택자` 활용
  - `active`를 `ID 선택자`로 이동

```html
<ol>
    <li><a href="index2.html" class="saw"> HTML </a></li>
    <li><a href="index2.html" class="saw" id="active"> CSS </a></li>
    <li><a href="index2.html"> Javascript </a></li>
</ol>
```

​		 - `ID` 값이 `active`인 값을 선택 -> `#active`

```
<style>
    a {
        color: black;
        text-decoration: none;
    }
    #active{
        color: red;
    }
    .saw {
        color: grey;
    }
</style>
```

=> `#active`로 적용하면 `.saw`가 마지막 style임에도 `active` 스타일이 적용됨

-  정리

  - **선택자 우선순위**

    태그 선택자`<a>` **<** 클래스 선택자`.saw` **<** ID 선택자`#active`

  - 모두 똑같은 형태의 선택자라면, **마지막에 선언한 선택자의 우선순위가 가장 높음**