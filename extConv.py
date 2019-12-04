#!/usr/bin/python3
'''
# automate the effect of converting multiple files in a specific directory
# you need ffmpeg installed to run this script
'''
import os
import sys

# TAKE USER INPUT
if len(sys.argv) != 3:
	#print(len(sys.argv))
	print("[~] Usage : python3 extConv.py wav mp3 ")
	print("To convert '.wav' media files into '.mp3' ")
	print()
	exit()

# ASSING USER INPUT INTO VARIABLES
inExt = sys.argv[1]
outExt = sys.argv[2]

# GET THE LIST OF FILES
os.system("ls *.{}|sort -u > /tmp/conv_list.txt".format(inExt))
file_path = '/tmp/conv_list.txt'

musicList = open(file_path, "r")

print("-" * 25)
for musicNames in musicList:
	musicNameStriped = musicNames.rstrip('\n')
	musicNameMultiStripped = musicNameStriped[:-len(inExt)] # STRIP THE LAST CHARACHETER PASSED ON THE LENGHT OF THE EXTENTIONs PROVIDED
	print("[*] Converting : \"{}\" ".format(musicNameStriped))
	print("[*] TO         : \"{}{}\" ".format(musicNameMultiStripped, outExt))
	print("-" * 25)
	os.system("ffmpeg -loglevel panic -i \"{}\" \"{}{}\" ".format(musicNameStriped, musicNameMultiStripped, outExt))

os.system("rm /tmp/conv_list.txt")
