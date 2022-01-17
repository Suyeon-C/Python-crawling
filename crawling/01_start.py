# 요청 가져오기 
import requests
# 번역 
from bs4 import BeautifulSoup 
# 마우스, 키보드 매크로 라이브러리, 간단한 입력 창 띄우기 
import pyautogui

# keyword = input("입력하세요")
# pyautogui는 문자열로 받음 ,따라서 아래 형변환 lastpage
keyword = pyautogui.prompt("검색어를 입력하세요 >>>>")
lastpage= pyautogui.prompt("마지막 페이지 번호를 입력해 주세요")
pageNum = 1
for i in range(1,int(lastpage)* 10,10): #1,11,21
    print(f"{pageNum}페이지 입니다.===========")
    # naver 서버에 대화를 시도 ,f스트링(문자열 포맷팅): 사용안하면 "https//~~query=" + {keyword} 이다
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={i}")
    html = response.text
    # html 번역선생님으로 수프 만듦
    soup = BeautifulSoup(html, 'html.parser')
    # id 값이 '' 인을 가져옴 
    links = soup.select(".news_tit")
    for link in links:
        title = link.text # 태그 안에 텍스트요소를 가져온다
        url = link.attrs['href'] # 속성이 href 가져오기 
        print(title,url)
    pageNum = pageNum + 1