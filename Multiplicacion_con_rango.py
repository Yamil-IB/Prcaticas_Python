#Crearemos un menu con las funciones 

#factorial
#tablas de multiplicar
#potencia

print("#fun FACTORIAL press 0\n#fun TABLA DE MULTIPLICACION press 1\n#fun Potecia press 2")
def mostrar_tablas():
    t=int(input("Mostrar tabla del :"))
    i=0
    while i<=10:
        m=t*i
        print(t,"*",i,"= ",m)
        i+=1