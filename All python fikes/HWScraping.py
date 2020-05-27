from bs4 import BeautifulSoup as bs
import urllib3.request

url = 'https://new.edmodo.com/groups/pfm-sem-2-2020-31010339'
http = urllib3.PoolManager()
page = http.request('GET', url)
soup = bs(page, 'lxml')
page.data