#Import argv method from sys library
from sys import argv
#Import numpy as np
import numpy as np
#Random method from random library
from random import random
#Time method from time library
from time import time

#This is the generator of zeros and ones
#and this generate the zeros and ones 
# from a frequencie of zeros
def generador(fz):
    if fz > random():
        return 0
    return 1

#This generate words and returns it in a tuple,
#take as a parameter the large of the word and
#the frequencie of zeros
def palabra(largo, fz):
    #empty tuple
    palabra = []
    #iterate the large of the word
    # and call generator to get
    # the large word 
    for x in xrange(largo):
        palabra.append(generador(fz))
    return palabra

#This make a transmissions of words
# take as a parameter the word,
# probability of zeros turn ones and
# probability of ones turn zeros
def transmisor(palabra, pz, pu):
    #empty tuple
    palabra_transmitida = []
    #iterate the word and verify if p is equal to 0 or 1
    #and verify his probability that turn 0 to 1 and 1 to 0
    #and return the transmitted word
    for p in palabra:
        if p == 0 and pz < random():
            palabra_transmitida.append(1)
        elif p == 1 and pu < random():
            palabra_transmitida.append(0)
        else:
            palabra_transmitida.append(p)
    return palabra_transmitida

#Get the standard desviation
# taking as a parameter the average, average**2 and the n number
def desviacion_estandar(s, x2, n):
    return ( ( x2 ) * ( n * x2 ) / ( n - 1.0 ) ) ** (1.0/2.0)

#This is that make the simulation of the channel taking as parameter
# the frequencies of zeros, probability of success zeros and ones
def simulador(freq_zero, probabilidad_de_exito_zero, probabilidad_de_exito_uno):
   #b is the base
   b = 2
   #s is the average
   s = 0
   # x is the square of the average
   x2 = 0
   #the power of the number y number maxium
   n = 10
   #Iterates the numbers of power
   for y in range(n):
       #print b ** y
       #initialize the counter of exitos
       exitos = 0
       #initialize the average
       s = 0
       #initialize the square of average
       x2 = 0
       #take the current time
       t1 = time()
       #make 30 proofs for each large of words
       for x in xrange(30):
           #Get the word from palabra()
           #where sends as parameters the large of the word and the frequency of zeros
           palabra_m = palabra(b ** y, freq_zero)
           #print "Mensaje a enviar: ",palabra_m
           #get the word transmitted using transmisor()
           #taking as parameters the word transmitted, probabilty of zeros
           #probability of ones
           palabra_transmitida = transmisor(palabra_m, probabilidad_de_exito_zero, probabilidad_de_exito_uno)
           #print "Mensaje despues de la transmision: ",palabra_transmitida
           #if the words are the same we'll get an success and add +1
           if palabra_m == palabra_transmitida:
               estado = "Exito"
               exitos += 1
           else:
               estado = "Fracaso"
           #print "Estado: ",estado
       # take the current time
       t2 = time()
       # take the average
       s += ( exitos ) / 30.0
       # take the square of the average
       x2 += ( ( exitos ) / 30.0 ) ** 2
       #desviacion_est = desviacion_estandar(probabilidad, 30, n_exitos_deseados)
       #print "LARGO: ",b**y," PROMEDIO DE EXITOS: ", ( ( exitos ) / 30.0 ) * 100
       #print "EXITOS: ",exitos
       #print "DESVIACION ESTANDAR: ", desviacion_est
       #print "TIEMPO TOTAL: ", ( t2 - t1 ) * 1000.0
   #print s, x2, n
   #print "Desviacion estandar: ", desviacion_estandar( s, x2, n )
       # print the frequency of zeros, probability of success in zeros, probability of success in ones, large of the word, average, and standard desviation
       print freq_zero, probabilidad_de_exito_zero, probabilidad_de_exito_uno, b**y, s,desviacion_estandar( s, x2, n )

def main():
    #the power of the base of the number selected
    n = 10
    #test all the possible combinations in frecuency of zeros, probabilty of zeros and probability of ones in simulador()
    for fz in xrange(n):
        for pz in xrange(n):
            for pu in xrange(n):
                freq_cero = ( fz * 1.0 ) / ( n * 1.0 )
                prob_cero =  ( pz * 1.0 ) / ( n * 1.0) 
                prob_uno = ( pu * 1.0 ) / ( n * 1.0) 
                simulador( freq_cero, prob_cero, prob_uno)
                
main()
