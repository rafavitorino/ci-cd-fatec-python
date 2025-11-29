# =============================================================================
# EXEMPLO 5: WEAK CRYPTOGRAPHY (CWE-327) 🟠 MEDIUM
# =============================================================================
# O CodeQL detectará uso de algoritmos de criptografia fracos



# Como corrigir:
import bcrypt

def hash_senha_seguro(senha):
    # ✅ SEGURO: Usar bcrypt ou argon2
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(senha.encode(), salt)
