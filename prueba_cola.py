cola=[]

def agregar(paciente):
    cola.append(paciente)
def atender():
    if cola==[]:
        return ("la cola est� vac�a")
    else:
        print("\n**El paciente con c�dula " +str(cola.pop(0)) + " ha sido atendido**\n")
def consultar():
    print cola

    
while True:
    print("1. agregar paciente")
    print("2. atender paciente")
    print("3. consultar cola")
    opcion = int(input())
    if opcion == 1:
        pa=input("c�dula del paciente\n")
        agregar(pa)
    elif opcion==2:
        atender()
    elif opcion==3:
        consultar()
    else:
        break
    
