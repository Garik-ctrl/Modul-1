# -*- coding: utf-8 -*-
"""
24.11.2024 - Programming Basics - Data Types and Structures
"""

a='AHOJ ' #ukládání do proměnné
b=' světe' #ukládání do proměnné
print(a+b)

c= a + b # sečetl jsem dva textové řetězce
print(c)

#práce s matematickými operacemi
print(2*3/(4+2)) 
c=2*3
d=4+2
print(c/d)
print(4/2) # dělení
print(4**2) #mocnina
print(5%3) # modulo (zbytek po dělení)
print(5//2) # dělení beze zbytku

"""
pole + tuple - základní vlastnosti
"""

Pole1=[5,3,2,11,13] #vytvoření listu - hranaté závorky
print(Pole1)
print(Pole1[::-1]) #vypsání listu od konce
Pole1[0]=999     #přepsání první hodnoty v listu
print(Pole1[0]) #vypsání hodnoty na nulté pozici

Tuple=(5,3,2,11,13) #vytvoření tuple - kulaté závorky
print(Tuple)
#Tuple[0]=999 - nelze přepisovat členy - vyhodí error
print(Tuple[3]) #vypsání hodnoty na nulté pozici

"""
vytvoření malého programu na výpočet
"""

a=int(input("Zadej a ")) 
#input - žádá uživatele, aby v terminaluzadal hodnotu
# int() - funce převede string na integer (text na číslo)
b=15
c=14
d=2*a-b**2+c*c
print(d)
"""
práce se sety
"""
# set - má složené závorky - každý prvek pouze jednou
my_set = {"apple", "banana", "cherry"}
exists = "banana" in my_set  # pokud je banán v setu, tak vypíše True, jinak False
print(exists)

my_set = {1, 2, 3}
my_set.add(4) #přidání hodnoty
my_set.add(-1)
my_set.update([4, 5, 6]) # přidání více hodnot
print(my_set)
my_set.remove(-1) #odebrání hodnoty
print(my_set)

"""
práce s tuply
"""
my_tuple = ("apple", "banana", "cherry")
my_tuple=my_tuple + ("orange",) #přidání hodnoty
print(my_tuple)
my_tuple.remove("orange") #odebrání hodnoty
print(my_tuple)
"""
práce s listem
"""
list2=[2,3,4,5,6,7,8,9]
list2.append(999) #přidání hodnoty
list2.insert(2, 666) #přidání hodnoty na konkrétní pozici
list2.extend([4,5]) #přidání více hodnot
list2.extend([(4,5)]) #přidání tuple
list2.pop(-1) #odebrání hodnoty v daném indexu

"""
CVIČENÍ
1. list, který bude 8 prvků
2. vytisknete list naopak
3. vytisknete každý druhý prvek
"""

import random
list1=random.sample(range(1, 101), 8) #jak naplnit pole jednoduše a náhodně
print(list1)
print(list1[::-1]) #pole naopak
print(list1[::2]) #pole ob jeden
print(list1[1::2]) #pole ob jeden a začátek v indexu 1

"""
CVIČENÍ
1. vytvoření setu (3 prvky)
2. přidat číslo 4 a 5
3. odebrat 4
"""
set1=set(list1) #převedení listu na set
print(set1)
set1.update([4, 5]) #přidání více hodnot
print(set1)
set1.remove(4) #odebrání hodnoty
print(set1)

"""
dictionary a práce s ním v listu
klíč: hodnota
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

print(books[0]["Title"])
print(books[0].get("Title"))
"""
Neděle - pokračování
"""

knihy=[{
        "title": "Moby Dick",
        "author": "Herrman Mellvile"},
       {
        "title": "Staroveká Kréta",
        "author": "Ludwika Pressová"
        }]

"""
for cyklus

for PROMĚNNÁ in POLE:
    
"""
for x in knihy:
    x["year2"]=2999 #vytvoření nového klíče s hodnotou 2999

for x in knihy:
    print(x["title"]) #vypsání všech knih

knihy[1]["year2"]=1950 #hodnota vepsána do klíče "year2" v knize na pozici 1
print(knihy)
"""
-----------------------------------------------------
"""
for x in knihy:
    x["year"]=None #přidání prázdných hodnot do klíče "year"
    
print(knihy)
knihy[0]["year"]=1950 #nastavení hodnoty v nulté pozici, klíč "year"
knihy[1]["year"]=1980
print(knihy)

for x in knihy:
    x["isNewerThan1970"]=None
    
knihy[0]["isNewerThan1970"]=False
knihy[1]["isNewerThan1970"]=True
print(knihy)

"""
IF podmínka

If PODMINKA >,<,>=, <=, == NĚCO :
    něco
else
    něco jiného

"""
for x in knihy: # pokud je kniha mladší než 1970 -> True, jinak False
    if x["year"]>1970:
        x["isNewerThan1970"]=True
    else:
        x["isNewerThan1970"]=False

print(knihy)

for x in knihy:
    x.pop("isNewerThan1970", None) #vypmazání klíče, "None" je přidáno, pokud by tam klíč nebyl

print(knihy)

"""
ALT+F/G [ ]
ALT+B/N { }
"""
knihy.append({"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813}) # přidání knihy




knihy=[{'title': 'Moby Dick', 
        'author': 'Herrman Mellvile', 
        'year': 1950, 'isNewerThan1970': False}, 
       {'title': 'Staroveká Kréta', 
        'author': 'Ludwika Pressová', 'year': 1980, 
        'isNewerThan1970': True}, 
       {'title': 'Pride and Prejudice', 
        'author': 'Jane Austen', 
        'year': 1813, 
        'isNewerThan1970': False}]


#počet let od vydání knihy
rok=2024
for x in knihy:
    x["age"]=rok- x["year"]


#přidání postav knihy
knihy[0]["characters"]=(["Capt. Achab", "Bílá Velryba","X","Y"])

print(knihy[0])

#vymazání klíče "characters"
for x in knihy:
    x.pop("characters",None)

#Vypsání titulu a autora z celého pole
for x in knihy:
    #print(x['title'], x['author'])
    print(f" titul je {x['title']}, autor je {x['author']}")
    
    
knihy[0]["characters"]=(["Capt. Achab", "Bílá Velryba","X","Y"])
print(knihy[0]["characters"][1])    


favoriteBook=[knihy[0],knihy[2]] #vytvoření nového pole s knihami na pozici 0 a 2
print(favoriteBook)
print(knihy)
print(favoriteBook[0]["year"])
print(favoriteBook[1]["year"])

print(abs(favoriteBook[1]["year"]-favoriteBook[0]["year"])) #počet let mezi jednotlivými vydáními


"""
další live training
"""
bestSellingAlbums = [
    {
        "artist": "Michael Jackson",
        "title": "Thriller",
        "year": 1982,
        "genres": ["pop", "post-disco", "funk", "rock"],
        "sale": 70000000,
    },
    {
        "artist": "AC/DC",
        "title": "Back in Black",
        "year": 1980,
        "genres": ["hard rock"],
        "sale": 50000000,
    },
    {
        "artist": "Whitney Houston",
        "title": "The Bodyguard",
        "year": 1992,
        "genres": ["r&b", "soul", "pop", "soundtrack"],
        "sale": 45000000,
    },
    {
        "artist": "Pink Floyd",
        "title": "The Dark Side of the Moon",
        "year": 1973,
        "genres": ["progressive rock"],
        "sale": 45000000,
    },
    {
        "artist": "Eagles",
        "title": "Their Greatest Hits (1971 - 1975)",
        "year": 1976,
        "genres": ["country rock", "soft rock", "folk rock"],
        "sale": 44000000,
    },
    {
        "artist": "Eagles",
        "title": "Hotel California",
        "year": 1976,
        "genres": ["soft rock"],
        "sale": 42000000,
    },
    {
        "artist": "Shania Twain",
        "title": "Come On Over",
        "year": 1997,
        "genres": ["country", "pop"],
        "sale": 40000000,
    },
    {
        "artist": "Fleetwood Mac",
        "title": "Rumours",
        "year": 1977,
        "genres": ["soft rock"],
        "sale": 40000000,
    },
]

#vytvoření průměrného prodeje 
aktualnirok=2024
for x in bestSellingAlbums:
    x["average_sale"]=x["sale"]/(aktualnirok-x["year"])
print(bestSellingAlbums[0])

#spočítání průměrného roku vydání
currentyear=([])
for x in bestSellingAlbums:
    currentyear.append(x["year"])
suma=0
pocet=0
for x in currentyear:
    suma+=x
    pocet+=1
prumernyRok=suma/pocet

for x in bestSellingAlbums:
    x["average_age"]=prumernyRok
print(bestSellingAlbums[0])


#zjištění nejstaršího a nejmladšího roku vydání alba
newest=-1
oldest=9999
for x in bestSellingAlbums:
    if x["year"]>newest:
        newest=x["year"]
    if x["year"]<oldest:
        oldest=x["year"]
print(newest, oldest)


# suma prodejů Eagles
suma_Prodeju_Eagles=0
for x in bestSellingAlbums:
    if x["artist"]=="Eagles":
        suma_Prodeju_Eagles+=x["sale"]
    
for x in bestSellingAlbums:
    if x["artist"]=="Eagles":     
        x["albums_eagles"]=suma_Prodeju_Eagles
    else:
        x["albums_eagles"]=0
print(bestSellingAlbums)



#přidání nového záznamu do našeho pole    
new_album = {
    "artist": "Adele",
    "title": "21",
    "year": 2011,
    "genres": ["pop", "soul", "r&b"],
    "sale": 31000000,
}

bestSellingAlbums.append(new_album)
print(bestSellingAlbums[-1])


#vytvoření klíče "i_like_it" - pokud obsahuje soft rock, pak se mi to líbí   
for x in bestSellingAlbums:
    if  "soft rock" in x["genres"]:
        x["i_like_it"]=True
    else:
        x["i_like_it"]=False

print(bestSellingAlbums)
    
    
