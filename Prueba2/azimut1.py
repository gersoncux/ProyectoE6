import math 


def azimut():
    #Latitud = 14.5877825       
# A comment.
    #Longitud = -90.5517531     ;coordenadas gps para usac

    l2 = 178.5                #longitud del satelite
    l1 = -90.5517531                 #longitud de la estación
    phi = 14.5877825                #latitud de la estación terrestre 
    dl = l2 - l1                #diferencia de longitudes

    b = math.tan(dl)            #tan(l2-l1)
    c = math.sin(phi)           #sen(phi)
    A = math.atan(b/c)          #calcular el azimut

    print("Grados de azimut: ",A)

def elevacion():
    phi = 14.5877825
    #Latitud = 14.5877825       
    #Longitud = -90.5517531     ;coordenadas gps para usac

    l2 = 53.6363                #longitud del satelite
    l1 = -90.5517531                 #longitud de la estación
    phi = 47.3877825                #latitud de la estación terrestre 
    dl = l2 - l1                #diferencia de longitudes

    d = math.cos(phi)*math.cos(dl)
    e = math.cos(d)
    f = math.acos(e)
    g = math.sin(f)
    E = math.atan((d-0.151267)/g)

    print("Grados de elvacion: ", E)

def Menu():
    correcto = False
    num = 0
    while(not correcto):
        try: 
            correcto = True
            num = int(input("Ingrese una opción: "))
        except ValueError:
            print("Seleccione una opción valida")
    return num
salir = False 
while not salir:
    print("\n1 para el azimut \n2 para la elevación \n3 para deterner el programa")
    opcion = Menu()
    if opcion ==1:
        azimut()
    elif opcion == 2:
        elevacion()
    elif opcion == 3:
        salir = True
    else:
        print("\nIngrese una opción valida")