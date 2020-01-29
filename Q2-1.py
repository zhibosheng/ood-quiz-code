
class City():
    def __init__(self,name):
        self.name = name

class Distance():
	def __init__(self):
		self.distancedict = {}
	
	def addDistance(self,city1,city2,distance):
		if (city1.name,city2.name) not in self.distancedict and (city2.name,city1.name) not in self.distancedict:
			self.distancedict[(city1.name,city2.name)] = distance

	def getDistance(self,city1,city2):
		if (city1.name,city2.name) in self.distancedict:
			return self.distancedict[(city1.name,city2.name)]
		elif (city2.name,city1.name) in self.distancedict:
			return self.distancedict[(city2.name,city1.name)]
		else:
			return str(-1)
#init city
paris = City("Paris")
berlin = City("Berlin")
vienna = City("Vienna")
london = City("London")

#init distance and add distances
distance = Distance()
distance.addDistance(paris,berlin,"1000km")
distance.addDistance(paris,vienna,"1200km")
distance.addDistance(berlin,vienna,"681km")

#result
print("The distance from Paris to Berlin is " + distance.getDistance(paris,berlin))
print("The distance from Paris to Vienna is " + distance.getDistance(paris,vienna))
print("The distance from Berlin to Vienna is " + distance.getDistance(berlin,vienna))
print("The distance from Berlin to Paris is " + distance.getDistance(berlin,paris))
print("The distance from Berlin to London is " + distance.getDistance(berlin,london))