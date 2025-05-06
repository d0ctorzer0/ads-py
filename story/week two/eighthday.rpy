label day7end:
    scene mctemproom with fade
    n "You enter back into your room."
    n "You weren't out for very long - the clock reads 12:35."
    n "You think back to Miss Esther's warning."
    mc "That was strangely out-of-character for her..."
    n "You shrug it off, for now."

    n "You have to prepare your paperwork for tomorrow."

    $ renpy.pause(1.0)

    n "Before you know it, your eyes are getting heavy."
    n "For a job with not a lot to do, there sure are a lot of emails to respond to..."

    n "You take a breath, mentally prepare yourself to start work again tomorrow, and lay down in your stasis chamber."

    scene black
    with fade
    $ daynum = "8"
    $ dayday = "Monday"

    if renpy.is_skipping() == False:
        show screen daytransition
        $ renpy.pause(2.0, hard=True)
    if renpy.is_skipping() == True:
        pass

    scene mctemproom
    with fade

    n "You wake up at 07:30. It's not so bad this time."
    n "Seems your body is getting used to the new sleep schedule - something it'll regret when you go back to work in Manufacturing."
    