samolot = {'name': 'boeing',
	   'przebieg': 10000,
	   'type': 'pasazerski'}

print(samolot['name'])
print("{0}".format(samolot['przebieg']))

for key in samolot:
    print(samolot[key])
#key to klucz do nazwy zmiennej samolotu, wartosci to value
#uzycie key w petli for nie nadaje wynikowi wyswietlenia kolejnosci, jest ona losowa

for key,value in samolot.iteritems():
    print("Key: {0} Value: {1}".format(key,value))

