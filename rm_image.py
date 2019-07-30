#!/usr/bin/env python3
import os

files = ['128x128', '16x16', '256x256', '32x32', '48x48']
filename = 'sublime-text.png'

def fatch_file(file, files):
	for dirctory in iter(files):
		yield f'/usr/share/icons/hicolor/{dirctory}/apps/{file}'

def rm_file():
	for path in fatch_file(file=filename, files=files):
		try:
			os.remove(path)
			print(f"[+] removed this file ==> {path}")
		except FileNotFoundError:
			# file = path.split('/')[-1]
			print(f"[-] Not Found File: {path}")

		except PermissionError as error:
			print(error)
rm_file()