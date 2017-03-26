#  Code written by Zachary Nafziger while working through Violent Python exercises
import crypt
import sys
def testPass(cryptPass, dictionary):
	salt = cryptPass[0:11] #rewritten for shadow file
	cryptPass =cryptPass.split('$')[3]
	dictFile = open(dictionary, 'r')
	for word in dictFile.readlines():
		word = word.strip('\n')
		cryptWord = crypt.crypt(word, salt).split('$')[3]
		if (cryptWord == cryptPass):
			print "\tFound a match: " + word + "\n"
			return
	print "\tNo matching passwords found"
	return
def main():
	print "************PYCRACK************ \nUse ./pycrack.py [dictionary file path] [shadow file path]\n*******************************\n"
	if(len(sys.argv) < 3):
		print "Not enough args!"
		return
	passFile = open(sys.argv[2])
	for line in passFile.readlines():
		if ":" in line:
			user = line.split(':')[0]
			cryptPass = line.split(':')[1].strip(' ').strip('\n')
			if (cryptPass[0] == '*'):
				return
			print "Attempting to crack " + user + "'s password..."
			testPass(cryptPass, sys.argv[1])
if __name__ == "__main__":
	main()
