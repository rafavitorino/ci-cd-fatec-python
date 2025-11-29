# =============================================================================
# EXEMPLO 1: SQL INJECTION (CWE-89) 🔴 CRITICAL
# =============================================================================
# O CodeQL detectará que estamos concatenando input do usuário em uma query SQL
# Isso permite que um atacante execute comandos SQL arbitrários

import sqlite3

def buscar_usuario_vulneravel(username):
    # ❌ VULNERÁVEL: Concatenação direta de input do usuário
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    query = f"SELECT * FROM usuarios WHERE username = '{username}'"
    cursor.execute(query)  # CodeQL vai detectar aqui!
    
    return cursor.fetchall()

