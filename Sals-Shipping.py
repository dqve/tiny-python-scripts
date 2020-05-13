def ground_shipping_cost(weight):
   if weight <= 2:
     cost = 1.5 * weight + 20   
    # some calculation
   elif weight <= 6 and weight > 2:
      cost = 3 * weight + 20
    # more calculation
   elif weight <= 10 and weight > 6:
    cost = 4 * weight + 20
    # more calculation
   elif weight > 10:
    cost = 4.75 * weight + 20
    # more calculation
   return cost
    # last calculation

print(ground_shipping_cost(8.4))

premium_ground_shipping = 125

def drone_shipping_cost(weight):
   if weight <= 2:
     cost = 4.5 * weight
    # some calculation
   elif weight <= 6 and weight > 2:
      cost = 9 * weight
    # more calculation
   elif weight <= 10 and weight > 6:
    cost = 12 * weight
    # more calculation
   elif weight > 10:
    cost = 14.25 * weight
    # more calculation
   return cost
    # last calculation

print(drone_shipping_cost(1.5))

def cheap_shipping(weight):
  ground = ground_shipping_cost(weight)
  drone = drone_shipping_cost(weight)

  if ground < drone and ground < premium_ground_shipping:
    print("The ground shipping method is the cheapest method at "+str(ground)+"$")
  elif ground > drone and ground < premium_ground_shipping:
      print("The drone shipping method is the cheapest method at "+str(drone)+"$")
  else:
    print("The cheapest way to ship a 41.5 pound package is using premium ground shipping and it will cost $"+str(premium_ground_shipping))

cheap_shipping(41.5)