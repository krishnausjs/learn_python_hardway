class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
		   "I don't want to get sued",
		   "So I'll stop right there"])

bulls_on_parade = Song (["They rally around the family",
			  "With pockets full of shells"])

jingle_bell = Song([ "Jingle bell Jingle bell",
		      "printed this rhyme"])

new_song =  { 
	"Wrote setence instead of a song",
	" This sentence is a variable song"
}

print_letter_by_letter = "Murali" 
print_word_by_word = [ 
	"Krishna",
	"Marimekala" 
]


happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

jingle_bell.sing_me_a_song()

variable_song = Song(new_song)
variable_song.sing_me_a_song()

letter_by_letter = Song(print_letter_by_letter)
letter_by_letter.sing_me_a_song()

print_word_by_word = Song(print_word_by_word)
print_word_by_word.sing_me_a_song()
