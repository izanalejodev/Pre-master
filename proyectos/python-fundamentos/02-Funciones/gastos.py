"""devuelve el importe con IVA, redondeado a 2 decimales con round(valor, 2)"""
def aplicar_iva(importe, iva=21):
    porcentaje = iva / 100
    descuento = importe * porcentaje
    importe += descuento
    return round(importe, 2)

"""recibe una lista de importes y devuelve tres valores: total, media y gasto máximo. 
Puedes usar sum(), len() y max(). Si la lista está vacía, devuelve 0, 0, 0. 
Piensa por qué hace falta ese caso: ¿qué pasaría con la media?"""

def resumen_gastos(gastos):
    if(len(gastos) == 0):
        return 0, 0, 0
    else:
        total = sum(gastos)
        media = sum(gastos) / len(gastos)
        gasto_maximo = max(gastos)
    return (total, media, gasto_maximo)

assert aplicar_iva(100) == 121.0
assert aplicar_iva(100, iva=10) == 110.0
assert resumen_gastos([10, 20, 30]) == (60, 20.0, 30)
assert resumen_gastos([]) == (0, 0, 0)

total, media, maximo = resumen_gastos([12.5, 30, 7.25])
print(f"Total: {total:.2f} € | Media: {media:.2f} € | Máximo: {maximo:.2f} €")
print("Todas las comprobaciones pasan ✅")