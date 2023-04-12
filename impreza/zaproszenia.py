with open("C:\\Users\\Filip\\Desktop\\programowanie\\impreza\\zaproszenia.txt") as plik:
    zawartosc = plik.read()
with open("C:\\Users\\Filip\\Desktop\\programowanie\\impreza\\zaproszenia2.txt") as plik2:
    zawartosc2 = plik2.read()
with open("C:\\Users\\Filip\\Desktop\\programowanie\\impreza\\bany.txt") as plik3:
    zawartosc3 = plik3.read()

zaproszeni1 = set(zawartosc.split() + zawartosc2.split ())
zaproszeni2 = set(zawartosc3.split())
zaproszeni3 = zaproszeni1 - zaproszeni2
print (zaproszeni3)

#print(zaproszeni1)
#print(zaproszeni2)
#print(zaproszeni3)

with open("C:\\Users\\Filip\\Desktop\\programowanie\\impreza\\zaproszenia_posortowane.txt", "w") as plik4:
    plik4.write('\n'.join(sorted(zaproszeni3)))