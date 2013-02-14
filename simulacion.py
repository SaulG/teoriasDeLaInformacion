#Se importa la libreria argv
from sys import argv
#Se libreria importa numpy
import numpy as np
#importa libreria random
from random import random
#se importa libreria tiempo
from time import time


#Este es el generador de ceros y unos
#esto lo hace apartir de la probabilidad
#de frecuencia
def generador(fz):
    if fz > random():
        return 0
    return 1

#Este genera palabras y las regresa en una tupla
#toma como parametro el largo de la palabra y la
# frecuencia de ceros
def palabra(largo, fz):
    #se declara una tupla vacia
    palabra = []
    #se itera segun el largo
    #para generar una letra llama segun
    # el tamanio de la palabra a generador
    for x in xrange(largo):
        palabra.append(generador(fz))
    return palabra

#Este hace una transmision de palabras
# tomando como parametro la palabra
# probabilidad de que cero se convierta
# a uno y de que uno se convierta a cero
def transmisor(palabra, pz, pu):
    #Se declara una tupla vacio
    palabra_transmitida = []
    #itera la palabra y verifica que si p es igual a un (0 o 1)
    #segun el cero o uno verifica su probabilidad de que 
    #cambien al finalizar regresa la palabra transmitida
    for p in palabra:
        if p == 0 and pz < random():
            palabra_transmitida.append(1)
        elif p == 1 and pu < random():
            palabra_transmitida.append(0)
        else:
            palabra_transmitida.append(p)
    return palabra_transmitida

#Este obtiene la desviacion estandar
# tomando como parametro promedio, promedio**2 y n numeros tomados
def desviacion_estandar(s, x2, n):
    return ( ( x2 ) * ( n * x2 ) / ( n - 1.0 ) ) ** (1.0/2.0)

#Este es el que hace la simulacion de el canal tomando como parametro
# la fecuencia de ceros, la probabilidad de exit de cero y la probabilidad de 
# exito de unos.
def simulador(freq_zero, probabilidad_de_exito_zero, probabilidad_de_exito_uno):
   #b es simplemente la base a lo que se le va a sacar la potencia 
   b = 2
   #s sera el promedio
   s = 0
   # el cuadrado del promedio
   x2 = 0
   # el numero de potencia y el no. maximo
   n = 10
   # Se itera el numero de potencias
   for y in range(n):
       #print b ** y
       #se inicializa el contador de exitos
       exitos = 0
       # se inicializa el promedio
       s = 0
       #se inicializa el cuadrado del promedio
       x2 = 0
       #se toma tiempo
       t1 = time()
       #se hacen 30 pruebas por cada largo de palabra
       for x in xrange(30):
           #se obtiene la palabra apartir del palabra()
           # donde envia como parametro el largo de la palabra y la frecuencia de ceros
           palabra_m = palabra(b ** y, freq_zero)
           #print "Mensaje a enviar: ",palabra_m
           #se obtiene la palabra transmitida por medio del transmisor()
           #tomando como palabra la palabra, probilidad de exito de zero y
           #probabilidad de exito de uno
           palabra_transmitida = transmisor(palabra_m, probabilidad_de_exito_zero, probabilidad_de_exito_uno)
           #print "Mensaje despues de la transmision: ",palabra_transmitida
           #si son las palabras iguales, se considera como exito sino se consideran
           #como fracaso
           if palabra_m == palabra_transmitida:
               estado = "Exito"
               exitos += 1
           else:
               estado = "Fracaso"
           #print "Estado: ",estado
       # se toma el tiempo
       t2 = time()
       # se toma el promedio
       s += ( exitos ) / 30.0
       # se toma el cuadrado del promedio
       x2 += ( ( exitos ) / 30.0 ) ** 2
       #desviacion_est = desviacion_estandar(probabilidad, 30, n_exitos_deseados)
       #print "LARGO: ",b**y," PROMEDIO DE EXITOS: ", ( ( exitos ) / 30.0 ) * 100
       #print "EXITOS: ",exitos
       #print "DESVIACION ESTANDAR: ", desviacion_est
       #print "TIEMPO TOTAL: ", ( t2 - t1 ) * 1000.0
   #print s, x2, n
   #print "Desviacion estandar: ", desviacion_estandar( s, x2, n )
       # se imprime la frecuencia de ceros, prob de exitos en cero probabilidad de exito en uno, largo, promedio y desviacion estandar
       print freq_zero, probabilidad_de_exito_zero, probabilidad_de_exito_uno, b**y, s,desviacion_estandar( s, x2, n )

def main():
    #potencia de la base del largo
    n = 10
    #se prueban todas las posibles combinaciones
    # de frecuencia de cero, probilidad de cero y probabilidad de unos
    # y se envian al simulador
    for fz in xrange(n):
        for pz in xrange(n):
            for pu in xrange(n):
                freq_cero = ( fz * 1.0 ) / ( n * 1.0 )
                prob_cero =  ( pz * 1.0 ) / ( n * 1.0) 
                prob_uno = ( pu * 1.0 ) / ( n * 1.0) 
                simulador( freq_cero, prob_cero, prob_uno)
                
main()
