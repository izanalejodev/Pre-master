"""Funciones para calcular el IVA y resumir una lista de gastos."""


def aplicar_iva(importe: float, iva: int = 21) -> float:
    """Devuelve el importe con el IVA aplicado, redondeado a 2 decimales."""
    cuota_iva = importe * iva / 100
    return round(importe + cuota_iva, 2)


def resumen_gastos(gastos: list[float]) -> tuple[float, float, float]:
    """Devuelve el total, la media y el máximo de una lista de gastos.

    Si la lista está vacía, devuelve (0, 0, 0) para evitar dividir entre cero.
    """
    if not gastos:
        return 0, 0, 0

    total = sum(gastos)
    media = total / len(gastos)
    return total, media, max(gastos)


assert aplicar_iva(100) == 121.0
assert aplicar_iva(100, iva=10) == 110.0
assert resumen_gastos([10, 20, 30]) == (60, 20.0, 30)
assert resumen_gastos([]) == (0, 0, 0)

total, media, maximo = resumen_gastos([12.5, 30, 7.25])
print(f"Total: {total:.2f} € | Media: {media:.2f} € | Máximo: {maximo:.2f} €")
print("Todas las comprobaciones pasan ✅")