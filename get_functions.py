import bs4
import re


async def get_link(div):
    try:
        info_link = div.find_all('a', {'class':'tr-item-link'})
        link = info_link[0]['href']
        return link
    except KeyError:
        print('Erro no processamento de Link')

async def get_name(div):
    try:
        info_name = div.find_all('div', {'class':'item__title'})
        
        name_str = str(info_name[0].text)
        pos_final = len(name_str)-1
        nome_formatado = name_str[1:pos_final]
        return nome_formatado
    except KeyError:
        print('Erro no processamento de nome')

async def get_brand(div):
    try:
        info_brand_div = div.find_all('div', {'class':'item__brand'})
        info_brand = info_brand_div[0].find_all('span')
        return info_brand[0].text
    except KeyError:
        print('Erro no processamento de marca')

async def get_price(div):
    try:
        info_price = div.find_all('span', {'class':'price'})
        str_price =  str(info_price[0].text)
        price_regex = re.findall('[-+]?\d*\.?\d+|\d+', str_price)
        ###Pode ser interessante mudar e entender melhor esse regex
        price = price_regex[0] + '.' + price_regex[1]
        return float(price)
    except KeyError:
        print('Erro no processamento de preço')
    