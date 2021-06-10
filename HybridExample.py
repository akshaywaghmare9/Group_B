

class Person:
  hasDNA = True


class Mother(Person): 
	def __init__(self, bloodGroup, genetic_Disease):
		self.bloodGroup = bloodGroup
		self.gender = 'Female'
		self.genetic_Disease = genetic_Disease


class Father(Person):
 	def __init__(self, bloodGroup, genetic_Disease):
 		self.bloodGroup = bloodGroup
 		self.gender = 'Male'
 		self.genetic_Disease = genetic_Disease


class Child(Father,Mother):
 	def __init__(self, bloodGroup, gender, genetic_Disease):
 		self.bloodGroup = bloodGroup
 		self.gender = gender
 		self.genetic_Disease = genetic_Disease

 	def print_data(self):
 		print(self.hasDNA,self.bloodGroup,self.gender, self.genetic_Disease)

    
father1 = Father('A', 'Diabetes')
mother1 = Mother('B', 'Aasthma')
child1 = Child(father1.bloodGroup, mother1.gender, father1.genetic_Disease)
child1.print_data()
