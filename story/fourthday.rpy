label day4:
    scene mctemproom
    with fade

    n "You put in the code to your room and enter it, dropping your paperwork on the floor."

    if wkd3:
        n "You never expected Kris to act so... sensitively. It seemed almost out-of-character."
    if whd3:
        n "You're glad you spent the day with Heath. She kept you entertained."
    if wad3:
        n "You figure you learned more about botany today than you ever did in your schooling years."
    if wcd3:
        n "CC's conversations can get very deep. It gave you a lot to think about."
    if wrd3:
        n "You're exhausted from your shift today, much more than usual. But it feels good."
    else:
        n "You wonder if maybe you should've done something different today, or asked Miss Esther to come with you despite management's wishes."
    
    n "Regardless, you need your rest for tomorrow's shift. You change out of your work attire and lay down for stasis."

    scene black
    with fade
    $ daynum = "4"
    $ dayday = "Thursday"

    show screen daytransition
    $ renpy.pause(2.0, hard=True)

    scene mctemproom with fade

    n "You wake up at 08:00 as usual, get dressed, and head out the door."