import time, re, requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import pdfkit, imgkit

with open("pages/otrade.html", 'r', encoding="UTF8") as f:
    soup = BeautifulSoup(f, 'html.parser')

titles = soup.select('span > span.cont > span.text_cut')
contents = soup.select("span > span.cont > span.line2_cut")
amounts = soup.select('span > span.cont > span.amount > span.pink_txt')
links_temp = soup.select('a[href]')
ids = []
links = []

titles = list(map(lambda title: title.text.strip() ,titles))
contents = list(map(lambda content: content.text.strip() ,contents))
amounts = list(map(lambda amount: 
    int(amount.text.replace('원','').replace(',','').strip()),  
    amounts ))
links_temp = list(map(lambda link: 
    str(link).replace('\n','').replace('  ',''),
    links_temp ))

for link in links_temp:    
    start_index = link.find("id_1")
    id = link[start_index:start_index+7]
    if len(id) != 0 :
        ids.append(id[3:])  #ex) 1176

for id in ids:
    link = f"https://otrade.co/contest/60/{id}/popup"
    links.append(link)


results = {}

for i in range(len(titles)):
    title = titles[i]
    content = contents[i]
    amount = amounts[i]
    link = links[i]
    results[title] = (amount, link, content)

# key 값에 따라 내림차순으로 정렬
results = sorted(results.items(), key=lambda x: x[1], reverse=True)

# 텍스트 파일로 저장
with open('results/result.txt', 'w', encoding="UTF8") as f:
    for i in range(len(results)):
        data = (f"{i+1}, {results[i][0]}, {results[i][1][0]}원 \n  {results[i][1][2]} \n  {results[i][1][1]} \n")
        f.write(data)

# 마크다운 파일로 저장
with open('results/result.md', 'w', encoding="UTF8") as f:
    f.write("# 결과")
    for i in range(len(results)):
        f.write(f"{i+1}, {results[i][0]}, {results[i][1][0]}원 \n  {results[i][1][2]} \n  {results[i][1][1]} \n")

#링크를 pdf 파일로 저장
# pdfconfig = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
# pdfkit.from_url('http://www.naver.com', 'out.pdf' , configuration=pdfconfig)
imgconfig = imgkit.config(wkhtmltoimage='C:/Program Files/wkhtmltopdf/bin/wkhtmltoimage.exe')
imgkit.from_url('https://otrade.co/contest/60/1168/popup', 'out.jpg', config=imgconfig)


########################################33
# for i in range(len(results)):
#     ranking = str(i+1)
#     title = results[i][0]
#     link = results[i][1][1]

#     req = requests.get(link)
#     html = req.text
#     soup = BeautifulSoup(html, 'html.parser')


#     with open(f"results/html/{ranking}_{title}.html", 'w', encoding="UTF8") as f:
#         f.write(soup.prettify())

    # pdfkit.from_url(link , f"results/pdf/{ranking}_{title}.pdf", configuration=pdfconfig)
    # imgkit.from_url(link , f"results/pdf/{ranking}_{title}.jpg", config=imgconfig)



# https://otrade.co/contest/60/1168/popup

# var url = "/contest/"+season_id+"/"+startup_id+"/popup";
# <a href="javascript:fnStartupPopup('60','1168');" id="id_1168">
# a href="javascript:fnstartupPopup

# sorted(d.items(), key=lambda x: x[1], reverse=True)

# with open('result.csv','w', newline='') as f:
#     w = csv.writer(f)
#     w.writerows(result.keys())
#     w.writerows(result.values())

# span class="name_text_cut" 이 제목
# span class="amount" > span class="pink_txt" 가 모집금액


#id_1382 > span > span.cont > span.name.text_cut
#id_1428 > span > span.cont > span.amount > span.pink_txt