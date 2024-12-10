# -*- coding: utf-8 -*-
"""
08.12.2024 - Control Flow and Logic
"""

"""
Př. 1
Uživatel zadá přirozené číslo N a vy zjistíte, zdali dané číslo je prvočíslo.
prvočíslo je dělitelné 1 a samo sebou
2,3,5

"""

cislo=int(input("Zadej přirozené číslo N: "))
pomoc=0
for i in range (2,int((cislo**0.5))+1):
    if cislo%i==0:
        pomoc=1
        break
    
if pomoc==1:  
    print(f"Číslo {cislo} není prvočíslem")
else:
    print(f"Číslo {cislo} je prvočíslem")

"""
definování funkce

def název_funkce(proměnné):
    tělo funkce
"""   

def soucet_dvou_cisel(a,b):
    c=0
    for i in range(2,b):
       c*=i 
    return c

a=5
b=10

print(soucet_dvou_cisel(a, b))


"""
Př. 2
Uživatel zadá přirozené číslo N a vy zjistíte, zdali dané číslo je prvočíslo.
prvočíslo je dělitelné 1 a samo sebou

za pomocí využití funkce
"""
def prvocislo(cislo):
    for i in range(2,int(cislo/2)+1):
        if cislo%i==0:
            print(f"Zadané číslo {cislo} není prvočíslo, je dělitelné číslem {i}")
            return 
    print(f"Zadané číslo {cislo} je prvočíslo")
    return

cislo=int(input("Zadej mi přirozené číslo N: "))

prvocislo(cislo)


"""
EXTRA
Naplnění pole náhodnými čísly pomocí import 
"""

import random

seznam = [random.randint(0, 50) for i in range(100)] # plnění pole 
print(seznam)

"""
Př. 3
Soucet a soucin dvou čísel pomocí funkce
"""
def soucet_dvou_cisel(a,b): #definování funkce sčítání dvou čísel
    return a+b

def soucin_dvou_cisel(a,b): #definování funkce násobení dvou čísel
    return a*b
a=5
b=10

print(soucet_dvou_cisel(a, b))
print(soucin_dvou_cisel(a, b))

"""
Př. 4
"""

def pocet_nul(a): #definování funkce pocet nul v listu
    pocet=0
    for i in a:
        if i==0:
            pocet+=1
    return pocet

def delitelne_tremi(a): #definování funkce pocet čísel dělitelných třemi
    pocet=0
    for i in a:
        if i%3==0:
            pocet+=1
    return pocet

def vypis_delitelne_tremi(a): #definování funkce počet prvků dělitených třemi a vypsat je
    suda_cisla=[]
    pocet=0
    for i in a:
        if i%3==0 and i!=0:
            pocet+=1
            suda_cisla.append(i)
    print(pocet)
    return suda_cisla

def vypis_delitelne_tremi_nebo_peti_nedelitelne_patnacti(a): 
    #definování funkce která vypíše všechna čísla, která jsou dělitelná třemi, nebo 5, ale nejsou dělitelná 15
    suda_cisla=[]
    pocet=0
    for i in a:
        if (i%3==0 or i%5==0) and i!=15:
            pocet+=1
            suda_cisla.append(i)
    print(pocet)
    return suda_cisla

seznam=[2, 46, 38, 49, 23, 28, 38, 27, 44, 8, 39, 2, 27, 31, 5, 3, 47, 17, 10, 3, 17, 40, 6, 49, 27, 40, 49, 34, 13, 18, 10, 29, 39, 14, 7, 40, 11, 34, 20, 32, 12, 10, 44, 9, 41, 16, 1, 33, 44, 1, 1, 40, 26, 31, 10, 28, 7, 24, 46, 23, 30, 1, 43, 18, 23, 1, 30, 21, 47, 34, 19, 46, 30, 27, 26, 49, 34, 18, 46, 15, 20, 47, 49, 0, 22, 13, 10, 30, 15, 18, 31, 48, 27, 35, 17, 13, 40, 18, 0, 46]
seznam2=[46, 0, 41, 27, 38, 48, 41, 43, 0, 1, 16, 29, 23, 10, 26, 22, 19, 39, 30, 4, 44, 20, 11, 22, 18, 47, 13, 37, 8, 35, 45, 16, 43, 26, 50, 49, 42, 34, 0, 40, 38, 23, 24, 30, 38, 46, 31, 50, 6, 5, 4, 19, 5, 19, 20, 31, 7, 24, 7, 37, 36, 17, 21, 31, 10, 23, 11, 35, 11, 17, 33, 42, 8, 3, 43, 48, 22, 10, 13, 2, 25, 38, 1, 31, 35, 19, 16, 37, 32, 16, 32, 9, 47, 25, 32, 24, 46, 32, 1, 18]

print(pocet_nul(seznam))
print(pocet_nul(seznam2))
print(delitelne_tremi(seznam))
print(delitelne_tremi(seznam2))
print(vypis_delitelne_tremi(seznam))


"""
Př. 5
"""

def porovnani_seznamu(a,b): #vypsat všechna čísla, která jsou v obou seznamech shodná
    shodne=[]
    a_set=set(a)
    b_set=set(b)
    for i in a_set:
        for j in b_set:
            if i==j:
                shodne.append(i)
    return set(shodne)

seznam=[2, 46, 38, 49, 23, 28, 38, 27, 44, 8, 39, 2, 27, 31, 5, 3, 47, 17, 10, 3, 17, 40, 6, 49, 27, 40, 49, 34, 13, 18, 10, 29, 39, 14, 7, 40, 11, 34, 20, 32, 12, 10, 44, 9, 41, 16, 1, 33, 44, 1, 1, 40, 26, 31, 10, 28, 7, 24, 46, 23, 30, 1, 43, 18, 23, 1, 30, 21, 47, 34, 19, 46, 30, 27, 26, 49, 34, 18, 46, 15, 20, 47, 49, 0, 22, 13, 10, 30, 15, 18, 31, 48, 27, 35, 17, 13, 40, 18, 0, 46]
seznam2=[46, 0, 41, 27, 38, 48, 41, 43, 0, 1, 16, 29, 23, 10, 26, 22, 19, 39, 30, 4, 44, 20, 11, 22, 18, 47, 13, 37, 8, 35, 45, 16, 43, 26, 50, 49, 42, 34, 0, 40, 38, 23, 24, 30, 38, 46, 31, 50, 6, 5, 4, 19, 5, 19, 20, 31, 7, 24, 7, 37, 36, 17, 21, 31, 10, 23, 11, 35, 11, 17, 33, 42, 8, 3, 43, 48, 22, 10, 13, 2, 25, 38, 1, 31, 35, 19, 16, 37, 32, 16, 32, 9, 47, 25, 32, 24, 46, 32, 1, 18]
print(porovnani_seznamu(seznam,seznam2))
print(len(porovnani_seznamu(seznam,seznam2)))

"""
EXTRA pomocí knihovny numpy
"""
import numpy as np
seznam=[2, 46, 38, 49, 23, 28, 38, 27, 44, 8, 39, 2, 27, 31, 5, 3, 47, 17, 10, 3, 17, 40, 6, 49, 27, 40, 49, 34, 13, 18, 10, 29, 39, 14, 7, 40, 11, 34, 20, 32, 12, 10, 44, 9, 41, 16, 1, 33, 44, 1, 1, 40, 26, 31, 10, 28, 7, 24, 46, 23, 30, 1, 43, 18, 23, 1, 30, 21, 47, 34, 19, 46, 30, 27, 26, 49, 34, 18, 46, 15, 20, 47, 49, 0, 22, 13, 10, 30, 15, 18, 31, 48, 27, 35, 17, 13, 40, 18, 0, 46]
seznam2=[46, 0, 41, 27, 38, 48, 41, 43, 0, 1, 16, 29, 23, 10, 26, 22, 19, 39, 30, 4, 44, 20, 11, 22, 18, 47, 13, 37, 8, 35, 45, 16, 43, 26, 50, 49, 42, 34, 0, 40, 38, 23, 24, 30, 38, 46, 31, 50, 6, 5, 4, 19, 5, 19, 20, 31, 7, 24, 7, 37, 36, 17, 21, 31, 10, 23, 11, 35, 11, 17, 33, 42, 8, 3, 43, 48, 22, 10, 13, 2, 25, 38, 1, 31, 35, 19, 16, 37, 32, 16, 32, 9, 47, 25, 32, 24, 46, 32, 1, 18]
shodne_prvky=np.intersect1d(seznam, seznam2)
print(shodne_prvky)


"""
Př. 6
vypsat unikátní prvky, které jsou pouze v souboru A a souboru B 
"""
def ruzne_prvky(a,b): # řešení pomocí for cyklu
    souborA=[]
    souborB=[]
    for i in a:
        pomoc=0
        for j in b:
            if i==j:
                pomoc=1
        if pomoc==0:
            souborA.append(i)
    
    for i in b:
        pomoc=0
        for j in a:
            if i==j:
                pomoc=1
        if pomoc==0:
            souborB.append(i)
    return souborA, souborB
            
def ruzne_prvky2(a,b): 
    a_set=set(a)
    b_set=set(b)
    souborA=list(a_set-b_set) # vypsat unikátní prvky které jsou pouze v souboru A
    souborB=list(b_set-a_set) # vypsat unikátní prvky které jsou pouze v souboru B
    return souborA, souborB

def ruzne_prvky3(a,b): # jednořádkové řešení předchozí funkce
    return list(set(a)-set(b)),list(set(b)-set(a))

seznam=[2, 46, 38, 49, 23, 28, 38, 27, 44, 8, 39, 2, 27, 31, 5, 3, 47, 17, 10, 3, 17, 40, 6, 49, 27, 40, 49, 34, 13, 18, 10, 29, 39, 14, 7, 40, 11, 34, 20, 32, 12, 10, 44, 9, 41, 16, 1, 33, 44, 1, 1, 40, 26, 31, 10, 28, 7, 24, 46, 23, 30, 1, 43, 18, 23, 1, 30, 21, 47, 34, 19, 46, 30, 27, 26, 49, 34, 18, 46, 15, 20, 47, 49, 0, 22, 13, 10, 30, 15, 18, 31, 48, 27, 35, 17, 13, 40, 18, 0, 46]
seznam2=[46, 0, 41, 27, 38, 48, 41, 43, 0, 1, 16, 29, 23, 10, 26, 22, 19, 39, 30, 4, 44, 20, 11, 22, 18, 47, 13, 37, 8, 35, 45, 16, 43, 26, 50, 49, 42, 34, 0, 40, 38, 23, 24, 30, 38, 46, 31, 50, 6, 5, 4, 19, 5, 19, 20, 31, 7, 24, 7, 37, 36, 17, 21, 31, 10, 23, 11, 35, 11, 17, 33, 42, 8, 3, 43, 48, 22, 10, 13, 2, 25, 38, 1, 31, 35, 19, 16, 37, 32, 16, 32, 9, 47, 25, 32, 24, 46, 32, 1, 18]

unikat_seznam, unikat_seznam2=ruzne_prvky3(seznam, seznam2)
print(f"Unikatni prvky v prvním seznamu {unikat_seznam}")
print(f"Unikatni prvky v druhém seznamu {unikat_seznam2}")
