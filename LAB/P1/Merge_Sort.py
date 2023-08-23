#MergeSort

def CrearSubArreglo (A, indIzq, indDer):
    return A[indIzq:indDer+1]

def Merge(A, p, q, r):
    Izq=CrearSubArreglo(A,p,q)
    Der=CrearSubArreglo(A,q+1,r)
    i=0
    j=0
    global comparacion
    for k in range (p, r+1):
        comparacion+=1
        if (j >= len(Der)) or (i< len(Izq) and Izq[i] < Der[j]):
            A[k] = Izq[i]
            i=i+1
        else:
            A[k] = Der[j]
            j= j+1
    

def MergeSort(A,p,r):
    if r - p>0:
        q=int((p+r)/2)
        MergeSort(A,p,q)
        MergeSort(A,q+1,r)
        Merge(A,p,q,r)

#Main
comparacion=0
A=[7,20,8,50,1,-1]
n=len(A)
MergeSort(A,0,n-1)
print(A)
print(comparacion)

print("\n\n")
comparacion=0
B=[9,1,2,3,4,5,6,7,8]
n=len(B)
MergeSort(B,0,n-1)
print(B)
print(comparacion)

print("\n\n")
comparacion=0
C=['Juan','Juana','Luis','Jose','Ana']
n=len(C)
MergeSort(C,0,n-1)
print(C)
print(comparacion)