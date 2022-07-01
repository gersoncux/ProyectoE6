from os import system
import os

def menu():
    print('\n#################################################')
    print('#    Menu de control de Orientacion de Antena   #')
    print('#################################################\n')

    print('======================')
    print('Seleccione una opción')
    print('======================\n')

    print("\n1. Giro manual de la antena1.")
    print("2. Seguimiento de la ISS.")
    print("3. Prueba Distancia.")
    print("4. Giro manual corregido.")
    print("5. Proyecto Final.")
    print("6. Pasos.")
    print("7. Salir.\n")

while True:
    menu()
    opc = input("Ingrese una opción: ")
    os.system ("clear")



    if opc == '1':
        print("Ingrese direccion de giro (derecha, Izquierda )")
        grados =  int(input("Ingrese asimut en grados: "))
        elevacion =  float(input("Ingrese elevacion en grados: "))
        print("Giro manual de la antena.s")
        print("\npython Control_manual.py \n")
        system(f"python3 Servo.py {elevacion}" )
        system(f"python3 Prueba2.py " )

    elif opc == '2':
        print("Seguimiento de la trayectoria de la ISS.")
        print("\npython3 seguimiento.py \n")
        system(f"python3 pasos.py")
        system(f"python3 iss1.py")

    
    elif opc == '3':

        print("Giro manual de la antena cuando este en rango")
        print("\npython Control_manual.py \n")
        system(f"python3 Distancia.py " )

    elif opc == '4':
        print("Prueba Proyecto.")
        print("\npython3 Final.py \n")
        system(f"python3 Final.py")
        
    elif opc == '5':
        print("Prueba Final.")
        print("\npython3 Final.py \n")
        system(f"python3 PruebaFinal.py")
        
    elif opc == '6':
        print("Pasos de ISS.")
        print("\npython3 Pasos.py \n")
        system(f"python3 pasos.py")

    elif opc == '7':
        print("||---------------------------------------------||")
        print("||                                             ||")
        print("||                  Saliendo.                  ||")
        print("||                                             ||")
        print("||---------------------------------------------||")
        break


    else:
        menu()
        opc = input("Ingrese una opción: ")
        os.system ("clear")
