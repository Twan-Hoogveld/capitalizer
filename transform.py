import sys
import pyperclip

if __name__ == '__main__':
	oldstr = input("Enter a sentence : ")
	strLst = oldstr.split(" ")
	wordStr = ''
	for keyword in strLst:
		for letter in keyword:
			wordStr += letter.upper() + ' '
		wordStr += ' '
	pyperclip.copy(wordStr)