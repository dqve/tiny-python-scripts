##
#This is a program that implements a Python chatbot's conversational flow
#This program aims at improving the wait time of a normal coffee preparation
#run by taking customers’ orders in advance.
##

def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  drink_type = get_drink_type()
  print('Alright, that\'s a {} {}!'.format(size, drink_type))
  print("Thanks, {name}! Your drink will be ready shortly.")

def print_message():
  print("""I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.""")

def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == 'a':
    res_size = 'small'
  elif res == 'b':
    res_size = 'medium'
  elif res == 'c':
    res_size = 'large'
  else:
    print_message()
    res_size = get_size()
    
  return res_size

def get_drink_type():
  drink = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')
  if drink == 'a':
    res_drink = 'brewed coffee'
  elif drink == 'b':
    res_drink = 'mocha'
  elif drink == 'c':
    res_drink = order_latte()
  else:
    print_message()
    res_drink = get_drink_type()
  return res_drink

def order_latte():
  milk = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ')
  if milk == 'a':
    res_milk = 'latte'
  elif milk == 'b':
    res_milk = 'non-fat latte'
  elif milk == 'c':
    res_milk = 'soy latte'
  else:
    print_message()
    res_milk = order_latte()
  return res_milk

coffee_bot()