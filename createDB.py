import sqlite3
import sys
import os

def menu():
	sane = 1
	while sane == 1:
		print "[ - ] Please enter absolute path to cred. database to be created: "
		in_path = raw_input()
		if os.path.exists(in_path):
			os.system('cls')
			print "[ - ] Invalid path, try again."
		else:
			sane = 0
	return(in_path)

def main(dbPath):
	createQ = "CREATE TABLE "+'"main"'+" ('pri_Index' INTEGER PRIMARY KEY AUTOINCREMENT, 'identifier' TEXT , 'clearTextP' TEXT , 'srcMD5' TEXT , 'srcSHA1' TEXT , 'srcBCRYPT' TEXT , 'rainTableMD5' TEXT , 'rainTableSHA1' TEXT , 'rainTableBCRYPT' TEXT)"
	try:
		db_conn = sqlite3.connect(dbPath)
	except:
		print "[ - ] Unable to create, check path and try again."
		sys.exit(1)
	cur = db_conn.cursor()
	cur.execute(createQ)
	print "[ - ] DB created at "+dbPath+"\nPress enter to exit."
	end = raw_input()

try:
	main(menu())
except KeyboardInterrupt:
	print "[ - ] CTRL+C caught, exiting."