#Function to break words. Uses split that returns word by word
def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words

#Sort all the words. Uses sorted call internally.
def sort_words(words):
	"""Sort the words."""
	return sorted(words)

#Print first words. Uses word pop with 0 arument for first word
def print_first_word(words):
	"""Print the first word after popping it off."""
	word = words.pop(0)
	print word

#Print last word. Uses pop with -1 to get last word
def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	print word

#Sort setence by sorti words
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

#Print first and last word in a sentence. Need to revisit this 
#as its not clear about breaking a setence into words and printing first and last
def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

#Print first and last sorted
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)

