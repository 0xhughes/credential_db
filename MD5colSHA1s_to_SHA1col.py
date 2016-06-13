import sqlite3
import sys
import os

def menu():
	sane = 1
	while sane == 1:
		print "[ - ] Please enter absolute path to cred. DB: "
		in_path = raw_input()
		if os.path.exists(in_path):
			pass
			sane = 0
		else:
			os.system('cls' if os.name == 'nt' else 'clear')
			print "[ - ] Invalid path, try again."
	return(in_path)

def main(in_path):
	in_path = in_path
	try:
		db_conn = sqlite3.connect(in_path)
	except sqlite3.OperationalError:
		print "[ - ] SQLite connection error to database, check path, exiting."
		sys.exit(1)
	curs = db_conn.cursor()
	rows = curs.execute("SELECT * FROM main WHERE length(srcMD5) = 40;")

	cnt = 0
	print "[ - ] Running..."
	for row in rows:
		curs = db_conn.cursor()
		pri_Index = str(row[0])
		bad_md5 = str(row[3])
		db_conn.execute('UPDATE main SET srcSHA1 = srcMD5 WHERE pri_Index = "'+pri_Index+'";')
		db_conn.execute('UPDATE main SET srcMD5 = NULL WHERE pri_Index = "'+pri_Index+'";')
		cnt+=1
	
	print "[ + ] "+str(cnt)+" rows updated, press enter to commit, or CTRL+C to cancel."
	end = raw_input()
	print "[ - ] Committing changes..."
	db_conn.commit()
	print "[ - ] Done."
	db_conn.close()
	
try:
	main(menu())
except KeyboardInterrupt:
	print "[ - ] Caught keyboard interrupt, closing"
	sys.exit(0)
