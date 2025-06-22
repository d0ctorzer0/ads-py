# wow!! SPOILERS!!! my favourite
default aceending = False
default unlikableending = False
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

    n "You wake up to a strange feeling in the air..."
    
    mc "Something feels off."

    n "Ignoring it, you grab your paperwork and leave your room. Only one more night in here..."

    scene office with fade

    if lock_kris or lock_aspen or lock_cc or lock_gregory or lock_heath or lock_rob or lock_unknown == True:
        jump estherattack
    else:
        jump enddecide_aceorunlikable
    
label estherattack:
    stop music
    stop music1
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
    e "You've become a problem. One I cannot ignore."
    e "I'm... I'm sorry, Doctor."

    jump battle

label enddecide_aceorunlikable:
    $ audio_crossFade(2, "music/one.ogg")
    if positive["Kris"] or positive["Heath"] or positive["Aspen"] or positive["CC"] or positive["Rob"] == 0:
        $ aceending = True
    else:
        $ unlikableending = True
    show e with easeinright
    e "Doctor! I apologize for my absence yesterday..."
    show e annoy
    e "I was trapped in my charging port - a simple code failure - but for {i}some{/i} reason, Repair didn't come by until 6pm..."

    mc "That's annoying."

    show e laugh
    e "Tell me about it!"

    show e
    e "But yes. I apologize."
    e "I do have good news for you though!"
    e "Management contacted me this morning and told me the permanent employee will be starting today."

    mc "What does that mean for me, then?"

    show e annoy
    e "Well, I hate to say, but you'll be on your way back down to Maintenance today."
    show e 
    e "I know it's very short notice, and I'm truly sorry about that, but..."
    e "I'm just following what upper management is telling me."

    mc "No, I understand. I'm sure my coworkers down there will be happy, anyways."

    n "Suddenly, there's a knock on the door."

    show e shock
    e "Oh! That must be her! Sorry, Doctor, but I need you to leave now."
    if aceending == True:
        show e
        e "It was a pleasure to work with you. Truly one of the best employees I've had in a while."
        e "I'll see you around, Doctor."
        jump END_ace
    if unlikableending == True:
        show e
        e "I hope you've enjoyed your time here. I'll see you around."
        jump END_unlikable

label END_ace:
    scene black
    "ace ending"
    $ MainMenu(confirm=False)()

label END_unlikable:
    scene black
    "unlikable ending"
    $ MainMenu(confirm=False)()