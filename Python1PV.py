import random
print("Arvaa luku peli, sinulla on kolme arvaus kertaa ! ")
#Alustetaan tarvittavat muuttujat
#Uusikomment
#Uusikomment
#Alustetaan tarvittavat muuttujat
#toimiiko gpg#Alustetaan tarvittavat muuttujat
#Uusikomment
#Uusikomment
#Alustetaan tarvittavat muuttujat
#toimiiko gpg

randomi = random.randint(1, 20)
laskuri = 3
while True:
    vastaus = (input("Arvaa luku: "))
    try:
        vastaus = int(vastaus)
    except ValueError:
        print(vastaus , "ei ole kokonaisluku, Anna luku 1 ja 20 väliltä!")
        continue
    if randomi == vastaus:
        print("oikein")
        break
    else:

        print("Arvasit väärin")
        laskuri -= 1
        if laskuri > 0:
            print(f'Arvauksia jäljellä {laskuri}')
        else:
            print(f'Oikea vastaus olisi ollut {randomi} ..')
            break

