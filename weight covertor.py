#to convert k to pounds
weight=int(input('weight: '))
unit=input('(L)bs or (K)g: ')
if unit.upper()=='L':
    converter=weight*0.45
    print(converter)
else:
    converted=weight//0.45


