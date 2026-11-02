frase = "Me estoy preparando para el curso de IA y Big Data"
palabras = frase.split()
#El programa debe imprimir, usando f-strings:
#- Número de palabras. 
print(f"Palabras: {len(palabras)}")

#- Número de vocales, contando también las mayúsculas.

vocales = 0
for letra in frase:
    if letra.lower() in "aeiou":
        vocales += 1
print(f"Vocales: {vocales}")
#- La palabra más larga.
mas_larga = palabras[0]
for palabra in palabras:
    if len(palabra) > len(mas_larga):
        mas_larga = palabra
print(f"Palabra más larga: {mas_larga}")

#- Cada palabra numerada desde 1, saltando las de 2 letras o menos (continue) 
#y parando al llegar a la primera palabra de más de 7 letras, sin imprimirla (break).

for i, palabra in enumerate(palabras, start=1):
    if(len(palabra) > 7):
            break
    if(len(palabra) <= 2):
            continue
    print(f"{i}: {palabra}")







