import bs4
import asyncio
import re
from datetime import date
from get_functions import get_link, get_brand, get_name, get_price
import datetime

array_infos = []

def busca_divs(html):
    divs = html.find_all('div', {'class':'tracker-item'})
    return divs

async def get_info(div):
    info = {}
    info_to_filter = {'nome':get_name, 'marca' : get_brand, 'preco' : get_price, 'link':get_link}
    for key, function in info_to_filter.items():
        valor = await function(div)
        info[key] = valor
    info['data'] = datetime.date(date.today().year, date.today().month, date.today().day)
    array_infos.append(info)


def get_all_infos(divs):
    loop = asyncio.get_event_loop()
    div_infos = [get_info(div) for div in divs]
    # div_infos = [get_info(div) for div in divs]
    wait_infos = asyncio.wait(div_infos)
    res,_=loop.run_until_complete(wait_infos)

    # loop.close()
    return res

def main(htmls):
    for html in htmls:
        divs = busca_divs(html)
        get_all_infos(divs)
    # for info in array_infos:
    #     print(info, '\n')

    return array_infos


