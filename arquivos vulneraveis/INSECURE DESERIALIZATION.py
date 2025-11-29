# =============================================================================
# EXEMPLO 6: INSECURE DESERIALIZATION (CWE-502) 🔴 CRITICAL
# =============================================================================
# O CodeQL detectará desserialização de dados não confiáveis

import pickle

def carregar_dados_vulneravel(data):
    # ❌ VULNERÁVEL: Pickle pode executar código arbitrário
    return pickle.loads(data)  # CodeQL vai detectar aqui!
