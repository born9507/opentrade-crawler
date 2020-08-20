from bs4 import BeautifulSoup

with open("test.html") as f:
    soup = BeautifulSoup(f, 'html.parser')

titles = soup.select('span > span.cont > span.text_cut')
amounts = soup.select('span > span.cont > span.amount > span.pink_txt')

print(len(titles))
print(len(amounts))

titles = list(map(lambda title: title.text.strip() ,titles))
amounts = list(map(lambda amount: 
    int(amount.text.replace('원','').replace(',','').strip()),  
    amounts 
))




# span class="name_text_cut" 이 제목
# span class="amount" > span class="pink_txt" 가 모집금액

#id_1382 > span > span.cont > span.name.text_cut
#id_1428 > span > span.cont > span.amount > span.pink_txt