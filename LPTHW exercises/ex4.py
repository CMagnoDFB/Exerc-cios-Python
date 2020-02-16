#Essa variável representa o numero de carros.
cars = 100
#Essa variável representa quantas pessoas cabem num carro.
space_in_a_car = 4
#Number of drivers
drivers = 30
#Number of passengers
passengers = 90
#Number of cars not driven
cars_not_driven = cars - drivers
#Number of cars driven
cars_driven = drivers
#This calculates the carpool capacity
carpool_capacity=cars_driven * space_in_a_car
#This calculates how many passengers per car are there in average
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.") 
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
