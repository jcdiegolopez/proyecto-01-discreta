

from time import sleep
global_dict = { 'A' : { '1' : True, '2' : True, '3' : True }, 'B' : { '4' : True, '5' : True, '6' : True } }

def showConjunto(conjunto,name):
    elementos = ", ".join(conjunto.keys())
    print(f"{name}: {{{ elementos }}}")
    
def construirConjunto():
    print("Construir Conjunto")
    name = input("Ingrese el nombre de su conjunto (A a la Z): ")
    if(name == "" or not(name.isalpha())):
        print("No es un nombre valido")
        return
    global global_dict
    global_dict[name.upper()] = {}
    print("Ingrese los elementos del conjunto separados por comas ( A a la Z, 0 al 9)")
    elements = input("Ingrese los elementos: ")
    elements = elements.split(",")
    for element in elements:
        if not(element.isalnum()):
            print("Elemento no valido")
            return
        else:
            global_dict[name.upper()][element] = True;
    print("Conjunto agregado con extio")
    showConjunto(global_dict[name.upper()],name.upper())

def complemento():
    print("Complemento")
    conjunto1name = input("Ingrese el conjunto (A a Z): ")
    if(conjunto1name not in global_dict):
        print("Conjunto no encontrado")
        return
    else:
        conjunto1 = global_dict[conjunto1name]
    
def union():
    print("Union")

def interseccion():
    print("Interseccion")

def diferencia():
    print("Diferencia")

def diferenciaSimetrica():
    print("Diferencia Simetrica")
    
def operarConjuntos():
    print("Operar conjunto")
    print("Conjuntos disponibles:")
    global global_dict
    for key in global_dict:
        showConjunto(global_dict[key],key)
    
    # conjunto1name = input("Ingrese el primer conjunto (A a Z): ")
    # if(conjunto1name not in global_dict):
    #     print("Conjunto no encontrado")
    #     return
    # else:
    #     conjunto1 = global_dict[conjunto1name]
    # conjunto2name = input("Ingrese el segundo conjunto (A a Z): ")
    # if(conjunto2name not in global_dict):
    #     print("Conjunto no encontrado")
    #     return
    # else:
    #     conjunto2 = global_dict[conjunto2name]
    print("Operaciones disponibles:")
    print("1. Complemento")
    print("2. Union")
    print("3. Interseccion")
    print("4. Diferencia")
    print("5. Diferencia Simetrica")
    print("6. Salir")
    opcion = input("Ingrese una opcion: ")
    match opcion:
        case '1':
            complemento()
        case '2':
            union()
        case '3':
            interseccion()
        case '4':
            diferencia()
        case '5':
            diferenciaSimetrica()
        case '6':
            return
    

while True:
    print("1. Construir Conjuntos")
    print("2. Operar Conjuntos")
    print("3. Salir")
    opcion = input("Ingrese una opción: ")
    
    match opcion:
        case '1':
            construirConjunto()
        case '2':
            operarConjuntos()
        case '3':
            print("Saliendo...")
            sleep(0.5)
            break
        
