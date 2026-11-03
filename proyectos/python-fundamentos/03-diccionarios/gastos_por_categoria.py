"""Agrupa gastos por categoría y encuentra la de mayor gasto."""
gastos = [
    {"concepto": "Supermercado", "categoria": "comida", "importe": 45.25},
    {"concepto": "Gasolina", "categoria": "transporte", "importe": 60.0},
    {"concepto": "Cena", "categoria": "comida", "importe": 32.5},
    {"concepto": "Netflix", "categoria": "ocio", "importe": 12.75},
    {"concepto": "Bus", "categoria": "transporte", "importe": 1.5},
]

def total_por_categoria(gastos: list[dict]) -> dict[str, float]:
    """Devuelve un diccionario con el total de cada categoría."""
    total_gastado = {}
    for gasto in gastos:
        categoria = gasto["categoria"]
        importe = gasto["importe"]
        total_gastado[categoria] = total_gastado.get(categoria, 0) + importe
    return total_gastado


def categoria_mas_cara(totales: dict[str, float]) -> str:
    """Devuelve la categoria con importe más elevado"""
    mejor_categoria = ""
    mejor_total = 0
    for categoria, total in totales.items():
        if total > mejor_total:
            mejor_categoria = categoria
            mejor_total = total
    return mejor_categoria

totales = total_por_categoria(gastos)

assert totales == {"comida": 77.75, "transporte": 61.5, "ocio": 12.75}
assert total_por_categoria([]) == {}
assert categoria_mas_cara(totales) == "comida"

for categoria, total in totales.items():
    print(f"{categoria:<12} {total:>8.2f} €")
print("Todas las comprobaciones pasan ✅")