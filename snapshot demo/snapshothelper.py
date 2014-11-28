# coding=utf8
#=======================================
#This is a helper module for snapshot.py
#
#=======================================

import os,pickle

def createSnapshot(directory,filename):
	allDirectories=[]
	allFiles=[]
	for root,dirs,files in os.walk(directory):
		#print root
		#print dirs
		#print files
		allDirectories=allDirectories+dirs
		allFiles=allFiles+files	
	try:
		#The open() opens or create a file:
		f=open(filename,'wb')	
		# The pickle module implements a fundamental, but powerful algorithm for serializing and 
		#de-serializing a Python object structure.
		#To serialize an object hierarchy, you first create a pickler, then you call the pickler’s dump() method.
		#To de-serialize a data stream, you first create an unpickler, then you call the unpickler’s load() method. 
		#The pickle module provides the following constant:
		#pickle.HIGHEST_PROTOCOL
		#The highest protocol version available. This value can be passed as a protocol value.
		pickle.dump((allDirectories,allFiles),f)
		#pickle.dump(allFiles,f)
		#pickle.dump(obj, file[, protocol])
		#Write a pickled representation of obj to the open file object file. This is equivalent to Pickler(file, protocol).dump(obj).
		#If the protocol parameter is omitted, protocol 0 is used. If protocol is specified as a negative value or HIGHEST_PROTOCOL, 
		#the highest protocol version will be used.
		f.close()
	except:
		print "Error while dumping objects to files"
	



def printSnapshotFile(filename):	
	allthings = pickle.load( open( filename, "rb" ) )
	directories=allthings[0]
	filess=allthings[1]	
	print "\nAll Directories\n"
	for a in directories:		
		print a
	print "\nAll Files\n"
	for a in filess:
		print a  


def listAllSnapshotFiles(extension):
	filelist=os.listdir(os.curdir)	 
	print "\n List of Snapshot Files"
	for files in filelist:
		if(files.find(extension)!=-1):
			print files

def compareSnapshots(file1,file2):
	snpFile1=open(file1,'rb')
	allFliesAndDir1=pickle.load(snpFile1)
	
	snpFile2=open(file2,'rb')
		
