#Dynamiczne przypisywanie metody do klasy lub instancji może się przydać wtedy,
# gdy na etapie pisania programu nie jest jeszcze na 100% pewne, jak ma działać pewna metoda tej klasy.
# Może być np. tak, że dane z klasy będzie trzeba eksportować zależnie od parameterów określonych
# przez użytkownika do pliku CSV, XLS, HTML itp. W kodzie aplikacji możesz mieć zdefiniowane odpowiednie
# funkcje, które realizują to zadanie, ale ponieważ nie wiadomo, jak użytkownik zechce eksportować dane,
# to żadna z tych funkcji oryginalnie nie będzie przypisana do klasy/instancji. Dopiero kiedy program się
# uruchomi, przeczyta swoje opcje, zadecyduje się o tym, która z funkcji ma pracować jako ta
# właściwa funkcja eksportująca dane zgodnie z życzeniem użytkownika.
# Tutaj (żeby zbytnio nie rozbudowywać przykładu) będziemy pracować z funkcją zapisującą
# dane w postaci HTML, ale jak masz ochotę, przygotuj również drugą, zapisującą dane
# np. w pliku CSV, a potem zależnie od potrzeby przypisuj do metod klasy/instancji jedną lub drugą.

import csv
import types

import types


def export_1_cake_to_html(obj, path):
	template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

	with open(path, "w") as f:
		content = template.format(obj.name, obj.kind, obj.taste, obj.additives, obj.filling)
		f.write(content)


def export_all_cakes_to_html(cls, path):
	template_header = """
<table border=1>"""
	template_data = """
     <tr>
       <th colspan=2>{}</th>
     </tr>
     <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>"""
	template_footer = """</indent>
</table>"""
	with open(path, "w") as f:
		f.write(template_header)
		for c in cls.bakery_offer:
			content = template_data.format(c.name, c.kind, c.taste, c.additives, c.filling)
			f.write(content)
		f.write(template_footer)


def export_this_cake_to_html(self, path):
	template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

	with open(path, "w") as f:
		content = template.format(self.name, self.kind, self.taste, self.additives, self.filling)
		f.write(content)


class Cake:
	known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
	bakery_offer = []

	def __init__(self, name, kind, taste, additives, filling, gluten_free, text):

		self.name = name
		if kind in self.known_kinds:
			self.kind = kind
		else:
			self.kind = 'other'
		self.taste = taste
		self.additives = additives.copy()
		self.filling = filling
		self.bakery_offer.append(self)
		self.__gluten_free = gluten_free
		if kind == 'cake' or text == '':
			self.__text = text
		else:
			self.__text = ''
			print('>>>>>Text can be set only for cake ({})'.format(name))

	def show_info(self):
		print("{}".format(self.name.upper()))
		print("Kind:        {}".format(self.kind))
		print("Taste:       {}".format(self.taste))
		if len(self.additives) > 0:
			print("Additives:")
			for a in self.additives:
				print("\t\t{}".format(a))
		if len(self.filling) > 0:
			print("Filling:     {}".format(self.filling))
		print("Gluten free: {}".format(self.__gluten_free))
		if len(self.__text) > 0:
			print("Text:      {}".format(self.__text))
		print('-' * 20)

	def set_filling(self, filling):
		self.filling = filling

	def add_additives(self, additives):
		self.additives.extend(additives)

	def __get_text(self):
		return __text

	def __set_text(self, new_text):
		if self.kind == 'cake':
			self.__text = new_text
		else:
			print('>>>>>Text can be set only for cake ({})'.format(self.name))

	Text = property(__get_text, __set_text, None, 'Text on the cake')


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream', False, 'Happy Birthday Margaret!')
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '', False, '')
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '', True, '')
cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', False, 'Good luck!')

# static method:
Cake.export_1_cake_to_html = export_1_cake_to_html
Cake.export_1_cake_to_html(cake01, 'c:/temp/cake01.html')

# class method:
Cake.export_all_cakes_to_html = types.MethodType(export_all_cakes_to_html, Cake)
Cake.export_all_cakes_to_html('c:/temp/all_cakes.html')

# instance method:
for c in Cake.bakery_offer:
	c.export_this_cake_to_html = types.MethodType(export_this_cake_to_html, c)
for c in Cake.bakery_offer:
	c.export_this_cake_to_html('c:/temp/{}.html'.format(c.name.replace)