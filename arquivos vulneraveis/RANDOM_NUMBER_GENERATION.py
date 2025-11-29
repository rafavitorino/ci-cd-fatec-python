# =============================================================================
# EXEMPLO 7: RANDOM NUMBER GENERATION (CWE-338) 🟠 MEDIUM
# =============================================================================
# O CodeQL detectará uso de gerador de números aleatórios fraco para segurança

"""
import random

def gerar_token_vulneravel():
    # ❌ VULNERÁVEL: random não é criptograficamente seguro
    return random.randint(1000, 9999)
"""

# Como corrigir:
import secrets

def gerar_token_seguro():
    # ✅ SEGURO: Usar secrets para dados sensíveis
    return secrets.token_hex(16)
