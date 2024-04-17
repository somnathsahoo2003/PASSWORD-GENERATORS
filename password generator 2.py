# TASK:- PASSWORD GENERATOR

'''A password generator is a useful tool that generates strong and
random passwords for users. This project aims to create a
password generator application using Python, allowing users to
specify the length and complexity of the password'''

# CONDITIONS:-

# User Input: Prompt the user to specify the desired length of the password.
# Generate Password: Use a combination of random characters to generate a password of the specified length.
# Display the Password: Print the generated password on the screen.

'''In my opnion,here it is a short and concise algorithm which easily to learning up to the implementation of code for the calculator program in python.'''
# STEP 1:-Getting password length using int to enter the no of size required in password
# STEP 2:- using multiple choice to generate passwords(DIGITS(0-9),LETTERS(A-Z,a-z),SPECIAL CHARACTER(!,@,#,$,%,^,&,*,.,'',"",:,;))
# STEP 3:- Using condition while(true)Now using if-else case to check condition
# STEP 3.1:-if choice==1 then,[' Adding letters to possible characters(string.ascii_letters)']
# STEP 3.2:-elif choice==2 then, ['Adding digits to possible characters(string.digits)']
# STEP 3.3:-elif choice==3' then ['Adding special characters to possible characters(string.punctuation)']
# STEP 3.4:-else invaild  ['print("Please pick a valid option!")']

# STEP 4:-Picking a random character from our character list
# STEP 5:-appending a random character to password
# STEP 6:-  printing password as a string ['print("The random password is " + "".join(password))']

# CODE:-

import string
import random
length = int(input("Enter password length: "))

print('''Choose character set for password from these : 
		1. Digits
		2. Letters
		3. Special characters
		4. Exit''')

characterList = ""
while(True):
	choice = int(input("Pick a number "))
	if(choice == 1):
		characterList += string.ascii_letters
	elif(choice == 2):
		characterList += string.digits
	elif(choice == 3):
		characterList += string.punctuation
	elif(choice == 4):
		break
	else:
		print("Please pick a valid option!")

password = []
for i in range(length):
	randomchar = random.choice(characterList)
	password.append(randomchar)
print("The random password is " + "".join(password))
