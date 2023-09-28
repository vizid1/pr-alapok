sebesseg = int(input())
if 0 < sebesseg <= 50:
    print('megengedett sebesség')
elif 50 < sebesseg <= 65:
    print('büntetés: 15.000Ft')
elif 65 < sebesseg <= 80:
    print('büntetés: 30.000Ft')
elif 80 < sebesseg <= 100:
    print('büntetés: 60.000Ft')
elif 100 < sebesseg:
    print('')
else:
    print('A megadott érték nem sebesség')