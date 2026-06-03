#init database.py

import sqlite3
from datetime import datetime
db = 'projeto.db'

def create_table():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    with open( 'Schema.sql', 'r', encoding='utf-8') as arq:
        script = arq.read()

    #executando o script
    cursor.executescript(script)
    conn.commit()
    conn.close()
    print(f'Banco de dados {db} criado com sucesso!')

    #abrir conexão com o banco de dados
def get_connect_db():
    conn = sqlite3.connect(db)
    return conn

if __name__ == '__main__':
    create_table()


#adicionar 

def insert_task(titulo, desc, prioridade):
    with get_connect_db() as conn:
        cursor = conn.cursor()
        script_insert = 'INSERT INTO tarefas (titulo, descricao, prioridade, status) VALUES (?, ?, ?, "Pendente")'
        cursor.execute(script_insert, (titulo, desc, prioridade))
        conn.commit()


# No arquivo database.py:
def select_task():
    with get_connect_db() as conn:
        cursor = conn.cursor()
        script_select = """
        SELECT 
            id,       
            titulo,
            descricao,
            prioridade,
            status
        FROM tarefas
        """
        cursor.execute(script_select)
        return cursor.fetchall()
    

def update_task(id, nv_status):
    with get_connect_db() as conn:
        cursor = conn.cursor()
        
      
        if nv_status == "Concluída":
            sql_update = """
            UPDATE tarefas
            SET status = ?, data_conclusao = ?
            WHERE id = ?
            """
            cursor.execute(sql_update, (nv_status, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), id))
        else:
           
            sql_update = """
            UPDATE tarefas
            SET status = ?, data_conclusao = NULL
            WHERE id = ?
            """
            cursor.execute(sql_update, (nv_status, id))
        
        conn.commit()

def delete_task(id):
    with get_connect_db() as conn:
        cursor = conn.cursor()
        sql_delete = 'DELETE FROM tarefas WHERE id = ?'
        cursor.execute(sql_delete, (id,))
        conn.commit()

def dash_pendentes_concluidas():
    with get_connect_db() as conn:
        cursor = conn.cursor()
        script_dash = """
        SELECT 
            status, 
            COUNT(*) as total
        FROM tarefas
        GROUP BY status
        """


        cursor.execute(script_dash)
        r = cursor.fetchall()
        return r
    
