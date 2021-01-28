# CSS #4-1

박스 모델(1)

*참고 도서: 생활코딩! HTML + CSS + Javascript*



- 기본 코드

  ```html
  <!DOCTYPE HTML>
  <html>
    <head>
        <meta charset="utf-8">
        <title></title>
    </head>
    <body>
        <h1>CSS</h1>Cascading Style Sheets (CSS) is a style language used for describing the presentation of a document written in a markup language like HTML.
    </body>
  </html>
  ```

  - `<a>` tag 추가

  ```html
  ...생략...
  
    <body>
        <h1>CSS</h1>Cascading Style Sheets (<a href="https://en.wikipedia.org/">CSS</a>) is a style language used for describing the presentation of a document written in a markup language like HTML.
    </body>
  </html>
  ```

- 의문점 1 : `<h1>` tag는 자동 줄바꿈이 됨 .  **BUT**, `<a>` tag는 줄바꿈되지 않고 다른 내용과 같은 라인에 위치함 

- 이유 

  -  `<h1>` tag는 **제목 태그**이기 때문에, 같은 라인 전체에 적용됨 **(블록 레벨 엘리먼트)**

  - `<a>` tag는 링크를 적용할 때마다 주변 내용들의 줄이 바뀐다면 불편해지기 때문에 해당 콘텐츠인 **링크**만 태그가 적용됨 **(인라인 엘리먼트)**

    

  - 실제 확인을 위해 테두리 그리기

    - `border-width` : 테두리 두께
    - `bolder-color` : 테두리 색상
    - `bolder-style` : 테두리 종류(실선, 점선)

    ```css
    ...생략...
    <title></title>
    <style>
        h1{
            border-width: 5px;
            border-color: red;
            border-style: solid;
        }
        a {
            border-width: 5px;
            border-color: red;
            border-style: solid;
        }
    </style>
    ```

    ![CSS_box](.\image\CSS(4)-1.png)






- **블록 레벨 엘리먼트**와 **인라인 엘리먼트** 값 변경하기 -> `display` 속성 활용

  ```CSS
  display: inline;  #블록 레벨 엘리먼트인 경우
  display: block;   #인라인 엘리먼트인 경우
  ```

- 코드 정리

  ```html
  <!DOCTYPE HTML>
  <html>
    <head>
        <meta charset="utf-8">
        <title></title>
        <style>
          h1{
              border-width: 5px;
              border-color: red;
              border-style: solid;
          }
          a {
              border-width: 5px;
              border-color: red;
              border-style: solid;
          }
        </style>
    </head>
    <body>
        <h1>CSS</h1>Cascading Style Sheets (CSS) is a style language used for describing the presentation of a document written in a markup language like HTML.
    </body>
  </html>
  ```

  **1. 코드 중복 제거 (1)**

     ```html
     <!DOCTYPE HTML>
     <html>
       <head>
           <meta charset="utf-8">
           <title></title>
           <style>
             h1, a{
                 border-width: 5px;
                 border-color: red;
                 border-style: solid;
             }
           </style>
       </head>
       <body>
           <h1>CSS</h1>Cascading Style Sheets (CSS) is a style language used for describing the presentation of a document written in a markup language like HTML.
       </body>
     </html>
     ```

     **2. 코드 중복 제거 (2) -> 순서 상관없음**

  ~~~html
    ```html
    <!DOCTYPE HTML>
    <html>
      <head>
          <meta charset="utf-8">
          <title></title>
          <style>
            h1, a{
                border: 5px solid red;
            }
          </style>
      </head>
      <body>
          <h1>CSS</h1>Cascading Style Sheets (CSS) is a style language used for describing the presentation of a document written in a markup language like HTML.
      </body>
    </html>
  ```
  ~~~
  
  
  ​      