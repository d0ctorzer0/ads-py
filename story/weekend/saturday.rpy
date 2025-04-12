label day6:
    scene mctemproom
    with fade

    n "You enter your room and change into your pajamas."
    n "You reflect back on the past week,"
    menu:
        extend " thinking..."
        "How tiring.":
            pass
        "How interesting.":
            pass
        "How boring.":
            pass
        "How fun!":
            pass
    
    n "You crash into your stasis chamber, ready for what the weekend could bring."

    scene black
    with fade
    $ daynum = "6"
    $ dayday = "Saturday"

    if renpy.is_skipping() == False:
        show screen daytransition
        $ renpy.pause(2.0, hard=True)
    if renpy.is_skipping() == True:
        pass

    scene mctemproom with fade
    n "You wake up at 11:00 today. No need to wake up early."
    n "You get changed, and decide..."
    menu:
        extend ""
        "I'm just going to stay in today.":
            jump stay
        "I think I'll wander the campus.":
            n "You open the door to your room and step outside."
            jump wander

label stay:
    d "Really? You're going to stay in?"
    d "You're staying in today? There's a bunch of stuff we programmed waiting for you outside!"
    d "Lots of dialogue and character interactions and fun stuff!"
    d "You're sure you want to stay in?"

    menu:
        extend ""
        "Yeah. I think so.":
            jump day6stayend
        "Actually... nevermind.":
            d "Good choice."
            n "You open the door to your room and step outside."
            jump wander

label wander:
    scene black with dissolve
    $ renpy.pause(1.0, hard=True)
    scene mapbg with dissolve
    call screen aptmap with easeinbottom

label satoffice:
    $ v_satoffice = True
    scene temphall with fade 
    n "You come up to the office door."
    n "You try to open it, but it's locked."
    n "Miss Esther must've locked it up behind her."
    n "You remember the email that mentioned keeping research supplies \"locked\" over the weekend."

    mc "I guess she took it literally..."

    n "You leave the office behind you."

    jump wander

label satcafe:
    $ v_satcafe = True
    scene tempcafe with fade
    n "You enter the cafeteria. You haven't actually been in here yet."
    n "You've been surviving off old protein bars and granola..."
    n "But it doesn't look like this place has much better."
    n "Gelatin... agar..."

    mc "What is this?"

    n "A weird, half-solid, half-liquid texture you've never seen before greets you at the buffet."

    menu:
        extend " You..."
        "Give it a shot.":
            jump cafejello
        "Pass on it.":
            mc "Not gonna risk it."
            n "You exit the cafeteria before your curiosity gets the better of you."
            jump wander