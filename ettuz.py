#!/usr/bin/env python3

import zipfile
import sys
import time



try:
	thenga = sys.argv[1]
	if thenga == '-h':
		print("Usage: python3 ettuz.py")
		exit()
except ValueError:
	pass
except IndexError:
	pass


actualzip = input("\033[93mEnter Name(or path) of zipfile to crack: ")
passlist =  input("\033[93mEnter Name(or path) of dictionary file : ")

numofwords = len(list(open(passlist, "rb")))
count = 0

with open(passlist,'rb') as passfile:
	words = passfile.readlines()
	for password in words:
		password = password.strip()

		try:
			with zipfile.ZipFile(actualzip,'r') as my_zip:
				my_zip.extractall('extracted',pwd=password)
				print("\033[1;32m-----------------------------------------------")
				print("       Password Found: --> " + password.decode('utf-8'))
				print("-----------------------------------------------")
				break
		except:
			print('\033[1;31m[{}/{}]  trying: '.format(count, numofwords) + str(password.decode('utf-8')))
			count += 1
			time.sleep(0.0001)




			
