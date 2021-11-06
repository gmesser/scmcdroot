# scmwd.py - Scan upwards in the directory tree until an SCM dir is found
# or the root directory is reached.

# Python version of scmwd

import sys
import os

# This is the list of SCM metadata directory names that we are looking for.
scmDirNames = ['.svn', '.git', '.bzr', '.p4']
scmDirFound = ['', '']

# Get the SCM metadata directory in effect for the current directory.
# Walk up the directory tree from the current directory looking for one of the defined SCM metadata directory names.  
def getScmDir():
	while True:
		cwd = os.getcwd()
		for dirName in scmDirNames:
			if os.path.exists(dirName) and os.path.isdir(dirName) :	
				scmDirFound[0] = cwd
				scmDirFound[1] = dirName[1:]
				return
		if cwd == '/':
			return
		else:
			os.chdir('..')

# Print the SCM metadata directory if one is found.	
if __name__ == '__main__':
	getScmDir()
	if len(scmDirFound[0]) > 0:
		print(scmDirFound[0])
		sys.exit(0)
	else:
		sys.exit(1)
