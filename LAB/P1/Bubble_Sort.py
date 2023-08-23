def bubbleSort2(A):
    global comparacion
    bandera = True
    pasada = 0
    while pasada < len(A) - 1 and bandera:
        bandera = False
        for j in range(len(A) - 1 - pasada):
            comparacion += 1
            if A[j] > A[j + 1]:  
                bandera = True
                temp = A[j]
                A[j] = A[j + 1]
                A[j + 1] = temp
        pasada = pasada + 1 

comparacion = 0
a1 = [7, 20, 8, 50, 1, -1]
bubbleSort2(a1)
print(a1)
print(comparacion)

comparacion = 0
a2 = [9, 1, 2, 3, 4, 5, 6, 7, 8]
bubbleSort2(a2)  
print(a2)
print(comparacion)

comparacion=0
a3 = ['Juan', 'Juana', 'Luis', 'Jose', 'Ana']
bubbleSort2(a3)
print(a3)
print(comparacion)