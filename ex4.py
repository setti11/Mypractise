
#cars = 100
#space_in_a_car = 4.0
#drivers = 30
#passengers = 90
#cars_not_driven = cars - drivers
#cars_driven = drivers
#carpool_capacity = cars_driven * space_in_a_car
#average_passengers_per_car = passengers / cars_not_driven

#print ("There are", cars, "cars avaialble.")
#print ("There are only", drivers, "drivers avaialble.")
#print ("There will be", cars_not_driven, "empty cars today.")
#print ("We can transport", carpool_capacity, "people today.")
#print ("We have", passengers, "to carpool today.")
#print ("We need to put about", average_passengers_per_car, "in each car.")

cars = 10
space_in_a_car = 4.5
drivers = 3
passengers = 4
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_not_driven

print ("There are ", cars, "cars available")
print ("There are only", drivers, "drivers available")
print ("There will be", cars_not_driven, "empty cars today ")
print ("There are ", carpool_capacity, "seats avaialble for passengers")
print ("For each car we have ", space_in_a_car, "seats" )
