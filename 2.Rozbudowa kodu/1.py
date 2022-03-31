##W tym zadaniu należy przerobić listy z poprzedniego LAB do postaci generatora.
# Nieco problematyczne będzie ustalenie ile wartości jest generowanych przez generator,
# bo w tym celu... trzeba go przejść!


##Na przekręcie z wpłatomatem z poprzedniego zadania postanawiasz wraz ze swoim szefem otworzyć
# linie lotnicze "Flying Python". Linie będą krajowe. Oto wykaz portów lotniczych:


ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

gen = ((start, stop) for start in ports for stop in ports if start != stop)

counter = 0
for (start, stop) in gen:
	print("{} - {}".format(start, stop))
	counter += 1

print(counter)