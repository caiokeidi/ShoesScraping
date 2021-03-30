import scraping
import filter 
import scrapingSynchronous
import time

##Apenas para teste
##Vou usar aqui depois para centralizar as chamadas

html = scraping.main()
start = time.time()
infos = filter.main(html)
elapsed = time.time() - start
print(f'tempo: {elapsed}')
