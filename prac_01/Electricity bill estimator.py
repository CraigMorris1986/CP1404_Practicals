# This is an electricity bill calculator which multiplies kWh price to daily use in kWh
# over a period of time.
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928


def main():
    print("Electricity bill estimator")
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
        tariff_used = int(input("Which tariff is in effect, tariff 11 or tariff 31? 11 / 31 : "))
        if tariff_used == int(11):
            tariff_used = TARIFF_11
            valid_choice = True
        elif tariff_used == int(31):
            tariff_used = TARIFF_31
            valid_choice = True
        else:
            print("Invalid choice.")
    kwh_daily_use = float(input("Please enter the daily amount of kWh used : "))
    billing_days = int(input("Please enter the total numbers of billed days : "))
    estimated_bill = tariff_used * kwh_daily_use * billing_days
    print("Your estimated bill is ${:.2f}".format(estimated_bill))


electricity_tariff()
