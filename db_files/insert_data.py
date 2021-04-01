import psycopg2
from . import config
import asyncio

def insert_data(data):
    commands = (
        f"""
        INSERT INTO calcados(
        DATA, 
        MARCA,
        NOME,
        PRECO) 
        VALUES (%s, %s, %s, %s
    )
        """,)
    conn = None
    records = None
    try:
        
        params = config()
        
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        for command in commands:
            cur.execute(command, (data['data'], 
        data['marca'], 
        data['nome'], 
        data['preco'], 
        ))
            
        cur.close()
        
        conn.commit()
        return records
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return(error)
    finally:
        if conn is not None:
            conn.close()
        
        return records


if __name__ == '__main__':
    insert_data()