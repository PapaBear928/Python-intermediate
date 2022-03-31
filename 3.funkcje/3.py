#W tym zadaniu zbudujesz proces służący do budowy łańcucha transformacji danych liczbowych.
#2. Zdefiniuj liczbę number o wartości 8
#3. Zdefiniuj listę transformations składającą sie z funkcji:
# double  square  div2   negative
#4. Do tymczasowej zmiennej tmp_return_value wpisz wartość number
#5. Napisz pętlę, która:
	#przejdzie przez wszystkie pozycje listy transformations

	#za każdym razem wywoła odpowiednią funkcję, przekazując do niej aktualną
		# wartość argumentu tmp_return_value

	#wyświetli aktualną wartość zmiennej tmp_return_value

#6. Przetestuj działanie skryptu również dla listy transformacji z operacjami:
#square  square  div2    double
def double(x):
	return 2 * x

def square(x):
	return x ** 2

def negative(x):
	return -x

def div2(x):
	return x / 2

number = 8
transformations = [double, square, div2, negative]

temp_return_value = number
#5
for i in transformations:```
	temp_return_value = i(temp_return_value)
	print(temp_return_value)