koszyk = ['jaja', 'mleko', 'czekolada']

print("Mam koszyk: ")
for s in koszyk:
    print(s)

del koszyk[1]

print("Koszyk bez mleka: ")
for s in koszyk:
    print(s)

koszyk.append('paluszki')

print("PAAAALUSZKI: ")
for s in koszyk:
    print(s)
