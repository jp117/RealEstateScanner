import requests
from bs4 import BeautifulSoup

page = requests.get('http://www.loopnet.com/for-sale/multifamily/?sk=b12008959ee0e3323746b123877acb2b&view=list')

soup = BeautifulSoup(page.content, 'html.parser')

links = soup.find_all('div', class_= 'listing-address-and-price')

elems = soup.select('#placardSec > div:nth-child(2) > div > div:nth-child(1) > div.gold > section.placard-details-container > div.placard-details > div > a')

#Need to use selenium, not BS4