# CSS #4-2

박스 모델(2) - border, margin, padding 학습하기

*참고 도서: 생활코딩! HTML + CSS + Javascript*



- **기본 코드**

  ```html
  <!DOCTYPE HTML>
  <html>
    <head>
        <meta charset="utf-8">
        <title></title>
        <style>
            h1 {
                border: 5px solid red;
            }
        </style>
    </head>
    <body>
        <h1>CSS</h1>Cascading Style Sheets (<a href="https://en.wikipedia.org/">CSS</a>) is a style language used for describing the presentation of a document written in a markup language like HTML.
    </body>
  </html>
  ```

  

#### 1. `padding` : 테두리와 내용 사이에 여백 주기 

   ```css
   <style>
       h1 {
       border: 5px solid red;
       padding: 20px;
       }
   </style>
   ```

#### 2. `margin` : 태그 별 테두리 간격 조정

   - `margin: 0;` : 간격 없음

   ```css
   <style>
       h1 {
       border: 5px solid red;
       padding: 20px;
       margin: 0;
       }
   </style>
   ```

   - `margin: 20px;` : 20px 만큼 간격 두기

   ```css
   <style>
       h1 {
       border: 5px solid red;
       padding: 20px;
       margin: 20px;
       }
   </style>
   ```

#### 3. `width` : box 크기 조정

   - `width`를 지정하지 않으면 tag의 디폴트 값으로 적용된 것(`display: block`이 생략된 상태)

   ```css
   <style>
       h1 {
       border: 5px solid red;
       padding: 20px;
       margin: 20px;
       width: 100px;
       }
   </style>
   ```

#### 4. 정리

  ![css box model](https://miro.medium.com/max/2948/1*CSL2YLWiUV_VlGCJnfygEA.png)



---



### 웹 브라우저의 CSS source 확인하기

- **개발자도구 (F12)** 혹은 **오른쪽 클릭>검사** -> **Styles** 확인
  - 어떤 CSS 스타일의 영향을 받는지 파악 가능

