from rental import Vehicle, Renter, ElectricCar, Motorbike

car = Vehicle("Toyota", "Yaris", "1AB234")
electric = ElectricCar("Tesla", "Model 3", "2CD567", 75)
bike = Motorbike("Honda", "CBR", "3EF890", 500)

renter = Renter("John", 12345)

print(car)
print(electric)
print(bike)

car.rent()
print(car)

car.return_vehicle()
print(car)

try:
    bad_renter = Renter("", 12345)
except ValueError as e:
    print(e)

try:
    bad_renter = Renter("John", 0)
except ValueError as e:
    print(e)

vehicles = [car, electric, bike]

for vehicle in vehicles:
    print(vehicle)

renter.name = "Mike"
renter.license_no = 67890

print(renter.name)
print(renter.license_no)

try:
    renter.name = ""
except ValueError as e:
    print(e)

try:
    renter.license_no = -1
except ValueError as e:
    print(e)