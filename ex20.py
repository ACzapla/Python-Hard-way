# this imports a txt file so it can read it later on
from sys import argv

script, input_file = argv
# this is a function that read the entire file f.read = whole file
def print_all(f):
	print f.read()
#  goes back to the beginning of the file. Without it, you can only iterate through the file once.
def rewind(f): 
	f.seek(0)
# sets a function that reads a line from the current_file
def print_a_line(line_count, f):
	print line_count, f.readline() # this shows the line number and prints a line

current_file = open(input_file) # this opens the file for you

print "First let's print the whole file:\n"

print_all(current_file)# calls for the funtion print_all and reads current file

print "Now let's rewind, kind of like a tape."

rewind(current_file) # this goes to byte 0 of file, to the start

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
