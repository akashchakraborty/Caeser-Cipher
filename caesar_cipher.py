############################################################## Caesar Cipher ######################################
ALPHABET=' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY=3
# ceaser encryption algorithm
def ceaser_encrypt(plain_text):
	# the encrpypted message
	cipher_text=''
	# converting all input to upper case
	plain_text=plain_text.upper()
	# considering all input letters
	for i in plain_text:
		# finding the number asssociated with the letter
		index=ALPHABET.find(i)
		# shifting the value as per the KEY
		index=(index+KEY)%len(ALPHABET)
		# append to the cipher_text
		cipher_text=cipher_text+ALPHABET[index]
	print(cipher_text)

# ceaser decryption algorithm
def ceaser_decrypt(cipher_text):
	# the plain text
	plain_text=''
	# converting all input to upper case
	cipher_text=cipher_text.upper()
	# considering all input letters
	for i in cipher_text:
		# finding the number asssociated with the letter
		index=ALPHABET.find(i)
		# shifting the value as per the KEY
		index=(index-KEY)%len(ALPHABET)
		# append to the cipher_text
		plain_text=plain_text+ALPHABET[index]
	print(plain_text)
####################################################################################################################	
banner="""
 _______  _______  _______  _______  _______  _______       _______ _________ _______           _______  _______   
(  ____ \(  ___  )(  ____ \(  ____ \(  ___  )(  ____ )     (  ____ \\__   __/(  ____ )|\     /|(  ____ \(  ____ )  
| (    \/| (   ) || (    \/| (    \/| (   ) || (    )|     | (    \/   ) (   | (    )|| )   ( || (    \/| (    )|  
| |      | (___) || (__    | (_____ | (___) || (____)|     | |         | |   | (____)|| (___) || (__    | (____)|  
| |      |  ___  ||  __)   (_____  )|  ___  ||     __)     | |         | |   |  _____)|  ___  ||  __)   |     __)  
| |      | (   ) || (            ) || (   ) || (\ (        | |         | |   | (      | (   ) || (      | (\ (     
| (____/\| )   ( || (____/\/\____) || )   ( || ) \ \__     | (____/\___) (___| )      | )   ( || (____/\| ) \ \__  
(_______/|/     \|(_______/\_______)|/     \||/   \__/     (_______/\_______/|/       |/     \|(_______/|/   \__/ 

	
					Developed by Akash Chakraborty

"""
print(banner)
####################################################################################################################
if __name__ == "__main__":

	print('WELCOME! User\nI will be your Caeser Cipher for the English Alphabet')
	print("What do you want to do?\nPress E to encrypt and D to decrypt")
	x=input()
	if (x=="D" or x=="d"):	
		print("Tell me the message to decrypt\n")
		ciphertext=input('')
		ceaser_decrypt(ciphertext)
	elif(x=="E" or x=="e"):
		print("Tell me the message to encrypt\n")
		plaintext=input('')
		ceaser_encrypt(plaintext)
	else :
		print("Sorry, Something went wrong")


