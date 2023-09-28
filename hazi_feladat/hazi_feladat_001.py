# hazi_feladat_001
"""
1.1 Feladat
Készíts egy programot, amely megkérdezi a felhasználótól, hogy jó napja van-e! A válasz kétféle lehet: igen vagy nem. 
A választól függően írjon ki üzenetet a gép!
"""
valasz = input(f'Jó a mai napod? (igen/nem) ')
if valasz == 'igen':
	print(f'Az szuper.')
elif valasz == 'nem':
	print(f'Az szomorú.')