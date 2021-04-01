import asyncio
import asyncpg
import datetime

async def insert_data(data, conn):
    var1 = await conn.execute("""
        INSERT INTO calcados(
        DATA, 
        MARCA,
        NOME,
        PRECO, 
        LINK) 
        VALUES ($1, $2, $3, $4, $5
    )
        """, data['data'], 
        data['marca'], 
        data['nome'], 
        data['preco'],
        data['link'])


async def inserts(infos):
    conn = await asyncpg.connect('postgres://postgres:8411mogi@localhost/shoes_scraping')
    for info in infos:
        await insert_data(info, conn)
    
    

def main(infos):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(inserts(infos))
    