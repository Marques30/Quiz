parts_of_speech1 = ["NAME", "PERSON", "VERB", "PLACE","ADJECTIVE"]
test_string1 = "My name is NAME, I live in a place called PLACE. Everyday I VERB, with my three friends: Justin, Angie, and PERSON."
test_string2 = ""
test_string3 = ""
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

print play_game(test_string3,parts_of_speech1)