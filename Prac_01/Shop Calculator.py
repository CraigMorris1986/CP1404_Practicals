# Shops calculator program to add values together to generate a currency output
# of totals.

def main():
    number_of_items = int(input("Please enter total number of items: "))
    item_total_cost = 0
    while number_of_items <= 0:
        print("Invaild amount of items.")
        number_of_items = int(input("Please enter total number of items: "))
    for i in range(number_of_items):
        item_total_cost += float(input("Price of item in AUD (Dollars): "))
        while item_total_cost < 0:
            print("Invalid price of item.")
            item_total_cost += float(input("Price of item in AUD (Dollars): "))
    print(item_total_cost)


main()


# while number_of_items != int():
#     print("Invalid input, please enter a numeric number of items.")
#     number_of_items = int(input("Please enter total number of items: "))