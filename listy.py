samochody = ['syrena', 'polonez']

print (samochody[0])
print (samochody[1])
print (samochody[-1])
print (len(samochody))

for s in samochody:
    print (s)

for idx in range( len(samochody) ) :
    print("indx: " + str(idx) + "  : " + samochody[idx])

kwiaty = ['roza', 'bratek', 'lilia', 'slonecznik']

for s in kwiaty:
    print (s)

print("Lista najpiekniejszych kwiatow:")
for idx in range( len(kwiaty) ):
    print("Miejsce " + str(idx + 1) + " to " + kwiaty[idx])


