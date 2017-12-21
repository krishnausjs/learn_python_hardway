from sys import argv

#Take input file
script, input_file = argv

#function to print input file contents
def print_all(f):
	print f.read()

#function to rewind the file
def rewind(f):
	f.seek(0)

#function to print a line
def print_a_line(line_count, f):
	print line_count, f.readline()

#Open the input file
current_file = open(input_file)

#Print file contents first
print "First let's print the whole file:\n"
print_all(current_file)

#Rewind to beginning of the file
print "Now let's rewind, kind of like a tape."
rewind(current_file)

#Print line by line. Firs three lines
print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)


