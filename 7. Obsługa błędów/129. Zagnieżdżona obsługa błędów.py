netto = 1230
brutto = 1000


def Process(netto,brutto):
	if netto > brutto:
		raise Exception("Netto shoud be lower than brutto")
	else:
		print("Processing invoice: netto = {} , brutto = {} ".format(netto,brutto))

Process(1222,11111)


try:
	Process(netto,brutto)
except ValueError as e:
	print("Values are incorrect: {}".format(e))
except Exception as e:
	print("Error processing invoice".format(e))