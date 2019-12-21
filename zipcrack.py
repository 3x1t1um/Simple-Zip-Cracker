# importation of modules
from zipfile import ZipFile
import sys
import argparse
import os

# recover the requested files
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('passlist',type=str, help='Set your password list (*.txt)')
	parser.add_argument('zipfile',type=str, help='Set your zip file (*.zip)')
	args = parser.parse_args()
	check(args.passlist, args.zipfile)

# check if the given files are valid
def check(passlist, zipfile):
	if os.path.isfile(passlist) & os.path.isfile(zipfile):
		bf(passlist, zipfile)
	else:
		print('[ * ] File Error')
		sys.exit(1)

# start brute force
def bf(passlist, zipfile):
	count = 1 # counter
	with open(passlist,'r') as liste:
		for passwd in liste.readlines(): # take all passwords 1 by 1
			try:
				zfile = ZipFile(zipfile)
				zfile.extractall(pwd=passwd.replace('\n', '').encode('utf-8')) # extracting files in the zip
				print('\n#=========================================#')
				print('	[ %s ] Password found : %s ' % (count, passwd.replace('\n', '')))
				print('#=========================================#')
				break # exit
			except:
				print('[ %s ] Password failed : %s ' % (count, passwd.replace('\n', '')))
				count += 1 # update the counter

# run the script
if __name__ == '__main__':
	main()
