###https://www.dafiti.com.br/calcados/
###https://www.glami.com.br/calcados-femini

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

arrHtmls = []

def getHTML(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()

    # print("Status:", response.status)
    # print("Content-type:", response.headers['content-type'])

    html = page.decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')

    arrHtmls.append(soup)
    return soup
            

def main(urls):
    for url in urls:
        getHTML(url) 

    return arrHtmls

if __name__ == '__main__':
    main()
