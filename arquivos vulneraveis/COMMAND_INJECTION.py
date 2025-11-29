# =============================================================================
# EXEMPLO 2: COMMAND INJECTION (CWE-78) 🔴 CRITICAL
# =============================================================================
# O CodeQL detectará execução de comandos do sistema com input do usuário

import os

def executar_comando_vulneravel(filename):
    # ❌ VULNERÁVEL: Execução de comando com input do usuário
    os.system(f"cat {filename}")  # CodeQL vai detectar aqui!
    # Atacante pode fazer: filename = "arquivo.txt; rm -rf /"

