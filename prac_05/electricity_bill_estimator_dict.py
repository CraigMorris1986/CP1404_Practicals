TARIFFS = {11: 0.244618, 31: 0.136928, 41: 0.14785, 9: 0.300214, 16: 0.200123}


def main():
    print("Electricity bill estimator 2.0")
    kwh_cost = float(input("Please enter the cost of electricity per kWh : "))
    kwh_daily_use = float(input("Please enter the daily amount of kWh used : "))
    billing_days = int(input("Please enter the total numbers of billed days : "))
    estimated_bill = kwh_cost * kwh_daily_use * billing_days
    print("Your estimated bill is ${:.2f}".format(estimated_bill))


def electricity_tariff():
    print("Electricity bill estimator 2.0")
    # using valid_choice as a boolean loop exit condition.
    valid_choice = False
    while not valid_choice:
        display_tariffs()
        try:
            tariff_used = int(input(">>>"))
            if tariff_used in TARIFFS:
                tariff_used = TARIFFS[tariff_used]
                valid_choice = True
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input, please use a number")
    kwh_daily_use = float(input("Please enter the daily amount of kWh used : "))
    billing_days = int(input("Please enter the total numbers of billed days : "))
    estimated_bill = tariff_used * kwh_daily_use * billing_days
    print("Your estimated bill is ${:.2f}".format(estimated_bill))


def display_tariffs():
    print("Select a electricity tariff:")
    for tariff in TARIFFS:
        print("tariff {}".format(tariff))


electricity_tariff()