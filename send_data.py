import asyncio
from db_files.insert_data import insert_data

records = []

async def send_data(info):
    record = insert_data(info)
    records.append(record)

def send_all_data(infos):
    loop = asyncio.get_event_loop()
    datas_send = [send_data(info) for info in infos]
    wait_send = asyncio.wait(datas_send)
    res,_=loop.run_until_complete(wait_send)

    return res

