import math

liczba_a = input("Podaj pierwszą liczbę: ")
liczba_b = input("Podaj drugą liczbę: ")

dodawanie = float(liczba_a) + float(liczba_b)
mnożenie = float(liczba_a) * float(liczba_b)
dzielenie = float(liczba_a) / float(liczba_b)
potega_a = float(liczba_a)** float(liczba_b)
potega_b = float(liczba_b)** float(liczba_a)
pierwiastek = math.sqrt(float(liczba_b)+float(liczba_a))

print("Wynik dodawania: ", dodawanie)
print("Wynik mnożenia: ", mnożenie)
print("Wynik dzielenia: ", dzielenie)
print("Wynik potęgi a^b: ", potega_a)
print("Wynik potęgi b^a: ", potega_b)
print("Wynik pierwiastkowania: ", pierwiastek)

promien = input("Podaj promień koła: ")
pole = math.pi * float(promien) ** 2

if float(promien) < 0:
    print("wpisz liczę dodatnią:")
else:
    pole = math.pi * float(promien) ** 2
    print("Pole koła: ", pole)
    obwod = 2*math.pi * float(promien)
    print("Obwód koła: ", obwod)

wiek = input("Podaj swój wiek: ")
imie = input("Podaj swoje imię: ")
print(imie + ", masz " + wiek + " lat.") #pokazuje ile lat ma gosc
