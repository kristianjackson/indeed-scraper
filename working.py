import requests
from bs4 import BeautifulSoup

def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    url = f'https://www.indeed.com/jobs?q&l=King%20George%2C%20VA&start={page}&vjk=6d36b2438acc5b72'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_='jcs-JobTitle')
    print(divs)
    return len(divs)

c = extract(0)
print(transform(c))
