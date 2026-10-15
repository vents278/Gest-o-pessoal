from decimal import Decimal, ROUND_HALF_UP
from typing import List, Tuple

TWOPLACES = Decimal("0.01")

def dividir_igualitario(valor_total: Decimal, user_ids: List[int]) -> List[Tuple[int, Decimal, Decimal]]:
    if not user_ids: return []
    qtd = len(user_ids)
    base = (valor_total / Decimal(qtd)).quantize(TWOPLACES, rounding=ROUND_HALF_UP)
    resultado = []
    soma = Decimal("0")
    for uid in user_ids:
        perc = Decimal("50.00") if qtd == 2 else (Decimal(100)/Decimal(qtd)).quantize(TWOPLACES)
        resultado.append((uid, base, perc))
        soma += base
    diff = (valor_total - soma).quantize(TWOPLACES)
    if diff != 0 and resultado:
        uid0, v0, p0 = resultado[0]
        resultado[0] = (uid0, (v0 + diff).quantize(TWOPLACES), p0)
    return resultado
