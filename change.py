# Python code example
# https://exercism.org/tracks/python/exercises/change

# Philip Woite

# Define and request input

# Gather input from the user
# https://stackoverflow.com/questions/7845165/how-to-take-input-in-an-array-python
print("Enter change amount in cents")
change = int(input())
print("Enter the types of coins in your coin tray - separate denominations with spaces")
coins = input() # This will take the whole line of coin types
coin_tray = list(map(int,coins.split(' '))) # Numbers split with spaces will be separated
print(" ")
print("Coin tray ",coin_tray)

# reverse the coin_tray list - i.e. into descending order
# an alternative would be to use the reversed() funcion

# https://www.askpython.com/python/array/reverse-an-array-in-python
coin_tray.reverse()
print("Descending coin tray: ",coin_tray)

# initialise the dispensed list so that it may be appended in the for loop
dispensed = [] 
print("Dispensed ",dispensed)

# https://www.tutorialspoint.com/iterate-over-a-list-in-python
# # https://datagy.io/append-to-lists-python/

for denomination in coin_tray:
    print("Change",change)
    print("Denomination ",denomination)
    coin_amount = change // int(denomination)
    print("Coin amount ",coin_amount)
    dispensed.append(coin_amount)
    print("Dispensed ",dispensed)
    change = change % int(denomination)
    print("Remaining change ",change)

# Reverse the dispensed and coin_tray lists into ascending order.
dispensed.reverse()
coin_tray.reverse()

# Present the solution
print("The coins should be dispensed as follows:")
print("Coin value ",coin_tray)
print("Number of ",dispensed)
