import bs4
import asyncio

array_infos = []

def busca_divs(html):
    divs = html.find_all('div', {'class':'tracker-item'})
    return divs

async def get_name(div):
    try:
        info_name = div.find_all('div', {'class':'item__title'})
        pos_final = len(info_name[0])-2
        nome_formatado = info_name[0][2:pos_final]
        return nome_formatado
    except:
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
        return info_price[0].text
    except KeyError:
        print('Erro no processamento de preço')
    


async def get_info(div):
    info = {}
    info_to_filter = {'nome':get_name, 'marca' : get_brand, 'preco' : get_price}
    for key, function in info_to_filter.items():
        valor = await function(div)
        info[key] = valor
    array_infos.append(info)


def get_all_infos(divs):
    loop = asyncio.get_event_loop()
    div_infos = [get_info(div) for div in divs]
    # div_infos = [get_info(div) for div in divs]
    wait_infos = asyncio.wait(div_infos)
    res,_=loop.run_until_complete(wait_infos)

    # loop.close()
    return res

def main(html):
    divs = busca_divs(html)
    get_all_infos(divs)
    print(array_infos)

    return array_infos


