# =============================================================================
# EXEMPLO 1: SQL INJECTION (CWE-89) 🔴 CRITICAL
# =============================================================================
# O CodeQL detectará que estamos concatenando input do usuário em uma query SQL
# Isso permite que um atacante execute comandos SQL arbitrários

# Como corrigir:
def buscar_usuario_seguro(username):
    # ✅ SEGURO: Usar parâmetros preparados
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    query = "SELECT * FROM usuarios WHERE username = ?"
    cursor.execute(query, (username,))
    
    return cursor.fetchall()

