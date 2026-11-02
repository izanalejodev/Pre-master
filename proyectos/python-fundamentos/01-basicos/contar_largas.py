"""Cuenta cuántas tienen más de 4 letras e imprímelo con un f-string. 
Debería salir 3. Si te atascas, vuelve al código de las vocales: la estructura es idéntica, 
solo cambia la condición."""


palabras = ["Me", "estoy", "preparando", "para", "el", "curso"]

mas_de_4 = 0
for i in palabras: 
  
   if(len(i) > 4):
      masDe3 += 1
print(f"Palabras de mas de 4 letras: {mas_de_4}")
