import time, re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

# https://otrade.co/contest/61 이런식
url = input("url: ")
scroll_time = int(input("scroll time: "))
filename = url.split("/")[-1]
print(filename)

driver = webdriver.Chrome('executables/chromedriver')

# 3초 기다린다
driver.implicitly_wait(3)

driver.get(url)

# 시작 시간 기록
startTime = time.time()

while True:
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # 60초동안 아래로 스크롤링
        if time.time() - startTime > scroll_time:
            break
    except KeyboardInterrupt:
        print(f"소요시간: {time.time()-startTime}")
        break
    except:
        pass

print("스크롤 종료")

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# html 파일로 export
with open(f"pages/{filename}.html", 'w', encoding="UTF8") as f:
    f.write(soup.prettify())

time.sleep(5)
############################################################################################################33

# soup 처리 과정
# with open("page.html") as f:
#     soup = BeautifulSoup(f, 'html.parser')

# titles = soup.select('span > span.cont > span.text_cut')
# amounts = soup.select('span > span.cont > span.amount > span.pink_txt')
# links = soup.select('a[href]')


# #id_1

# # a href="javascript:fnstartupPopup

# # var url = "/contest/"+season_id+"/"+startup_id+"/popup";

# print(len(titles))
# print(len(amounts))

# titles = list(map(lambda title: title.text.strip() ,titles))
# amounts = list(map(lambda amount: 
#     int(amount.text.replace('원','').replace(',','').strip()),  
#     amounts 
# ))

# results = {}

# for i in range(len(titles)):
#     title = titles[i]
#     # title = euc2utf(title)
#     amount = amounts[i]

#     results[title] = amount

# # key 값에 따라 내림차순으로 정렬
# results = sorted(results.items(), key=lambda x: x[1], reverse=True)

# # 
# with open('result.txt', 'w') as f:
#     for i in range(len(results)):
#         data = (f"{i+1}, {results[i][0]}, {results[i][1]}원, \n")
#         f.write(data)
