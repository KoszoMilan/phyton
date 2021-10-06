össz = 0

# walrus (=rozmár) operátor: értéket ad és vissza is tér vele
while össz <= 35 and (ivás:=int(input('Hány decit ittál? '))):
    print(f'Már {(össz:=össz+ivás)/10:3.1f} litert ittál.')
    if össz >= 25:
        print('Már sikerült elérned a 2,5 litert.')
print('Béka nől a hasadba\'!')