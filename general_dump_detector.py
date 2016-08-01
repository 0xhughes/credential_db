import os
from shutil import move
import sys

def menu():
	path = raw_input("Please enter path to input dump directory:\n ")
	out_path = raw_input("Please enter path to output directory:\n ")
	if out_path.endswith("\\") or out_path.endswith("\\\\"):
		pass
	else:
		out_path = out_path+"\\"
		
	if path.endswith("\\") or path.endswith("\\\\"):
		pass
	else:
		path = path+"\\"
		
	if os.path.exists(path) and os.path.exists(out_path):
		pass
	else:
		sys.exit(1)
	return(path, out_path)

	
def main(paths):
	path = paths[0]
	out_path = paths[1]
	delims = ":;+=-|"
	for delim in delims:
		for item in os.listdir(path):
			file = open(path+item, 'r').readlines()
			chk_comp = 0
			chk_len = len(file)
			for line in file:
				if len(line.strip().split(delim)) == 2:
					chk_comp+=1
				if line.startswith("file:") or line.startswith("http") or line.startswith("ed2k") or line.startswith("INFO [") or line.startswith("LIVES =") or line.startswith("END") or line.startswith("BEGIN"):
					chk_comp+=10000
				if "," in line or '"' in line or "'" in line or "\\" in line or "*" in line or "|" in line:
					chk_comp+=10000
				for sect in line.split(delim):
					if " " in sect.strip() or ";" in sect.strip() or ":" in sect.strip():
						chk_comp+=10000
					if len(sect.strip()) == 32 or len(sect.strip()) == 40:
						chk_comp+=10000
			if chk_comp == chk_len or chk_comp == chk_len-1 or chk_comp == chk_len+1:
				if chk_comp > 1:
					move(path+item, out_path+item)
					
main(menu())
