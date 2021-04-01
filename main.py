import scraping
import scrapingSynchronous
import filter 
import time
from send_data import send_all_data
from get_urls import get_urls

##Apenas para teste
##Vou usar aqui depois para centralizar as chamadas
def main():
    start = time.time()

    urls = get_urls(6)
    htmls = scraping.main(urls)
    #htmls = scrapingSynchronous.main(urls)

    infos = filter.main(htmls)
    res = send_all_data(infos)

    elapsed = time.time() - start
    print(f'tempo: {elapsed}')



if __name__ == '__main__':
    main()



### 3 ciclos com 23.1s Ass
### 3 ciclos com 24.7s Sin
### 6 ciclos com 43.3s Ass
### 6 ciclos com 49.4s SIn