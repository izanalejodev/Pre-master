"""Debe imprimir del 1 al 30, cambiando los múltiplos de 3 por “Fizz”, 
los de 5 por “Buzz” y los de ambos por “FizzBuzz”. """


for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)