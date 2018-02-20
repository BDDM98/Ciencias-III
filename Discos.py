pila=[]

def apilar(peliculas):
    pila.append(peliculas)

def desapilar():
    print("la pelicula " + str(pila.pop()) + " se ha retirado de la pila")

def consultar():
    print pila

while True:
    print("1. agregar pelicula")
    print("2. buscar ultima pelicula ingresada")
    print("3. consultar pila de peliculas")
    opcion= int(input())
    if opcion==1:
        pe=raw_input("nombre de la pelicula\n")
        apilar(pe)
    elif opcion==2:
        desapilar()
    elif opcion==3:
        consultar()
    else:
        break
