#Importing argv from sys
from sys import argv

#Read script and filename through argv
script, filename = argv

#Open the file with filename
txt = open(filename)

#Print your file name and then contents of the file
print "Here's your file %r:" % filename
#Use the file object and read function to read the file
print txt.read()

#Display a prompt to user to read the file name
print "Type the filename again."
file_again = raw_input("> ")

#Now open the file again using open that returns the file object
txt_again  = open(file_again)

#Using the object and read(), try displaying the file contents
print txt_again.read()
