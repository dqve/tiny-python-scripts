from utils import print_message, get_size, order_latte

def coffee_bot():
  print('Welcome to the cafe!')
  order_drink = 'y'
  drinks = []

	while order_drink == 'y':
		size = get_size()  
		drink_type = get_drink_type()

		drink = '{} {}'.format(size, drink_type)
		drinks.append(drink)
		print('Alright, that\'s a {}!'.format(drink))
		  
		for i in drinks:
		  print("Okay, so I have:\n -"+str(drink))

		while True:
		  order_drink = input("Would you like to order another drink? (y/n)\n>")
		  if order_drink in ['y', 'n']:
		    break

	name = input('Can I get your name please? \n> ')
  print('Thanks, {}! Your order will be ready shortly.'.format(name))