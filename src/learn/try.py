#! /usr/bin/env python
try:
	filename=raw_input('Enter file name:')
	fileObj=open(filename,'r')
	for eachLine in fileObj:
		print eachLine,
	fileObj.close
except IOError,e:
	print 'file open error:',e



