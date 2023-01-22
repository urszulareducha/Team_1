#Program dla dorosłych do alkoholu
wiek = input("Podaj wiek użytkownika jako liczbe calkowitą:")
# Sprawdzamy czy podany wiek jest liczbą
if wiek.isdigit() == False:
	exit("Wiek musi być liczbą albo podana liczba nie jest calkowita")
wiek=int(wiek)
if wiek>=18 and wiek<=40:
	print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
elif wiek>40:
	print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
	print("Uważaj w Twoim wieku nie przasadzaj ze spożyciem")
else:
  exit("Jesteś za młoda/y na alkohol. Zapraszamy na disney.com")

region=input("Skad pochodzisz (Europa/USA):")

region=str(region)
if region=="Europa":
    print("Cześć! Hola! Ciao!")
elif region=="USA":
    print("Hello!")
else:
    print("Wybierz region")
    region=input("Skad pochodzisz (Europa/USA):")

plec = input("Jesteś kobietą czy mężczyzną? Wpisz K / M")
if plec == "K":
    print("Witaj")
elif plec == "M":
    print("Witaj")
else:
    print("Nie rozpoznałem płci. Podaj proszę czy jesteś K czy M?")
plec = str()
plec = input("podaj płeć ")

if plec == "K" and wiek>30:
    print("Hej, odbierz swój pierwszy aperol spritz za darmo")
else:
	exit()

