label day9:
    n "You enter your chambers for what feels like the 8th time."
    n "...probably because this is the 8th time."

    n "Only 4 more days till you're out of here..."

    menu:
        extend ""
        "I can't wait to go back.":
            pass
        "I don't really want to leave, but...":
            pass
    
    n "You lay down in your stasis chamber for the night and close your eyes."

    scene black
    with fade
    $ daynum = "9"
    $ dayday = "Tuesday"

    if renpy.is_skipping() == False:
        show screen daytransition
        $ renpy.pause(2.0, hard=True)
    if renpy.is_skipping() == True:
        pass

    scene mctemproom
    with fade

    n "You wake up at 07:30, ready for the day."
    n "Well, as ready as you can be."
    n "You get dressed and head out the door."

    scene office with fade
    show e annoy with easeinright
    e "Hello... Doctor."

    mc "Miss Esther? Are you okay?"

    e "Yes, just... incredibly tired."

    mc "How can a core be tired?"

    e "I'm not even sure. I just know I'm exhausted for some reason."
    e "Anyways, let's get started on our shift, Doctor."

    mc "Yes ma'am."

    jump krisday9

label krisday9:
    scene kristemproom with fade
    n "It takes you no time at all to get to the conference room."
    show e annoy with easeinright
    e "Kris, it's time... for your check-in."
    hide e with easeoutright
    show k flirt with easeinright
    k "Er, Miss Esther... is everything alright?"

    mc "She's tired, apparently."

    show e b at bounce
    e "Very much so."
    hide e b 

    show k
    k "Well. I have good news for you, then - everything's running smoothly here."
    k "I don't have anything to report today."
    k "The stock is looking better than ever, and I'm running smoothly as well."
    if romance_points["Kris"] >= 13:
        show k flirt
        k "Do you want to see how smoothly I'm running, Doctor?"
        mc "I-I'm okay. Thank you. Haha."
        show k
        k "Your loss."
        mc "Anyways..."
    if positive["Kris"] == 0:
        jump p_krisday9
    if positive["Kris"] == -1:
        jump n_krisday9

label p_krisday9:
    mc "That's great to hear, Kris. I'm glad things are going well."
    k "As am I."
    if romance_points["Kris"] >= 15:
        k "Doctor, I know you have your one-on-one supervising shift tomorrow, and..."
        show k flirt
        k "...well, I know I can't ask you to choose me, but..."
        k "It would be well in your interest to supervise me tomorrow."
        k "That's all I'll say."
        show e b annoy at bounce
        e "Kris... what are you saying?"
        hide e b 
        k "Nothing, Miss Esther. I apologise."
    k "Always good to see your face, Doctor."
    show k flirt
    k "Sunshine on a cloudy day."
    show k angry
    k "...whatever that means."

    menu:
        extend ""
        "That's sweet of you, Kris.":
            $ romance_points["Kris"] += 2
            $ priority["Kris"] -= 1
            jump p_krisday9neutral
        "You shine quite a bit yourself.":
            $ romance_points["Kris"] += 3
            $ priority["Kris"] += 1
            jump p_krisday9positive

label p_krisday9neutral:
    show k
    k "Well. You should be going. I know you have plenty to do today."
    if romance_points["Kris"] >= 13:
        show k flirt
        k "I hope I see you here tomorrow."
    
    show k
    mc "Goodbye, Kris. I'll see you later."

    n "You check Kris off your list and leave the conference room."

    jump unknownday9

label p_krisday9positive:
    show k
    k "Ah. Ahem. Thank you, Doctor."
    k "It's msot likely because I polished my chassis last night, but..."

    show k flirt
    k "Um. You should be going. I know you have plenty to do today."

    if romance_points["Kris"] >= 13:
        k "I... hope I see you tomorrow."
    
    show k
    mc "Goodbye, Kris. I'll see you later."

    n "You check Kris off your list and leave the conference room."

    jump unknownday9

label n_krisday9:
    mc "I'm glad things are going well. That's good to hear."

    show k flirt
    k "Thank god, right? Now you don't have to check off a different box than usual."
    show k angry
    k "Such an exhausting task."

    show e b annoy at bounce
    e "Now, Kris, just because I'm tired -"
    hide e b 

    show k
    k "I apologize, Miss Esther."
    show k angry
    k "Haha... truly, I do not know what's gotten into me lately."
    k "Forgive me."

    mc "Uh... well, if everything's okay in here, we should probably be going."

    show k
    k "Mmm. That's an excellent idea, Doctor."
    k "Have a good day."

    mc "You too."

    n "You hesitantly check Kris off your list and leave the conference room."

    jump unknownday9

label unknownday9:
    "m"