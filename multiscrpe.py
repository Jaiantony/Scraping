import requests
from bs4 import BeautifulSoup
import numpy as np
pages=np.arange(11,20)
for page in pages:
    page=requests.get("")
    soup=BeautifulSoup(page.content,'lxml')
    soup.prettify()
    #title=soup.find_all('div',attrs={'class':'col_f_content'})
    table = soup.find_all('h4')
    name=str(table)
f=open("Movies.html","a+")
f.write (str(name))
f.close()
print("Data Scraped")
    


