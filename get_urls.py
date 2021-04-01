import asyncio
import scraping

arr_scraps = []
BASE_URL = 'https://www.glami.com.br/calcados-femininos/?p='

def get_urls(qtd):

    for i in range(1, qtd+1, 1):
        url = BASE_URL + str(i)
        arr_scraps.append(url)
    
    return arr_scraps
