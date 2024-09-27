pila=[1,2,3,4,5,1,7,8,9,10]

def Pares_pila():
    i=0
    par=0
    while i<len(pila):
        if (pila[i]%2)==0:
            par+=1
        i+=1
    print("Cantidad de pares: ",par)        
#Invocamos a la funcion
Pares_pila()
