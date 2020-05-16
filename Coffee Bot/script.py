from utils import print_message, get_size, order_latte

# Coffee bot main function
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

# Get drink type sub-function
def get_drink_type():
	res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')

	if res == 'a':
		return 'brewed coffee'
	elif res == 'b':
		return order_mocha()
	elif res == 'c':
		return order_latte()
	else:
		print_message()
		return get_drink_type()

# Define Handle Mocha orders
def order_mocha():
	while True:
		res = input('Would you like to try our limited-edition peppermint mocha? \n[a] Sure!\n[b] Maybe next time!\n>')
		if res == 'a':
			return 'peppermint mocha'
		elif res == 'b':
			return 'mocha'
		else:
			return res
		print_message()


#initialize Bot
coffee_bot()