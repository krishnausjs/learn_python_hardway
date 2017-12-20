#assigning string to x
x = "There are %d types of people." % 10
#assigning a variable with strings
binary = "binary"
do_not = "don't"
#Printing strings
y = "Those who knows %s and those who %s." % (binary, do_not)

#Print x and y
print x
print y

#Using %r to print raw data. Usually used for debugging. Also %s for string
print "I said: %r." % x
print "I also said : '%s'." % y

#String assignment and using a string to print partial print statement
hilarious = False
joke_evaluation = "Isn't that joke so funny ?! %r"
 
print joke_evaluation % hilarious

#String concatenating
w = "This is the left side of ..."
e = "a string with a right side."

print w+e
