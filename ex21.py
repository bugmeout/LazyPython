def add(a,b):
	print "ADDING %d + %d" % (a,b)
	return a+b

def subtract(a,b):
	print "SUBTRACTING %d - %d" %(a,b)
	return a-b

def multiply(a, b):
		print "MULTIPLYING %d * %d " %(a, b)
		return a * b
	
def divide(a, b):
	print "DIVIDING %d / %d" %(a, b)
	return a / b

	
age = add(30, 7)
height = subtract(78 , 4)

weight = multiply(90 , 2)

iq = divide( 100 ,2)

#JUST NOW i forgot the char % before (age,.....).NOTICE IT.

print "Age: %d ,Height: %d, Weight: %d , IQ: %d" % (age,height,weight,iq)