import psycopg2
from config import config

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
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    insert_data()