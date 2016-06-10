import sqlite3
import hashlib
import os

def menu():
	sane = 1
	while sane == 1:
		print "[ - ] Please enter absolute path to cred. database: "
		in_path = raw_input()
		if os.path.exists(in_path):
			sane = 0
		else:
			os.system('cls')
			print "[ - ] Invalid path, try again."
	return(in_path)

conn = sqlite3.connect(menu())
conn.text_factory = str

cur1 = conn.cursor()
x = cur1.execute("SELECT * FROM main")
cur2 = conn.cursor()

cnt = 0

def is_ascii(s):
	return all(ord(c) < 128 for c in s)

for row in x:
	try:
		if is_ascii(str(row[2])):
			if str(row[2]) != "None":
				if len(str(row[2])) > 3:
					if len(str(row[6])) == 4:
						pas = str(row[2])
						m = hashlib.md5()
						m2 = hashlib.sha1()
						m.update(pas)
						m2.update(pas)
						ind = row[0]
						cur2.execute("UPDATE main SET rainTableMD5 = '"+str(m.hexdigest())+"' WHERE pri_Index = '"+str(ind)+"'")
						cur2.execute("UPDATE main SET rainTableSHA1 = '"+str(m2.hexdigest())+"' WHERE pri_Index = '"+str(ind)+"'")
						cnt+=1
						if cnt % 100 == 0:
							os.system('cls')
							print "[ + ] "+str(cnt)+" rain SHA1/MD5s calculated and entered."
	except UnicodeEncodeError:
		pass
	except KeyboardInterrupt:
		print "CTRL+C caught..."
		break
		
raw_input("Press enter to commit...")
conn.commit()