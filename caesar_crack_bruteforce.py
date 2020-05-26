##################################################### Caesar Cipher Crack #####################################################
ALPHABET=' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def caeser_crack(cipher_text):
	for key in range(len(ALPHABET)):
		plain_text=" "
		for i in cipher_text:
			index=ALPHABET.find(i)
			index=(index-key)%len(ALPHABET)
			plain_text=plain_text+ALPHABET[index]
		print("With key %s, the result is: %s " %(key,plain_text))

banner = """

   ___                                                _     _                _        
  / __| __ _  ___  ___ __ _  _ _   __  _ _  __ _  __ | |__ | |__  _ _  _  _ | |_  ___ 
 | (__ / _` |/ -_)(_-</ _` || '_| / _|| '_|/ _` |/ _|| / / | '_ \| '_|| || ||  _|/ -_)
  \___|\__,_|\___|/__/\__,_||_|   \__||_|  \__,_|\__||_\_\ |_.__/|_|   \_,_| \__|\___|

"""

if __name__ == '__main__':

	print(banner)
	print("Hello!\nI am the bruteforce cracker for caeser cipher!\nEnter the cipher text you want to crack and know the key")
	ciphertext=input()
	caeser_crack(ciphertext)
