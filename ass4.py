#!/opt/bin/python3
# Author: Saige Liu V00812068

import sys
from os.path import isfile,join
import os
import re

suffix = 'c|cpp|C|cc' 
#all the file with ".c"".C"".cpp"or".cc"
SRCS = []
OBJS = []
WorkingDependncies = []

def selectfile():
	if len(sys.argv)>1:
		folderpath = sys.argv[1]
		try:
			os.chdir(folderpath)
		except:
			print("Error: invalid path")
			exit(1)
	else:
		print('usage: %s [path]' % sys.argv[0])
		exit(1) 
	for f in os.listdir(os.getcwd()):
		if isfile(join(os.getcwd(),f)):
			checkfilename(f)

def checkfilename(f):
	r = re.match(r'(.*)\.(%s)$' % suffix, f);
	#if there is a .c
	if r:
		SRCS.append(f)
		OBJS.append(r.group(1) + '.o')
		#change to a .o
		WorkingDependncies.append(findDependencies(f))

def createList(theList):
	result = ''
	for string in theList:
		result += ' ' + string
	return result + '\n'

def writeMakefile():
#what we write in the file
	makefile = open('Makefile','w')
	makefile.write('SRCS =' + createList(SRCS))
	makefile.write('OBJS =' + createList(OBJS))
	makefile.write('PROG = prog.exe\n\n')
	makefile.write('$(PROG): $(OBJS)\n')
	makefile.write('\t$(CC) $(LDFLAGS) $(OBJS) $(LDLIBS) -o $(PROG)\n')
	for j in range(0,len(SRCS)):
		makefile.write('\n%s: %s%s' % (OBJS[j],SRCS[j],createList(WorkingDependncies[j])))
		#name of the programme like foo.o:foo.c
		if (SRCS[j].split('.')[-1] == 'c'):
			makefile.write('\t$(CC) $(CPPFLAGS) $(CFLAGS) -c %s\n' % SRCS[j])
		if (SRCS[j].split('.')[-1] in ['C', 'cpp', 'cc']) :
			makefile.write('\t$(CXX) $(CPPFLAGS) $(CXXFLAGS) -c %s\n' % SRCS[j])
	makefile.write('\nclean:\n')
	makefile.write('\trm -f $(OBJS)\n')
	makefile.close()

def Recursive(soureceFileName, fileName, dependencyList):
#use recursive function to findDependencies
	newHeaderFileList = []
	try:
		f = open(fileName, 'r')
		lines = f.readlines()
		for line in lines:
			r = re.match(r'#include\s*\"(.*)\".*', line)
			if r:
				possibleHeaderName = r.group(1)
				if(not possibleHeaderName.endswith('.h')):
					continue
				if(not(possibleHeaderName in dependencyList)):
					newHeaderFileList.append(possibleHeaderName)
		f.close()
		dependencyList += newHeaderFileList
		for eachFile in newHeaderFileList:
			Recursive(soureceFileName, eachFile, dependencyList)
	except:
		print("%s: contains #include for missing file %s" % (soureceFileName, fileName))

def findDependencies(fileName):
	result = []
	Recursive(fileName, fileName, result)
	return result

def main():
	selectfile()
	writeMakefile()
	
if __name__ == "__main__":
	main()
