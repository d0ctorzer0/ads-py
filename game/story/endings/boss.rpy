# wow!! SPOILERS!!! my favourite
label day12:
    $ audio_crossFade(2, "music/fourteen.ogg")
    scene mctemproom with fade
    mc "Nothing from Miss Esther..."
    mc "Oh well. I guess I'll see her tomorrow."
    mc "Maybe..."

    n "You throw down your paperwork, exhausted, and fall into your stasis chamber."

    scene black
    with fade
    $ daynum = "12"
    $ dayday = "Friday"

    if renpy.is_skipping() == False:
        show screen daytransition
        $ renpy.pause(2.0, hard=True)
    if renpy.is_skipping() == True:
        pass

    scene mctemproom
    with fade

    jump endtest



























label boss:

    play music boss fadein 0.5

    scene office with fade

    show e annoy with easeinright
    e "Doctor."
    e "I'm sure you're well aware of the warning I gave you a while back."

    show e
    e "\"Don't get too attached to the cores?\""
    e "\"It won't end up well for you?\""
    show e annoy
    e "Any of this ringing any bells?"
    e "Because you didn't heed my advice."
    e "I have an obligation to Aperture. And, personally, I'd like to keep my job."
    e "There is a very, very specific clause in my contract."
    e "It tells me not to let any employee I supervise make a strong emotional connection with any of the cores in my section."
    e "The clause prevents issues with HR."
    e "Don't date your subordinates, doctor. It's as simple as that."
    show e laugh
    e "I mean, God, they're robots! We're robots!"
    e "There are SO MANY HUMANS you could have gone for instead!"
    show e annoy
    e "But no."
    e "You're just like the last employee."
    show e laugh
    e "What is WITH you humans and forming such strong emotional attachments?"
    e "To BARELY ANIMATE OBJECTS, mind you!"
    show e annoy
    e "Oh well. It's none of my concern."
    e "But you..."