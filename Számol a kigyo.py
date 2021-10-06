import math, cmath

a= input('Kérem a másodfoku egyenlet feőeggyütthatojat:')
a= float(a)
while a==0:
    print('Ez nem lesz masodfoku egyenlet; ezt nem oldom meg ')
    a= input('Kérem a másodfoku egyenlet feőeggyütthatojat: ')
    a = float(a)

b = input('kérem az elsőfoku tag együtthatojat:')
c= input('kérem a konstans tagt:')
b= float(b)
c= float(c)

d= b*b-4*a*c
print('A diszkirmináns értéke')

if d>=0:
    print('Van valos megoldas')
    x1 = (-b-math.sqrt(d))/(2*a)
    x2 = (-b+math.sqrt(d))/(2*a)
    print('Az egyik megoldas', x1)
    print('a masik megoldas', x2)

else d>=0:
    x1 = (-b-math.sqrt(d))/(2*a)
    x2 = (-b+math.sqrt(d))/(2*a)
    print('nincs valos megoldas', x1)
    print('nincs valos megoldas', x2)


