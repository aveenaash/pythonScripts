#===========================================================#
#SNAPSHOT.PY                                                #
#DEVELOPED BY ABINASH BASTOLA AS FIRST PROJECT IN PYTHON    #
#===========================================================#

import os,sys,snapshothelper

os.system('clear')
os.system('date')

def menu():
	print '''
	DIRECTORY/FILE SYSTEM COMPARISION
	=================================
	Make a choice in number:
	
	1. Create a snapshot
	2. List snapshot files
	3. Compare 2 sanpshot
	4. View Snapshot File
	5. Exit
	'''
	choice =raw_input("\t")
	return choice


#MENU DEscision Structure
choice=""
while choice !="5":
	choice=menu()
	if choice == "1":
		os.system('clear')
		print '''
		========================
	      	CREATE SNAPSHOT
		========================
		'''

		directoryName=raw_input('Enter directory name to create snapshot of: ')
		fileName=raw_input('Save snapshot as file: ')	
		snapshothelper.createSnapshot(directoryName,fileName)
	elif choice=="2":
                os.system('clear')
                print '''
                ========================
                LIST OF  SNAPSHOT FILES
                ========================
                '''
		extension=raw_input('Extension of snapshot files: ')
                snapshothelper.listAllSnapshotFiles(extension)
	elif choice=="4":
		os.system('clear')
                print '''
                ========================
                VIEW SNAPSHOT
                ========================
                '''
		fileName=raw_input('Enter snapshot filename : ')
                snapshothelper.printSnapshotFile(fileName)
