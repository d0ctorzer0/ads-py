from os import listdir
from os.path import isfile

#
# UNUSED FILE FINDER
#
# Instructions:
# - Update dialogue.tab
# - Run this file
#

filenames = listdir("game/audio/voice/")
filenames.sort()

usedfiles = []
with open("dialogue.tab") as file:
    lines = [line.rstrip() for line in file]
    for line in lines:
        splitline = line.split('	')
        usedfiles.append(splitline[0])

for file in filenames:
    id = file.split('.')[0]
    if id not in usedfiles and "_" in id: # _ filters out blooper lines
        print(id)