weight = input("How much does your mailing weigh? ")

#Ground Shipping
if weight <= 2:
  print(weight * 1.5 + 20)
elif weight <= 6:
  print(weight * 3 + 20)
elif weight <= 10:
  print(weight * 4 + 20)
else:
  print (weight * 4.75 + 20)

#Ground Shipping Premium
ground_shipping_premium = 125
print(ground_shipping_premium)

#Drone Shipping
if weight <= 2:
  print(weight * 4.5)
elif weight <= 6:
  print(weight * 9)
elif weight <= 10:
  print(weight * 12)
else:
  print (weight * 14.25)
