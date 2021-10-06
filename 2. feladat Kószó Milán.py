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

d= a*b*4
print('A diszkirmináns értéke', d)

if d>=0:
    print('Van valos megoldas')
    x1 = (-b-math.sqrt(d))/(4*a)
    x2 = (-b+math.sqrt(d))/(4*a)
    print('Az egyik megoldas', x1)
    print('a masik megoldas', x2)

else:
      print('Van valos megoldas')
    x1 = (-b-math.sqrt(d))/(4*a)
    x2 = (-b+math.sqrt(d))/(4*a)
    print('Az egyik megoldas', x1)
    print('a masik megoldas', x2)


   
