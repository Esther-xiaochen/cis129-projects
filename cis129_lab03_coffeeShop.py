# cis129_lab03_coffeeShop.py

#Coffee at $5 each: $ 5.00
#Muffins at $4 each: $ 8.00
#6% tax: $ .78

# Author: Xiaochen zhang

#this input many coffee and muffin 
print("***********************************")
print("My Coffee and Muffin Shop ")
print("how much coffee")

coffee = input ()

print("how many muffins do you want?")

muffins = input ()

print("***********************************")
print()
print()
print("***********************************")

#this caclculates the total cost of the coffee
totalcoffeecoat = int(coffee) * 5

totalmuffinscoat = int(muffins) * 4

totalcost = (totalcoffeecoat + totalmuffinscoat)

#this print the recpeit
print("My Coffee and Muffin Shop Receipt")
print (coffee + " coffer at $5 each:$" + str (totalcoffeecoat) + ".00" )
print (muffins + " muffins at $4 each:$" + str (totalmuffinscoat) + ".00")
print ("6% tax: $" + str (totalcost * .06))
print ("------------")
print("total: $" + str(totalcost + (totalcost * .06)))
print("***********************************")

