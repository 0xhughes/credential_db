# Get params.
import os
import sqlite3

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

print "[ - ] Is this a source MD5, BCrypt, SHA1, or Clear Text input?"

sane = 0
sel_opts = ["1", "2", "3", "4"]
while sane == 0:
	sel = raw_input("[ + ] 1 - MD5\r\n[ + ] 2 - SHA1\r\n[ + ] 3 - BCrypt\r\n[ + ] 4 - Clear Text\r\nSelection: ")
	if sel in sel_opts:
		sane = 1
	else:
		os.system('cls')
		print "[ - ] Please enter 1, 2, 3, or 4, for your selection."

if sel == "1":
	sel_type = "srcMD5"
if sel == "2":
	sel_type = "srcSHA1"
if sel == "3":
	sel_type = "srcBCRYPT"
if sel == "4":
	sel_type = "clearTextP"

print "[ - ] Please enter delimiter:"
deli = raw_input("[ + ]: ")
print "[ - ] Please enter absolute path to directory containing dump files:"
in_path = raw_input("[ + ]: ")
print "Is the following information correct?"
print "[ + ] Delimiter: "+deli
print "[ + ] Dump Directory: "+in_path
print "[ + ] Input Type: "+sel_type
print "[ - ] If not, press CTRL+C to stop, otherwise press enter."
raw_input("[ - ] Continue...")

conn = sqlite3.connect(menu())

cnt = 0
cur = conn.cursor()

def is_ascii(s):
	return all(ord(c) < 128 for c in s)

for file in os.listdir(in_path):
	print str(file)
	a = open(in_path+"\\"+file)
	b = a.readlines()
	for item in b:
		item = item.split(deli)
		if len(item) == 2:
			if is_ascii(item[0]):
				if is_ascii(item[1]):
					cur.execute('INSERT into main (identifier, '+sel_type+') VALUES ("'+item[0].strip()+'", "'+item[1].strip()+'")')
					cnt+=1

print "[ + ] "+str(cnt)+" records processed. Press enter to commit to DB."
raw_input("Continue...")
conn.commit()