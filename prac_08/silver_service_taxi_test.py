from prac_08.sivler_service_taxi import SilverServiceTaxi

fancy_car = SilverServiceTaxi("Silver Service", 100, 2)
print(fancy_car)
print(fancy_car.price_per_km)
fancy_car.start_fare()
fancy_car.drive(18)
print(fancy_car)
print("${:.2f}".format(fancy_car.get_fare()))
