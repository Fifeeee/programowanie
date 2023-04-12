import math
import sys

liczba_a = float(input("Podaj pierwszą liczbę: "))
liczba_b = float(input("Podaj drugą liczbę: "))

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

promien = 0

while promien <= 0:
    promien = float(input("Podaj promień koła: "))
pole = math.pi * float(promien) ** 2
print("Pole koła: ", pole)
obwod = 2*math.pi * float(promien)
print("Obwód koła: ", obwod)

wiek = input("Podaj swój wiek: ")
imie = input("Podaj swoje imię: ")
print(imie + ", masz " + wiek + " lat.")