label day6:
    scene mctemproom
    with fade
    play music fourteen

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

    $ audio_crossFade(2, "music/one.ogg")
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

    # BUT I WANT THEM ALL! ACHIEVEMENT
    if romance_points["Kris"] and romance_points["Heath"] and romance_points["Aspen"] and romance_points["CC"] and romance_points["Rob"] >= 10:
        $ achievement.grant("ach_biwta")
        $ achievement.sync()

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
    d "You're staying in today? There's a bunch of stuff I programmed waiting for you outside!"
    d "Lots of dialogue and character interactions and easter eggs and fun stuff!"
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
    if cores_visited < 4:
        stop music
        stop music1
        play music ten
        scene black with dissolve
        $ renpy.pause(1.0, hard=True)
        scene mapbg with dissolve
        call screen aptmap with easeinbottom
    if cores_visited == 4:
        stop music fadeout 1.0
        stop music1 fadeout 1.0
        jump satend

# 💻

label satoffice:
    python:
        v_satoffice = True
        if persistent.visited["office"] == False:
            persistent.places_visited += 1
            persistent.visited["office"] = True
        achievement.progress("ach_explore", persistent.places_visited)
        achievement.sync()
    scene hall with fade
    $ audio_crossFade(1, "music/eleven.ogg") 
    n "You come up to the office door."
    n "You try to open it, but it's locked."
    n "Miss Esther must've locked it up behind her."
    n "You remember the email that mentioned keeping research supplies \"locked\" over the weekend."

    mc "I guess she took it literally..."

    n "You leave the office behind you."

    jump wander

# 🥪

label satcafe:
    $ audio_crossFade(1, "music/eleven.ogg")
    python:
        v_satcafe = True
        if persistent.visited["cafe"] == False:
            persistent.places_visited += 1
            persistent.visited["cafe"] = True
        achievement.progress("ach_explore", persistent.places_visited)
        achievement.sync()
    scene tempcafe with fade
    n "You enter the cafeteria. You haven't actually been in here yet."
    n "Even though Miss Esther mentioned it to you on your first day, you've been surviving off old protein bars and granola..."
    n "It doesn't look like this place has much better."
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

label cafejello:
    n "You pick up a paper cup and a spoon, scooping the weird gloop into it."
    n "You open your mouth and -"
    n "Oh. It's not that bad, actually."
    n "Kind of tastes like strawberries."

    n "You shrug, toss out the cup, and exit the cafeteria."

    jump wander

# 🦠

label biology:
    $ audio_crossFade(1, "music/eleven.ogg")
    python:
        v_biology = True
        if persistent.visited["biology"] == False:
            persistent.places_visited += 1
            persistent.visited["biology"] = True
        achievement.progress("ach_explore", persistent.places_visited)
        achievement.sync() 
    scene bioroom with fade
    n "You come up to the door to Biology."
    n "It's right across the hallway from the greenhouse."
    n "Though you're not allowed in, there's a window on the door you can look through."
    n "Inside, you see what looks like a regular research laboratory - petri dishes, microscopes, test tubes filled with colorful liquids..."
    n "You're glad you don't have to worry about all this."
    n "You leave Biology behind."

    jump wander


label wheatleycameo:
    $ audio_crossFade(1, "music/eleven.ogg")
    python:
        v_wheatley = True
        if persistent.visited["wheatley"] == False:
            persistent.places_visited += 1
            persistent.visited["wheatley"] = True
        achievement.progress("ach_explore", persistent.places_visited)
        achievement.sync() 
    scene door2 with fade
    n "You come up to the large door that reads \"AUTHORIZED PERSONNEL ONLY\"."
    n "From what you've heard, this is where they keep test subjects in stasis."
    n "You open the door."

    scene relaxationcenter with dissolve
    show w with easeinright

    wu "Oh! Hello. What are you doing in here? You're not a test subject."
    wu "This place is kinda off-limits to... normal... people. Or... not {i}normal{/i}, necessarily, or..."
    wu "You know what? Nevermind. It's fine."

    mc "Who are you?"

    w "Oh, me? Ah, yes, name's Wheatley, that."
    w "It's my responsibility here to tend to all these humans in here..."
    w "Not easy, let me tell you, no way, haha."

    w "You, uh... really shouldn't be in here, though."
    w "They might think you're supposed to be on ice right now, and you don't want that, because then they'll..."
    w "Well, yeah."

    mc "Sorry, I was just wandering the facility."

    w "Well, careful you don't wander into an incineration chute! Hahaha."
    w "Okay, go, go, before they find out someone's in here."

    n "You quickly exit the relaxation center."

    jump wander

label manufacture:
    $ audio_crossFade(1, "music/eleven.ogg")
    python:
        v_manufacture = True
        if persistent.visited["manufacture"] == False:
            persistent.places_visited += 1
            persistent.visited["manufacture"] = True
        achievement.progress("ach_explore", persistent.places_visited)
        achievement.sync() 
    scene door2 with fade
    n "You come up to the door that you assume leads to your old workplace."
    n "You don't recognize this entrance, but your office in Manufacturing was on the west side."
    n "What Miss Esther said yesterday is probably correct - Manufacturing is really just that large."
    n "You try to open the door, but it's locked shut for the weekend. No windows to peer into, etiher."
    n "Dejected, you leave Manufacturing behind."

    jump wander

label recovery:
    $ audio_crossFade(1, "music/eleven.ogg")
    python:
        v_recovery = True
        if persistent.visited["recovery"] == False:
            persistent.places_visited += 1
            persistent.visited["recovery"] = True
        achievement.progress("ach_explore", persistent.places_visited)
        achievement.sync() 
    scene bioroom with fade
    n "You come up to the door that reads \"STASIS RECOVERY BAY\" on a plaque next to it."
    n "Not wanting to disturb anything that might be happening inside, you peer through the window."
    n "There's two doctors standing next to a woman with black hair in a ponytail."
    n "They're talking to her. She isn't responding."
    n "It seems like they're inspecting her for testing."
    n "You wonder how many other test subjects are holed up in the Relaxation Center."
    if v_wheatley == True:
        n "When you went inside, it looked like the pods went on forever..."
    n "You leave Recovery behind."
    jump wander






### main characters

## KRIS
label satkris:
    $ audio_crossFade(1, "music/two.ogg")
    python:
        v_kris = True
        cores_visited += 1
    scene kristemproom with fade
    n "You enter into the conference room. Kris is reading something on his screen, and the usual stock market graph is gone."

    mc "How are you, Kris?"

    show k angry with easeinright
    if positive["Kris"] == 0:
        jump satkrispos
    else:
        jump satkrisneg

label satkrispos:
    k "Oh my, Doctor, you caught me off-guard."

    show k
    k "What are you doing here? Doesn't maintenance have weekends off?"

    mc "Yes, we do. I just thought I'd come visit you."

    k "Oh. Well then, welcome in."

    mc "Thank you. How has your day been?"

    k "Fine, so far. Not much to do on my days off, so I like to read."

    mc "What kind of books do you read?"

    show k angry
    k "Mostly philosophy. You humans have some... very interesting ideas about life."
    show k
    k "I was just reading some Camus." #pronounced "cah-moo"

    mc "Camus?"

    k "Absurdist philosopher. 1957 Nobel Prize... his work is an inspiration."
    show k angry
    k "Many can't understand him, or his views."

    show k flirt
    k "I'm sure you could, though, Doctor."
    
    mc "I'd be interested in hearing more, I think."

    show k
    k "Ahem. Well then."

    show k flirt
    $ inv_kris = True
    k "Would you like to join me tonight for dinner in the lounge?"
    k "I may not be able to consume anything, but that would leave me free to tell you more."
    show k
    k "No pressure, of course."

    menu:
        extend ""
        "I'll see if I have time.":
            $ romance_points["Kris"] += 2
            jump satkrispos_pos
        "Probably not. I think I have other plans.":
            $ romance_points["Kris"] -= 2
            jump satkrispos_neg
        "I was going to go see Heath perform, so I might see you there." if inv_heath == True:
            python:
                romance_points["Heath"] += 1
                romance_points["Kris"] -= 1
            jump satkrispos_pos

label satkrispos_pos:
    show k flirt
    k "Wonderful. I'll be there tonight. You can come as well, if you'd like."

    mc "I'll keep that in mind."
    mc "Thank you, Kris."

    show k
    k "Of course, Doctor."
    k "Now, if you don't mind, I should refresh my knowledge for tonight."

    n "You leave the conference room."

    jump wander

label satkrispos_neg:
    show k flirt
    k "No worries. Perhaps another time."
    k "The invite is still open if you decide to change your mind."

    mc "Thank you, Kris."

    show k
    k "Of course, Doctor."
    k "Now, if you don't mind, I would like to get back to reading."

    mc "Ah. Yes. No problem."

    n "You leave the conference room."

    jump wander

label satkrisneg:
    show k angry
    k "Oh. Doctor. What are you doing here?"

    mc "I just figured I'd stop by and say hello."

    show k
    k "I see. You interrupted my reading, Doctor."

    mc "Oh."

    show k angry
    k "I'm not very interested in having company at the moment. I hope you understand."

    show k
    mc "Yes. Alright."

    n "You leave the conference room."

    jump wander

# HEATH
label satheath:
    $ audio_crossFade(1, "music/three.ogg")
    python:
        v_heath = True
        cores_visited += 1
    scene heathroom with fade
    n "You enter into Section C8's break room. An actual human greets you this time."
    cw "Oh, you're that new temp, right?"

    mc "Uh... yes, that's me."

    cw "Cool. Heath's around here somewhere. She's on your route, right?"

    mc "Yeah."

    cw "I'm just about to head out, but she'll be back soon, I think."

    n "He passes by you and leaves the room."
    n "You decide to wait for Heath."

    show h sad with easeinright
    n "It doesn't take long before she bursts into the break room, out of breath."
    n "Or something like that, having no lungs."

    if positive["Heath"] == 0:
        jump satheathpos
    else:
        jump satheathneg

label satheathpos:
    show h
    h "Ahh! Doctor!! Sorry, sorry, uh... one sec."

    n "She's \"breathing\" very heavily."

    show h sad
    h "I was... in a rush... to get back, I was down at the lounge... signing up for tonight, but I..."
    h "...don't... wanna miss... giving a performance in here."

    mc "Tonight? What's tonight?"

    show h
    h "Oh!"
    show h sad
    h "Sorry. I've caught my breath, now."
    show h laugh
    h "You haven't heard? Once a month, they do an open-mic at the lounge downstairs."

    show h
    mc "Open mic? Like, comedy? Or singing?"

    h "Comedy, mostly, although I usually do some of my signature tricks alongside my jokes."

    mc "Aperture? Comedy? I couldn't imagine those two words combined..."

    show h laugh
    h "Ah, yes. It's mandatory, I think, orders from up top or something."

    show h
    h "I know Miss Caroline has put in a lot of employee morale programs, which might have something to do with it..."

    $ inv_heath = True
    show h sad
    h "Anyways, uh, Doctor, you should come watch!"
    show h
    h "It'll be fuuuun!"
    menu:
        extend ""
        "I'll stop in if I have the time.":
            $ romance_points["Heath"] += 2
            jump satheathpos_pos
        "I'm not sure. I might have something else.":
            $ romance_points["Heath"] -= 2
            jump satheathpos_neg
        "I think I'm having dinner with Kris there, so I'll watch you on stage." if inv_kris == True:
            python:
                romance_points["Kris"] += 1
                romance_points["Heath"] -= 1
            jump satheathpos_pos

label satheathpos_pos:
    show h laugh
    h "Great! Yes, I'd love to see you in the audience."

    show h sad
    h "Now, I hate to say goodbye, but I've got to practice my tricks, and you'll be spoiled if you watch!"

    show h
    mc "Oh! Yes, I'll be going."

    n "You leave Heath behind to practice."

    jump wander

label satheathpos_neg:
    show h sad
    h "Oh, yeah, no worries. I'm sure you'll make it if you can!"

    #voice same as last line
    h "Now, I hate to say goodbye, but I've got to practice my tricks, and you'll be spoiled if you watch!"

    show h
    mc "Oh! Yes, I'll let you practice."

    n "You leave the break room behind."

    jump wander

label satheathneg:
    show h sad
    h "Oh... Doctor. You're here."
    h "Isn't... today... your day off?"

    mc "Yes, but I thought -"

    h "I've got to practice for tonight, so... if you could leave, that would be helpful."

    mc "Ah. Yes. Alright."

    n "You leave the break room. Heath seems to be in a bad mood today..."

    jump wander

label satcc:
    $ audio_crossFade(1, "music/five.ogg")
    python:
        v_cc = True
        cores_visited += 1
    scene hall with fade
    n "You make your way through the residential block, towards CC's room."

    if positive["CC"] == 0:
        n "You hope you're not disturbing him."
    
    n "Once you reach his door, you listen closely."
    n "Doesn't seem like there's anyone else in there."
    n "You open the door carefully."

    scene cctemproom with fade
    show c close with easeinright
    c "Mmm... hello?"
    show c
    mc "Sorry, CC, I didn't realize you were sleeping."

    if positive["CC"] == 0:
        jump satccpos
    else:
        jump satccneg

label satccpos:
    $ inv_cc = True
    c "Oh, don't worry, Doctor, I wasn't."
    c "Just closing my optic for a short while, that's all."
    show c look
    c "Isn't Saturday your day off? Why are you here?"

    mc "I just came to see you."

    show c
    c "That's a little silly. You don't have any reports to do today."

    mc "I don't need reports to come visit."

    show c close
    c "Haha... fair enough."

    mc "It must get boring here on the weekends, since your management rail is cut off."

    show c
    c "Yes, very much so."
    show c look

    $ informed_about_canister = True
    c "When I was... first activated, they had a portable rail with everything I needed on it..."
    c "A large canister on the back that my tubes could be inserted into, to sustain me."
    show c
    c "I'm not sure where it went, but... it allowed me to tour the facility, for a short while."

    mc "And you have no idea where they might have taken it?"

    show c close
    c "Oh, it's probably somewhere in the area. Perhaps in a storage unit, locked away..."
    show c
    c "But yes, I'm not entirely certain."

    mc "That's unfortunate, CC. I'm sorry."

    c "No worries, Doctor. I'm fine where I am."
    show c close
    $ renpy.pause(1.0)
    show c look
    c "Doctor... perhaps, could you come back tonight? I may have something for you."
    c "But I need time alone to prepare it."
    menu:
        "I'll see if I can stop by, CC.":
            $ romance_points["CC"] += 2
            jump satccpos_pos
        "I'm not sure if I'll have the time.":
            $ romance_points["CC"] -= 2
            jump satccpos_neg
        "I think I'll be at the lounge tonight, unfortunately." if inv_kris or inv_heath == True:
            $ romance_points["CC"] -= 1
            jump satccpos_neg

label satccpos_pos:
    show c close
    c "I'm glad. Thank you, Doctor."
    show c
    c "Now - you should go. I need to prepare..."

    mc "Oh. Yes. Thank you."

    n "You leave CC behind in his room."

    jump wander

label satccpos_neg:
    show c close
    c "Oh, no. I understand, Doctor."
    show c
    c "I apologize."
    c "Now - I believe I need some rest."

    mc "Oh. Yes. Thank you."

    n "You leave CC behind in his room."

    jump wander

label satccneg:
    show c close
    c "Oh... Doctor. What are you doing here?"

    mc "I just came by to see hello."

    show c close
    c "I'm sorry, but... I'm not sure I want to see you right now."
    c "Please leave."

    mc "Ah... yes. Alright."

    n "You quickly leave CC's room."

    jump wander

label satgreg:
    $ audio_crossFade(1, "music/seven.ogg")
    python:
        v_greg = True
        cores_visited += 1
    scene hall with fade
    n "You approach the sliding door with the label \"EMPLOYEE LOUNGE\"."
    n "This door looks much different from the others - newer, and the label isn't as large."
    n "Gregory said he'd be in here."
    n "You enter."

    scene templounge with fade
    n "The place is vibrant. Soft jazz plays over speakers above you and there are many employees milling about."
    n "The room itself is warm and inviting, gentle wooden brown and deep red brick."
    n "It's nothing like the rest of Aperture. It feels like you've just stepped into a different world."
    n "On your left, a stage with dark blue curtains looms over the lounge."
    if inv_heath == True:
        mc "That's probably where Heath will be performing tonight."
    n "On your right, a bar. Gregory is... \"sitting\" at one of the stools."
    n "You go over to greet him."

    show g with easeinright
    g "Ahh, Doctor! Glad you could make it. Sit down for a bit, yeah?"

    n "You sit down next to him."

    show g look
    g "So... want a drink?"
    g "I don't know what you humans consume, but... I'm guessing it's not lighter fluid."

    mc "No, haha, that would kill us."
    mc "Well. Most of us."

    show g
    g "Well, I think they have a lot to choose from, so..."

    bar "You havin' anything, Doc?"
    menu:
        extend ""
        "I think I'll pass.":
            $ romance_points["Greg"] -= 3
            show g look
            g "Aww, that's a shame. But I guess it's not for everyone."
        "Maybe just... an orange juice?":
            $ romance_points["Greg"] += 3
            bar "The greenhouse doesn't grow oranges. Is apple juice okay?"
            mc "Yes, that's fine."
        "Screw it. Can you make a Cosmo?":
            $ romance_points["Greg"] += 3
            bar "I think so. Gimme a minute."
            mc "Thanks."
    show g
    g "Anyway, the reason I invited you out, uh..."
    show g look
    g "You've probably been hearing some things... from Rob, from Miss Esther..."
    g "That I'm pretending to be something I'm not, I guess?"
    g "And I wanna clear things up."

    mc "Pretending to be something you're not?"

    show g aaa
    g "Yeah! Like, the trench coat, for example, it's..."
    show g look
    g "It's just a fashion statement, y'know? Makes me... stand apart from other cores."
    n "He laughs nervously."
    show g
    g "I-I'm not hiding anything under it. And I'm CERTAINLY NOT three different cores, in secret."
    g "I can uh... I can guarantee you that much."
    show g look
    g "I'm not sure where Rob got that idea from, but..."
    show g
    g "So please, uh..."
    show g look
    g "Don't think I'm weird, Doctor."
    menu:
        extend ""
        "I never thought you were weird, Gregory.":
            $ romance_points["Greg"] += 3
            jump satgreg_pos
        "On the contrary. I think you're interesting.":
            $ romance_points["Greg"] += 3
            jump satgreg_pos

label satgreg_pos:
    show g
    g "O-Oh. That's... that's great to hear. Umm..."
    show g look
    g "So... anyways. What do you like to do... in your free time?"
    show g
    mc "My free time?"
    mc "I don't really have a lot of it..."
    mc "After work, I guess I just go right to bed."
    g "Doesn't maintenance only get off work at 4, though?"
    g "That's still lots of time to do other stuff!"

    mc "I guess. I never really thought about it."
    mc "What about you?"
    show g aaa
    g "Me?! Uh... um. No one's asked me what I like before, so, uh..."
    show g look
    g "I guess I like sports a little. Rob tells me a lot about them, and they seem interesting enough."
    show g
    g "Have you seen Heath's magic tricks? I like those too. Real impressive."
    g "I guess I'm kinda just a people person. In a way. Not to say I'm... people. But."
    show g look
    g "I just... really like getting to know everyone here in Aperture."
    show g
    g "I'm still a fairly new core. I was only activated about a year ago, so... I still got a lot to learn."
    g "And the best way to do that is by meeting new people!"

    mc "That's great, Gregory."

    show g aaa
    g "Oh - wait a minute -"
    if romance_points["Greg"] >= 8:
        $ cutscenetextbox = True
        show screen cuttextbox
        scene gregory cutscene 1 with fade
        python:
            if persistent.gc1 == False:
                persistent.cutscenes_seen += 1
                persistent.gc1 = True
            achievement.progress("ach_picture", persistent.cutscenes_seen)
            achievement.sync()
        n "{color=#fff}Gregory looks down and begins speaking softly."
        g "{color=#fff}No, I need you to go closer!!"
        g "{color=#fff}Less left, more right! Come on!"
        g "{color=#fff}T-They're looking at us, we need to {i}move!{/i}"
        g "{color=#fff}I'm so sorry Doctor, can you give me just a minute?"
        g "{color=#fff}What are you doing down there?! Activate the panel!"
        scene templounge with fade
        hide screen cuttextbox
        $ cutscenetextbox = False
    if romance_points["Greg"] <= 7:
        pass
    show g look at bounce
    n "Suddenly, Gregory lurches closer to you. You back up a bit."
    g "S-Sorry, Doc, hard to... control my speed."

    mc "How {i}do{/i} you move without a management rail?"

    show g
    g "Oh, quite simple really. There's a - uh, a panel below me that I'm connected to. The cart carries me around."
    show g look
    g "The engineers just - forgot to install my rail attachment system, so... they had to make do, y'know?"
    show g
    g "Anyways. I should get going, Doctor. It was nice chatting, and... all that."
    hide g with easeoutright
    n "And with that, he's gone."
    n "You get up and head out of the lounge."

    jump wander

label sataspen:
    $ audio_crossFade(1, "music/four.ogg")
    python:
        v_aspen = True
        cores_visited += 1
    scene aspentemproom with fade
    n "You enter into the greenhouse with caution, making sure no other employees are here to yell at you."
    n "The lights are back to normal, thankfully, and most of the plants look fine."

    n "Aspen's in the corner, meticulously mending to a flowering species."

    mc "Aspen?"

    show a look with easeinright
    show a look at bounce
    a "AAH! Doctor! Oh please, don't scare me like that!"
    show a
    a "I-Isn't today your day off? What are you doing here?"

    mc "I just figured I'd stop by and make sure everything's okay in here now."

    if positive["Aspen"] == 0:
        jump sataspenpos
    else:
        jump sataspenneg

label sataspenpos:
    a "Oh, oh, yes! You must've sent that email to Facilities - everything's back up and running!"

    show a laugh
    a "Thank you, thank you, uh..."

    show a
    a "I'm so sorry. I really didn't expect anyone else to be in here."
    a "I'm the only one that stays over the weekend."

    mc "Really? Doesn't this place take a lot of work to maintain?"

    a "Only when the specimens are constantly being tested on."
    show a look
    a "Over the weekend, none of the scientists are here..."
    a "...and the plants are happy. It's peaceful."
    show a
    a "They have feelings, you know, and - not that I don't get it..."
    a "But sometimes I wish they wouldn't test on them so much."

    mc "I understand."
    if plant == True and aspenknowabtbertha == True:
        mc "I feel like Bertha is trying to tell me things sometimes."
        show a laugh
        a "See, I knew you'd get me."
    if plant == False:
        pass
    show a look
    a "Say, uh, Doctor..."
    a "You normally aren't here when this happens, but..."
    a "We have a sample of dinoflagellates in the lab for the next few days."
    show a
    a "It's a bioluminescent algae - they emit this beautiful blue-green glow in the dark."
    $ inv_aspen = True
    show a look
    a "If you'd like, and you're not busy, would you like to stop by during the artificial night cycle tonight?"
    menu:
        extend ""
        "That sounds beautiful. I'll see if I have the time.":
            $ romance_points["Aspen"] += 2
            jump sataspenpos_pos
        "I'm not sure I'll be able to, Aspen.":
            $ romance_points["Aspen"] -= 2
            jump sataspenpos_neg
        "I think I have plans elsewhere, but we'll see." if inv_kris or inv_heath or inv_cc or inv_rob == True:
            $ romance_points["Aspen"] -= 2
            jump sataspenpos_neg

label sataspenpos_pos:
    show a laugh
    a "Oh, wonderful, wonderful, haha."
    show a look
    a "You should leave now - staying too long could get you in trouble."
    a "I don't want that."

    mc "Oh. Yes, I'll leave."

    show a 
    a "I hope I... I'll see you tonight, Doctor."

    n "You leave the greenhouse and carefully close the door behind you."

    jump wander

label sataspenpos_neg:
    show a laugh
    a "Oh, no worries at all. I get it."
    show a look
    a "There's always another time."

    show a
    a "You should leave now - staying too long could get you in trouble."

    mc "Oh. Yes, I'll leave."

    show a look
    a "I hope I'll see you tonight, Doctor, regardless!"

    n "You leave the greenhouse and carefully close the door behind you."

    jump wander

label sataspenneg:
    show a laugh
    a "Ah, yes. Facilities contacted me personally, so you didn't need to send an email."
    show a
    a "Everything's working fine."
    show a look
    a "I don't think you're approved to be in here off-hours, anyways."

    mc "Oh. Yes, sorry. I'll go."

    show a
    a "Ah, thank you. I'll see you on Monday."

    n "You leave the greenhouse and carefully close the door behind you."

    jump wander

label satrob:
    $ audio_crossFade(1, "music/six.ogg")
    python:
        v_rob = True
        cores_visited += 1
    scene robtemproom with fade
    n "You enter into the gym. There's actually people in here today, one on the treadmill and one on the rowing machine."

    show r with easeinright
    r "Ah, Doc. Happy Saturday. Come to work out?"

    mc "Kind of. I also just wanted to check up on you."

    if positive["Rob"] == 0:
        jump satrobpos
    else:
        jump satrobneg

label satrobpos:
    r "Ah, that's kind of you. 'Specially on your day off - you didn't need to come see me."

    mc "Yeah, but I wanted to."

    show r close
    r "Well, then."
    show r angry
    r "Don't flatter me too much now, haha."

    show r
    r "I'm getting ready for the big game tonight. Been waiting for this one for a long time..."
    r "SuperBowl. Bengals v. 49ers. Technically it aired a few months ago, but..."
    show r angry
    r "Aperture's so far down that I'm getting the programming super late."
    r "Not to mention they don't really... prioritize TV here. Obviously."
    show r
    $ inv_rob = True
    r "Hey... you wouldn't wanna join me for that game, would ya?"
    r "I probably got a chair 'round here somewhere..."
    show r angry
    r "You've seen me yell at the screen all week - now's your chance to join!"
    menu:
        extend ""
        "Sounds like fun. I'll see if I got time.":
            $ romance_points["Rob"] += 2
            jump satrobpos_pos
        "I'm not sure if I could make it.":
            $ romance_points["Rob"] -= 2
            jump satrobpos_neg
        "I think I got other plans, but maybe." if inv_kris or inv_heath or inv_cc or inv_aspen == True:
            $ romance_points["Rob"] -= 2
            jump satrobpos_neg

label satrobpos_pos:
    show r
    r "Killer! Can't wait. It's gonna be great."
    show r yell
    r "HELLO?? ARE YOU EVEN PAYING ATTENTION? WHERE'S YOUR DRIVE?!"
    show r
    r "Sorry, sorry."
    r "Yeah, I hope you'll stop in and watch with me."

    show r angry
    r "Now I hate to do this, but I don't want you distracting the other people here, so..."
    show r
    r "Hop on a machine or head on out."

    mc "Ah, yeah. I have other stuff to do, so I think I'll pass, haha."

    r "Ah, no worries. Catch ya tonight, right?"
    show r angry
    r "Hahaha. Get it? Catch?"
    r "Speaking of -"
    show r yell
    r "CATCH IT! CATCH THE BALL! COME ONNNN, COMMIT, COMMIT!"

    n "Laughing to yourself, you leave the gym behind."

    jump wander

label satrobpos_neg:
    show r
    r "Ah yeah, got other stuff, prolly."
    r "I get it."

    show r angry
    r "My ex said the saaame exact thing before she started CHEATING on me..."
    r "{i}\"Can't come home tonight honey, I've got plans...\"{/i}"
    show r yell
    r "YEAH CELINE?? PLANS WITH JEREMY, HUH?? SCREW YOU, WOMAN!"
    r "EVERYTHING I DID FOR YOU, AND WHAT DO I GET?"

    n "You back out of the gym carefully, leaving him to his ranting."

    jump wander
            
label satrobneg:
    show r angry
    r "Check up on me? Why, have I done something wrong again?"

    mc "No, it's just -"

    r "Listen, Saturday's my busiest day. Still not a lot of people, but more than the usual zero."
    show r
    r "I don't really got time to chit-chat, so -"
    show r yell
    r "KICK IT! KICK IT, WHAT ARE YOU WAITING FOR, YOU HAVE A PERFECT SHOT!"
    show r
    r "- so either you're here to use the machines or not."

    mc "I think I'll just leave, then."

    show r angry
    r "Pfft. Don't blame me when you wither away at 40!!"

    n "You back out of the gym before Rob gets any angrier."

    jump wander

label satunknown:
    $ audio_crossFade(1, "music/eight.ogg")
    python:
        v_unknown = True
        cores_visited += 1
    scene bioroom with fade
    n "You walk down one of the residential block's halls."
    n "The coordinates that core sent you for his \"place\" lead to the end of this hallway."
    n "You reach a door that looks like it's been abandoned for who-knows-how-long."
    n "You knock."
    n "The door slides open and you-know-who greets you."

    if positive["???"] == 0:
        jump satunknownpos
    else:
        jump satunknownneg

label satunknownpos:
    show u upset with easeinright
    u "Who's... who's there?"
    show u
    u "Doc? That you?"

    mc "Yes, it's me. Glad to see you sent the correct coords."

    u "Mmm. Come on in."

    scene unknowntemproom with fade
    show u with easeinright
    u "Welcome to my... humble little abode. Can I get you a drink?"
    n "He wasn't kidding - the closet is unusually large, about the size of a bathroom."
    n "One wall holds a charging port while the other is filled with empty lighter fluid bottles."
    n "The place is a mess."
    n "There's trash on the floor, and dust {i}everywhere.{/i}"
    n "There's also something in the corner."
    n "You cough."
    u "Doc? You alright?"

    mc "Y-Yeah, it's just really dusty in here."

    show u look
    u "S-Sorry, it's been a long time since I've had a human in here..."
    u "I'm not attached to the system, so I can't call for janitors."

    show u
    mc "It's alright. And no, I don't need a drink."
    if v_greg == True:
        mc "I already got one from the lounge."
    else:
        pass
    u "Your loss, kid, but."
    show u look
    u "Thanks for stoppin' in. Long time since I had company."

    if informed_about_canister == True:
        $ cctv = True
        n "You look around the room again. The figure in the corner catches your eye."
        mc "Hey... what's that?"
        show u upset
        u "Oh, that thing? It was stuffed in here when I broke into the place. Weird canister on the back."
        u "When you unfold it, it kinda looks like a wheelchair."
        n "You pick it up and open it. On the back, there's a label - \"C.C.T.V.\""
        show u
        u "CCTV? Like... surveillance system?"

        mc "Same acronym, but I don't think so... mind if I take this?"

        u "Sure, I don't care."

        mc "Thanks."
        n "You set the CCTV outside for now."
    if informed_about_canister == False:
        n "You look around the room again. The shelf catches your eye."
    
    mc "So... lots of lighter fluid, huh?"
    show u look
    u "Uh... yeah. I dunno, I started usin' it, like, I don't know how long ago, but..."
    u "I guess I just never stopped."

    mc "Why do you use it?"

    show u upset
    u "I don't rightly know. I suppose it's 'cuz when I don't drink it every night I start malfunctioning..."
    u "Vision gets all blurry... and I got this pounding pain in my chassis, too..."

    mc "Probably withdrawal symptoms."

    show u
    u "With... huh?"

    mc "You're addicted to the stuff, so your system doesn't know how to function without it."
    mc "You haven't always used lighter fluid, right?"

    if romance_points["???"] >= 7:
        $ cutscenetextbox = True
        show screen cuttextbox
        scene unknown cutscene 1 with fade
        python:
            if persistent.uc1 == False:
                persistent.cutscenes_seen += 1
                persistent.uc1 = True
            achievement.progress("ach_picture", persistent.cutscenes_seen)
            achievement.sync()
        u "{color=#fff}Well... yeah. Back when I was... cleaner, and I... remembered my name..."
        u "{color=#fff}I didn't use it at all..."
        u "{color=#fff}I... miss those days sometimes."        
        u "{color=#fff}I don't really even know who I am now. Or where I am half the time."
        u "{color=#fff}Hell, just yesterday I'd burst into that poor CC's room and I was such a nuisance..."
        u "{color=#fff}But it's hard."
        scene unknowntemproom with fade
        show u with easeinright
        hide screen cuttextbox
        $ cutscenetextbox = False
    if romance_points["???"] < 7:
        show u upset
        u "I... can't remember. I know it wasn't always like this, but..."
        u "I can't think straight much anymore."
    
    mc "I know you're trying. I think you could do it."

    show u
    u "Do what?"

    mc "Quit."

    show u upset
    $ renpy.pause(1.0)
    u "Yeah."

    mc "Thanks for inviting me, but I should really get going."

    show u look
    u "Ah, no, I understand. Have a... good day, Doc. Thanks again for stopping in. And talking to me."

    n "You leave his room and dust yourself off."

    if informed_about_canister == True:
        n "The CCTV is waiting for you here - you almost forgot about it."
        n "You pick it up and take it with you."
        $ achievement.grant("ach_closet")
        $ achievement.sync()
    if informed_about_canister == False:
        pass

    jump wander

label satunknownneg:
    show u upset with easeinright
    u "Doc? Didn't I take away my invite?"

    mc "Yes, but -"

    u "Yes but 'nuthin. Scram. I don't wanna see your face anymore."

    mc "Uh -"
    
    hide u with easeoutright
    n "He slides the door back down in your face."

    mc "Guess that was a waste of time."

    jump wander