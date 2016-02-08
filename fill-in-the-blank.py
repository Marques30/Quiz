parts_of_speech1 = ["NAME", "PERSON", "VERB", "PLACE","ADJECTIVE"]
test_string1 = "My name is NAME, I live in a place called PLACE. Everyday I VERB, with my three friends: Justin, Angie, and PERSON."
test_string2 = "For some reason my friends always argue about ADJECTIVE. And everyday I have no idea why. There is another group of people well more of a pair Mark and PERSON. There the kinds of people that VERB and who say they will help then disappear to go to PLACE."
test_string3 = "However, today is the day that I finally ADJECTIVE. It has finally come to the point where I can leave everyone and go to PLACE. But before any of this I have to meet PERSON. Because he/she is the one to teach me VERB."
def word_in_pos(word, parts_of_speech):
	for pos in parts_of_speech:
		if pos in word:
			return pos
	return None

def play_game(ml_string, parts_of_speech):
	replaced = []
	ml_string = ml_string.split()
	for word in ml_string:
		replacement = word_pos(word, parts_of_speech)
		if replacement != None:
			user_input = raw_input("type in a: " + replacement + " ")
			word = word.replace(replacement, user_input)
			replaced.append(word)
		else:
			replaced.append(word)
	replaced = " ".join(replaced)
	return replaced

print play_game(test_string3, parts_of_speech1)