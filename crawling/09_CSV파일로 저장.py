from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv


# 브라우저 생성 
browser = webdriver.Chrome('/Users/choesuyeon/Documents/chromedriver')
# window에 경우 C:/chromedriver.exec

# 웹 사이트 열기 
browser.get('https://www.naver.com')
# 로딩이 끝날때까지 10초는 기다려줌
browser.implicitly_wait(10)

# 쇼핑 메뉴 클릭하기 
browser.find_element_by_css_selector('a.nav.shop').click()
time.sleep(2) # 2초간 기다림 

# 검색 창 클릭
search = browser.find_element_by_css_selector('input.co_srh_input._input')
search.click()

# 검색어 입력 
search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER) # 엔터

# 스크롤 전 높이, execute_script = 자바스크립트 명령어 실행 메소드 
before_h = browser.execute_script("return window.scrollY")

# 무한 스크롤
while True:
        # 맨 아래로 스크롤 내린다
        browser.find_element_by_css_selector("body").send_keys(Keys.END)
        # 스크롤 사이 페이지 로딩 시간
        time.sleep(1)
        # 스크롤 후 높이
        after_h = browser.execute_script("return window.scrollY")

        if after_h == before_h:
            break
        before_h = after_h

# 크롤링 하기 전 파일 생성 open 안에 파일 경로 넣기, "w"=쓰기모드, 인코딩, 줄바꿈 없앰
f = open("/Users/choesuyeon/Desktop/crawling/data.csv","w",encoding='UTF-8', newline='')
csvWriter = csv.writer(f)

# 상품 정보 div
items = browser.find_elements_by_css_selector(".basicList_info_area__17Xyo")

for item in items:
    name = item.find_element_by_css_selector(".basicList_title__3P9Q7").text
    price = item.find_element_by_css_selector(".price_num__2WUXn").text
    link = item.find_element_by_css_selector(".basicList_title__3P9Q7 > a").get_attribute('href')
    print(name, price, link)
# 예외처리 
# ex)NosuchElementException, price에서 오류가 났다면
# try:
# price = item.find_element_by_css_selector(".price_num__2WUXn").text 
# except: 
# price = "판매중단"
    csvWriter.writerow([name,price,link])
# 파일 닫기 
f.close()