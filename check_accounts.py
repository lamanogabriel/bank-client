
import requests
from sqlite3 import connect

def buscar_clientes():
    conn = connect('support.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome FROM clientes WHERE status = 'ativa'")
    return cursor.fetchall()

def verificar_status(cliente_id):
    r = requests.get(f"http://localhost:5000/transacao/status/{cliente_id}")
    return r.json()

clientes = buscar_clientes()
for cid, nome in clientes:
    status = verificar_status(cid)
    print(f"{nome} | Status: {status['status']}")
