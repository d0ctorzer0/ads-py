import os

#
# AUTOSYNCER (Hell yeah!)
# Devised by Russell's infinite genius.
#
# Instructions:
# - Copy dialogue.tab into old.tab
# - Make changes
# - Extract dialogue
# - Run this file
#
# Note: old.tab and dialogue.tab have to be the same length.
# Only helpful for editing lines, not adding new ones.
#

with open("old.tab") as file:
    oldlines = [line.rstrip() for line in file]

with open("dialogue.tab") as file:
    newlines = [line.rstrip() for line in file]

if len(oldlines) != len(newlines):
    print("Files must be same length")
else:
    for i in range(len(oldlines)):
        oldline = oldlines[i].split('	')
        oldid = oldline[0]

        newline = newlines[i].split('	')
        newid = newline[0]
        
        if oldid != newid:
            os.rename(f"game/audio/voice/{oldid}.ogg", f"game/audio/voice/{newid}.ogg")
            print(oldid, newid)