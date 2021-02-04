#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup
import time
import pandas as pd


# # location -> 시,군,구 통합

# In[ ]:


# 각 변수 담을 리스트
room_id = []
room_name = []
room_location = []
room_link = []
idx_list = []

# 300 page crawling
for page in range(300):
    roomID = str(50400+page)  
    link = 'https://www.goodchoice.kr/product/detail?ano=' + roomID   #임의의 roomID부터 차례로 300개 검색
    
    url = requests.get(link)
    url = url.text
    
    soup = BeautifulSoup(url, 'html.parser')
    
    infos = soup.select('div.right')  # <div class="right"> 하위의 값을 가져와라
    
    for info in infos:
        name = info.select_one('h2').text   #infos 하위의 <h2> 태그에 있는 값 중 텍스트만 선택해서 저장
        room_name.append(name)              # room_name 리스트에 추가
        
        location = info.select_one('p.address').text    # infos 하위의 <p class="address"> 의 값 중 텍스트만 선택해서 저장
        room_location.append(location)                  # room_location 리스트에 추가
        
        room_id.append(roomID)                          # room_id 추출하기 위해 리스트에 저장 
        room_link.append(link)                          # room_link 추출하기 위해 리스트에 저장
        
        time.sleep(3)   # 잠시 멈추기
        
for idx, value in enumerate(room_name):     # 정보가 없는 숙소의 roomID 찾기 위해 room_name의 index 이용
    if not room_name[idx]:
        idx_list.append(idx)        
    else:
        pass
    
idx_list = list(reversed(idx_list))       # room_name의 index 순서대로 삭제하면, loop 할 때마다 index 순서가 앞당겨짐
                                          # (리스트 요소가 삭제되면서 index가 조정되기 때문)
                                          # 따라서 reversed() 함수로 index 역순으로 변경 -> 다시 list 형태로 저장

for n in idx_list:     # 역순으로 각 리스트 요소 삭제
    del room_id[n]
    del room_name[n]
    del room_location[n]
    del room_link[n]

# print(room_id)
# print(room_name)
# print(room_location)
# print(room_link)


# In[ ]:


accomodation_data = pd.DataFrame({'roomID' : room_id, 'room_name': room_name, 'location' : room_location, 'link' : room_link})
accomodation_data.to_csv('accomodation_data.csv', index=False)

