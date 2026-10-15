from decimal import Decimal
import re

def normalizar_valor(s: str) -> Decimal:
    if not s: return Decimal("0")
    s = s.strip().replace("R$", "").replace(" ", "").replace(",", ".")
    s = re.sub(r"[^0-9\.\-]", "", s)
    try: return Decimal(s)
    except: return Decimal("0")
