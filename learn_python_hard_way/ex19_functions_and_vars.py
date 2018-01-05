#Actual function definition that takes input and prints the sentences
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers !" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanker.\n"

prompt = '>'

print "Enter number of cheeses"
amount_of_cheese = raw_input(prompt)

print "Enter number of crackers"
amount_of_crackers = raw_input(prompt)

cheese_and_crackers(int(amount_of_cheese),int(amount_of_crackers))

#Just pass fixed numbers and call the function
print "We can just give the functions numbers directly.:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

#Call the function with two variables assigned with values
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#Do some math while passing arguments
print "We can even do math inside to"
cheese_and_crackers(10+20, 5+6)

#Do more math while passing arguments
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
