#import argv feature from sys package
from sys import argv
#import exists from os.path package
from os.path import exists

#Read input arguments , we expect 3 args
script, from_file, to_file  = argv

#Print the info
print "Copying from %s to %s" % (from_file, to_file)

#we could do these two ways
#in_file = open(from_file)
indata = open(from_file).read()
#indata = in_file.read()

#Use len to find the size of data
print "The input file is %d bytes long\n" % len(indata)

#Check if the file exist
print "Does the output file exist? %r" % exists(to_file)

#Know if user really wants to continue or abort
print "Ready, hit RETURN  to continue, Ctrl-C to abort."
raw_input()

#Output the filee
open(to_file, 'w').write(indata)
#out_file = open(to_file, 'w')
#out_file.write(indata)

print "Alright , all done"
#out_file.close()
#in_file.close()
