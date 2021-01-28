# CSS #1

HTML 정보 중, **디자인과 관련한** 요소들을 분리하기 위해 적용하는 언어

*참고 도서 : 생활코딩! html + css + Javascript*



### 1. `<style>` tag

- (대상) {적용할 디자인}

```css
<style>
    a {      */a : 적용할 대상 (선택자)*/
        color: black;  */ delaration (선택자에 적용할 효과)*/
    }
</style>
```

=> 해석하자면 모든 `<a>` tag 에 대해 `black` 색상을 적용하라.



### 2. `style` 속성

- `HTML`에 `style`속성을 활용하여 효과 적용

```html
<li><a href="index2.html" style="color:red"> CSS </a> </li>
```

=> 해당 링크에만 `red` 색상을 적용하라.



### 추가 CSS 효과

- 링크의 밑줄 없애기

```css
<style>
    a {
        color: black;
        text-decoration: none;
    }
```

- 특정 링크에만 밑줄 효과 주기

```html
<li><a href="index2.html" style="color:red; text-decoration:underline;"> CSS </a></li>
```

- `;` : 적용한 효과의 구분자



### CSS 용어

```css
<style>
    a {
        color: black;
        text-decoration: none;
    }
```

- `a` : `Selector`(선택자)

- `Declaration`(선언, 효과)

  ```css
  color: black;
  text-decoration: none;
  ```

- `Property` (속성)

  ```css
  color:
  text-decoration:
  ```

- `Value`(값)

  ```css
   black;
   none;
  ```

  