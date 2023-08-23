def maximo_comun_divisor(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a

def minimo_comun_multiplo(a, b):
    return (a * b) / maximo_comun_divisor(a, b)

a=int(input("Ingrese el primer valor: "))
b=int(input("Ingrese el segundo valor: "))

mcm = minimo_comun_multiplo(a, b)
print(f"El mínimo común múltiplo de {a} y {b} es {mcm}")

resultado = maximo_comun_divisor(a, b)
print(f"El Máximo común divisor de {a} y {b} es {resultado}.")
