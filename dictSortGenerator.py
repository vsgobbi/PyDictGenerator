__author__ = 'ongui'

#!/usr/bin/env python


import sys

def delRepeated(myList):
	outputList = []
	for i in myList:
		if i not in outputList:
			outputList.append(i)
	return outputList

def makeWordList(text, wordlist):
	textFile = open ( text , 'rt') #rt # 'a
	dump = textFile.read()
	textFile.close()
	myList = dump.split()
	myList.sort()
	myList = delRepeated(myList)
	wordPos=0
	wordListFile = open( wordlist , 'at')
	for i in myList:
		wordListFile.write (myList[wordPos]+"\n")
		wordPos=wordPos+1
	wordListFile.close()
	return wordPos

if (__name__=="__main__" ):
	if len(sys.argv) != 3:
		print("usage:\n")
		print("python 'locale/to/file/onguiDictSortGenerator.py' [inputText.txt] [onguiWordList.txt]\n\n")
	else:
		text = sys.argv[1];
		wordlist = sys.argv[2];
		wordListFile = open (wordlist, 'wt')
		wordListFile.close()
		numWords = makeWordList(text, wordlist)
		print("Word-list created in: {0}\nTotal words: {1}.".format(sys.argv[2], numWords))
