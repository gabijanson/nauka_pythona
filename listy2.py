samochody = ['syrena', 'polonez']
ilosc = [3,5]

for idx in range( len(samochody) ):
    print("idx: " + str(idx) + " : " + samochody[idx])
    print(samochody[idx] + " ma ilosc drzwi " + str(ilosc[idx]))

samochody.append('audi')
samochody.append('mercedes')

for s in samochody:
   print(s)


samochody[2] = 'kia'
del samochody[0]

for s in samochody:
    print(s)

for idx in range( len(samochody) ):
    if idx == 1:
        print("skipping 1!")
    else:
        print( "{0} : {1}".format([idx],samochody[idx]))


for idx in range( len(samochody) ):
    if samochody[idx]!='kia':
        print("{0} : {1}".format([idx],samochody[idx]))
