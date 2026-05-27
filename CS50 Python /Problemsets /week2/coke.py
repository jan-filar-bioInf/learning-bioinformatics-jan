
#coke costs 50 cent
Amount_Due = 50

# Keep asking for coins while money is still owed
while Amount_Due > 0:
    print ("Amount Due: ",Amount_Due )
    # Ask user to insert a coin
    coin = int(input("Insert Coin: "))
    # Only accept valid coins: 25, 10, or 5 cents
    if coin in [5, 10, 25]:
        Amount_Due = Amount_Due - coin

#Once paid, print the change owed
print("Change Owed: ",-Amount_Due)










