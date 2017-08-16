"""  Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%. """


# def main():
#     sales = float(input("Enter sales: $"))
#     if sales < 1000:
#         bonus = float(sales * 0.1)
#         print ("${:.2f}".format(bonus))
#     else:
#         bonus = float(sales * 0.15)
#         print ("${:.2f}".format(bonus))
#
#
# main()

def bonus_loop():
    sales = 0
    while sales >= 0:
        sales = float(input("Enter sales: $"))
        if sales < 1000 and sales > 0:
            bonus = float(sales * 0.1)
            print("${:.2f}".format(bonus))
        else:
            bonus = float(sales * 0.15)
            print("${:.2f}".format(bonus))
    print("Complete")


bonus_loop()
