#!/bin/bash

for i in 1 2 4 8 16 32 64 128 256 512 
do
    ./separa.awk -v seleccionado=$i < experimento.dat > largo$i.dat
done