class Animal(object):
	pass  #do nothing 

class Dog(Animal):
	
	def __init__(self,name):
		self.name = name
		
class Cat(Animal):
	
	def __init__(self,name):
		self.name = name

class Person(object):
	
	def __init__(self,name):
		self.name = name
		self.pet = None

class Employee(Person):
	
	def __init__(self,name,salary):
	#子类对父类的构造方法进行调用的方法 super(本子类名,self)__init__(其他参数)  
	#记住，不是super(父类)，因为super的意思本身就是向上的意思。
		super(Employee,self).__init__(name)
		self.salary = salary

class Fish(object):
	pass

class Salmon(Fish):
	pass

class Halibut(Fish):
	pass

rover = Dog("Rover")
satan = Cat("Satan")
mary = Person("Mary")
wang = Person("Wang")
mary.pet = satan

frank = Employee("Frank",120000)
frank.pet = rover

filpper = Fish()

crouse = Salmon()

harry = Halibut()

#终于想起来了，对象和实例是一个意思。
	