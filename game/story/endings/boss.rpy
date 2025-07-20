# wow!! SPOILERS!!! my favourite
default aceending = False
default unlikableending = False
label day12:
    $ audio_crossFade(2, "music/fourteen.ogg")
    scene mcroom night with fade
    mc "Nothing from Miss Esther..."
    mc "Oh well. I guess I'll see her tomorrow."
    mc "Maybe..."

    n "You throw down your paperwork, exhausted, and fall into your bed."

    scene black
    with fade
    $ daynum = "12"
    $ dayday = "Friday"

    if renpy.is_skipping() == False:
        show screen daytransition
        $ renpy.pause(2.0, hard=True)

    scene mcroom day
    with fade

    n "You wake up to a strange feeling in the air..."
    
    mc "Something feels off."

    n "Ignoring it, you grab your paperwork and leave your room. Only one more night in here..."

    scene office with fade

    if lock_kris or lock_aspen or lock_cc or lock_gregory or lock_heath or lock_rob or lock_unknown:
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
    if esther_affection >= 10:
        jump battleskip    
    e "You've become a problem. One I cannot ignore."
    e "I'm... I'm sorry, Doctor."

    scene black with fade
    $ savequestionpopup = True
    call screen savequestion
    $ savequestionpopup = False
    jump battle

screen savequestion:
    style_prefix "notif"
    add "gui/options/black.png"
    add "gui/overlay/save_popup.png" yalign .5 xalign .5 zoom 1.2

    hbox:
        textbutton "Yes, save my game.":
            text_style "notif" 
            action Show("file_slots", transition=easeinbottom), Play("sound", "sfx/paperopen3.ogg"), Hide("savequestion", transition=fade)
            xpos 600 ypos 640
        textbutton "I like the risk.":
            text_style "notif"
            action Hide("savequestion", transition=fade), SetVariable("savequestionpopup", "False"), Jump("battle")
            xpos 750 ypos 640

label enddecide_aceorunlikable:
    $ audio_crossFade(2, "music/one.ogg")
    if gotconfession:
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
    e "Well, I hate to say, but you'll be on your way back down to Manufacturing today."
    show e 
    e "I know it's very short notice, and I'm truly sorry about that, but..."
    e "I'm just following what upper management is telling me."

    mc "No, I understand. I'm sure my coworkers down there will be happy, anyways."

    n "Suddenly, there's a knock on the door."

    show e shock
    e "Oh! That must be her! Sorry, Doctor, but I need you to leave now."
    if aceending == True:
        jump END_ace
    if unlikableending == True:
        jump END_unlikable

label END_ace:
    show e
    e "It was a pleasure to work with you. Truly one of the best employees I've had in a while."
    show e shock
    e "I'll... miss you. You'll be back to visit, yes?"
    mc "I'll certainly try, Miss Esther."
    show e
    e "Wonderful."
    e "I'll see you around, Doctor."
    scene hall with fade
    n "You enter back out into the hall."
    n "Despite the weirdly... romantic connotation of the cores you encountered, it was fairly uneventful."
    n "Your outlook is bright."
    n "You're glad you got to meet so many... interesting personalities."
    n "You'll definitely be back to visit."

    n "Credits will go here when they're ready."
    python:
        if persistent.endings_got["ace"] == False:
            persistent.endings_count += 1
            persistent.endings_got["ace"] = True
        achievement.progress("ach_seenitall", persistent.endings_count)
        achievement.sync()
        achievement.grant("ach_amoh")
        achievement.sync() 
    $ MainMenu(confirm=False)()

label END_unlikable:
    show e
    e "I hope you've enjoyed your time here. I'll see you around."
    scene hall with fade
    n "You enter back out into the hall."
    n "You hated that."
    mc "Personality cores are so annoying..."
    n "Maybe it's that, or maybe {i}you're{/i} the problem."
    n "Regardless, you can't wait to get back down to Manufacturing..."
    n "...where the cores don't talk back to you."

    n "Credits will go here when they're ready."
    python:
        if persistent.endings_got["unlikeable"] == False:
            persistent.endings_count += 1
            persistent.endings_got["unlikeable"] = True
        achievement.progress("ach_seenitall", persistent.endings_count)
        achievement.sync()
        achievement.grant("ach_unlikeable")
        achievement.sync() 
    $ MainMenu(confirm=False)()

label battleskip:
    show e look
    e "I-I..."
    show e close
    e "I can't, Doctor. I..."
    show e look
    e "You've been so kind to me. More than anyone before you."
    e "My programming is screaming at me..."
    e "To not let you do this. To not let you go."
    show e laugh
    e "Y-You know, if Aperture finds out I'm letting you get away with this, they'll..."
    show e look
    e "They'll..."
    show e close
    n "She sighs."
    show e look
    e "You remember... how I said I have... difficulty connecting with anyone?"
    e "Cores... humans... doesn't matter. It's such a struggle."
    e "And I feel I can be... a bit negative, sometimes."
    show e laugh
    e "There's a reason they called me the Sociopath Core up in Testing! Haha!"
    show e look
    e "Hah..."
    show e close
    e "Y-You should go. Before I can change my mind."
    e "I don't think I could ever hurt my first... true... {i}friend."
    show e look
    e "Doctor. Thank you. And... I'm sorry."
    e "You will not see me again. I-I have to leave, I..."
    e "Please stay safe."
    e "I... care for you."
    hide e with easeoutright
    n "...And she's gone."
    n "You have a deep, nagging feeling you just avoided something horrible."
    n "You take a deep breath."
    n "Your office, once a somewhat calming place, seems so unwelcoming now."
    n "The chairs look uncomfortable. The desks look suffocating."
    n "Would it even be worth finishing your shift now?"
    n "Would Aperture care?"
    n "You decide it's probably best to just lay down for a bit."
    n "You certainly have a lot to think about."

    scene mcroom day with fade
    jump day12endcont

label day12end:
    n "You take a deep breath. The room is a mess of papers and burn marks on the walls."
    n "How you're going to explain this to management, you have no idea."
    n "Still shaking, you gather what's left of your paperwork from off the floor."
    n "You look at the clock."
    n "It would be useless to try to finish your shift as normal now - it's nearly 16:00."
    n "You sigh."
    mc "What the hell."
    n "Defeated, but alive, you stumble your way out of your office and back to your quarters."

    scene mcroom night with fade
    n "Your bed looks so much more unwelcoming now."

    jump day12endcont

label day12endcont:
    if lock_kris:
        mc "I hope Kris is doing better than I am..."
    elif lock_heath:
        mc "I hope Heath is doing better than I am..."
    elif lock_aspen:
        mc "I hope Aspen is doing better than I am..."
    elif lock_cc:
        mc "I hope CC is doing okay..."
    elif lock_rob:
        mc "I hope Rob is doing better than I am..."
    elif lock_gregory:
        mc "I hope Gregory is doing better than I am..."
    elif lock_unknown:
        mc "I hope... whatever his name is... is doing better than I am."
    else:
        "ERROR CODE [[ EBLC ]\nThis is a bug. If you are seeing this text please report it."
    n "Whatever happens tomorrow..."
    n "It's bound to be better than this."

    jump day13