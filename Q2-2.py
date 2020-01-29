class Person():
	def __init__(self,name):
		self.name = name
		self.mate = []
		self.child = []
		self.sibling = []
		self.cousin = []

	def setMate(self,person):
		self.mate.append(person.name)

	def getMate(self):
		return ",".join(self.mate)

	def setChild(self,person):
		self.child.append(person.name)

	def getChild(self):
		return ",".join(self.child)

	def setSibling(self,person):
		self.sibling.append(person.name)

	def getSibling(self):
		return ",".join(self.sibling)

	def setCousin(self,person):
		self.cousin.append(person.name)

	def getCousion(self):
		return ",".join(self.cousin)

#init Person
grandmother = Person("grandmother")
grandfather = Person("grandfather")
father      = Person("father")
mother      = Person("mother")
aunt        = Person("aunt")
cousin      = Person("cousin")
you         = Person("you")

#set association
grandfather.setMate(grandmother)
grandmother.setMate(grandfather)
grandfather.setChild(father)
grandmother.setChild(father)
father.setSibling(aunt)
aunt.setSibling(father)
father.setMate(mother)
mother.setMate(father)
aunt.setChild(cousin)
mother.setChild(you)
you.setCousin(cousin)
cousin.setCousin(you)

#result
print("grandfather's mate is " + grandfather.getMate())
print("grandmother's mate is " + grandmother.getMate())
print("grandfather's child is " + grandfather.getChild())
print("grandmother's child is " + grandmother.getChild())
print("father's mate is " + father.getMate())
print("mother's mate is " + mother.getMate())
print("father's sibling is " + father.getSibling())
print("aunt's sibling is " + aunt.getSibling())
print("mother's child is " + mother.getChild())
print("aunt's child is " + aunt.getChild())
print("you's cousion is " + you.getCousion())
print("cousin's cousin is " + mother.getCousion())


