import requests
from bs4 import BeautifulSoup

request = requests.get('https://beomi.github.io/beomi.github.io_old/')

## HTTP status (200: normal)
status = request.status_code
is_ok = request.ok

html = request.text
header = request.headers

soup = BeautifulSoup(html, 'html.parser')
my_titles = soup.select(
    'h3 > a'
)