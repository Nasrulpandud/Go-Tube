"""
Go Tube <CLI VERSION>
Original Author		: Nasrulpandud <https://github.com/Nasrulpandud>
Original Project	: https://github.com/Nasrulpandud/Go-Tube 
Forked By		: Dagimal <https://github.com/Dagimal>
Date			: 02-Oct-2021 <HackTober Fest>
"""

import os

def banner():
	print("""
                             
	 _____     _____     _       
	|   __|___|_   _|_ _| |_ ___ 
	|  |  | . | | | | | | . | -_|
	|_____|___| |_| |___|___|___|
	-- YouTube Downloader Toolkit <CLI> --
	Original Author : Nasrulpandud
	Forked By	: Dagimal
""")

def main():
	menu()

def clear():
	os.system('clear')

def menu():
	banner()
	print('		@@@@@@ GO TUBE @@@@@@		')
	choice = input('''
		<<< Main Menu >>>
		[1] Download Videos By URL
		[2] Search Videos By Keyword
		[0] Exit

		Please enter your choice : ''')
	if choice == '1':
		byURL()
	elif choice == '2':
		byKeyword()
	elif choice == '0':
		exit()
	else:
		clear()
		menu()

main()
