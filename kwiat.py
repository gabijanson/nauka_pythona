kwiat = "Roza"
ilosc_platkow = 23
kolor = "Czerwony"

print (kwiat + " ma " + str(ilosc_platkow) + " platki, a ich kolor to: " + kolor)
print ("Dwie roze maja: " + str( 2 * ilosc_platkow) + " platkow")
print (kwiat.upper())
print (kwiat.lower())
print (kwiat.swapcase())

print ("{0} ma {1} platkow, a ich kolor to {2}".format(kwiat, ilosc_platkow, kolor))
print ("Dwie roze maja {0} platkow".format(2 * ilosc_platkow))

kwiaty = ['roza', 'bratek', 'fiolek']
ilosci_platkow = [23, 34, 12]

for idx in range( len(kwiaty) ):
    print (kwiaty[idx] + " ma " + str(ilosci_platkow[idx]) + " platki/ow.")



