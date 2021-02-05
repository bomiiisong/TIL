# Project Data

Web Project에 사용한 데이터 설명입니다.





### accomodation_base

- '여기어때' 사이트 크롤링 데이터 

- roomID [50000] ~ roomID [50699] 범위 크롤링

- 변수 설명

  | Column              | 설명 |
  | ------------------- | --------- |
  | roomID | 숙소 상세페이지 ID |
  | room_name | 숙소 이름 |
  | location | 숙소 위치 |
  | link | 숙소 상세페이지 링크 |

   
  
  
  
  

### accomodation_imagelink

- '여기어때' 사이트 크롤링 데이터

- `accomodation_base.csv` 에 **image link** 컬럼 추가

- 변수 설명

  | Column    | 설명                 |
  | --------- | -------------------- |
  | roomID    | 숙소 상세페이지 ID   |
  | room_name | 숙소 이름            |
  | location  | 숙소 위치            |
  | link      | 숙소 상세페이지 링크 |
  | image_link | 숙소 대표 이미지 링크 |







### accomodation_final

- 숙소의 위도, 경도 컬럼 추가

- `Google Maps API` 활용

- 변수 설명

  | Column    | 설명                 |
  | --------- | -------------------- |
  | roomID    | 숙소 상세페이지 ID   |
  | room_name | 숙소 이름            |
  | location  | 숙소 위치            |
  | link      | 숙소 상세페이지 링크 |
  | image_link | 숙소 대표 이미지 링크 |
  | latitude | 숙소 위도 정보 |
  | longitude | 숙소 경도 정보 |