(these are mainly for me; they don't need to make ***tooo*** much sense

- i think "set words", "import words", and "load words",
are quite vague, and i should probabably find a clear way to differentiate between 
the lower level importing words, and the higher level feeding in file path and calling the import functions


- okay im gonna go to sleep and hopefully have a better idea of how i want to structure the classes when i wake up

- scratch that ive got a pretty banging structure now. what i want to work on is using the property 
decorator to get rid of my getters. ill do that later though. first i need to git init!

- might remove the player class cuz i dont actually think i need it (oh wait no cuz input method)

- to reduce repeated code in the random bot, i could probably oop-ize the green/yellow/grey letter part


- actually i 100% am.

 	def getGreyLetters(self):
		grey_letters = []
		for guess in self.guesses:
			for letter,colour in zip(guess.word,guess.colourPattern):
				if colour == Colour.GREY:
					grey_letters.append(letter)
		return grey_letters


	def getYellowLetters(self):
		yellow_letters = []
		yellow_positions = []
		for guess in self.guesses:
			for index,(letter,colour) in enumerate(zip(guess.word,guess.colourPattern)):
				if colour == Colour.YELLOW:
					yellow_letters.append(letter)
					yellow_positions.append(index)
		return yellow_letters,yellow_positions

	def getGreenLetters(self):
		green_letters = []
		green_positions = []
		for guess in self.guesses:
			for index,(letter,colour) in enumerate(zip(guess.word,guess.colourPattern)):
				if colour == Colour.GREEN:
					green_letters.append(letter)
					green_positions.append(index)
		return yellow_letters,green_positions

^ old monstrosity


aaactually maybe ill just make 

 def getletters(color) where color is like Colour.GREEN or sometin

 also i went from yellow letters, yellow position to yellow lettters[0] and [1], but this is also not good, and i will switch to classes evnetually


 also i wanna fix the "thinking_ratio" implementation so it only applies to the specific bots that need it
