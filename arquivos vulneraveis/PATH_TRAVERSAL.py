# =============================================================================
# EXEMPLO 3: PATH TRAVERSAL (CWE-22) 🔴 HIGH
# =============================================================================
# O CodeQL detectará acesso a arquivos sem validação do caminho


def ler_arquivo_vulneravel(filename):
    # ❌ VULNERÁVEL: Sem validação do caminho
    with open(f"/var/www/uploads/{filename}", 'r') as f:
        return f.read()
    # Atacante pode fazer: filename = "../../etc/passwd"

"""
# Como corrigir:
import os

def ler_arquivo_seguro(filename):
    # ✅ SEGURO: Validar que o caminho está dentro do diretório permitido
    base_dir = "/var/www/uploads"
    filepath = os.path.join(base_dir, filename)
    
    # Verifica se o caminho real está dentro do diretório base
    if not os.path.realpath(filepath).startswith(os.path.realpath(base_dir)):
        raise ValueError("Caminho inválido")
    
    with open(filepath, 'r') as f:
        return f.read()
"""