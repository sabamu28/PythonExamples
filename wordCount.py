#read path , read all files, filter 'the' from those files

import os
from collections import Counter

filesList=[]

class WordCount:

	def __init__(self):
		print("WordCount")
		
	def listFilesPath(self,path1):
		global filesList
		dirNames=os.listdir(path1)
		for dn in dirNames:
			joinedPath=os.path.join(path1,dn)
			if os.path.isdir(joinedPath):
				self.listFilesPath(joinedPath)
			else:
				filesList.append(joinedPath)
		return filesList

	def countWords(self,files):
		words=[]
		for file in files:
			print(file)
			with open(file, 'rt') as f:
				for line in f:
					words=words+line.split(" ")
		word_counts = Counter(words)
		return word_counts
		
	
if __name__ == '__main__':
	dirPath="~/Desktop/python/testData"
	dirPath=os.path.expanduser(dirPath)
	wc=WordCount()
	files=wc.listFilesPath(dirPath)
	print files
	word_counts=wc.countWords(files)
	print word_counts
	print "-------------------Common-Words--------------- %s",word_counts.most_common(2)