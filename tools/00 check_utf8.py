import glob
import re


for filename in glob.glob("./*.csv"):
	with open(filename, 'rU') as f:
		for line in f:
			if re.search(r'[\x80-\xFF]', line):
				print 'bad string in file ' + filename + ' at line ' + re.sub(r'([\x80-\xFF])', '->\1<-', line)
