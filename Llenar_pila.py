#Llenar una pila con datos del usuario
array=[]
def llenar():
    i=0
    while i<1:
        a=int(input("introduzca valor: ")) 
        i+=1
        return a;

def introducir_dato():
    J=0
    while j < len(array):
        array.append(llenar())
        j+=1
        return array;



array=introducir_dato()
print("Nuevo array: ",array)
#a=llenar()
#print("Nuevo dato: ",a)