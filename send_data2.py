import asyncio
import aiohttp


records = []
url = 'http://localhost:8080/insere'


async def send_data2(infos):
    for info in infos:
        info['data'] = info['data'].strftime("%Y/%m/%d") 
        records.append(info)

    await insert_datas()
    
def send_all_data2(infos):
    loop = asyncio.get_event_loop()
    datas_send = [send_data2(infos)]
    wait_send = asyncio.wait(datas_send)
    res,_=loop.run_until_complete(wait_send)

    return res

async def insert_datas():
    async with aiohttp.ClientSession() as session:
        res = await session.post(url, json=records)
        # await session.close()
        ##Está dando um erro unclosed connection.
        return res
    

# async def send_data2(info):
#     info['data'] = info['data'].strftime("%Y/%m/%d") 
#     record = await insert_data(info)
#     records.append(record)

# def send_all_data2(infos):
#     loop = asyncio.get_event_loop()
#     datas_send = [send_data2(info) for info in infos]
#     wait_send = asyncio.wait(datas_send)
#     res,_=loop.run_until_complete(wait_send)

#     return res

# async def insert_data(info):
#     async with aiohttp.ClientSession() as session:
#         res = await session.post(url, json=info)
#         return res

