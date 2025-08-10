label day10:
    scene mcroom night with fade
    play music fourteen
    n "You enter your room once more."

    menu:
        extend ""
        "I'm gonna miss this place when I leave.":
            pass
        "I'm so excited to use my own bed again.":
            pass
    
    n "You lay down and close your eyes."
    n "Tomorrow's a big day."

    scene black
    with fade
    $ daynum = "10"
    $ dayday = "Wednesday"

    if renpy.is_skipping() == False:
        show screen daytransition
        $ renpy.pause(2.0, hard=True)

    scene mcroom day
    with fade

    n "You wake up at 07:30, groggy and tired. Not a good start to what's probably going to be a long shift."
    n "Almost done with this week..."
    n "You get up, grab your paperwork, and leave for your office."

    scene office with fade
    show e with easeinright
    $ audio_crossFade(2, "music/one.ogg")
    e "Doctor! Good morning. How are you?"

    mc "I'm alright. You seem to be feeling better."

    show e laugh
    e "Yes, much better, haha. Not as tired, for sure!"
    show e
    e "Alright - you know the drill. Today's the one-on-one observation day."
    if not positive["Kris"] and not positive["Heath"] and not positive["Aspen"] and not positive["CC"] and not positive["Rob"]:
        show e annoy
        e "Unfortunately, every single one of the cores under our section has specifically requested -"
        e "- either to me, or to HR -"
        e "- that you don't oversee them today."
        show e laugh
        e "I don't know what you did to cause that, but..."
        show e
        e "I'm going to put you with CC today. Since he doesn't have a job to maintain, the shift should go by quickly."
        show e annoy
        e "Just try not to be too bothersome to him, alright?"
        show e
        e "Have a good shift, Doctor."

        jump unlikableday10
    else:
        e "Who are you interested in overseeing?"
    
        jump day10choice

default krischooseagain = False
default heathchooseagain = False
default aspenchooseagain = False
default ccchooseagain = False
default robchooseagain = False

label day10choice:
    menu:
        extend ""

        "Kris." if krischooseagain == False:
            if positive["Kris"] == False or romance_points["Kris"] <= 5:
                $ krischooseagain = True
                show e annoy
                e "Unfortunately, Kris has requested you not supervise him today."
                show e
                e "You'll have to choose again."
                jump day10choice
            else:
                $ romance_points["Kris"] += 3
                $ esther_affection -= 1
                jump krisday10

        "Heath." if heathchooseagain == False:
            if positive["Heath"] == False or romance_points["Heath"] <= 5:
                $ heathchooseagain = True
                show e annoy
                e "Heath has specifically requested you not supervise her alone."
                show e
                e "You'll have to choose again."
                jump day10choice
            else:
                $ romance_points["Heath"] += 3
                jump heathday10

        "Aspen." if aspenchooseagain == False:
            if positive["Aspen"] == False or romance_points["Aspen"] <= 5:
                $ aspenchooseagain = True
                show e annoy
                e "I'm afraid Aspen contacted HR and asked that you not oversee them today."
                show e
                e "You'll have to choose again."
                jump day10choice
            else:
                $ romance_points["Aspen"] += 3
                jump aspenday10
        "CC." if ccchooseagain == False:
            if positive["CC"] == False:
                $ ccchooseagain = True
                show e annoy
                e "CC asked me personally not to see you today, Doctor. I'm sorry."
                show e
                e "You'll have to choose again."
                jump day10choice
            else:
                $ romance_points["CC"] += 3
                jump ccday10
        "Rob." if robchooseagain == False:
            if positive["Rob"] == False or romance_points["Rob"] <= 5:
                $ robchooseagain = True
                show e annoy
                e "Rob asked me not to let you in the gym today, for some reason."
                show e
                e "You'll have to choose again."
                jump day10choice
            else:
                $ romance_points["Rob"] += 3
                jump robday10

label krisday10:
    show e annoy 
    e "I don't know how you can stand to be around that man..."
    show e
    e "None of my concern, though!"
    e "I'm sure you remember your way to the conference room - it's just right around the corner, after all."
    e "Have a good shift, Doctor."

    mc "Thank you, Miss Esther."

    scene krisroom
    with fade
    n "You enter the conference room. Kris turns to you."
    $ audio_crossFade(2, "music/two.ogg")
    jump krisconfession

label krisconfession:
    $ gotconfession = True
    show k flirt with easeinright
    k "Doctor... hello."

    mc "Uh... hello, Kris."

    show k
    k "I'm glad you chose to supervise me today. I was... nervous. You wouldn't."

    mc "Ha. You. Nervous."

    show k flirt
    k "I can be."
    show k
    k "I was still surprised when Miss Esther sent me the message."
    k "But... glad."

    mc "Is that so?"
    show k flirt
    k "Why yes. I do enjoy your company, you know."
    k "I wouldn't be... treating you like I have recently, if I didn't."
    show k look
    k "...I'm a little anxious today."

    mc "You're okay, Kris."

    show k flirt
    k "Listen... I have something to ask you, Doctor."
    k "And it's not what you think it is."

    mc "It isn't?"

    show k angry
    k "Well, I'm actually not quite sure, but..."
    k "...you might..."

    show k flirt
    n "He sighs."

    k "Whatever."
    $ cutscenetextbox = True
    $ cutscenechoice = True
    show screen cuttextbox
    scene kris cutscene 3 with fade
    python:
        if persistent.kc3 == False:
            persistent.cutscenes_seen += 1
            persistent.kc3 = True
        achievement.progress("ach_picture", persistent.cutscenes_seen)
        achievement.sync()
    if persistent.advcap == True:
        "{color=#fff}{i}The scene fades to Kris looking down, offering you a silver watch in a blue box."
    k "{color=#fff}This... is for you. It's a watch."
    k "{color=#fff}Obviously."
    k "{color=#fff}A few years ago, when I was still a consultant, I won employee of the month in my department."
    k "{color=#fff}The prize for it was a watch."
    k "{color=#fff}I told them, \"I don't have wrists - what am I supposed to do with this?\""
    k "{color=#fff}Well. Now I know."
    k "{color=#fff}I've... really been enjoying your company lately, Doctor, and I..."
    k "{color=#fff}Don't want it to end. Anytime soon."
    k "{color=#fff}Your time in Maintenance may be coming to an end, but..."
    k "{color=#fff}I hope our relationship won't."
    menu:
        extend ""
        "I feel the same way, Kris.":
            $ lock_kris = True
            k "{color=#fff}Oh, Doctor..."
            k "{color=#fff}I'm so glad."
            jump krisacceptance
        "I'm sorry, but I can't accept this.":
            jump krisrejection

label krisacceptance:
    $ cutscenechoice = False
    hide screen cuttextbox
    scene krisroom with fade
    $ cutscenetextbox = False
    show k look with easeinright
    k "Well then. Ahem."
    show k
    k "Doctor, now that we're... closer..."
    k "I suppose you might want to know some things about me."
    show k flirt
    k "I'm ashamed to admit it, but I do stretch the truth sometimes in terms of my monetary success..."
    show k
    k "I am just a core, after all."
    k "I do own stock, and I am quite financially successful, but most of that interest goes right back into Aperture's pocket..."
    show k angry
    k "So as of right now, I don't have any funds of my own, really."

    mc "That's alright."

    show k look
    k "I don't want to be dishonest with you, Doctor."
    show k flirt
    k "So... what about you?"

    mc "Well, there's not much to say about me, really."
    mc "I'm kind of a homebody... I stay inside a lot."
    mc "I got my degree in engineering about a year ago, and got hired here shortly after."

    show k
    k "That explains your original position in Manufacturing, then."

    mc "Yes. I've always liked engineering."

    show k look
    k "Well, I'm glad you gave Maintenance a fair shot, then."

    show k
    n "The rest of your shift is a little awkward, but nice."
    n "Kris seems incredibly happy..."
    show k flirt
    n "Though he would never let that slip."
    n "You ask him about the watch he gave you."
    show k
    k "I'm not sure of the brand - frankly, I believe Aperture may have made the model, cheap and in-house."
    show k angry
    k "Mr. Johnson would do {i}anything{/i} to save even a penny in the years before his death..."
    k "So it makes sense employee rewards were cut back..."
    show k
    k "I'm surprised I even recieved anything in the first place, haha."
    k "And now it's in your hands."

    mc "I'll treat it well, Kris."

    show k flirt
    k "Hopefully as well as you treat me, aha..."
    show k
    n "Eventually, the time comes for you to leave."
    
    mc "It's almost time for my shift end, Kris. I should be going."
    mc "I'm sure Miss Esther is waiting."

    show k look
    k "Yes, I..."

    menu:
        extend ""
        "(Kiss him.)":
            n "You lean over to him and gently kiss him on the chassis."
            show k angry at bounce
            k "Doctor!"
            show k flirt
            k "W-Well then. Yes, you should be going, I..."
            show k
            k "Ahem. Have a good night."
            mc "You too, Kris."
            n "You finish your checklist quickly and leave the conference room, and Kris, behind."
            jump day10end
        "(Say goodbye.)":
            mc "Goodbye, Kris. I'll see you tomorrow."
            show k
            k "Yes. I'll see you tomorrow, Doctor."
            n "You finish your checklist quickly and leave the conference room, and Kris, behind."
            jump day10end

label krisrejection:
    $ cutscenechoice = False
    hide screen cuttextbox
    scene krisroom with fade
    $ cutscenetextbox = False
    show k look with easeinright
    k "Well then. Ahem. I'm... sorry for assuming things, Doctor."
    k "You can keep the watch. I obviously have no use for it, haha."
    show k flirt
    k "I hope this won't sour your opinion of me."

    mc "No, it's alright, Kris. I understand."
    mc "I'm just..."

    show k
    k "You don't have to explain yourself."
    k "I am aware what I just asked was... a difficult question."
    
    show k look
    n "The rest of your shift is a little awkward, but it goes by quickly."
    n "Kris seems a little uneasy and nervous..."
    show k flirt
    n "Though he would never let that slip."
    n "You ask him about the watch he gave you."
    show k
    k "I'm not sure of the brand - frankly, I believe Aperture may have made the model, cheap and in-house."
    show k angry
    k "Cave would do {i}anything{/i} to save even a penny in the years before his death..."
    k "So it makes sense employee rewards were cut back, as well."
    show k look
    k "I'm surprised I even recieved anything in the first place, haha."

    n "Eventually, the time comes for you to leave."
    
    mc "It's almost time for my shift end, Kris. I should be going."
    mc "I'm sure Miss Esther is waiting."

    show k
    k "Ah, yes. Thank you for your time, Doctor."
    show k flirt
    k "And... for earlier."

    mc "It's okay, Kris."
    n "You finish your checklist quickly and leave the conference room, and Kris, behind."
    jump day10end

label heathday10:
    e "Alright! Should be a fun shift, then, at least."
    e "I'm sure you remember the way to the break room. Have a good shift, Doctor."
    mc "Thank you, Miss Esther."

    scene heathroom with fade
    $ audio_crossFade(2, "music/three.ogg")
    n "You enter the break room to find all the lights turned off - except for one."
    n "The stage is lit up by a spotlight, something you're {i}certain{/i} wasn't there before."

    h "Welcome, ladies and gentlemen..."
    h "Or... well, I guess it's just you, Doctor..."
    h "...to {i}the Magic Core's{/i}, grandest show yet!"

    n "The curtains part slightly and Heath comes rolling out on her management rail."

    show h with easeintop
    h "Doctor! Welcome, welcome! Do I have a surprise for you today..."
    show h sad
    n "She turns down for just a second, seemingly fiddling with something inside her chassis."
    show h laugh
    h "Behold... my magnum opus!"

    $ gotconfession = True
    $ cutscenechoice = True
    show screen cuttextbox
    scene heath cutscene 3 with fade
    $ cutscenetextbox = True
    python:
        if persistent.hc3 == False:
            persistent.cutscenes_seen += 1
            persistent.hc3 = True
        achievement.progress("ach_picture", persistent.cutscenes_seen)
        achievement.sync()
    "{color=#fff}With a sudden explosion of sparkle and feathers, a dove emerges from Heath's chassis."
    "{color=#fff}In its beak, it's holding a perfectly-preserved letter."
    h "{color=#fff}TADA! For you, Doctor - a special letter!"
    h "{color=#fff}You see, this past week and a half has been possibly the most exciting of my life so far..."
    h "{color=#fff}A captive audience! A caring one, at that!"
    h "{color=#fff}Someone who doesn't find my... energy off-putting."
    h "{color=#fff}And so - with this letter - I ask you one simple question, Doctor..."
    h "{color=#fff}Ahem."
    h "{color=#fff}I've enjoyed my time with you... performing, talking, showing off, of course..."
    h "{color=#fff}...and I know, soon, you'll have to leave to go back to Manufacturing."
    h "{color=#fff}My question is... um..."
    h "{color=#fff}...will you please keep coming by to see me, Doctor?"
    h "{color=#fff}I have so many shows I can put on for you, so many things I want to tell you... I..."
    h "{color=#fff}I really, really like you, Doctor. Do you... get what I'm saying?"
    menu:
        extend ""
        "Oh, Heath. I feel the same way.":
            $ lock_heath = True
            h "{color=#fff}Oh, Doctor..."
            h "{color=#fff}Thank you, thank you!"
            jump heathacceptance
        "I can't say I do, Heath. I'm sorry.":
            jump heathrejection

label heathacceptance:
    $ cutscenechoice = False
    hide screen cuttextbox
    scene heathroom with fade
    $ cutscenetextbox = False
    show h with easeinright
    h "I'm so, so glad you do, Doctor."
    show h laugh
    h "Aha... I was worried... I was overstepping my place."
    h "Didn't think you'd take a chance on a core - let alone one as energetic as myself!"

    mc "What can I say? You're entertaining."

    show h
    h "Oh trust me... you haven't seen the half of it."
    show h sad
    h "Though, Doctor... there is something you should know about me... that might affect... this."

    mc "What's up?"

    h "Well - you know how I'm SO GOOD at magic, right?"
    h "Actually performing magic takes a lot of quick-thinking skills, quick movements..."
    h "Stuff a lot of cores can't do with their natural programming."

    show h
    h "When I was being manufactured, the engineers... overclocked my systems."
    h "I'm running about two times as fast as I should be!"
    show h sad
    h "Helps with the magic, but..."
    h "Here, touch me."

    mc "Uh... okay."

    n "You reach out your hand and touch Heath's chassis. It's incredibly warm."

    mc "What the... you're burning up, Heath."

    show h laugh
    h "Haha, yeah, they forgot to account for that... I'm not cooled properly."
    show h
    h "It really isn't an issue - the pain doesn't really bother me at all - but I figured I should let you know."

    mc "The pain?"

    h "Oh, and don't worry about the letter, haha. They were just props! Nothing in the letter."
    show h sad
    h "The dove, though... don't know where she went..."

    show h
    n "The rest of your shift is exciting. Heath's natural charm makes the initial awkwardness fade away fast."
    n "She seems incredibly happy. Moreso than usual, even."

    h "You know - even if you and I are - uh, a thing now..."
    show h laugh
    h "You still don't get to know the secrets behind my tricks!"
    show h
    n "Eventually, the time comes for your shift to end."
    
    mc "Miss Esther is waiting for me, Heath. I should be going."
    
    h "Oh, yes. You should. I wouldn't want to keep you {i}too{/i} long, haha!"
    show h sad
    h "Doctor, I..."
    menu:
        extend ""
        "(Kiss her. Or try, at least.)":
            n "You lean over and gently kiss Heath on the chassis. It's very warm, but it doesn't hurt too much."
            show h laugh at bounce
            h "Oh! Doctor, I - well! Didn't see that one coming!"
            show h
            h "Looks like I'm not the only one full of surprises, haha."
            h "Have a good day, Doctor!"

            mc "You too, Heath. I'll see you tomorrow."

            n "You finish your checklist and head back to the office."
            jump day10end
        "(Say goodnight.)":
            mc "Goodnight, Heath."

            show h
            h "Oh yes! Goodnight, Doctor. I'll see you tomorrow."
            mc "Yes. You will."

            n "You finish your checklist and head back to the office."
            jump day10end

label heathrejection:
    $ cutscenechoice = False
    hide screen cuttextbox
    scene heathroom with fade
    $ cutscenetextbox = False
    show h sad with easeinright
    h "Oh, no worries, Doctor. I'm sorry!"
    h "I must've read things wrong. That's on me."

    mc "It's alright, Heath, I just -"

    show h
    h "No! No need to explain! You're alright, I understand!"
    h "Oh, and don't worry about the letter, haha. They were just props! Nothing in the letter."
    show h sad
    h "The dove, though... don't know where she went..."

    show h
    n "The rest of your shift is pretty normal, all things considered."
    n "Heath's stage presence makes the initial awkwardness fade away fast."

    h "You know - even if I just, like... revealed my heart to you..."
    show h laugh
    h "You still don't get to know the secrets behind my tricks!"
    show h
    n "Eventually, the time comes for your shift to end."
    
    mc "Miss Esther is waiting for me, Heath. I should be going."
    
    h "Oh, yes. You should! Sorry to keep you, Doctor."
    
    mc "Have a good day, Heath. I'll see you tomorrow."

    h "Yes you will!"

    n "You finish your checklist and head back to the office."
    jump day10end

label aspenday10:
    e "Oh, good. I was hoping you'd choose them."

    e "You remember the way - upstairs and on your left."

    mc "Yes. Thank you, Miss Esther."

    e "Have a good shift!"

    scene aspenroom with fade
    $ audio_crossFade(2, "music/four.ogg")
    n "You enter the greenhouse and are immediately greeted by Aspen."
    show a look with easeinright
    a "Doctor! Hello, I, uh..."
    a "Wasn't expecting you today."
    a "And I wasn't... entirely prepared... for you, either."
    show a laugh
    a "Hahaha! Ignore me, I'm alright."

    mc "How are you, Aspen?"

    show a
    a "I'm good. Great, even. You're here. And I..."
    show a look
    a "Well, uh..."
    show a
    n "They sigh."
    show a laugh
    a "I've gotta get over this someday..."
    a "And I'm running out of time to."

    mc "What are you talking about?"

    show a look
    a "Uhh..."

    $ gotconfession = True
    $ cutscenechoice = True
    show screen cuttextbox
    scene aspen cutscene 3 with fade
    $ cutscenetextbox = True
    python:
        if persistent.ac3 == False:
            persistent.cutscenes_seen += 1
            persistent.ac3 = True
        achievement.progress("ach_picture", persistent.cutscenes_seen)
        achievement.sync()
    acg "{color=#fff}This cactus is for you."
    acg "{color=#fff}...You're probably tired of my botany facts, but..."
    acg "{color=#fff}This is a Scarlet Ball Cactus - {i}parodia haselbergii{/i}."
    acg "{color=#fff}S-She's easy to care for, as most cacti are..."
    acg "{color=#fff}...but she reminds me of... you and I."
    acg "{color=#fff}I'm the prickly, hard-to-reach, defensive thorns, but..."
    acg "{color=#fff}You're these beautiful flowers o-on top, bringing light to my darkness."
    acg "{color=#fff}I'm really sorry if this is me being too... forward, but, Doctor..."
    acg "{color=#fff}I-I really like you. A lot. You've brought more to my life than anyone has... than any{i}thing{/i} has, and I -"
    acg "{color=#fff}I hope you accept this token of affection from me, and I..."
    acg "{color=#fff}When you leave, I truly hope you don't forget me."
    menu:
        extend ""
        "I'd never forget you, Aspen.":
            $ lock_aspen = True
            a "{color=#fff}Oh, Doctor, I..."
            a "{color=#fff}Goodness. You're something, alright."
            jump aspenacceptance
        "I can't accept this. I'm sorry.":
            jump aspenrejection

label aspenacceptance:
    $ cutscenechoice = False
    hide screen cuttextbox
    scene aspenroom with fade
    $ cutscenetextbox = False
    show a look with easeinright
    mc "This cactus is beautiful, Aspen. Thank you."

    a "You're welcome, Doctor."
    show a
    a "What are you going to name her?"
    menu:
        extend "" 
        "Gertrude.":
            pass
        "Beatrice.":
            pass
        "Emily.":
            pass
    
    a "That's a great name!"
    show a look
    a "Anyways, Doctor, I'm glad you've been accepting of me, and my... awkward confession here."

    mc "It wasn't awkward. It was cute."

    a "I - uh... please stop complimenting me, I don't know how to handle it, haha..."
    show a 
    a "I'm so happy you don't think I'm weird."
    show a laugh
    a "Being alone in this greenhouse all day, it... doesn't help my anxiety."
    
    show a look
    a "So I'm glad I have you... and I'm so, so lucky."
    show a
    n "The rest of your shift is peaceful. As usual, Aspen talks the majority of the time, rattling off facts about all kinds of plants."

    a "{i}Heliotropium arborescens{/i} has been my most recent study - the garden heliotrope."
    show a look
    a "It has these beautiful flowers that smell like vanilla... or so I'm told. I can't really smell them myself."
    show a
    a "And it's poisonous! That's one thing I love about the plant world..."
    show a laugh
    a "The most beautiful flowers can also be the most deadly!"
    show a
    a "Isn't that interesting?"

    mc "Yes, it is."

    show a look
    a "Sorry, sorry, I'm rambling again, aren't I?"

    mc "Don't stop. I like it."

    a "Oh..."

    show a
    n "Before you know it, the shift has rushed by, and it's almost 16:00."

    mc "Aspen - it's time for me to go. I don't want to, but..."

    show a laugh
    a "Oh no, I understand."
    show a
    a "And, Doctor, I..."
    menu:
        extend ""
        "(Kiss them.)":
            n "You lean over and gently kiss Aspen's chassis, avoiding the moss-covered areas."
            show a look at bounce
            a "O-Oh... Oh my goodness. I... well. Doctor."
            a "That was..."
            a "Well."

            mc "I'll see you tomorrow, Aspen."

            show a laugh
            a "I, uh, yes! I'll see you tomorrow."
        "(Let them get back to work.)":
            a "Have a great night. I'll see you tomorrow."

            mc "See you tomorrow, Aspen."
    
    n "You finish your checklist and leave the greenhouse."

    jump day10end

label aspenrejection:
    $ cutscenechoice = False
    hide screen cuttextbox
    scene aspenroom with fade
    $ cutscenetextbox = False
    scene aspenroom with fade
    show a look with easeinright
    a "O-Oh. I'm sorry for assuming, Doctor, I..."
    a "That's on me."
    a "I hope we can stay... friends?"

    mc "Of course we can, you're alright."

    a "I'm so happy you don't think I'm weird."
    show a laugh
    a "Being alone in this greenhouse all day, it... doesn't help my anxiety."
    
    show a look
    a "So I'm glad you're understanding."
    show a
    n "The rest of your shift is peaceful. As usual, Aspen talks the majority of the time, rattling off facts about all kinds of plants."

    a "{i}Heliotropium arborescens{/i} has been my most recent study - the garden heliotrope."
    show a look
    a "It has these beautiful purple flowers that smell like vanilla... or so I'm told. I can't really smell them myself."
    show a
    a "And it's poisonous! That's one thing I love about the plant world..."
    show a laugh
    a "The most beautiful flowers can also be the most deadly!"
    show a
    a "Isn't that interesting?"

    mc "Yes, it is."

    show a look
    a "Sorry, sorry, I'm rambling again, aren't I?"

    mc "Yes, but it's alright."

    show a
    n "Before you know it, the shift has rushed by, and it's almost 16:00."

    mc "Aspen - it's time for me to go."

    show a laugh
    a "Oh no, I understand."
    show a
    a "Have a good day, Doctor. Thanks for choosing me today."
    a "I'll see you tomorrow."

    n "You finish your checklist and leave the greenhouse."

    jump day10end

label ccday10:
    e "Oh, good. I was hoping you'd pick him."
    show e annoy
    e "I know he's been getting sicker..."
    e "I'm sure he'd love the company."
    show e
    e "I'm sure you remember your way to the residential district."
    e "Have a great shift!"
    mc "Thank you, Miss Esther."

    scene ccroom with fade
    $ audio_crossFade(2, "music/five.ogg")
    n "It takes no time at all to reach CC's room."
    
    if giveccpicture == True:
        n "When you enter, you find him staring at the photo you gave him."
    else:
        n "When you enter, you find him staring out his window once again."
    
    mc "Hello, CC."

    n "He stays turned away from you."

    show c close with easeinright
    c "Hello, Doctor."

    mc "Are you alright?"

    c "Yes. I am. I just..."

    n "He turns to face you."
    show c look
    c "I have something very important to tell you."

    mc "Oh. Alright."

    show c
    
    c "I'm going to phrase it in a particular way, however, as I'm..."
    c "...not sure I have the words otherwise."

    $ gotconfession = True
    $ cutscenechoice = True
    show screen cuttextbox
    scene cc cutscene 3 with fade
    $ cutscenetextbox = True
    python:
        if persistent.cc3 == False:
            persistent.cutscenes_seen += 1
            persistent.cc3 = True
        achievement.progress("ach_picture", persistent.cutscenes_seen)
        achievement.sync()
    c "{color=#fff}I wore apathy like armor..."
    c "{color=#fff}...but cracked every time you looked at me, like I was worth being seen."

    c "{color=#fff}Even now I blame timing."
    c "{color=#fff}As if clocks are crueler than my own hesitation."
    c "{color=#fff}As if... love didn't stand right in front of me -"
    c "{color=#fff}- and wait with open hands -"
    c "{color=#fff}- as mine stayed tucked in pockets."
    c "{color=#fff}I..."
    c "{color=#fff}Doctor, you have been so kind to me over the past week and a half, and I..."
    c "{color=#fff}I've never felt anything like this before."
    c "{color=#fff}I feel... energized. Like I'm truly living, like... there's a light at the end of my tunnel."
    c "{color=#fff}Please, Doctor. When your time in Maintenance ends, I hope our time together won't."
    c "{color=#fff}Please stay by me."
    menu:
        extend ""
        "I will, CC. Always.":
            $ lock_cc = True
            c "{color=#fff}Oh. I..."
            c "{color=#fff}You..."
            n "{color=#fff}He sighs."
            c "{color=#fff}Thank you, Doctor."
            jump ccacceptance
        "This is lovely, but...":
            mc "{color=#fff}...I don't think I can accept this, CC. I'm sorry."
            jump ccrejection

label ccacceptance:
    $ cutscenechoice = False
    hide screen cuttextbox
    scene ccroom with fade
    $ cutscenetextbox = False
    show c look with easeinright
    c "I honestly didn't expect you to... say yes."
    show c
    c "Not only am I a robot, not only am I stuck in this godforsaken room..."
    c "But I'm so horribly sick."
    c "I hope you aren't simply taking pity on me, Doctor."

    mc "Not at all, CC. I do truly enjoy your company."
    
    show c close
    c "Thank you."

    show c
    n "Your shift continues on slowly. You and CC chat gently, pausing occasionally to let him rest."

    c "Life is an... interesting concept to me."
    c "It's not as easily definable as a lot of the scientists here seem to think..."
    c "Me, for example. Am I alive? And on top of that, am I {i}living?{/i}"
    c "Stuck in this room all day..."

    show c look
    c "That's why I find waterfalls so interesting. And sunlight."
    c "Though I've never seen either, they seem to be almost the epitome of what life is..."
    show c close
    c "I do hope I'll get to see them one day."

    mc "I'm sure you will, CC."

    show c
    c "Doctor... one of the reasons I asked you the question... {i}now{/i}..."
    c "When we've just gotten to know each other, I..."
    show c close
    c "I do think my time will be coming to an end soon."
    show c look
    c "I've only been getting worse. There was that one day I felt a little better, but..."
    c "After you put your report in, I think they updated my program."
    show c close
    c "I'm not supposed to die. I'm an experiment, after all. They can't test on me if I'm dead."
    show c
    c "I think they made a mistake, though. Increased the program effectiveness too much."

    mc "Oh, CC... I'm so sorry."

    show c look
    c "That's why I needed you to know how I felt about you."
    c "Before I pass."

    mc "You mean {i}if{/i} you pass."

    show c
    c "I always appreciate your optimism, Doctor."

    n "Before you know it, it's almost 16:00, and it's time to clock out."

    show c close
    c "You should be going, Doctor. Miss Esther is most likely waiting for you."
    mc "Ah. Yes. Thank you, CC."
    show c look
    c "And..."
    menu:
        extend ""
        "(Kiss him.)":
            n "You lean over CC's bed and gently place a kiss on his plates."
            show c close
            c "You... are incredible."
            show c look
            c "Thank you. I... that was lovely."
            c "I'll see you tomorrow."

            mc "Yes, you will."

            n "You finish your checklist and head out of his room."
            jump day10end
        "(Say goodnight.)":
            mc "Goodnight, CC."

            show c
            c "Goodnight, Doctor. Have a good day."
            n "You finish your checklist and head out of his room."
            jump day10end

label ccrejection:
    $ config.allow_skipping = True
    $ cutscenechoice = False
    hide screen cuttextbox
    scene ccroom with fade
    $ cutscenetextbox = False
    show c look with easeinright
    c "It's alright, Doctor. I understand."
    show c close
    c "Please, don't think I will hold animosity towards you because of this."
    show c
    c "I hope we can remain friends, regardless."

    show c
    n "Your shift continues on slowly. You and CC chat gently, pausing occasionally to let him rest."

    c "Life is an... interesting concept to me."
    c "It's not as easily definable as a lot of the scientists here seem to think..."
    c "Me, for example. Am I alive? And on top of that, am I {i}living?{/i}"
    c "Stuck in this room all day..."

    show c look
    c "That's why I find waterfalls so interesting. And sunlight."
    c "Though I've never seen either, they seem to be almost the epitome of what life is..."
    show c close
    c "I do hope I'll get to see them one day."

    mc "I'm sure you will, CC."

    show c
    c "Doctor... one of the reasons I asked you the question... {i}now{/i}..."
    c "When we've just gotten to know each other, I..."
    show c close
    c "I do think my time will be coming to an end soon."
    show c look
    c "I've only been getting worse. There was that one day I felt a little better, but..."
    c "After you put your report in, I think they updated my program."
    show c close
    c "I'm not supposed to die. I'm an experiment, after all. They can't test on me if I'm dead."
    show c
    c "I think they made a mistake, though. Increased the program effectiveness too much."

    mc "Oh, CC... I'm so sorry."

    show c look
    c "That's why I needed you to know how I felt."
    c "Before I pass."

    mc "You mean {i}if{/i} you pass."

    show c
    c "I always appreciate your optimism, Doctor."

    n "Before you know it, it's almost 16:00, and it's time to clock out."

    show c close
    c "You should be going, Doctor. Miss Esther is most likely waiting for you."
    mc "Ah. Yes. Thank you, CC."

    n "You finish your checklist, say goodbye to CC, and leave his room."

    jump day10end

label robday10:
    show e annoy
    e "At least you'll keep him entertained."
    show e
    e "Just try not to yell at him, alright?"
    e "I'm sure you remember the way to the gym."

    mc "I do. Thank you, Miss Esther."

    scene robroom with fade
    $ audio_crossFade(2, "music/six.ogg")
    
    show r with easeinright
    r "Doctor! It's good to see you again."
    r "Glad you chose me for your one-on-one - I promise I won't be too much of an annoyance, haha."
    r "Or I'll try. No guarantees, actually."

    mc "Hey Rob. Good to see you alive and active."

    show r close
    r "As usual!"
    show r
    r "So - come to work out, or..."
    show r close
    r "Actually... there's something I gotta tell ya first, Doc."

    mc "Really?"

    show r
    r "Yeah! And I got somethin' for ya. Come up to my desk real quick."

    n "You approach the gym kiosk."

    $ gotconfession = True
    $ cutscenechoice = True
    show screen cuttextbox
    scene rob cutscene 3 with fade
    $ cutscenetextbox = True
    python:
        if persistent.rc3 == False:
            persistent.cutscenes_seen += 1
            persistent.rc3 = True
        achievement.progress("ach_picture", persistent.cutscenes_seen)
        achievement.sync()
    r "{color=#fff}This is my most prized possession - it's an authentic 1988 Topps baseball card."
    r "{color=#fff}Jose Canseco. The guy on the card."
    r "{color=#fff}It's pretty hard to find baseball cards this far down..."
    r "{color=#fff}This one was given to me by the guy in the position before ya."
    r "{color=#fff}Anyway. I want you to have it now."

    mccut "{color=#fff}Rob... this seems very personal to you."

    r "{color=#fff}Yeah. 'Course it is. That's why I'm giving it to ya."
    r "{color=#fff}It's important to me. Just like... you are."
    r "{color=#fff}Listen, Doc, I ain't gonna beat 'round the bush -"
    r "{color=#fff}I really like you. I haven't felt feelings this strong since my wife left me! Ha!"
    r "{color=#fff}So. Anyway."
    r "{color=#fff}Wanna go out? Y'know... you n' me?"
    menu:
        extend ""
        "You're funny. I'd love to.":
            $ lock_rob = True
            r "{color=#fff}Hell yeah! You're the best, Doc."
            r "{color=#fff}Haha... thank you."
            jump robacceptance
        "I don't think I can accept this.":
            jump robrejection

label robacceptance:
    $ cutscenechoice = False
    hide screen cuttextbox
    scene robroom with fade
    $ cutscenetextbox = False
    show r close with easeinright
    r "Now that you and I are {i}\"official\"..."
    show r
    r "You should prolly know some more about me. And my ex, I guess."

    n "He begins to ramble about his ex-wife, Celine."

    show r angry
    r "She was beautiful, y'know, all orange and stuff..."

    mc "Orange?"

    show r
    r "Yeah, like... well, I dunno."
    r "But she was crazy! Yellin' at me for no reason, and she hated when I watched the game -"
    show r yell
    r "WHAT'S THE BIG IDEA? ARE YOU STUPID? WHY ARE YOU NOT RUNNING?!"
    show r
    r "- AND, to top it ALL OFF, that bitch fuckin' cheated on me."

    mc "That's terrible."

    show r angry
    r "I know, right?! Anyway."

    show r
    r "I'm glad you don't find my... volume too off-putting, haha."
    r "I can be a little much, I'll admit. But I know when to tone it down!"

    mc "Don't worry, Rob. I like you just the way you are."

    show r angry
    r "Jeez, you really know how to flatter a core..."

    show r
    n "The rest of your shift is energizing. Rob talks more about Celine, but he also talks about you, too."

    r "You're really somethin', Doc."

    mc "Something good, I hope."

    r "Ha! 'Course you are."

    show r yell
    n "He'll also randomly yell at the TV occassionally - but you've come to expect that from him."

    show r
    n "Before you know it, it's 16:00, and time to pack things up."

    mc "I have to get going, Rob. But... thank you."

    show r angry
    r "No prob, Doc. And - uh. Before ya go..."
    menu:
        extend ""
        "(Kiss him.)":
            n "You lean over - making sure he's not about to go ballistic at the TV again - and kiss him lightly on the chassis."
            show r yell at bounce
            r "Doc! Jeez!"
            show r
            r "Not that I didn't like it, ya just scared me, I uh... didn't see it comin'."
            r "Haha... thanks. I liked it."

            mc "Good, because I like you."

            n "You finish your checklist and head out for the night, waving goodbye to Rob."

            jump day10end

        "(Say goodnight.)":
            show r
            r "Goodnight. I'll see ya tomorrow, yeah?"

            mc "Of course you will, Rob."

            r "Awesome."

            n "You finish your checklist and head out for the night."

            jump day10end

label robrejection:
    $ cutscenechoice = False
    hide screen cuttextbox
    scene robroom with fade
    $ cutscenetextbox = False
    show r close with easeinright
    r "Ah, no, Doc, it's alright."

    show r angry
    r "I'm aware I'm not for everyone!"
    show r
    r "Hell, that's why I have an ex-wife! Ha!"
    show r angry
    r "Speakin' of..."
    n "He begins to ramble about his ex-wife, Celine."

    show r angry
    r "She was beautiful, y'know, all orange and stuff..."

    mc "Orange?"

    show r
    r "Yeah, like... well, I dunno."
    r "But she was crazy! Yellin' at me for no reason, and she hated when I watched the game -"
    show r yell
    r "WHAT'S THE BIG IDEA? ARE YOU STUPID? WHY ARE YOU NOT RUNNING?!"
    show r
    r "- AND, to top it ALL OFF, that bitch fuckin' cheated on me."

    mc "That's terrible."

    show r angry
    r "I know, right?! Anyway."

    show r
    r "Sorry... went off on another tangent. I meant to say..."
    r "I hope this won't, uh, tarnish our friendship, y'know?"
    r "Hope you still like me alright and all."

    mc "Don't worry, Rob. You're still a good friend to me."

    show r close
    r "Phew! Thank God."

    show r
    n "The rest of your shift is energizing. Rob talks about sports nearly non-stop. You listen patiently."

    r "And in 1977, both the Mariners {i}and{/i} the Blue Jays made their debut..."
    
    n "You don't understand half the stuff he's saying. It doesn't bother you, though."

    show r yell
    n "He'll also randomly yell at the TV occassionally - but you've come to expect that from him."

    show r
    n "Before you know it, it's 16:00, and time to pack things up."

    mc "I have to get going, Rob. But thank you."

    r "No problem, Doctor. I hope you have a good night! I'll see ya tomorrow."

    n "You finish your checklist and head out for the night."

    jump day10end

label unlikableday10:
    scene ccroom with fade
    $ audio_crossFade(2, "music/five.ogg")
    n "It takes no time at all to reach CC's room."
    
    n "When you enter, you find him staring out his window once again."

    show c with easeinright
    n "He turns to face you."
    c "Hello, Doctor."

    mc "Hi, CC."
    c "As I'm sure you're well aware, I asked not to see you today."
    c "I suppose Miss Esther had no other choice."

    mc "That's correct."

    show c close
    c "Unfortunate."
    show c
    c "Please, show me some grace - I'd like silence."

    mc "Okay."

    n "The shift goes by slowly, but nothing bad happens."
    n "Generally CC stays quiet, only mumbling to himself every now and then."
    n "He never talks to you directly."
    n "Eventually, 16:00 comes along."

    show c close
    c "Thank you for the quiet shift, Doctor."
    show c
    c "Have a good day."

    mc "Will do."

    n "You finish your checklist and leave the room."

    jump day10end


label day10end:
    scene office with fade
    show e with easeinright
    e "Doctor! How was your shift?"

    if not positive["Kris"] and not positive["Heath"] and not positive["Aspen"] and not positive["CC"] and not positive["Rob"]:
        "It was okay. Quiet. Boring."

        e "That's understandable. Go ahead and finish your paperwork and check your emails."
    else:
        mc "It was alright. Just like last week's, honestly."

        e "Glad to hear. Go ahead and finish your paperwork and check your emails."

    e "Only two more days to go!"

    mc "Thank you, Miss Esther."

    jump e10first

label endtest:
    "endtest"
    $ MainMenu(confirm=False)