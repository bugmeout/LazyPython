class TheThing(object):
	def __init__(self):
		self.number  = 0
	
	def some_function(object):
		
		print object
		print "I got called."
		print object.number
	
	def add_me_up(self,more):
		self.number += more
		return self.number
	
a = TheThing()
b = TheThing()

#actually,it is some_function(a) 
a.some_function()

b.some_function()

print a.add_me_up(20)
print b.add_me_up(30)

print a.number
print b.number

class TheMultiplier(object):
	def __init__(self,base):
# self._init__(base)
		self.wahu = base
	def do_it(self,m):
		return self.wahu * m

x = TheMultiplier(a.number)
print x.do_it(b.number)