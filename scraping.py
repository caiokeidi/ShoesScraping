###https://www.dafiti.com.br/calcados/
###https://www.glami.com.br/calcados-femininos/

import asyncio
import aiohttp
from bs4 import BeautifulSoup


arrHtmls = []

async def getHTML(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')

            arrHtmls.append(soup)
            return soup
            

def main(urls):
    """Traz de maneira assíncrona os dados da página buscada,
        ele retorna em formato HTML pelo BeautifulSoup."""
    loop = asyncio.get_event_loop()
    links_scraps = [getHTML(url) for url in urls]
    wait_scraps = asyncio.wait(links_scraps)
    infos = loop.run_until_complete(wait_scraps)

    return arrHtmls

if __name__ == '__main__':
    main()
