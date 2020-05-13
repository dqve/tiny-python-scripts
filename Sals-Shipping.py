# This is a program that will take the weight of a package and
# determine the cheapest way to ship that package using Sal’s Shippers.
#
## Ground Shipping:
#
#Weight of Package	                     |Price per Pound |	Flat Charge
#2 lb or less	                           |  $1.50	        |   $20.00
#Over 2 lb but less than or equal to 6 lb	|  $3.00	        |   $20.00
#Over 6 lb but less than or equal to 10 lb|  $4.00         |   $20.00
#Over 10 lb	                              |  $4.75	        |   $20.00
#
## Drone Shipping:
#
#Weight of Package	                     |Price per Pound |	Flat Charge
#2 lb or less	                           |  $4.50	        |   $0.00
#Over 2 lb but less than or equal to 6 lb	|  $9.00	        |   $0.00
#Over 6 lb but less than or equal to 10 lb|  $12.00        |   $0.00
#Over 10 lb	                              |  $14.25	     |   $0.00
#
##Premium Ground Shipping
#
#Flat charge: $125.00
#
#The program below asks the user for the weight of their package and then tells them which method of shipping is 
#cheapest and how much it will cost to ship their package using Sal’s Shippers.
##



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

def sals_shipper(weight):
  ground = ground_shipping_cost(weight)
  drone = drone_shipping_cost(weight)

  if ground < drone and ground < premium_ground_shipping:
    print("The ground shipping method is the cheapest method at "+str(ground)+"$")
  elif ground > drone and ground < premium_ground_shipping:
      print("The drone shipping method is the cheapest method at "+str(drone)+"$")
  else:
    print("The cheapest way to ship a 41.5 pound package is using premium ground shipping and it will cost $"+str(premium_ground_shipping))

sals_shipper(41.5)
#test
