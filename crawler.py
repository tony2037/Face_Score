# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup

base_url = "https://www.ptt.cc"


def craw_target():
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

def craw_in(route ="/bbs/Beauty/M.1524314952.A.CD3.html"):
    """
    given a route of /ptt /Beauty
    e.g : "/bbs/Beauty/M.1524314952.A.CD3.html"
    return the score of the block
    """

    res = requests.get(base_url + route)
    print(res.encoding)
    soup = BeautifulSoup(res.text)

    image_block = soup.find("blockquote" ,{"class":"imgur-embed-pub"})
    image_url = image_block.find("a")["href"]

    #calculate score
    pushes = soup.select("span.push-tag")
    score = 0
    for p in pushes:
        #print(p.contents[0][0])
        if (ord(p.contents[0][0]) == ord("推")):
            score=score+1

    print(score)
    #print("score:{}".format(score))
    return score

if __name__ == "__main__":
    craw_in()