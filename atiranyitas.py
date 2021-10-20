import sys
oldout = sys.stdout
print("Képernyőre ir")
wr = open("test.txt", "w")
sys.stdout = wr
print("fájlba ir")
wr.close()
sys.stdout = oldout
print("Képernyőre ir ismét")