pila = [1, 2, 3, 3]
#Funcion eliminar elemento redundante
def Delete_repeat():
    i = 0
    while i < len(pila):       
          j = i + 1
          #print("Elemento :", pila[i])
          while j < len(pila):
           #print("Repetición: ", pila[j])
           if pila[i] == pila[j]:
            #print("Redundante : ", pila[j])
            pila.pop(j)
           else:
             j += 1
          i += 1  
#Invocamos a dicha funcion
Delete_repeat()
print("Pila resultante: ",pila)