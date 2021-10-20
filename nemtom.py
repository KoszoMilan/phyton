honap = ["január", "február", "március", "április", "május"]
for i in honap:
    print(i, end="")
print("tömb mérete:", len(honap))
for j in range(len(honap)):
    print("%d. honap: %s" % (j+1, honap[j]))

import random
print(random.choice(honap))


str1 = "isz"
hb = ""
hb = "h" + str1 + "ed"
hb = "h" + "isz" + "ed" 
print(hb)
print(hb[3])



str2 = "hiszed"
print(len(str2))
print(str2[1:4])


str2 = str2[1:]
print(str2)


str2 = str2[:3]+"o"+str2[4:]
print(str2)



