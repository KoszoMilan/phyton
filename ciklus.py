#2-100   primszamok
"""
for  x in range (101,1,-2):
    print(x)
"""

for x in range(2,101):
    for oszto in range(2, x//2+1):#4 nem lesz prim
        if (x % oszto) ==0:
            break
    else:
        print('A', x, 'prim szám' )









