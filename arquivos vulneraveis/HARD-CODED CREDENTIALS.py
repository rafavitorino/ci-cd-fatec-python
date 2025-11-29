# =============================================================================
# EXEMPLO 4: HARD-CODED CREDENTIALS (CWE-798) 🔴 HIGH
# =============================================================================
# O CodeQL detectará credenciais fixas no código

# Como corrigir:
import os
from dotenv import load_dotenv

# ✅ SEGURO: Usar variáveis de ambiente
load_dotenv()
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
API_KEY = os.getenv('API_KEY')
