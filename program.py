wiek = input("Podaj wiek użytkownika jako liczbę całkowitą:")
# Sprawdzamy czy podany wiek jest liczbą
if wiek.isdigit() == False:
    exit("Wiek musi być liczbą albo podana liczba nie jest całkowitąa")
wiek = int(wiek)
if wiek>=18 and wiek<=40:
    print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
elif wiek>40:
    print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
    print("Uważaj w Twoim wieku nie przasadzaj ze spożyciem")
else:
  exit("Jesteś za młoda/y na alkohol. Zapraszamy na disney.com")

plec = str()
plec = input("podaj płeć ")

if plec == "K" and wiek>30:
    print("Hej, odbierz swój pierwszy aperol spritz za darmo")
else:
	exit()

