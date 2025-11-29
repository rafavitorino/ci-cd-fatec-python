# =============================================================================
# EXEMPLO 2: COMMAND INJECTION (CWE-78) 🔴 CRITICAL
# =============================================================================
# O CodeQL detectará execução de comandos do sistema com input do usuário

# Como corrigir:
import subprocess

def executar_comando_seguro(filename):
    # ✅ SEGURO: Usar subprocess com lista de argumentos
    subprocess.run(["cat", filename], check=True)
