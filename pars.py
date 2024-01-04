import requests
from bs4 import BeautifulSoup as BS
import urllib.request

def get_price(url):

    with open("prices.txt", "w", encoding='utf-8') as file:
        file.write("")

    response = requests.get(url, allow_redirects=True)
    html = BS(response.content, 'lxml')
    price = html.select("tbody > tr > td.td-price > div.rel > p.price > strong")
    
    for i in range(5, 6):
        with open("prices.txt", "a", encoding='utf-8') as file:
            file.write(str(price[i].text) + '\n')    
            
    return price[5].get_text()

def get_title(url):

    response = requests.get(url, allow_redirects=True)
    html = BS(response.content, 'lxml')
    title = html.select("tbody > tr > td.title-cell > div.rel > h3 > a > strong")

    with open("titles.txt", "w", encoding='utf-8') as file:
        file.write(str(title[5].text))    

    return title[5].text

def old_new(url):
    result = "old"
    f1 = []
    file_do = open("titles.txt", encoding='utf-8')
    f1 = str(file_do.read())

    response = requests.get(url, allow_redirects=True)
    html = BS(response.content, 'lxml')
    title = html.select("tbody > tr > td.title-cell > div.rel > h3 > a > strong")

    with open("123.txt", "w", encoding='utf-8') as file:
        file.write(str(title[5].text))
    file_posle = open("123.txt", encoding='utf-8')
    f2 = []
    f2 = str(file_posle.read())

    if f1!=f2:

        with open("titles.txt", "w", encoding='utf-8') as file:
            file.write(str(title[5].text))    
    
        result = "new"

    return result

def get_img(url):
    response = requests.get(url, allow_redirects=True)
    html = BS(response.content, 'lxml')
    img = html.select('tbody > tr > td.photo-cell > a > img')
    i = 0

    for link in img:
        if i == 5:
            link_src = link.get('src')
            img = urllib.request.urlopen(link_src).read()
            with open(f"img/new.jpg", "wb") as out:
                out.write(img)
            return img
            #break
        i+=1

    #return "Complete!"

def get_link(url="https://www.olx.ua/detskiy-mir/tovary-dlya-shkolnikov/?search%5Border%5D=created_at%3Adesc"):
    response = requests.get(url, allow_redirects=True)
    html = BS(response.content, 'lxml')
    img = html.select('tbody > tr > td.photo-cell > a')
    i = 0

    for link in img:
        if i == 5:
            link_href = link.get('href')
            #img = urllib.request.urlopen(link_href).read()
            with open(f"link.txt", "w") as file:
                file.write(link_href)
            return link_href
            #break
        i+=1


def main():
    # print(get_title())
    # print(old_new())
    print(get_link())
    #print(get_img())
    #print(get_title(), get_price())

if __name__ == "__main__":
    main()