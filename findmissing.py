from os import listdir
from os.path import isfile

#
# MISSING FILE FINDER
# Lists files that are called in dialogue.tab but aren't found in audio
#
# Instructions:
# - Update dialogue.tab
# - Run this file
#

filenames = listdir("game/audio/voice/")
audiofiles = []

for file in filenames:
    id = file.split('.')[0]
    audiofiles.append(id)

nonspeaking = ['', 'begmc', 'n', 'mc', 'mccut', 'extend', 'wu', 'w']

with open("dialogue.tab") as file:
    lines = [line.rstrip() for line in file]
    for line in lines:
        splitline = line.split('	')
        id = splitline[0]
        sayer = splitline[1]
        text = splitline[2]
        if sayer in nonspeaking: continue
        if id in audiofiles: continue
        if text == "...": continue
        print(id, sayer)