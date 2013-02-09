from sys import argv
import numpy as np
from random import random
from time import time


def generador(fz):
    if fz > random():
        return 0
    return 1
    
def palabra(largo, fz):
    palabra = []
    for x in xrange(largo):
        palabra.append(generador(fz))
    return palabra

def transmisor(palabra, pz, pu):
    palabra_transmitida = []
    for p in palabra:
        if p == 0 and pz < random():
            palabra_transmitida.append(1)
        elif p == 1 and pu < random():
            palabra_transmitida.append(0)
        else:
            palabra_transmitida.append(p)
    return palabra_transmitida

def desviacion_estandar(s, x2, n):
    return ( ( x2 ) * ( n * x2 ) / ( n - 1.0 ) ) ** (1.0/2.0)

def simulador(freq_zero, probabilidad_de_exito_zero, probabilidad_de_exito_uno):
   b = 2
   s = 0
   x2 = 0
   n = 10
   for y in range(n):
       #print b ** y
       exitos = 0
       s = 0
       x2 = 0
       t1 = time()
       for x in xrange(30):
           palabra_m = palabra(b ** y, freq_zero)
           #print "Mensaje a enviar: ",palabra_m
           palabra_transmitida = transmisor(palabra_m, probabilidad_de_exito_zero, probabilidad_de_exito_uno)
           #print "Mensaje despues de la transmision: ",palabra_transmitida
           if palabra_m == palabra_transmitida:
               estado = "Exito"
               exitos += 1
           else:
               estado = "Fracaso"
           #print "Estado: ",estado
       t2 = time()
       s += ( exitos ) / 30.0
       x2 += ( ( exitos ) / 30.0 ) ** 2
       #desviacion_est = desviacion_estandar(probabilidad, 30, n_exitos_deseados)
       #print "LARGO: ",b**y," PROMEDIO DE EXITOS: ", ( ( exitos ) / 30.0 ) * 100
       #print "EXITOS: ",exitos
       #print "DESVIACION ESTANDAR: ", desviacion_est
       #print "TIEMPO TOTAL: ", ( t2 - t1 ) * 1000.0
   #print s, x2, n
   #print "Desviacion estandar: ", desviacion_estandar( s, x2, n )
       print freq_zero, probabilidad_de_exito_zero, probabilidad_de_exito_uno, b**y, s,desviacion_estandar( s, x2, n )

def main():
    n = 10
    for fz in xrange(n):
        for pz in xrange(n):
            for pu in xrange(n):
                freq_cero = ( fz * 1.0 ) / ( n * 1.0 )
                prob_cero =  ( pz * 1.0 ) / ( n * 1.0) 
                prob_uno = ( pu * 1.0 ) / ( n * 1.0) 
                simulador( freq_cero, prob_cero, prob_uno)
                
main()
