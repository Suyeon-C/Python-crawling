# requests의 한계 == 셀레니움 사용 이유
# 로그인이 필요한 사이트 
# 동적(페이지 전체가 아닌 특정한 부분을 바꿀때)으로 html를 만드는 경우 
# ex) 스크롤 하거나 클릭하면 데이터 생성됨 
# ex) url 주소를 변경하지 않았는데 데이터가 변함
# ex) 표, 테이블 형태의 데이터 

# 셀레니움 이란? 웹 어플리케이션 테스트를 위한 도구 
# 브라우저를 실제로 띄워서 동작 
# 크롬 드라이버 설치, 라이브러리 다운로드 (pip3 install selenium)