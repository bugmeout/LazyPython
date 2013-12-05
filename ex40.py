
cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = 'PortLand'

def find_city(themap,state):
	if state in themap:
		return themap[state]
	else:
		return "Not Found"

#这句话表示将cities['_find']来接find_city的结果
cities['_find'] = find_city

while True:
	print "State?(Enter to quit)"
	state = raw_input("> ")
	
	if not state : break
	
#	city_found= cities['_find'](cities,state)
	city_found= find_city(cities,state)
	print city_found
	
#体会一下这种写法哈。
#	city_found= cities['_find'](cities,state)
#Here, we're storing the function itself in the dictionary, to be called later --------From StackOverFlow
#也就是说，在cities['_find']=find_city这句话中，字典列表中把一个函数当做元素存了起来，对应的索引是_find.
#我想，现实中应该没有人会这样，作者这样做的目的应该是告诉我们，字典集合是个非常宽泛的组合，里面只要有index和key，什么都可以存，哪怕你放的是函数。
#
#cities['_find']存放函数名。这里，计算机先找到cities['_find']=find_city,而后知道这是一个函数，参数还得带括号。
#

