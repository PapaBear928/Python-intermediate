import random
#Zaimportuj moduł random

'''Zdefiniuj generator random_with_sum, który:

Przyjmuje argumenty:

number_of_values - ilość wartości do wylosowania (u nas 3)

asserted_sum - założona suma, do której mają się zsumować wylosowane liczby

Zainicjuj zmienne:

trial - na zero - będzie to licznik prób losowania wartości nim uda się wylosować liczby sumujace się do asserted_sum (u nas 100)

numbers - tablica licząca number_of_values wartości (u nas 3)'''


def random_with_sum(number_of_values,asserted_sum):
	trial = 0
	numbers = list(range(number_of_values))
'''W nieskończonej pętli while

zwiększ trial o 1

dla liczby i od 0 do number_of_values wylosuj liczby z zakresu 1-100 i zapisz je w tablicy numbers'''
	while True:
		trial += 1
		for i in range(number_of_values):
			numbers[i] = random.randint(1,101)
'''jeżeli wylosowane liczby sumują się do asserted_sum, to

zwróć tuple (trial, numbers) - skorzystaj z funkcji yield

wyzeruj zmienną trial'''
		if sum(numbers) == asserted_sum:
			yield ((trial,numbers))
			trial = 0

'''W swoim programie:

w pętli for wykonywanej 10 razy

zapisz do tuple (number_of_trials, numbers) kolejną wartość generowaną przez random_with_sum(3, 100)

wyświetl tą wartość'''
for i in range(10):
	(number_of_trials, numbers) = next(random_with_sum(3, 100))
	print(number_of_trials, numbers)