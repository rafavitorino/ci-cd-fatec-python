# =============================================================================
# EXEMPLO 6: INSECURE DESERIALIZATION (CWE-502) 🔴 CRITICAL
# =============================================================================
# O CodeQL detectará desserialização de dados não confiáveis


# Como corrigir:
import json

def carregar_dados_seguro(data):
    # ✅ SEGURO: Usar JSON para dados não confiáveis
    return json.loads(data)
