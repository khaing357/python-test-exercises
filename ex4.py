cars=100
space_in_a_car=4.0
drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_drivern=drivers
carpool_capacity=cars_drivern * space_in_a_car
average_passengers_per_car=passengers/cars_drivern
print "There are",cars,"cars available."
print "There are only",drivers,"drivers availabele."
print "There will be ",cars_not_driven,"empty cars today."
print "we can transport",carpool_capacity,"people today."
print "We have",passengers,"to carpool today."
print "We need to put about", average_passengers_per_car,"in each car."
