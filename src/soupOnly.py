from bs4 import BeautifulSoup
import csv

def euc2utf(x):
    return str(x.encode('utf-8'))

with open("page.html") as f:
    soup = BeautifulSoup(f, 'html.parser')

titles = soup.select('span > span.cont > span.text_cut')
amounts = soup.select('span > span.cont > span.amount > span.pink_txt')
links = soup.select('a[href]')


#id_1

# a href="javascript:fnstartupPopup

# var url = "/contest/"+season_id+"/"+startup_id+"/popup";

print(len(titles))
print(len(amounts))
print(len(links))

titles = list(map(lambda title: title.text.strip() ,titles))
amounts = list(map(lambda amount: 
    int(amount.text.replace('원','').replace(',','').strip()),  
    amounts 
))

results = {}

for i in range(len(titles)):
    title = titles[i]
    # title = euc2utf(title)
    amount = amounts[i]

    results[title] = amount

# key 값에 따라 내림차순으로 정렬
results = sorted(results.items(), key=lambda x: x[1], reverse=True)

# 
with open('result.txt', 'w') as f:
    for i in range(len(results)):
        data = (f"{i+1}, {results[i][0]}, {results[i][1]}원, \n")
        f.write(data)


# sorted(d.items(), key=lambda x: x[1], reverse=True)

# with open('result.csv','w', newline='') as f:
#     w = csv.writer(f)
#     w.writerows(result.keys())
#     w.writerows(result.values())

# span class="name_text_cut" 이 제목
# span class="amount" > span class="pink_txt" 가 모집금액


#id_1382 > span > span.cont > span.name.text_cut
#id_1428 > span > span.cont > span.amount > span.pink_txt