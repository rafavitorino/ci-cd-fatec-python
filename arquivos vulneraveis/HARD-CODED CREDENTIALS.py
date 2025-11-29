# =============================================================================
# EXEMPLO 4: HARD-CODED CREDENTIALS (CWE-798) 🔴 HIGH
# =============================================================================
# O CodeQL detectará credenciais fixas no código

# ❌ VULNERÁVEL: Credenciais no código
DATABASE_PASSWORD = "senha123"
API_KEY = "sk-1234567890abcdef"
