i = 0
numbers = []
new_numbers = []
j = 0
def while_loop(count):
	while j < count:
		global j #Without this we will face UnboundLocalError
		new_numbers.append(i)
		j = j + 1
		print "Value of j is %d" % j

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)

	i = i + 1
	print "Number now: ", numbers

	print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
	print num 

print "Calling while loop definition"
while_loop(6)
