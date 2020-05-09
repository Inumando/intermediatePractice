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

#Quest Numero 1----------------------------------------------------------------
salary = data['ConvertedComp'].tolist()
sexo = data['Gender'].tolist()

#Lista Hombres
h = [e for e,s in zip(salary, sexo) if 'Man' in str(s).split(';') and not mt.isnan(e)]

print(h[0])
#Lista Mujeres
m = [e for e,s in zip(salary, sexo) if 'Woman' in str(s).split(';') and not mt.isnan(e)]


#lista otros
otros = [e for e,s in zip(salary, sexo) 
if 'Non-binary, genderqueer, or gender non-conforming' in str(s).split(';') and not mt.isnan(e)]


def quest01(listaMax):
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

print('\nDatos para hombres:')
quest01(h)
print('\nDatos para Mujeres:')
quest01(m)
print('\nDatos para otros: ')
quest01(otros)

#Quest Numero 2----------------------------------------------------------------
ethnicity = data['Ethnicity'].tolist()

african = [e for e,s in zip(salary, ethnicity) if 'Black or of African descent' in str(s).split(';') and not mt.isnan(e)]
asian = [e for e,s in zip(salary, ethnicity) if 'East Asian' in str(s).split(';') and not mt.isnan(e)]
latino = [e for e,s in zip(salary, ethnicity) if 'Hispanic or Latino/Latina' in str(s).split(';') and not mt.isnan(e)]
eastern = [e for e,s in zip(salary, ethnicity) if 'Middle Eastern' in str(s).split(';') and not mt.isnan(e)]
native = [e for e,s in zip(salary, ethnicity) if 'Native American, Pacific Islander, or Indigenous Australian' in str(s).split(';') and not mt.isnan(e)]
southAsian = [e for e,s in zip(salary, ethnicity) if 'South Asian' in str(s).split(';') and not mt.isnan(e)]
european = [e for e,s in zip(salary, ethnicity) if 'White or of European descent' in str(s).split(';') and not mt.isnan(e)]
biracial = [e for e,s in zip(salary, ethnicity) if 'Biracial' in str(s).split(';') and not mt.isnan(e)]
multiracial = [e for e,s in zip(salary, ethnicity) if 'Multiracial' in str(s).split(';') and not mt.isnan(e)]

print('\nDatos para africanos:')
quest01(african)
print('\nDatos para Asiaticos:')
quest01(asian)
print('\nDatos para latinos:')
quest01(latino)
print('\nDatos para Medio oeste:')
quest01(eastern)
print('\nDatos para Nativos Americanos:')
quest01(native)
print('\nDatos para Sur Asiaticos:')
quest01(southAsian)
print('\nDatos para Europeos:')
quest01(european)
print('\nDatos para Biracial:')
quest01(biracial)
print('\nDatos para Multiracial:')
quest01(multiracial)
