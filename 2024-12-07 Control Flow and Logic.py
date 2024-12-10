# -*- coding: utf-8 -*-
"""
07.12.2024 - Control Flow and Logic
"""

"""
přiřazení proměnné
Př.1
"""

a=5
b=5

for i in range(10):
    a+=1 #ekvivalentní zápis a=a+1 -> a+=1
    b=b+1    
print(a, b)

"""
Př.2
"""
c=2
d=2

for i in range(10):
    c*=2 #Shodně pro násobení ->c=c*2 -> c*=2
    d=d*2
    
    #print(c, d) #když tisknu uvnitř cyklu, tak vytiskne pokaždé
print(c,d)    

"""
použití logické proměnné OR - stačí, aby byla splněna alespoň jedna podmínka
Př.3
"""

dnes="pondeli"

if dnes=="pondeli" or dnes=="streda" or dnes=="patek" :
    print("muzu do divadla")
else:
    print("nemuzu do divadla")
"""
Cyklus WHILE - dokud není splněna podmínka, běží tělo cyklu
Př.4
"""   
    
x = 0
y=0
while x < 5:
    print(x)
    x+=1
    
"""
Cyklus WHILE - podmínka v tomto případě není níkdy splněna, cyklus běží do nekonečna (kdo to spustí, tak musí zastavit v terminalu)
Př.5
"""   
    
x = 0
y=0
while y < 5:
    print(x)
    x+=1



"""
-----------------------------------------------------------------------------------------------------------------------------------
Live coding 
-----------------------------------------------------------------------------------------------------------------------------------
"""

books= [{
"Title": "To Kill a Mockingbird", 
"Author": "Harper Lee", 
"Year of First Publication":"1960",
"Characters": "['Scout Finch', 'Atticus Finch', 'Jem Finch', 'Tom Robinson']"},
    {
"Title": "1984",
"Author": "George Orwell",
"Year of First Publication": "1949",
"Characters": "['Winston Smith', 'Julia', 'O'Brien', 'Big Brother']"}]


"""
Př. 6
Make both book titles visible in the terminal using 
only one print() inside a for loop.
"""

for tituly in books:
    print(tituly["Title"])
    
"""
Př. 7
Display the authors of both books in the terminal using a simple for loop.
"""
for tituly in books:
    print(tituly["Author"])
    
    
"""
Př. 8
Check if the first book is newer than 
1950 using its is_published_after_1950 key and display the title only if it's True.
"""
#1. krok is_published_after_1950
for tituly in books:
    if int(tituly["Year of First Publication"])>1950:
        tituly["is_published_after_1950"]=True
    else:
        tituly["is_published_after_1950"]=False

print(books)

for tituly in books:
    if tituly["is_published_after_1950"]==True:
        print(tituly["Title"])

"""
Př. 9
Concatenate the title of the books with a 
string indicating if the book is newer or older than 1950.
"""
        
for tituly in books:
    if tituly["is_published_after_1950"]==True:
          print(f"Titul {tituly['Title']} " \
                f"autora {tituly['Author']} " \
                "byl vydán po roce 1950")

"""
Př. 10
Use the not-equal operator (!=) 
for the same result as the previous task.
"""
        
for tituly in books:
    if tituly["is_published_after_1950"]!=False:
          print(f"Titul {tituly['Title']} " \
                f"autora {tituly['Author']} " \
                "byl vydán po roce 1950")
"""
Př. 11
Use inequality operators to display the book title 
with a prefix indicating if it's newer or older than 1950.
"""        
for tituly in books:
    if int(tituly["Year of First Publication"])>1950:
          print(f"Titul {tituly['Title']} " \
                f"autora {tituly['Author']} " \
                "byl vydán po roce 1950")


"""
Př. 12
-----------------------------------------------------------------------------------------------------------------
input - vyzve k zadání hodnoty - my čteme jako string (text)
int() - převede text na integer - pokud je to možné

"""
roky=int(input("kolik ti je? "))
if roky<20:
    print("Jsi náctiletý")
    

"""
Př. 13
Napište program, který požádá uživatele o jakékoliv přirozené číslo N větší než 0 
a vypíše všechna čísla od 1 do N na druhou

pomocí while cyklu
"""    

prirozene_cislo=int(input("Zadej jakékoliv přirozené číslo větší než 0 "))

pomocne_cislo=1
if prirozene_cislo>0:
    while pomocne_cislo<=prirozene_cislo:
        print(pomocne_cislo**2)
        pomocne_cislo+=1    
else:
    print("Zadane cislo neni větší než nula")
    


"""
Př. 14
Napište program, který požádá uživatele o jakékoliv přirozené číslo N větší než 0 
a vypíše všechna čísla od 1 do N na druhou 

pomocí for cyklu
"""
prirozene_cislo=int(input("Zadej jakékoliv přirozené číslo větší než 0 "))

if prirozene_cislo>0:
    for i in range(prirozene_cislo):
        print((i+1)**2)
else:
    print("Zadane cislo neni větší než nula")      


"""
Př. 15

Napište program, který od uživatele jako vstup přijme slovo 
a poté zobrazí každý druhý znak zadaného textu. 
Následně by program měl zobrazit další textovou zprávu z ostatních písmen.
"""

seznam=input("Zadej slovo ")
print(seznam[1::2])
print(seznam[::2])

"""
Př. 16
Napište program, který požádá uživatele, aby zadal rok, 
a poté zkontroluje, zda je rok přestupný. 
(Rada: Rok je přestupný, když je dělitelný 400 nebo když je 
 dělitelný 4, ale není dělitelný 100).
"""
rok = int(input("Zadej rok: "))
if (rok % 400 == 0) or (rok % 4 == 0 and rok % 100 != 0):
    print(f"Rok {rok} je přestupný.")
else:
    print(f"Rok {rok} není přestupný.")

"""
Př. 17
Napište program, který požádá uživatele o vstup přirozeného čísla N, 
poté vytvoří slovník s klíči od 1 do N, jejichž hodnoty jsou druhé mocniny těchto klíčů.
5

slovnik={
    1:1,
    2:4
    3:9
    4:16
    5:25}
"""


cislo=int(input("Zadaj cislo do slovnika:  "))
slovnik={}
for x in range (1,cislo + 1):
    slovnik[x]=x**2
    
print(slovnik)

"""
Alternativně
"""
cislo=int(input("Zadaj cislo do slovnika:  "))

slovnik2={x:x**2 for x in range(1,cislo+1)}

pole=[x**2 for x in range(1,10+1)]

print(pole)


