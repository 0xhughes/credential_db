import sqlite3
import hashlib
import os
import threading
import sqlalchemy.pool as pool

global pas
global ind2
global sql_thread_pool

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

conn = sqlite3.connect(menu(), check_same_thread=False)
conn.text_factory = str

cur1 = conn.cursor()
cur2 = conn.cursor()
cur3 = conn.cursor()
pcur = conn.cursor()

pcur.execute("PRAGMA cache_size=999999")
pcur.execute("PRAGMA journal_mode=WAL")

d_list = []
in_list = []

def is_ascii(s):
	return all(ord(c) < 128 for c in s)
	
cnt = 0
cnt2 = 0
cnt3 = 0

x = cur1.execute("SELECT * FROM main")

for row in x:
	try:
		if is_ascii(str(row[2])):
			if len(str(row[2])) > 4:
				if len(str(row[6])) > 4:
					pas = str(row[2])
					md5 = str(row[6])
					ind = str(row[0])
					in_list.append(str(ind)+":--:"+str(pas)+":--:"+str(md5))
					cnt2+=1
					if cnt2 % 1000 == 0:
						os.system('cls')
						print "[ + ] "+str(cnt2)+" rainbow table md5s with clear text passes read in..."
	except UnicodeEncodeError:
		pass

def sqlite_connect():
	con = sqlite3.connect(menu(), check_same_thread=False)
	con.text_factory = str
	return con
	
sql_thread_pool = pool.QueuePool(sqlite_connect, max_overflow=20, pool_size=10)

def queryMain(pas, ind2):
	t_conn = sql_thread_pool.connect()
	cursor = t_conn.cursor()
	cursor.execute("UPDATE main SET clearTextP = '"+str(pas)+"' WHERE pri_Index = '"+str(ind2)+"'")
	t_conn.close()

for item in in_list:
	try:
		item = item.split(":--:")
		md5 = item[2]
		ind = item[0]
		pas = item[1]
		while threading.active_count() >= 10:
			c = 1
		if md5 not in d_list:
			y = cur2.execute("SELECT * FROM main WHERE srcMD5='"+md5+"'")
			d_list.append(md5)
			cur3.execute("begin")
			for row2 in y:
				ind2 = str(row2[0])
				query_t = threading.Thread(target=queryMain, args=(pas, ind2, ))
				query_t.start()
				cnt+=1
				if cnt % 10 == 0:
					os.system('cls')
					print "[ + ] "+str(cnt2)+" md5s with cleartext passes read in..."
					print "[ + ] "+str(cnt)+" clear text passes found and added to records."
					print "[ + ] "+str(len(d_list))+" md5s added to list."
					print "[ + ] "+str(cnt3)+" exceptions caught."
	except KeyboardInterrupt:
		print "CTRL+C caught..."
		break
	except:
		cnt3+=1

raw_input("Press enter to commit records...")
conn.commit()