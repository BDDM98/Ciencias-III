alfabeto=list('abcdefghijklmnopqrstuvwxyz')
digitos=list('0123456789')
n=50
pila=[]
EP=[]
tope=-1

def llena():
    if(tope==(n-1)):
        print("llena")
        return True
    return False

def vacia():
    if(tope==-1):
        print("vacia")
        return True
    return False

def push(dato):
    if(llena()!=True):
        global tope
        tope=tope+1
        pila.apilar(tope,dato)

def pop():
    if (vacia()!=True):
        global tope
        aux=pila[tope]
        del pila[tope]
        tope=tope-1
        return aux
    else:
        return -9999

def infijo(i,EI):
    if(EI[i]=='^'):
        prioridadop=4
        return prioridadop
    elif (EI[i]=='*'):
        prioridadop=2
        return prioridadop
    elif (EI[i]=='/'):
        prioridadop=2
        return prioridadop
    elif (EI[i]=='+'):
        prioridadop=1
        return prioridadop
    elif (EI[i]=='-'):
        prioridadop=1
        return prioridadop
    elif (EI[i]=='('):
        prioridadop=5
        return prioridadop

def pripila(pila):
    if(pila[tope]=='^'):
        prioridadpi=3
        return prioridadpi
    elif(pila[tope]=='*'):
        prioridadpi=2
        return prioridadpi
    elif(pila[tope]=='/'):
        prioridadpi=2
        return prioridadpi
    elif(pila[tope]=='+'):
        prioridadpi=1
        return prioridadpi
    elif(pila[tope]=='-'):
        prioridadpi=1
        return prioridadpi
    elif(pila[tope]=='('):
        prioridadpi=5
        return prioridadpi


eistring=rsw_input("ingrese la operacion sin espacios")
EI=list(eistring.upper())
x=0
y=0
for i in range(len (EI)):
    if (EI[i] in abod or EI[i] in udt):
        EP.append(EI[i])

    elif(EI[i]!= ')'):
        if (tope==-1):
            push(EI[i])
        else:
            if (infijo(i,EI)<=pripila(pila)):
                EP.append(pop())
                push(EI[i])
            elif(infijo(i,EI)>pripila(pila)):
                push(EI[i])
    elif(EI[i]==')'):
        while (pila[tope]!='('):
            EP.append(pop())
        if (pila[tope]=='('):
            pop()
            x=x+1
        elif (tope!=-1):
            EP.append(pop())

while (tope>-1):
    EP.append(pop())
print ''.join(EP)
    
        
        
