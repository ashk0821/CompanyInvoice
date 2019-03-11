names = []
counts = []
prices = []
totals = []
grand = 0

print("This program will help to calculate the customer's invoice.\n")

x = input("Please enter the name of the first item.")
names.append(x)

# This while loop keeps the program looping until the user presses enter
while x != "":
    c = int(input("How many were purchased?"))
    counts.append(c)

    p = float(input("What was the price of each item purchased?"))
    prices.append(p)

    totals.append(p * c)

    x = input("Name of the next item purchased. Press enter when done.")
    if x != "":
        names.append(x)

# Prints the heading of the table of values.
print("\n%-20s %-15s %-15s %-15s\n" % ("Item","Count","Item Price","Item Total"))

# Prints all the names, counts, prices, and totals for all items and adds the totals to the grand total
for n in range (len(names)):
    print("%-20s %-15d %-15.2f %-15.2f" % (names[n-1], counts[n-1], prices[n-1], totals[n-1]))
    grand += totals[n-1]

# Prints the grand total
print("\nGrand total: %-.2f" % grand)


