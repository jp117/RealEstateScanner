import requests
from bs4 import BeautifulSoup

page = requests.get('http://www.loopnet.com/for-sale/multifamily/?sk=63b914a1552119b05ef714d0276d7001&bb=np6wjo2t8S3z_ujn17uG&view=list&e=v')

soup = BeautifulSoup(page.content, 'html.parser')

links = soup.find_all('div', class_= 'listing-address-and-price')

for a in links.find('a', href=True):
    print (a['href'])

