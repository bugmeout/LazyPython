class Room(object):
	def __init__(self,name,description):
		self.name = name
		self.description = description
		self.paths = {}
		
	def go(self,direction):
		return self.paths.get(direction,None)
	
	def add_paths(self,paths):
		self.paths.update(paths)

#center = Room("Center", "Test room in the center.")
#north = Room("North", "Test room in the north.")
#center.add_paths({'north': north})

#center = Room("center","it's center.")
#center.add_paths({'north': north, 'south': south})
#center.add_paths({'north':yes,'south':south})
#center.add_paths({'north': yes})