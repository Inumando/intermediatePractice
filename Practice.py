# -*- coding: utf-8 -*-
"""
Created on Fri May  8 18:16:40 2020

@author: inu_s
"""

import pandas as pd #Pandas al leer los archivos crea un datraframe
import matplotlib.pyplot as plt
import math as mt

#Funcion de percentiles
def percentil(lista, nPercentil):
    lista.sort() #Ordena mi lista (sorted devuelve una nueva lista ordenada)
    per = nPercentil/4
    perPos = (len(lista)-1)*per
    cu = mt.ceil(perPos)
    pl = mt.floor(perPos)
    resPer = lista[pl] + (lista[cu] - lista[pl]) * per
    return resPer

#funcion de balla
def fences(fq, tq):
    IQR = tq - fq
    lFence = fq-IQR*1.5
    uFence = tq+IQR*1.5
    return lFence, uFence

#Funcion de los Whiskers
def whisker(fq, tq, lista):
    fence = fences(fq, tq)
    lWhis = 0
    uWhis = 0
    for item in lista:
        if item >= fence[0]:
            lWhis = item
            break
    for item in lista[-1::-1]:
        if item <= fence[1]:
            uWhis = item
            break
    return lWhis, uWhis

#funcion Outliers    
def outliers(fq, tq, lista):
    fence = fences(fq, tq)
    output = []
    for item in lista:
        if item < fence[0] or item > fence[1]:
            output.append(item)
    return output

#Funcion frecuencia
def frequencies(lista):
    frequencies = {}
        
    for value in lista:
        if value in frequencies:
            frequencies[value] += 1
        else:
            frequencies[value] = 1
        
    return frequencies

def recorte(listaObj, per):
    n = len(listaObj)
    k = (per/100)*n
    k = mt.floor(k)
    for i in range(k):
        listaObj.pop(0)
        listaObj.pop(-1)

#Función promedio
def mean(listaObj):
    prom = 0
    for item in listaObj:
        prom += item
    prom = prom / len(listaObj)
    return prom

#Desviacion estandar
def dEst(listaObj):
    media = mean(listaObj)
    suma = 0
    for i in listaObj:
        suma += (i-media)**2
    var = suma/(len(listaObj)-1)
    dvs = var**(1/2)
    return dvs


wf = 'C:\\Users\\inu_s\\Documents\\Escuela\\2020\\MineriaDeDatos\\intermediatePractice\\'
file = wf + '\survey_results_public.csv'
data = pd.read_csv(file, encoding = 'utf-8')

#Funcion que separa las columnas por tipo u opccion
def separate(listObj):
    output = []
    for i in listObj:
        aux = str(i).split(';')
        for j in aux:
            if j not in output and j != 'nan':
                output.append(j)
    return output

#Función que crea las listas
def listCreator(kinds, obj1, obj2):
    output = []
    for i in kinds:
        aux = [int(e) for e,s in zip(obj1, obj2) if i in str(s).split(';') and not mt.isnan(e)]
        output.append(aux)
    output.sort()
    return output
        
    

#Quest Numero 1----------------------------------------------------------------
salary = data['ConvertedComp'].tolist()
sexo = data['Gender'].tolist()

#Crear listas
gend = separate(sexo)
genders = listCreator(gend, salary, sexo)

def quest01(listaMax, types, count):
    mini = listaMax[0]
    maxi = listaMax[-1]
    fq = percentil(listaMax, 1)
    mediana = percentil(listaMax, 2)
    tq = percentil(listaMax, 3)
    promedio = mean(listaMax)
    print('Minimo: ' + str(mini) + '\nMaximo: ' + str(maxi) + '\nPrimer cuartil: ' +
          str(fq) + '\nMediana: ' + str(mediana) + '\nTercer cuartil: ' + str(tq) 
          + '\nPromedio: ' + str(promedio))
    plt.figure()
    plt.boxplot(listaMax)
    plt.suptitle(types[counter], fontsize=16)
    count += 1
    return count

counter = 0
for i in range(len(gend)):
    print('\nDatos para ' + gend[i] + ': ')
    counter = quest01(genders[i], gend, counter)
    
#Quest Numero 2----------------------------------------------------------------
ethnicity = data['Ethnicity'].tolist()

#Crear listas
etnias = separate(ethnicity)
listaEtnias = listCreator(etnias, salary, ethnicity)

counter = 0
for i in range(len(etnias)):
    print('\nDatos para ' + etnias[i] + ': ')
    counter = quest01(listaEtnias[i], etnias, counter)

#Quest03-----------------------------------------------------------------------
devType = data['DevType'].tolist()

#Crear listas
devSep = separate(devType)
devList = listCreator(devSep, salary, devType)

counter = 0
for i in range(len(devSep)):
    print('\nDatos para ' + devSep[i] + ': ')
    counter = quest01(devList[i], devSep, counter)

#Quest4------------------------------------------------------------------------














