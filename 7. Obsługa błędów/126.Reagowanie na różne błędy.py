clients = {
	"Alfa": 0.5,
	"Beta": 0.2,
	"Gamma": 0.15,
	"Delta": 0.1,
	"Ypsilon": 0.05,
}
'''POCZĄTKOWE
myClient = input("Enter clients name")
totalcost = 19.90
try:
	print("The % ratio for {} is {}".format(myClient, clients[myClient]))
except Exception as e:
	print("Sorry we have an error... \n Details \n {}".format(e))
else:
	print("The cost for {} is {}".format(myClient, clients[myClient] * totalcost))
finally:
	print(" =- Calculation finished -=")'''


myClient = input("Enter clients name")
totalcost = 19.90
try:
	ratio = float(input("Enter new ratio"))
	print("The % ratio for {} is {}, a new one is {}".format(myClient, clients[myClient], ratio))
	print("The cost for {} is {}".format(myClient, ratio * totalcost))
	print("The new ratio in comparision to old ratio : {}".format(clients[myClient]/ratio))
except KeyError as e:
	print("Client {} is not on the customer list {} . \n Details \n {}".format(myClient, [c for c in clients.keys()], e))
except (ValueError,ZeroDivisionError ) as e:
	print("Its problem with your value. It must be a number. \n Details \n {}".format(e))
#except ZeroDivisionError as e:
	print("The new ratio cant be 0.\n Details \n {}".format(e))
except Exception as e:
	print("Sorry we have an error... \n Details \n {}".format(e))
'''else:
	print("The cost for {} is {}".format(myClient, clients[myClient] * totalcost))
finally:
	print(" =- Calculation finished -=")'''