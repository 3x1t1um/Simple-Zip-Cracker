from zipfile import ZipFile
import sys
import argparse
import os

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('passlist',type=str, help='Set your password list (*.txt)')
	parser.add_argument('zipfile',type=str, help='Set your zip file (*.zip)')
	args = parser.parse_args()
	check(args.passlist, args.zipfile)

def check(passlist, zipfile):
	if os.path.isfile(passlist) & os.path.isfile(zipfile):
		bf(passlist, zipfile)
	else:
		print('[ * ] File Error')
		sys.exit(1)

def bf(passlist, zipfile):
	count = 1
	with open(passlist,'r') as liste:
		for passwd in liste.readlines():
			try:
				zFile = ZipFile(zipfile)
				zFile.extractall(pwd=passwd.replace('\n', '').encode('utf-8'))
				print('\n#=========================================#')
				print('	[ %s ] Password found : %s ' % (count, passwd.replace('\n', '')))
				print('#=========================================#')
				break
			except:
				print('[ %s ] Password failed : %s ' % (count, passwd.replace('\n', '')))
				count += 1


if __name__ == '__main__':
	main()