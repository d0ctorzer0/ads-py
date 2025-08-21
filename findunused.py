from os import listdir
from os.path import isfile

#
# UNUSED FILE FINDER
# Lists files that are in audio but aren't called in dialogue.tab
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
    if id not in usedfiles:
        if "_" not in id: continue # _ filters out blooper lines
        if "talk_" in id or "fool_" in id or "win_" in id: continue
        print(id)