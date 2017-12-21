#Function that adds a and b
def add(a, b):
	print "Adding %d + %d" % (a,b)
	return a + b

#Function that substracts a and b
def substract(a, b):
	print "Substracting %d - %d" % (a,b)
	return a - b

#Function that multiply a and b
def multiply(a, b):
	print "Multiplying %d * %d" % (a,b)
	return a * b

#Function that divide a and b
def divide(a, b):
	print "Dividing %d / %d" % (a,b)
	return a / b

print "Lets do some math with just functions!"

#call functions
age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit , type it in anyway
print "Here is a puzzle"
what = add(age, substract(height,multiply(weight, divide(iq,2))))

print "This becomes:", what, "Can you do it by hand ?"

#My puzzle
myformula = multiply(add(divide(iq,2),substract(5,1)),2)

print "My formula value is %d" % myformula
