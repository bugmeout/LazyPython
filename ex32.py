#python中，for a in array 中，a代表array[a]，执行完之后默认a++。print中出现的全部是值，不是索引值。从20行的那个例子最容易看出来。


the_count = [1,2,3,4,5]
fruits = ['apple','oranges','pears','apricots' ]
changes = [1,'pennies',2,'dimes',3,'quarters']

#this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" %number
	
for fruit in fruits:
	print "A fruit of type: %s" %fruit
	
for i in changes:
	print "I got %r" %i

elements = []

for i in range(10,15):
	print "Adding %d to the list" %i
	elements.append(i)


for i in elements:
	print "Element was: %d" %i
	
test = range(100,115)
for i in test:
	print "test was: %d" %i