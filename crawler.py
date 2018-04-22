import requests
from bs4 import BeautifulSoup

base_url = "https://www.ptt.cc"

res = requests.get("https://www.ptt.cc/bbs/Beauty/index2456.html")
soup = BeautifulSoup(res.text)

titles = soup.findAll('div',{"class": "title"})

links=[]

for n in titles:
    link = n.find("a")
    print(link)
    if(link != None):
        links.append(link["href"])

print(links)




#imgs = soup.find("blockquote" ,{"class":"imgur-embed-pub"})
#imgs.find("a")["href"]

def craw_in():
    route =""
    res = requests.get(base_url + route)
    soup = BeautifulSoup(res.text)

    image_block = soup.find("blockquote" ,{"class":"imgur-embed-pub"})
    image_url = image_block.find("a")["href"]