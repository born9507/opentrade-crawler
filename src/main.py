import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./chromedriver')

#3초 기다린다
driver.implicitly_wait(3)

driver.get('https://otrade.co/contest/60')

startTime = time.time()
print('스크롤링 시작')

while True:
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        if time.time() - startTime > 60:
            break
    except KeyboardInterrupt:
        print(f"소요시간: {time.time()-startTime}")
        break
    except:
        pass

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

with open("test.html", 'w') as f:
    f.write(soup.prettify())


#class item 중에서 
# span class="name_text_cut" 이 제목
# span class="amount" > span class="pink_txt" 가 모집금액

#id_1382 > span > span.cont > span.name.text_cut
#id_1428 > span > span.cont > span.amount > span.pink_txt

# with open("test.html", 'w') as f:
#     f.write(html)