##1- Nufusu 100 milyonun uzerinde olan ulkeler hangileridir?
##
##2- Isminin sonunda “land” kelimesi gecen ulkeler hangileridir?
##
##3- 500 bin ile 1 milyon arasinda nufusu olan sehirler hangileridir?
##
##4- Avrupa (“Europe”) kitasinda bulunan ulkelerin tamamini bulunuz.
##
##5- Tum ulkeleri yuzolcumleri buyukten kucuge olacak sekilde siralayaniz.
##
##6- Hollanda’nin (Netherlands) tum sehirlerini bulunuz.
##
##7- Amsterdam’in nufusu kactir?
##
##8- Avrupa’nin (Europe) en kalabalik sehri hangisidir?
##
##9- Afrika kitasinin (Africa) yuzolcumu en buyuk ulkesi hangisidir?
##
##10- Asya (Asia) kitasinda yuzolcumune gore en buyuk 10 ulke hangileridir?
##
##11- Yuzolcumu en kucuk olan ulkeyi bulunuz.
##
##12- En kalabalik 10 sehri bulunuz.
##
##13- Dunyanin nufusunu hesaplayiniz.


import sqlite3 as sql

vt = sql.connect('world.db')

im = vt.cursor()

##1- Nufusu 100 milyonun uzerinde olan ulkeler hangileridir?

im.execute("""SELECT Name
              FROM country
              WHERE population > 100000000 ;""")
print(im.fetchall())


##2- Isminin sonunda “land” kelimesi gecen ulkeler hangileridir?

im.execute("""SELECT name
            FROM country
            WHERE name LIKE '%land%' ;""")
print(im.fetchall())


##3- 500 bin ile 1 milyon arasinda nufusu olan sehirler hangileridir?

im.execute("""SELECT Name, Population
            FROM city
            WHERE Population  BETWEEN 500000  AND 1000000;""")

print(im.fetchall())






##4- Avrupa (“Europe”) kitasinda bulunan ulkelerin tamamini bulunuz.

im.execute("""SELECT Name
            FROM country
            WHERE continent = 'Europe'
           AND population; """)
print(im.fetchall())



##5- Tum ulkeleri yuzolcumleri buyukten kucuge olacak sekilde siralayaniz.

im.execute("""SELECT Name
            FROM country ORDER BY SurfaceArea DESC;""")
             
print(im.fetchall())




##6- Hollanda’nin (Netherlands) tum sehirlerini bulunuz.

im.execute("""SELECT Name
            FROM city
            WHERE CountryCode = 'NLD'; """)
print(im.fetchall())


##7- Amsterdam’in nufusu kactir?

im.execute("""SELECT Name,Population
            FROM city
            WHERE Name = 'Amsterdam'; """)
print(im.fetchall())



##8- Avrupa’nin (Europe) en kalabalik sehri hangisidir?

im.execute("""SELECT city.Name, MAX(city.population)
           FROM city INNER JOIN country ON city.CountryCode=country.Code
           WHERE country.continent='Europe';""")
print(im.fetchall())


##9- Afrika kitasinin (Africa) yuzolcumu en buyuk ulkesi hangisidir?


im.execute("""SELECT Name, MAX(SurfaceArea)
           FROM country
           WHERE continent='Africa';""")
print(im.fetchall())



##10- Asya (Asia) kitasinda yuzolcumune gore en buyuk 10 ulke hangileridir?

im.execute("""SELECT Name
           FROM country
           WHERE continent='Asia' ORDER BY SurfaceArea DESC LIMIT 10;""")
print(im.fetchall())





##11- Yuzolcumu en kucuk olan ulkeyi bulunuz.

im.execute("""SELECT Name, MIN(SurfaceArea)
           FROM country; """)
print(im.fetchall())



##12- En kalabalik 10 sehri bulunuz.

im.execute("""SELECT Name
           FROM city ORDER BY population DESC LIMIT 10;""")
print(im.fetchall())


##13- Dunyanin nufusunu hesaplayiniz.


im.execute("""SELECT SUM(population )
           FROM  country; """)
print(im.fetchall())
