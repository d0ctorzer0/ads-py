label day2:

    play music fourteen
    scene mcroom night with fade

    n "You arrive at your new quarters. They're humble, really only meant to house you while you sleep and no more."
    n "You sigh."

    mc "What a weird first day..."

    n "You drop off your bag and lay down on your bed, which will wake you up in the morning."
    n "You wonder if this thing actually makes sleep more efficient or not."
    n "With that, you gently close your eyes."

    scene black
    with fade
    $ daynum = "2"
    $ dayday = "Tuesday"

    if renpy.is_skipping() == False:
        show screen daytransition
        $ renpy.pause(2.0, hard=True)
    if renpy.is_skipping() == True:
        pass

    scene mcroom day with fade

    n "You gently wake up and look at the clock. It's 08:00 on the dot."
    n "Groaning, you get up and head towards your office."


    scene office
    with fade
    $ audio_crossFade(2, "music/eight.ogg")

    n "Miss Esther isn't here yet. You organize your files while you wait."
    n "Suddenly, there's a knock on the door."

    mc "Yes? Who is it?"

    u "I'm havin' some trouble here, can't seem to activate these here door mechanisms..."

    n "You get up and go over to the office entrance."

    menu:
        extend ""
    
        "This room is only accessible to maintenance staff.":
            $ romance_points["???"] -= 3
            jump lockout
        
        "I'll open the door, but just this once.":
            $ romance_points["???"] += 3
            jump letin

        "(Stay silent.)":
            $ romance_points["???"] -= 1
            jump silence

label lockout:
    u "Well, y-yeah, but I was thinkin', y'know, you'd make an exception?"

    mc "And why would I do that?"

    u "'Cuz I'm so charmin'?"

    mc "And risk losing my job?"

    u "Alrigh', now, no need to get so serious on me..."

    mc "Get out of here before Miss Esther comes and reprimands you."

    u "I'm goin', I'm goin'."

    n "You scoff and return back to your desk."
    
    jump estherday2

label letin:
    n "You unlock the door using the keypad, and a familiar face comes \"stumbling\" in."

    $ emailfromunknownday2 = True
    show u
    with easeinright
    u "Why hello there, pretty little thing."

    mc "What do you want?"

    u "I jus' wanted to come 'n say hi."

    u "Oh, and also invite you out to my place after work, of course..."

    mc "Haha, and why's that?"

    show u upset
    u "Well, s'not everyday now that a beautiful human like yourself shows their face 'round here."

    show u
    u "I'm takin' a chance while I still got it, now."

    mc "I appreciate the gesture, but I'm very busy. I have a lot of work to get done."

    u "Yea, yea, I know. You scientists are always busy."

    show u look
    n "The core glances around himself nervously."

    show u upset
    u "Listen, I should scram 'fore that little pink core of yours shows up again."

    mc "Miss Esther, you mean?"

    u "Yeah, yeah, her. So. I'll send you a little message tonight."
    show u
    u "Keep an eye on your inbox, yeah?"

    hide u
    with easeoutright
    n "The core gives a little bow and exits the room."

    mc "If nothing else, he's certainly interesting..."

    n "You return back to your desk."

    jump estherday2

label silence:
    n "You stay quiet."

    u "Uhhh... hello?"

    mc "..."

    u "I swear I coulda heard you answer me. I know you're in there."

    mc "..."

    u "Or maybe not..."

    u "Maybe I'll try again later."

    n "You hear the core zoom away from your door. You sigh."

    n "You return to your desk."

    jump estherday2

label estherday2:
    $ audio_crossFade(2, "music/one.ogg")
    n "Just as you sit back down, the door opens and Miss Esther comes barreling in extremely fast."

    show e shock
    with easeinright
    e "Sorry! Sorry I'm late! I got caught up in rail traffic..."

    show e annoy
    n "She shakes her chassis."

    e "You'd think with the increase in robots working at Aperture, they'd at least {i}try{/i} to expand the rail system..."

    show e
    e "Regardless! Welcome back. Since we're a little behind, we should get started right away. Do you have everything you need?"

    mc "Yes, I believe so."

    e "Perfect. Come along, now."

    jump krisday2

label krisday2:
    scene hall
    with fade
    show e
    with easeinright
    n "You and Miss Esther approach the conference room, just as yesterday."

    e "I know maintenance can be a tedious job, but don't get discouraged."
    e "A lot of other employees in this department would kill to have a route like yours."
    show e annoy
    e "Especially considering the majority of personality cores aren't... great."

    scene krisroom with fade
    show screen secretbendy
    $ audio_crossFade(2, "music/two.ogg")
    show k with easeinright
    k "Why hello, and welcome back. I'm assuming your route went well yesterday if you're still here now."

    mc "I'd say so. Any changes in the stock today?"

    show k flirt
    k "Not that I've seen, no. Ever since the new CEO took over, things have mostly been quiet."

    mc "She maintains the finance department well, then?"

    show k
    k "Yes, I'd say so. Smart one, that."

    menu:
        extend ""
        
        "You know, I manage my funds pretty nicely myself.":
            $ romance_points["Kris"] += 3
            jump impresskris2

        "It's pretty easy to not spend recklessly.":
            $ romance_points["Kris"] -= 3
            jump offendkris2
        
        "I agree. She's doing well for the company.":
            $ romance_points["Kris"] += 1
            jump krisday2cont
    
label impresskris2:
    show k flirt
    k "Is that so?"

    mc "Why yes. I watch my spending carefully, especially after the turmoil the company recently went through."

    show k angry
    k "Do you have any investments?"

    mc "Of course. I'm not an idiot."

    show k
    k "That's not what I was implying."
    show k flirt
    k "It's important to invest. I'm glad you see that."

    jump krisday2cont

label offendkris2:
    show k angry
    k "What do you mean by that?"

    mc "The former CEO. His reckless spending put the company deep in the gutter, from what I've been told."

    k "I'm aware, but I don't like your tone."
    k "Finances are not easy to manage."
    show k
    k "The fact you think they are speaks measures about how well you truly manage your own."

    jump krisday2cont

label krisday2cont:
    hide k
    with easeoutright
    show e annoy
    with easeinright

    e "We've really ought to be going, now."

    if romance_points["Kris"] >= 5:
        hide e with easeoutright
        show k flirt with easeinright

        k "I hope I'll see you tomorrow."
        n "Miss Esther rolls her optic."

        hide k flirt with easeoutright

    elif romance_points["Kris"] <= 4:
        hide e with easeoutright
        show k with easeinright

        k "Yes, you have more to attend to."

        hide k with easeoutright

    n "You check Kris off your list and head out."
    hide screen secretbendy
    jump heathday2

label heathday2:
    scene hall
    with fade

    show e annoy with easeinright
    e "Heath likes to show a new \"trick\" every day, so don't be surprised if she tries to do one again."

    mc "Does she actually think what she does is \"magic\"?"

    e "I have no clue. I'm not particularly interested in... uh..."
    e "...getting to know any of them."

    mc "Why not?"

    e "\"Connection\"... it's just not my thing. I don't understand how you humans can do it."

    scene heathroom
    with fade
    $ audio_crossFade(2, "music/three.ogg")

    n "You enter the stage room to find Heath already waiting for you."

    show h with easeinright
    h "Apologies for the delay yesterday, it won't happen again! I'm ready this time!"

    n "You wait with bated breath."

    show h sad
    h "Now... choose a card... any card..."

    show h
    h "Well, any card that I have on me, preferably, but..."

    jump heathmenuday2

label heathmenuday2:
    menu:
        extend ""

        "Heath, I don't really have time for this.":
            $ romance_points["Heath"] -= 3
            jump offendheath2

        "Uhh... the three of clubs?":
            $ romance_points["Heath"] += 3
            jump impressheath2
        
        "Ace of spades." if spades == True:
            $ romance_points["Heath"] += 1
            jump neutralheath

label offendheath2:

    show h sad
    h "Oh. Yeah. You've got important science stuff to get to, huh?"

    mc "Sorry. I just don't really like magic all too much."

    h "That's alright."

    mc "You're doing everything you need to, yes? Keeping morale high and all that?"

    h "I think so."

    mc "Great."

    jump heathday2cont

label impressheath2:

    show h laugh
    h "Is {b}THIS{/b} your card?"

    n "She pulls out exactly what you thought of - the three of clubs."

    show h
    mc "Wow! Yes, that's exactly it! Amazing."

    h "Hahaha, thank you, thank you very much."

    show e b annoy at bounce
    n "Miss Esther groans."
    hide e b annoy

    h "Is your morale improved? Your spirits lifted?"

    mc "Definitely. And on top of that, I'm impressed, too."

    show h sad
    h "O-Oh, really? It's nothing, honestly, haha."

    mc "Everything's alright here? Everything working fine?"

    show h
    h "Job's proceeding as normal. No complaints!"

    show h laugh
    h "From me, or your coworkers! Haha!"
    jump heathday2cont

label neutralheath:
    $ spades = False
    show h sad
    h "Oh, um, actually, I don't have that card with me. Can you... choose again?"

    jump heathmenuday2

label heathday2cont:
    hide h with easeoutright
    n "You check Heath off your list. Aspen is next."

    show e annoy with easeinright
    e "I hope that disgusting core we saw yesterday doesn't make another appearance..."

    scene hall
    $ audio_crossFade(2, "music/eleven.ogg")
    with fade

    n "You and Miss Esther make your way over to the greenhouse."
    show e annoy with easeinright
    n "She looks annoyed."

    menu:
        extend ""

        "(Ask her what's wrong.)":
            $ esther_affection += 1
            jump whatswrong

        "(Stay quiet.)":
            n "You decide to stay quiet. Eventually, you reach the greenhouse."
            show e
            e "Go on, now."
            n "You enter the greenhouse."
            jump aspenday2

label whatswrong:
    $ askestherday2 = True
    mc "What's up, Miss Esther? Is something wrong?"

    show e
    e "Hmm? Oh, nothing, nothing. Just thinking about work."

    show e annoy
    mc "Do you not like your job?"

    e "No, don't get me wrong, I do. It's just tedious."
    e "I used to work in Testing, you know."
    
    mc "Testing?? That's, like, top-level work. Why'd they move you down here?"

    e "Budget cuts, basically. Testing isn't half the program it used to be."
    
    show e laugh
    e "Wayyy back in the early days of Aperture, from what I've heard, we used to test on olympians and astronauts and..."

    show e annoy
    e "...y'know, the best of the best."
    e "Then the 70's hit. And the funds started running low."
    e "And..."

    show e
    e "Oh look, we're here. Go on in, now. I'm sure Aspen needs a check-up."

    n "You decide not to question her further. You enter the greenhouse."

label aspenday2:

    scene aspentemproom with fade
    $ audio_crossFade(2, "music/four.ogg")
    n "Once again, you are taken aback by the sheer number of plants in the greenhouse."

    n "Aspen greets you happily."

    show a with easeinright
    a "Welcome back, welcome back."

    mc "Everything's still alright in here?"

    show a laugh
    a "Yep! Pretty as a picture. No issues with my sprinkler, either."

    mc "How come I haven't seen any other humans in here?"

    show a look
    a "They really only come in the evening to do their experiments."
    a "Sometimes when I come in the next morning, plants are missing or mutated or..."
    a "...then there was that one time with the potato battery..."

    menu:
        extend ""

        "Sounds like they keep you pretty busy.":
            $ romance_points["Aspen"] += 2
            jump impressaspen2

        "Don't they have more important things to do than playing with children's toys?":
            $ romance_points["Aspen"] -= 4
            jump offendaspen2

        "You know, I have my own plant that I take care of, too." if plant == True:
            $ romance_points ["Aspen"] += 4
            jump bertha

label impressaspen2:
    show a
    a "Yes, very busy. Thankfully, I love botany. And I love my job."

    mc "Well, you know what they say. If you love what you do, you'll never work a day in your life."

    show a laugh
    a "No, I didn't know that. But now I do! And I love that!"

    if romance_points["Aspen"] >= 4:
        jump aspenfunny
    else:
        mc "I should probably get going, now. Miss Esther's waiting."
        show a
        a "Alrighty. Have a good day."
        jump aspenday2cont

label offendaspen2:
    show a look
    a "Children's toys?! Potato batteries are incredibly important to science, you know."
    a "First of all... well, yes, they're good for teaching children. But on top of that!"

    show a
    a "It's a beautiful fusion of electronics and botany. Just like me."

    mc "Uh-huh."

    show a look
    a "You just don't get it. You're just like the last guy."

    mc "I should be going."

    a "Yes. You should."
    jump aspenday2cont

label bertha:
    $ aspenknowabtbertha = True
    show a laugh
    a "WHAT? No way! What type is she?"

    mc "She's a snake plant named Bertha."

    show a look
    a "Snake plants? I think we had those a while back."
    show a
    a "That's wonderful. How does she survive this far down? There's sunlight down in the offices?"

    mc "I think they pump it in from the surface, like how they do in here."
    a "That's amazing."

    if romance_points["Aspen"] >= 4:
        jump aspenfunny
    else:
        mc "I should probably get going, now. Miss Esther's waiting."
        a "Alrighty. Have a good day! Say hi to Bertha for me."
        mc "I will."
        jump aspenday2cont

label aspenfunny:
    a "Haha. You're great. Better than the last guy."

    mc "What was wrong with the last guy?"

    show a look
    a "He just... didn't really {i}get it{/i}, y'know? Thought plants were stupid."
    a "And me. He thought I was stupid, too."

    mc "That's horrible."

    show a laugh
    a "Tell me about it!"
    a "But you're here now, and you're so much better."

    mc "That's sweet of you."

    show a look
    a "Well... uh, ahem. You should get going. Miss Esther is waiting. Probably."

    mc "Yes. You're right."

    jump aspenday2cont

label aspenday2cont:
    n "You check Aspen off your list and exit the greenhouse."

    scene hall with fade
    show e with easeinright
    e "I hope everything went well in there. We should get back on track towards CC, now."

    mc "Why is CC even alive?"

    show e annoy
    e "What do you mean?"

    mc "Sorry. Why did they make him? Or even... how?"
    show e
    e "I couldn't say. I'm not an expert on the way you humans think, but I have seen Aperture do many things over the years."
    e "I'm still fairly sure we've got about 10,000 test subjects on ice in the basement, still."

    mc "Really? I thought that was just a myth."

    n "You continue down the hallway towards CC. No interruptions so far..."
    jump ccday2

label ccday2:
    scene ccroom with fade
    $ audio_crossFade(2, "music/five.ogg")
    show c close with easeinright

    c "Welcome back, Doctor. How have your rounds been?"

    mc "They've been alright. Nothing crazy."

    c "I'm glad. An easy day is a good day."

    mc "Are you still feeling... sick?"

    show c
    c "Haha. Yes."

    menu:
        extend ""
        "Is there anything I can do to help?":
            $ romance_points["CC"] += 3
            jump impresscc2
        "Alright. That's all I needed to know.":
            $ romance_points["CC"] -= 3
            jump offendcc2

label impresscc2:
    show c look
    c "I appreciate the offer, Doctor, but there's really nothing for me."

    show c
    c "You could unplug me. That would kill me faster."

    show e b sad at bounce
    e "I'm afraid not, CC. Goes against our contract."
    hide e b

    show c close
    n "CC coughs harshly."
    
    show c
    c "It's alright, I understand. Thank you, regardless."

    mc "Please let me know if there's anything I can do."
    
    hide c with easeoutright
    n "You check CC off your list and solemnly leave the room."

    jump ccday2cont

label offendcc2:
    hide c with easeoutright
    show e annoy with easeinright
    e "Let's go."

    jump ccday2cont

label ccday2cont:
    scene hall with fade
    
    n "As you close the door to CC's room behind you, you glance around."
    n "No sign of that strange figure from yesterday, thankfully."

    show e with easeinright
    e "Time for our last stop of the day."

    mc "It feels like this route's gone a lot quicker than yesterday's."

    show e annoy
    e "Yes, most likely because we haven't had any unnecessary interruptions."

    n "The two of you head off towards the gym."

    jump robday2

label robday2:
    scene robtemproom with fade
    $ audio_crossFade(2, "music/six.ogg")
    show r with easeinright
    r "Welcome back, welcome back, doctor. Interested in a run on the treadmill today?"

    mc "Maybe another time. Any visitors today?"

    r "Well, yes, actually - Dr. Pierce came in earlier today, said he had a dream he needed to exercise more? Or somethin'..."
    show r angry
    r "He's kind of crazy, not gonna lie."

    show e b at bounce
    e "Working in neurology will do that do a person."
    hide e b

    r "I am having some trouble with my equipment, though. Rowing machine's busted."
    r "Come to think of it, it was prolly busted yesterday and I just forgot to mention it."

    menu:
        extend ""
        "That's definitely an issue. I'll get that fixed right away.":
            $ romance_points["Rob"] += 3
            jump impressrob2
        "If no one's using it, why bother fixing it?":
            $ romance_points["Rob"] -= 3
            jump offendrob2
        "I'll put in a work order tonight.":
            r "Thanks. I'd do it myself, but, uh... I don't think I know how."
            mc "No issues."
            jump robday2cont

label impressrob2:
    show r
    r "Ahh, thank you. Sometimes it feels like half the machines in here are broke due to, uh, lack of use."

    n "Rob suddenly looks at the screen above him."

    show r yell
    r "AH, DAMN YOU! LOST THE BALL AGAIN?"

    show r angry
    mc "You really like sports, don't you?"

    show r
    r "Uh, ahem, yeah. They keep me occupied."
    r "Kinda need it with how lonely it gets in here."
    r "Even when I {i}do{/i} get visitors, they hardly ever talk to me..."
    r "Assholes."

    show e b annoy at bounce
    e "Doctor, we really ought to be going."
    hide e b

    r "Go on - I'll catch you later."

    jump robday2cont

label offendrob2:
    show r angry
    r "That's not very kind. Machines have feelings, too, y'know."
    r "And I think I'd know! I AM one, after all."

    show r yell
    r "I wasn't always a machine, though, I had limbs, once..."

    hide r with easeoutright
    show e annoy with easeinright
    e "No he didn't. That's just a straight-up lie."
    e "Rob, you were manufactured using melted-down turret panels and a lack of hope."
    hide e with easeoutright
    show r with easeinright
    show r angry
    r "Whatever, Essie."

    n "Rob turns to face you."

    show r
    r "She's crazy."

    hide r with easeoutright
    show e annoy with easeinright
    e "Ugh. Let's go, Doctor."

    jump robday2cont

label robday2cont:
    n "You check Rob off your list once more to finish the day off."
    scene hall with fade
    $ audio_crossFade(2, "music/eleven.ogg")
    show e with easeinright
    n "As you leave the gym, Miss Esther turns to you as you begin walking back to your office."

    e "Tomorrow's agenda will be slightly different, so just be prepared for a switch in the routine."

    mc "A switch in the routine? It's only the second day."

    e "Yes, but even temps have to follow the maintenance schedule."

    mc "How will it be \"different\"?"

    e "I'll let you know tomorrow. For now, get some rest."

    jump e2first