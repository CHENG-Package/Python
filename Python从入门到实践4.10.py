

L=[L for L in range (1,16)]

print(L)

print('Thefirst threeitems in thelistare:')
for Lfront in L[:3]:
    print(Lfront)

print('')

print('Threeitems fromthe middle ofthelistare:')
for Lcenter in L[6:9]:
    print(Lcenter)

print('')

print('Thelast threeitems in thelistare:')

for Lfinally in L[12:]:
    print(Lfinally)
