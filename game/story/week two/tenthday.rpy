label day10:
    play music fourteen
    n "You enter your room once more."

    menu:
        extend ""
        "I'm gonna miss this place when I leave.":
            pass
        "I'm so excited to use an actual bed again.":
            pass
    
    n "You lay down in your stasis chamber."
    n "Tomorrow's a big day."

    scene black
    with fade
    $ daynum = "10"
    $ dayday = "Wednesday"

    if renpy.is_skipping() == False:
        show screen daytransition
        $ renpy.pause(2.0, hard=True)
    if renpy.is_skipping() == True:
        pass

    scene mctemproom
    with fade

    n "You wake up at 07:30, groggy and tired. Not a good start to what's probably going to be a long shift."