import scraping
import scrapingSynchronous
import filter 
import time
from send_data import send_all_data
from get_urls import get_urls
from db_files_async import insert_asyncpg

##Apenas para teste
##Vou usar aqui depois para centralizar as chamadas
def main():
    start = time.time()

    urls = get_urls(5)
    htmls = scraping.main(urls)
    #htmls = scrapingSynchronous.main(urls)

    infos = filter.main(htmls)
    insert_asyncpg.main(infos)
    #res = send_all_data(infos)

    elapsed = time.time() - start
    print(f'tempo: {elapsed}')


if __name__ == '__main__':
    main()


## 5 ciclos ASSINCRONO 2.3884129524230957
## 5 ciclos SINCRONO   41.394619941711426

