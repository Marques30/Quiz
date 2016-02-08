parts_of_speech = ["NAME", "PERSON", "PLACE","ADJECTIVE"]
test_string1 = ""
test_string2 = ""
test_string3 = ""
def word_in_pos(word, parts_of_speech):
	for pos in parts_of_speech
		if pos in word:
			return pos
	return None

def quiz(ml_string, parts_of_speech):
	replaced = []
		for word in ml_string
		replacement = word_pos(word, parts_of_speech)
		if replacement != None:
			user_input = raw_input("type in a: " + replacement + " ")
			word = word.replace(replacement, user_input)
			replaced.append(word)
		else:
			replaced.append(word)
	replaced = "".join(replaced)
	return replaced