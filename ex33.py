i = 0
numbers = []

while i < 6 :
	print "At the top i is %d" %i
	numbers.append(i)
	
	i += 1
	print "Numbers now: ",numbers
	print "At the bottom i is %d" %i 
	
print "The numbers:"

#python 中，print是个很神奇的函数，尤其是加上comma之后
for num in numbers:
	print num ,
	
	
print "----------------------"
#print一个数组，就代表全部输出，好牛逼的样子啊。
print numbers