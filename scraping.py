###https://www.dafiti.com.br/calcados/
###https://www.glami.com.br/calcados-femininos/

import asyncio
import aiohttp
from bs4 import BeautifulSoup

URL = 'https://www.glami.com.br/calcados-femininos/'

async def getHTML():
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')

            # soup.find_all('div', {'class':'tracker-item'})
            return soup
            ##Checar se coloca aqui ou em outro arquivo essa busca do find_all

def main():
    loop = asyncio.get_event_loop()
    infos = loop.run_until_complete(getHTML())
    return infos

if __name__ == '__main__':
    main()
