
import sqlite3

def buscar_usuario_vulneravel(username):
    # ❌ VULNERÁVEL: Concatenação direta de input do usuário
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    query = f"SELECT * FROM usuarios WHERE username = '{username}'"
    cursor.execute(query)  # CodeQL vai detectar aqui!
    
    return cursor.fetchall()
"""
# Como corrigir:
def buscar_usuario_seguro(username):
    # ✅ SEGURO: Usar parâmetros preparados
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    query = "SELECT * FROM usuarios WHERE username = ?"
    cursor.execute(query, (username,))
    
    return cursor.fetchall()
"""