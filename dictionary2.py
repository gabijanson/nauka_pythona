mleko =  {'nazwa': 'mleko',
	  'cena': 10}
czekolada = {'nazwa': 'czekolada',
	     'cena': 5}
maka = {'nazwa': 'maka',
	'cena': 3}
cukier = {'nazwa': 'cukier',
	  'cena': 2}

koszyk =[]
koszyk.append(mleko)
koszyk.append(czekolada)
koszyk.append(maka)
koszyk.append(cukier)

suma = 0
for prod in koszyk:
    print(prod)
    suma = suma + prod['cena']
print("Wartosc koszyka: " +  str(suma))






#wartosc_koszyka = 0

#for idx in range( len(koszyk) ) :
#    for key in koszyk[idx]:
#        wartosc_koszyka + 





#dodac do koszyka
#wysiwetlic nazwy prod w koszyku
#podsumowac wartosc koszyka

