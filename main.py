
alphabet = "abcdefghijklmnopqrstuvwxyz"


# Returns a letter's index in the alphabet
def find_pos(letter):
	index = 0
	for l in alphabet:
		if l == letter:
			return index
		else:
			index += 1
# print(find_pos("h"))


# returns user input for shift direction
def get_shift_direction():
	shift_dir = ""
	while shift_dir != "l" or shift_dir != "r":
		shift_dir = input("Would you like to shift left or right? Please enter l or r")
		if shift_dir == "l":
			print("You have chosen left shift cypher")
			return shift_dir
		elif shift_dir == "r":
			print("You have chosen right shift cypher")
			return shift_dir


# returns user input for cypher key
def get_shift_key():
	while True:
		key = int(input("What is the encryption key? Numbers only."))
		if type(key) == int:
			return key


# Returns a letter in the alphabet given an index
def find_letter(index):
	return alphabet[index]
# print(find_letter(4))


# takes in a text message and returns the indices for the characters in the alphabet array
def convert_to_indices(message):
	message_indices = []
	for letter in message:
		message_indices.append(find_pos(letter))
	return message_indices
# print(convert_to_indices("hello"))


# increments a list of numbers by the amount specified in the key using list comprehension
def right_shift(indices, key):
	cyphered_list = [(x + key) % 26 for x in indices]
	return cyphered_list
# indices for "hello" passed as input:
# print(right_shift([7, 4, 11, 11, 14], 12, "r"))


# decrements a list of numbers by the amount specifies in the key
def left_shift(indices, key):
	cyphered_list = [(x + (26 - key)) % 26 for x in indices]
	return cyphered_list
# print(right_shift([7, 4, 11, 11, 14], 12, "r"))


def convert_to_text(list_of_indices):
	string_array = []
	for index in list_of_indices:
		string_array.append(alphabet[index])
	output = "".join(string_array)
	return output
# print(convert_to_text([7, 4, 11, 11, 14]))


def encrypt(message):
	shift_direction = get_shift_direction()
	key = get_shift_key()

	# convert text to indices
	message_indices = convert_to_indices(message)
	# shift indices
	if shift_direction == "r":
		new_message_indexes = right_shift(message_indices, key)
	else:
		new_message_indexes = left_shift(message_indices, key)

	print(convert_to_text(new_message_indexes))


#  Takes in the key, and then gives user two options of what the message could be by executing both a left + right shift
def decrypt(message):
	key = get_shift_key()
	message_indices = convert_to_indices(message)

	lshift_message_indices = left_shift(message_indices, key)
	left_shifted_message = convert_to_text(lshift_message_indices)

	rshift_message_indices = right_shift(message_indices, key)
	right_shifted_message = convert_to_text(rshift_message_indices)

	print(f"The message is either {right_shifted_message}, or {left_shifted_message}")


encrypt_or_decrypt = ""
while (encrypt_or_decrypt != "encrypt") and (encrypt_or_decrypt != "decrypt"):

	encrypt_or_decrypt = input("Would you like to encrypt or decrypt a message?")

	if encrypt_or_decrypt == "encrypt":
		while True:
			message = input("What is the message you would like encrypted?")
			if type(message) == str:
				encrypt(message)
				exit()

	elif encrypt_or_decrypt == "decrypt":
		while True:
			message = input("What is the message you would like decrypted?")
			if type(message) == str:
				decrypt(message)
				exit()

