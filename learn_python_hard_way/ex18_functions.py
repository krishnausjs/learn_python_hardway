#This one is like your scripts with argv
#A function to print two arguments passed using args
def _print_two(*args):
   arg1, arg2 = args
   print "arg1: %r, arg2: %r" % (arg1, arg2)

#ok that *args is actually pointless, we can just do this
#Function to print arg1 and arg2
def _print_two_again(arg1, arg2):
	print "arg1: %r , arg2: %r" % (arg1, arg2)

#This jus takes one argment
#Function to print one argument
def print_one(arg1):
	print "arg1: %r " % arg1

#This prints none
#Function to print nothing
def print_none():
	print "I got nothing."

#Print the output
_print_two("Murali","Marimekala")
_print_two_again("Radhika","Tanguturi")
print_one("Prathyu")
print_one("Rana")
print_none()
