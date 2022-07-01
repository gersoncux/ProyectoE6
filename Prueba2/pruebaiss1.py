import urllib.request as url
import json
import math 
import time
from cmath import sqrt
##################################################################################################################################################################################
def estacion1():
    while True:
        try:
            ISS = url.Request("http://api.open-notify.org/iss-now.json")
            response_ISS = url.urlopen(ISS)
            ISS_obj = json.loads(response_ISS.read())
            dato3 = ISS_obj['iss_position']['latitude'];
            dato4 = ISS_obj['iss_position']['longitude'];
            latitud1 = 14.64433 #latitud de nuestro punto
            longitud1 = -90.51339 #longitud de nuestro punto
            lat2 = float(dato3) #latitud del satelite
            lon2 = float(dato4) #longitud del satelite
            rad = math.pi/180
            dlat = lat2-latitud1
            dlon = lon2-longitud1
            Rdt = 6372.795477598 #radio de la tierra en km
            a = math.sin(rad*dlat/2)**2 + math.cos(rad*latitud1)*math.cos(rad*lat2)*math.sin(rad*dlon/2)**2 #datos dentro de la raíz
            distancia = 2*Rdt*math.asin(math.sqrt(a)) #formula Haversine, distancia de nuestro punto a la proyección del satelite
            h = 408 #altura de la iss en km
            el = math.atan(h/distancia)
            sube = el*(180/math.pi)
            h = 1501.8
            medida = 2*h*Rdt+h**2
            horizonte = math.sqrt(medida)
            print("El horizonte es de: ", round(horizonte,2))
##################################################################################################################################################################################
            if(float(dato3) > latitud1 and float(dato4) > longitud1): #Cuadrante I; longitud > -90.51327 ; Latitud > 14.64072------DISTANCIA DE LONGITUD
                dlatI = 0 
                dlonI = lon2-longitud1
                a = math.sin(rad*dlatI/2)**2 + math.cos(rad*latitud1)*math.cos(rad*lat2)*math.sin(rad*dlonI/2)**2 #datos dentro de la raíz
                distanciaI = 2*Rdt*math.asin(math.sqrt(a)) #formula Haversine, distancia de nuestro punto a la proyección del satelite
                azimut = math.acos(distanciaI/distancia)
                giro = azimut*(180/math.pi) 
                print("Distancia de origen a proyección del iss: ", round(distancia,2), "km. Distancia en longitud: ", round(distanciaI,2),"km, I cuadrante")
                print("Angulo de elevación: ", round(sube,2),"Azimut: ",round(90-giro,2) ,"en grados, a favor de las agujas del reloj \n")
            elif(float(dato3) > latitud1 and float(dato4) < longitud1): #Cuadrante II; longitud > -90.51327 ; Latitud > 14.64072-----DISTANCIA DE LATITUD
                dlatII = lat2-latitud1
                dlonII = 0 
                a = math.sin(rad*dlatII/2)**2 + math.cos(rad*latitud1)*math.cos(rad*latitud1)*math.sin(rad*dlonII/2)**2 #datos dentro de la raíz
                distanciaII = 2*Rdt*math.asin(math.sqrt(a)) #formula Haversine, distancia de nuestro punto a la proyección del satelite
                azimut = math.acos(distanciaII/distancia)
                giro = azimut*(180/math.pi) 
                print("Distancia de origen a proyección del iss: ", round(distancia,2), "km. Distancia en latitud: ", round(distanciaII,2), "km, II cuadrante")
                print("Angulo de elevación: ", round(sube,2),"Azimut: ", round(90-giro,2) ,"en grados, en contra de las agujas del reloj \n")
            elif(float(dato3) < latitud1 and float(dato4) < longitud1): #Cuadrante III; longitud > -90.51327 ; Latitud > 14.64072-----DISTANCIA DE LONGITUD
                dlatIII = 0 
                dlonIII = lon2-longitud1
                a = math.sin(rad*dlatIII/2)**2 + math.cos(rad*latitud1)*math.cos(rad*latitud1)*math.sin(rad*dlonIII/2)**2 #datos dentro de la raíz
                distanciaIII = 2*Rdt*math.asin(math.sqrt(a)) #formula Haversine, distancia de nuestro punto a la proyección del satelite
                azimut = math.acos(distanciaIII/distancia)
                giro = azimut*(180/math.pi) 
                print("Distancia de origen a proyección del iss: ", round(distancia,2), "km. longitud: ", round(distanciaIII,2),"km, cuadrante III")
                print("Angulo de elevación: ", round(sube,2),"Azimut: ", round(180-giro,2) ,"en grados, en contra de las agujas del reloj \n")
            elif(float(dato3) < latitud1 and float(dato4) > longitud1): #Cuadrante IV; longitud > -90.51327 ; Latitud > 14.64072------DISTANCIA DE LATITUD
                dlatIV = lat2-latitud1
                dlonIV = 0
                a = math.sin(rad*dlatIV/2)**2 + math.cos(rad*latitud1)*math.cos(rad*lat2)*math.sin(rad*dlonIV/2)**2 #datos dentro de la raíz
                distanciaIV = 2*Rdt*math.asin(math.sqrt(a)) #formula Haversine, distancia de nuestro punto a la proyección del satelite
                azimut = math.acos(distanciaIV/distancia)
                giro = azimut*(180/math.pi) 
                print("Distancia de origen a proyección del iss: ", round(distancia,2), "km. latitud: ", round(distanciaIV,2), "km, cuadrante IV")
                print("Angulo de elevación: ", round(sube,2)," Azimut: ", round(180-giro,2) ,"en grados, a favor de las agujas del reloj \n")
##################################################################################################################################################################################
            time.sleep(5)
        except Exception as e:
            print(str(e))
            break 
##################################################################################################################################################################################
def separacion():
    lat1 = 14.64433
    lon1 = -90.51339
#########################################################################################
    ISS = url.Request("http://api.open-notify.org/iss-now.json")
    response_ISS = url.urlopen(ISS)
    ISS_obj = json.loads(response_ISS.read())
    dato3 = ISS_obj['iss_position']['latitude'];
    dato4 = ISS_obj['iss_position']['longitude'];
    print('Latitud', dato3)
    print('Longitud', dato4)
#########################################################################################
    lat2 = float(dato3)
    lon2 = float(dato4)

    rad = math.pi/180
    dlat = lat2-lat1
    dlon = lon2-lon1
    r = 6372.795477598

    a = math.sin(rad*dlat/2)**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*math.sin(rad*dlon/2)**2
    distancia = 2*r*math.asin(math.sqrt(a))
    print("la distancia es de ",int(distancia)," Km")
##################################################################################################################################################################################
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
    print("\n1 El azimut y la elevación \n2 para la distancia que hay de un punto a otro \n3 para deterner el programa")
    opcion = Menu()
    if opcion ==1:
        estacion1()
    elif opcion == 2:
        separacion()
    elif opcion == 3:
        salir = True
    else:
        print("\nIngrese una opción valida")
    