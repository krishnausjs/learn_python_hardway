#Pick ten things 
ten_things = "Apples Oranges Crows Telephone Light Sugar"

#We dont see 10 things here
print "Wait there's not 10 things in that list, let's fix that."

#Lets separate each by space and copy them to stuff
stuff = ten_things.split(' ')

#More stuff with strings
more_stuff = [ "Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

#Till stuff count not equal to 10, pop strings from more_stuff and append it to stuff
while len(stuff) != 10:
	#pop one from more stuff
	next_one = more_stuff.pop()
	print "Adding:" , next_one
	#Append to stuff
	stuff.append(next_one)
	print "There's %d items now." % len(stuff)
	
print "There we go. Elements of stuff are \n: ", stuff

print "Let's do some things with stuff."

#print first element not 0th one
print "First element of stuff is " , stuff[1]
#print last element
print "Last element of stuff is", stuff[-1] #whoa! fancy
#Pop last element of stuff
print "Pop of stuff is" , stuff.pop()
#Join everthing in stuff by space
print "join of stuff is " , ' '.join(stuff) #what ? cool !
#join 4th till 6th by #
print "Join # of stuff is " , '#'.join(stuff[3:5]) #super stellar !
