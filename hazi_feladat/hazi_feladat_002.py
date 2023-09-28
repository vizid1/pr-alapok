# hazi_feladat_002
"""
1.2 Feladat
Fejleszd tovább az első feladat programját úgy, hogy amennyiben a felhasználó nem a két lehetséges válasz (igen/nem) közül ad meg egyet,
a gép kiírja: "Sajnos nem értem a válaszodat!"
"""
valasz = input(f'Jó a mai napod? (igen/nem) ')
if valasz == 'igen':
	print(f'Az szuper.')
elif valasz == 'nem':
	print(f'Az szomorú.')
else:
	print(f'Sajnos nem értem a válaszodat!')