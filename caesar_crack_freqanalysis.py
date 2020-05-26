import matplotlib.pylab as plt 
LETTERS=" ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def freq_analysis(cipher_text):
	cipher_text=cipher_text.upper()
	# dictionary to hold letter and freq pairs
	letter_freq={}
	for letters in LETTERS:
		letter_freq[letters]=0
	for letters in cipher_text:
		if letters in LETTERS:
			letter_freq[letters] += 1
	return letter_freq

def plot_distribution(letter_freq):
	plt.bar(letter_freq.keys(), letter_freq.values())
	plt.xlim([0,len(LETTERS)-1])
	plt.show()

def Keycrack(letter_freq):
	print(letter_freq)
	val_list=list(letter_freq.values())
	val_list.sort()
	x=(val_list[-2])
	# finding the letter which matches with E
	alp=(list(letter_freq.keys())[list(letter_freq.values()).index(x)]) 
	alpVal=LETTERS.find(alp)
	eVal=LETTERS.find("E")
	key=(alpVal-eVal)%(len(LETTERS))
	print("Key is %s"%(key))
	return key

banner="""
 _____                                                  _     ______                 ___              _           _      
/  __ \                                                | |    |  ___|               / _ \            | |         (_)     
| /  \/ __ _  ___  ___  __ _ _ __    ___ _ __ __ _  ___| | __ | |_ _ __ ___  __ _  / /_\ \_ __   __ _| |_   _ ___ _ ___  
| |    / _` |/ _ \/ __|/ _` | '__|  / __| '__/ _` |/ __| |/ / |  _| '__/ _ \/ _` | |  _  | '_ \ / _` | | | | / __| / __| 
| \__/\ (_| |  __/\__ \ (_| | |    | (__| | | (_| | (__|   <  | | | | |  __/ (_| | | | | | | | | (_| | | |_| \__ \ \__ \ 
 \____/\__,_|\___||___/\__,_|_|     \___|_|  \__,_|\___|_|\_\ \_| |_|  \___|\__, | \_| |_/_| |_|\__,_|_|\__, |___/_|___/ 
                                                                               | |                       __/ |           
                                                                               |_|                      |___/            

"""
print(banner)

if __name__ == '__main__':
	print("Hello Cracker!!\nI will help you to find the key and crack the secret message you intercepted ")
	print("Enter the cipher text\n")
	text=input()
	freq=freq_analysis(text)
	plot_distribution(freq)
	keyvalue=Keycrack(freq)
	plainText=''
	text=text.upper()
	# considering all input letters
	for i in text:
		# finding the number asssociated with the letter
		index=LETTERS.find(i)
		# shifting the value as per the KEY
		index=(index-keyvalue)%len(LETTERS)
		# append to the cipher_text
		plainText=plainText+LETTERS[index]
	print(plainText)