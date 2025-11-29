# =============================================================================
# EXEMPLO 3: PATH TRAVERSAL (CWE-22) 🔴 HIGH
# =============================================================================
# O CodeQL detectará acesso a arquivos sem validação do caminho


def ler_arquivo_vulneravel(filename):
    # ❌ VULNERÁVEL: Sem validação do caminho
    with open(f"/var/www/uploads/{filename}", 'r') as f:
        return f.read()
    # Atacante pode fazer: filename = "../../etc/passwd"
