label day3:

    play music fourteen
    scene mctemproom
    with fade

    n "You make your way to your quarters. After organizing your paperwork, you lay down in your stasis chamber."
    n "Before you fall asleep, you wonder what Miss Esther meant by tomorrow being \"different\"."

    scene black
    with fade
    $ daynum = "3"
    $ dayday = "Wednesday"

    if renpy.is_skipping() == False:
        show screen daytransition
        $ renpy.pause(2.0, hard=True)
    if renpy.is_skipping() == True:
        pass

    scene mctemproom with fade

    n "You wake up, slowly but surely, and turn to the clock. 08:00, again." 
    n "Work in manufacturing doesn't begin until 11, and it's going to take a bit to get used to this new schedule."
    n "You get up and go towards your office."

    scene office
    with fade
    $ audio_crossFade(2, "music/one.ogg")
    n "Miss Esther is here on time today, and greets you happily."

    show e with easeinright
    e "Hello, Doctor!"

    mc "Hello, Miss Esther."

    e "Today's agenda is very simple."
    e "Once a week, the maintenance employee must spend one full shift with a core under their section, to ensure that work is {i}actually{/i} getting done."
    show e laugh
    e "After all, they {i}could{/i} just pretend to do their job when you come in, and completely ignore their responsibilities otherwise."
    show e
    e "The core that gets overseen changes every week, so it keeps them on alert, so to speak."

    mc "I see. Makes sense."

    show e annoy
    e "In addition, I am not permitted to accompany you today. They'd like to see if you can handle the position without my supervision."
    show e laugh
    n "Miss Esther laughs."
    show e
    e "I think that's ridiculous. Of course you can. I don't see why I shouldn't accompany you, but..."
    e "Policy, I suppose."
    e "Anyway! Which core are you interested in overseeing today?"

    jump day3choice

label day3choice:
    menu:
        extend ""

        "Kris.":
            $ romance_points["Kris"] += 3
            $ esther_affection -= 1
            jump krisday3
        "Heath.":
            $ romance_points["Heath"] += 3
            jump heathday3
        "That core we ran into on my first day." if askforu == False:
            $ romance_points["???"] += 3
            $ esther_affection -= 1
            jump uchooseagain
        "Aspen.":
            $ romance_points["Aspen"] += 3
            $ esther_affection += 1
            jump aspenday3
        "→":
            jump day3choice2

label day3choice2:
    menu:
        extend ""
        "Is CC an option here?":
            $ romance_points["CC"] += 3
            $ esther_affection += 1
            jump ccday3
        "Gregory." if askforg == False:
            $ romance_points["Greg"] += 3
            jump gchooseagain
        "Rob.":
            $ romance_points["Rob"] += 3
            jump robday3
        "←":
            jump day3choice

label uchooseagain:
    $ askforu = True

    show e annoy
    e "Ugh, that thing?"
    e "Unfortunately, I have no idea who he even is, much less what his job is."
    e "I don't even know if he's a core in our section."
    e "I have nothing in my database to allow you to oversee... that {i}thing{/i}, so, no. Choose again."

    mc "Okay, then..."

    jump day3choice

label gchooseagain:
    $ askforg = True

    show e annoy
    e "I'm afraid that Gregory isn't under our supervision. He's technically a Section C7 core, which puts him out of our scope of work."
    e "I'm not even sure what his responsibilities {i}are.{/i}"

    show e
    e "You'll have to pick somebody else."

    mc "Alright, then..."

    jump day3choice

# KRIS
# ======================================
label krisday3:

    show e annoy
    e "Really? That egotistic idiot?"
    e "I suppose it doesn't matter who you pick, as long as I can log it properly."

    show e
    e "I'll put it in my database that you'll be supervising Kris today. Do you remember the way to the conference room?"

    mc "Yes, I do."

    e "Perfect. You should be on your way, then."

    scene kristemproom
    with fade
    $ audio_crossFade(2, "music/two.ogg")

    n "You enter the conference room to see Kris staring at the screen. You can't understand what's happening, but that's his job, not yours."

    mc "Kris?"

    show k with easeinright

    n "Kris turns to face you, smug as ever."
    k "Well, well. Miss Esther sent me a notification that you'd be overseeing my work today."

    mc "Yes, that's right."

    k "Couldn't get enough of my charm, hmm?"

    mc "Haha, very funny."

    show k flirt
    k "Be prepared for a long and boring shift. Watching a screen all day isn't all it's made out to be."

    menu:
        extend ""
        "On the contrary. I'm sure it'll be exciting with you here.":
            $ romance_points["Kris"] += 3
            jump krisday3good
        
        "That's why I chose to oversee you. Not a lot of work to do, and I can just relax.":
            $ romance_points["Kris"] -= 3
            jump krisday3bad

label krisday3good:
    $ goodday3 = True
    $ wkd3 = True
    show k
    k "Me? Exciting? Well now. I try not to be {i}too{/i} exciting."
    show k angry
    k "Especially after the disaster that was our former management."

    mc "What was wrong with the former management?"

    show k
    k "Oh, that's right. Esther did say you were a... newer employee."
    k "You must not have been here when Mr. Johnson was still at the head of the company."

    mc "No, I wasn't. I was part of the first new hire wave about 9 months ago. But I've heard... stories about him."

    k "Mr. Johnson was an... interesting man. You might hear some... {i}lesser{/i} cores refer to him by his first name, \"Cave\"."
    show k angry
    k "I still have some semblance of respect for the man, regardless of his ridiculous financial policies."
    k "He just... did not handle the company very well in terms of our monetary investments."

    mc "Were you working during the time?"

    show k
    k "In a way, yes. I was activated in 1979, but I was originally a consultant. As Mr. Johnson lost more and more employees due to mandatory testing, he began replacing them with... us."
    k "That's why there's so many personality cores around now. We're... remnants."

    show k angry
    k "The man never stopped spending Aperture's money. And it led him to his death."

    mc "You seem bitter about it, still."

    show k
    k "Hmm. I suppose I am. I enjoyed my consulting work. After Miss Caroline took over as CEO, a lot of things happened."
    k "Projects got shut down. Employees were fired. Personality cores became... less important."

    # FIRST KRIS CUTSCENE HERE!! YAY!!
    if romance_points["Kris"] >= 7:
        $ cutscenetextbox = True
        show screen cuttextbox
        scene kris cutscene 1 with fade
        $ persistent.kc1 = True
        if persistent.advcap == True:
            "{color=#fff}{i}The scene fades to Kris looking down solemnly."
        k "{color=#fff}I'm stubborn for that reason."
        k "{color=#fff}My job is... simple. Perhaps not every personality core can read a stock market graph, but... it's a useless job."

        mccut "{color=#fff}I think what you do is very important."

        k "{color=#fff}Not as important as it should be. Miss Caroline, she..."
        k "{color=#fff}She doesn't trust us. And I'm not sure why."
        k "{color=#fff}She is excellent at what she does. She's dragged Aperture out of the ditch it was in, but..."
        k "{color=#fff}The company now... it's different. Mr. Johnson was fascinated with us. Miss Caroline is not."
        hide screen cuttextbox
        scene kristemproom with fade
        show k
        $ cutscenetextbox = False
        jump krisday3goodpt2
    else:
        jump krisday3goodpt2

label krisday3goodpt2:
    if persistent.advcap == True:
        "{i}The screen fades back to normal."
    k "But that's neither here nor there. I'm satisfied enough with the work I do, regardless of how inconsequential it is."

    mc "I see."

    n "The rest of your shift is uneventful. Kris does his job well enough for your audit on him to pass."

    show k flirt

    n "He flirts with you a little. You feel your face flush."
    n "When your shift is over, you wish it wasn't."

    show k
    k "Ahh, it's 16:00. That's your clock-out time, correct?"

    mc "Yes. I suppose it is."

    show k flirt
    k "Unfortunate. I enjoyed our time today."

    mc "Me too."

    show k
    k "I'll see you tomorrow, yes?"

    mc "Yes. You will."

    n "You finish your checklist, and leave the conference room to head back to your office."

    jump day3end

label krisday3bad:
    show k angry
    k "I see. Well then, I hope you brought some entertainment."
    hide k with easeoutright

    n "Kris turns back to the screen."
    n "Though you try to make conversation with him to pass the time, he either ignores you or brushes you off."
    n "Perhaps you shouldn't have dismissed him so easily."

    n "The time ticks by incredibly slowly, and the graph doesn't change enough to entertain you."
    n "Eventually, it's 16:00, and it's time for you to go."

    n "You finish your checklist and leave the conference room without a word."

    jump day3end

# HEATH
# ======================================
label heathday3:
    e "Well, if anything, at least you'll be entertained."
    e "Truly, it doesn't matter who you pick, as long as they're in my systems."

    e "I'll put it in my database that you'll be supervising Heath today. Do you remember the way to the break room?"

    mc "Yes, I do."

    e "Perfect. On your way, then."

    scene heathtemproom
    with fade
    $ audio_crossFade(2, "music/three.ogg")

    n "You enter the empty break room cautiously. Heath is nowhere to be seen."

    mc "Heath? I'm here."

    n "You hear her voice from behind the curtain."

    h "Uh... yes, yes!! One minute, please. You got here faster than I thought..."

    n "The crashing and rattling taking place doesn't ease your conscience."
    n "Suddenly, Heath whirls out with a puff of smoke, coughing."

    show h sad with easeinright
    h "Ahem. Uh. Sorry, I've been trying to get my next big performance ready."
    h "It's not going so great."

    show h
    h "But anyways! Welcome back! Good to see you."
    h "Miss Esther told me you chose ME, of all cores, to oversee today."

    mc "Yes, that's right."

    show h laugh
    h "Well, you're in for a treat. My whole job is entertainment, so I'll be sure to keep you awake and aware!"
    show h
    h "Don't be surprised if I sweep you off your feet!"

    menu:
        extend ""
        "I'd be surprised if you didn't.":
            $ romance_points["Heath"] += 3
            jump heathday3good
        
        "You've yet to impress me, so I'm interested.":
            $ romance_points["Heath"] -= 3
            jump heathday3bad

label heathday3good:
    $ goodday3 = True
    $ whd3 = True
    show h sad
    h "Oh, haha, that's not what I... {i}expected{/i} you to say..."

    show h
    h "But I'd be thrilled to oblige!! Prepare for the show of your lifetime!"

    hide h with easeoutright
    n "Heath goes back behind her curtain and begins mumbling to herself. Bowling pins and an 8-ball roll out."
    n "You have no idea how she does magic without hands."

    mc "Heath?"

    h "Yes?"

    mc "What's behind that curtain of yours, anyway?"

    if romance_points["Heath"] >= 7:
        h "Oh! Would you like to see?"

        mc "Uhhh... sure, why not?"

        n "Heath parts the curtains."
        $ cutscenetextbox = True
        show screen cuttextbox
        scene heath cutscene 1 with fade
        $ persistent.hc1 = True
        n "{color=#fff}You're stunned by what you see - a hidden-away, wooden room, lined with fairy lights, shelves stocked with magic paraphenalia."
        h "{color=#fff}Tada!! This is my magic room. It's where I keep all the stuff I use to perform my tricks."

        mccut "{color=#fff}Wow, Heath. I can't believe this. It's amazing."

        h "{color=#fff}Yes, yes, I know."
        h "{color=#fff}There's my magic 8 ball, my stuffed rabbit, my bowling pins - for juggling."

        mccut "{color=#fff}You can juggle?"

        h "{color=#fff}Hahaha, no. But you could!"
        h "{color=#fff}I haven't shown anyone else this room, so you should consider yourself lucky!"

        n "{color=#fff}Heath comes back out and closes the curtains."
        scene heathtemproom with fade
        show h with easeinright
        hide screen cuttextbox
        $ cutscenetextbox = False
        jump heathday3goodpt2
    else:
        h "Oh, just some miscellaneous props and such. Nothing too special."
        show h with easeinright
        n "Heath comes back out of the curtains. You try to get a peek at what's behind them, but it's no use."
        
        jump heathday3goodpt2

label heathday3goodpt2:
    n "The rest of the day is exciting. Heath keeps you entertained with plenty of tricks, all which leave you bewildered."
    n "She somehow manages to pull off some of these better than the human magicians you know."
    show h sad
    n "An occasional coworker comes into the break room and watches her, too. They don't seem as into it as they should be, you think."

    show h laugh
    n "You find her inspiring."
    show h
    n "But every show must come to an end, and once hers does, you find yourself disappointed."

    mc "Thank you, Heath. This was great. I had an amazing time today watching you perform."

    h "Thank you, thank you, Doctor. You're the most captive audience I've had in ages!"

    n "She gives you a bow as you finish your checklist and head back to your office."
    hide h with easeoutright
    
    jump day3end

label heathday3bad:
    show h sad
    h "I really haven't impressed you at all??"
    h "I don't even have hands! You're not impressed by that?"

    mc "I don't know. I've seen crazier stuff happen at Aperture."

    h "Oh."

    n "The shift isn't very fun, after that. Heath tends to keep to herself."
    show h
    n "The occasional coworker comes in, and she'll put on a show for them - but generally doesn't speak to you otherwise."
    n "You think you offended her."

    n "The time ticks by incredibly slowly."
    n "Eventually, it's 16:00, and it's time for you to go."
    n "You finish your checklist and leave."

    jump day3end

label aspenday3:
    show e
    e "Good choice. They're a nice kid."
    e "I'm sure they'll appreciate the company."

    e "I'll put it in my database that you'll be supervising Aspen today. Do you remember the way to the greenhouse?"

    mc "Yes, I do."

    e "Good. Off you go!"

    scene aspentemproom
    with fade
    $ audio_crossFade(2, "music/four.ogg")

    n "You enter the greenhouse. Aspen is humming quietly while they water the plants."

    mc "Aspen?"

    n "They jump and spin around rapidly."
    
    show a look with easeinright
    a "Holy Aperture!! You scared me."

    mc "Sorry, sorry. Didn't mean to."

    show a
    a "You're here early..."
    a "Oh! Today's the one-on-one observation day!"

    show a look
    a "Yes, now I see the message Miss Esther sent me about you overseeing me today..."
    show a
    a "Sorry. I can get a little \"in-the-zone\" so to speak, when I'm working."

    mc "You're alright."

    a "So wait, why'd you choose to supervise me? All I do is water plants all day."

    show a laugh
    a "I don't think the last guy {i}ever{/i} chose me on his Wednesdays..."

    menu:
        extend ""
        "Your excitement sparked my interest about Aperture's botany subsection.":
            $ romance_points["Aspen"] += 3
            jump aspenday3good
        
        "I figured my shift would be easy, supervising you.":
            $ romance_points["Aspen"] -= 3
            jump aspenday3bad

label aspenday3good:
    $ goodday3 = True
    $ wad3 = True
    show a
    a "Oh! Well then, I'm happy to oblige. What are you interested in?"

    mc "How many of you are in Botany?"

    show a look
    a "Let me think..."

    show a
    a "I believe there's a total of about 70 of us. That's researchers, scientists, gardeners like me."

    mc "That's not a lot."

    show a laugh
    a "Haha, you're right - it's really not!"
    show a
    a "I kind of like it though. It keeps us accountable. If even one of us falters, the whole team will suffer."

    mc "That's a lot of pressure."

    a "Tell me about it."

    mc "So, uh... do you have a favorite plant? Out of all of these?"

    if romance_points["Aspen"] >= 7:

        show a laugh
        a "Oh yes! Absolutely! Come over here, and I'll show you."

        hide a with easeoutright
        n "You follow Aspen on his management rail as he leads you to a back corner."

        $ cutscenetextbox = True
        show screen cuttextbox
        scene aspen cutscene 1 with fade
        $ persistent.ac1 = True
        if persistent.advcap == True:
            "{i}The screen fades to a close-up shot of Aspen looking down at a fern. The scene is softly lit and is mostly dark."
        a "{color=#fff}This is Penelope. She's an \"Adiantum\" - a maidenhair fern."
        a "{color=#fff}She's extremely tempermental. Doesn't listen to anyone but me."
        a "{color=#fff}I swear, if any other greenhouse employee tries to water her or test on her, she throws a fit."
        a "{color=#fff}Haha, not literally, of course. She'll just wilt. But she's my favourite."

        mccut "{color=#fff}She's beautiful."

        a "{color=#fff}Thank you. I know."

        n "{color=#fff}You suddenly realize how close you are to Aspen. They realize, too."

        scene aspentemproom with fade
        show a look with easeinright
        hide screen cuttextbox
        $ cutscenetextbox = False
        a "Oh! Ahem, uh, sorry. I was excited to show you my - uh... favorite plant."

        mc "No worries."
        jump aspenday3goodpt2
    else:
        a "Oh, not really. I like all my plants equally."

        show a laugh
        a "Can't be picking favorites - what if it dies? Haha."
        jump aspenday3goodpt2

label aspenday3goodpt2:
    show a
    n "The rest of your shift is very informative."
    show a laugh
    n "Aspen spends their time watering the plants and rattling off botanical facts."
    n "You learn more about botany than you ever thought you'd care to."

    show a look
    n "They seem to love their job."
    n "You're happy for them."

    show a
    n "Before you know it, it's 16:00 and time to go home."
    n "You finish off your checklist and head out."
    jump day3end

label aspenday3bad:
    show a look
    a "Oh... yeah. I suppose. All I do is water plants, after all."

    n "The rest of your shift is easy, yes, but boring."
    n "You spend most of your time sitting there while Aspen focuses whole-heartedly on their job."
    n "You have no idea what to say to them."
    n "Perhaps you shouldn't have been so harsh."

    n "The time ticks by incredibly slowly. Eventually, it's 16:00, and it's time for you to go."
    n "You finish your checklist and leave."

    jump day3end

label ccday3:
    e "Yes. As long as they're along our usual route, yes."
    e "I'm sure he'll appreciate the company."

    e "I'll put it in my database that you'll be supervising CC today. Do you remember the way to his room?"

    mc "Yes, I do."

    e "Perfect. On your way, then!"
    

    scene cctemproom
    with fade
    $ audio_crossFade(2, "music/five.ogg")

    n "You make your way into CC's \"hospital\" room. He is hanging in the same spot."

    show c close with easeinright

    n "You believe he may be sleeping. Or something similar."
    n "You gently poke his chassis."

    mc "CC?"

    show c with gentleswitch
    c "Ahh, Doctor. Apologies, I was... trying to conserve my energy."

    mc "You need to conserve energy?"
    mc "What're all these tubes and pumps for, then?"

    c "A multitude of things. A lot of them I'm not even sure of."

    c "Oh, sorry - I just got a message from Miss Esther..."
    c "Oh."

    show c close
    c "Haha... you chose to supervise me today?"

    show c
    c "Well then..."
    c "You're going to be very bored."

    menu:
        extend ""
        "Not at all. You interest me.":
            $ romance_points["CC"] += 3
            jump ccday3good
        "Yeah. I planned on just sleeping through my shift.":
            $ romance_points["CC"] += 3
            jump ccday3bad

label ccday3good:
    $ goodday3 = True
    $ wcd3 = True
    show c look
    c "I... interest you?"

    show c
    c "Haha. That's silly."
    c "But it's..."
    c "...more than the last doctor said."
    c "You know, you woke me up from my dream."

    mc "You can dream?"

    c "In a way, I suppose. Cores don't quite... \"dream\" the same way humans do, but... yes. We can visualize things."

    mc "What were you... visualizing... about?"

    if romance_points["CC"] >= 7:
        $ knowabtwaterfall = True
        $ cutscenetextbox = True
        show screen cuttextbox
        scene cc cutscene 1 with fade
        $ persistent.cc1 = True
        if persistent.advcap == True:
            "{i}The scene fades to CC looking down solemnly. He's back-lit by his window. In the foreground, you can see the computers that monitor his health."
        c "{color=#fff}Well... it's a little embarrassing."
        c "{color=#fff}See, I have so many bio-simulators and pain receptors stuffed into my chassis, it's like I'm practically organic."
        c "{color=#fff}And I've heard the scientists talk about these {i}wondrous{/i} things called \"waterfalls\"..."
        c "{color=#fff}They must be beautiful. Water falling so freely, no... tubes to tether it down, management rails to confine it..."

        c "{color=#fff}I think about it a lot."
        c "{color=#fff}I would give anything to see one."

        scene cctemproom with fade
        show c close with easeinright
        hide screen cuttextbox
        $ cutscenetextbox = False

        c "But I know I never will. So I look at pictures. And it's almost the same."
        jump ccday3goodpt2
    else:
        show c close
        c "Nothing, really. Just wishing I was healthy."
        show c
        c "I always dream about that."
        jump ccday3goodpt2

label ccday3goodpt2:
    show c
    n "The rest of the day is quiet, slow, but nice."
    n "CC is more full of life than ever."
    show c look
    n "He talks about his daily routine. Asks you plenty of questions about your own life."
    n "Your shift goes by quickly, and when it ends, you find you don't want to leave."
    n "But 16:00 comes as always."

    show c
    mc "I need to get going, CC. But... this was nice. Relaxing."
    mc "Especially after the weirdly chaotic week I've had."

    c "Yes. I understand. I'm glad I could give you a... break, sort of."

    n "You finish your checklist and head out for the day."

    jump day3end

label ccday3bad:
    show c close
    c "Well, I guess we can both preserve our energy, then."

    n "The rest of your shift is boring."
    n "CC won't wake up no matter what you do, and it's nearly impossible to fall asleep in the hard chair you're in."
    n "You end up trying to read the manual next to him, but it's full of technical jargon."
    n "Even with all your experience in manufacturing, some of these terms still don't ring any bells."

    n "Eventually, just as you're about to drift off, the clock hits 16:00, and it's time to go home."
    n "You finish your checklist and quietly leave the room."

    jump day3end

label robday3:
    show e annoy
    e "You want to supervise {i}him?{/i} Well, don't let me stop you."

    e "I'll put it in my database that you'll be supervising Robert today. Do you remember the way to the gym?"

    mc "Yes, but - sorry, Robert?"

    show e annoy
    e "His full name. He prefers to go by Rob, though, so... don't tell him I told you."

    scene robtemproom with fade
    show r yell with easeinright
    $ audio_crossFade(2, "music/two.ogg")

    r "GO! GO! GO!!! COME ON, PUT YOUR BACK INTO IT!"

    n "You enter the gym and immediately spot Rob yelling at the screen in front of him."

    r "CAN'T RUN TO SAVE YOUR GODDAMN LIFE! COME ON!!"

    mc "Um... Rob?"

    show r angry
    r "Sorry, Doc. One second. The game's on."

    n "He turns back to the screen just in time for -"

    show r yell
    r "TOUCHDOWN!! HELL YEAH!"

    show r

    if ball == True:
        n "The crowd on the screen goes wild, yelling and shouting. You forgot how big American football used to be."
    else:
        n "The crowd on the screen goes wild, yelling and shouting. You assume this is a good thing, because Rob looks pleased."

    r "Sorry, sorry, Doc. The game gets me excited. You should know this by now."

    mc "No worries."

    r "I saw the message from Essie. You chose to supervise me today, huh?"

    mc "Yes, that's right."

    r "Well, that's perfect. Great time to get those muscles to work, now!"
    
    menu:
        extend ""

        "Mind if I use the elliptical?":
            $ romance_points["Rob"] += 3
            jump rday3good
        "Uh... I actually don't work out. At all.":
            $ romance_points["Rob"] -= 3
            jump rday3bad

label rday3good:
    $ goodday3 = True
    $ wrd3 = True
    show r angry
    r "I'm surprised you even know the name of one of the machines."
    r "Most of the doctors here don't care."

    mc "I do try to keep in shape a little bit, when I can. Usually on the weekends."

    show r
    r "Well alright then! Elliptical's right over there. Feel free to use any of the machines."

    if romance_points["Rob"] >= 7:
        show r angry
        r "Need a coach?"

        mc "Sure. Why not?"

        show r
        n "Rob moves on his management rail over to the elliptical machine."

        $ cutscenetextbox = True
        show screen cuttextbox
        scene rob cutscene 1 with fade
        $ persistent.rc1 = True
        if persistent.advcap == True:
            "{i}The scene fades to Rob looking down at you, \"HANG IN THERE!\" poster and TV screen behind him."
        r "Alright, hop on, let's get started."

        n "You begin your workout, and Rob coaches you on your form."

        r "You're too tight. Loosen up."
        mccut "How do you know so much about fitness without... well... having limbs?"
        r "Well, it's partially 'cuz it's programmed into me."
        r "I'm also just real passionate about humans in general. Fitness is just the one aspect I really enjoy."

        mccut "Interesting."
        r "You're going too slow, now. You need to pick up the pace."
        mccut "I'm... trying."

        r "Don't overwork yourself."
        scene robtemproom with fade
        $ cutscenetextbox = False
        hide screen cuttextbox
        show r with easeinright
        jump rday3goodpt2
    else:
        mc "Thanks, Rob. I will."
        jump rday3goodpt2

label rday3goodpt2:
    show r
    n "The rest of your shift is hard work!"
    n "You spend most of your time trying out the different machines. Though you try to keep fit, it's hard with a job like this."
    n "It's nice to actually focus on a workout for once."

    show r yell
    n "In between yelling at the screen, Rob talks about his day-to-day."
    show r angry
    n "He talks about his ex-wife and two kids - you don't bother to ask how that's even possible."
    show r
    n "At the end of the day, you're sweating and tired, but satisfied."
    n "No doubt you'll be sore tomorrow, though."
    n "Rob looks pleased with you."

    r "Great job. Great workout. Hope you got something out of it."

    mc "Oh, I definitely did. Haha."

    n "You tiredly finish your checklist and head out."

    jump day3end

label rday3bad:
    show r angry
    r "You don't work out?! Why the hell are you here then?"

    mc "I figured I could just watch the game you're always looking at."

    r "Nuh-uh. That won't do."
    show r yell
    r "You are a DISGRACE to the nature of the game!"
    r "Get your head in it!"
    
    mc "Uh... what?"

    show r angry
    r "Nevermind. Just sit down."

    n "The rest of your shift is pretty entertaining, at least."
    show r yell
    n "Rob refuses to acknowledge you, but his outbursts at the screen keep you awake."
    show r angry
    n "The time goes by quickly enough, even though you feel judged the entire time."
    n "16:00 comes around, and it's time to head out."

    n "You finish your checklist and go back to the office."

    jump day3end

# DAY END
# ==================
label day3end:
    scene office
    with fade
    show e with easeinright
    e "Welcome back, Doctor! How did your shift go?"

    if goodday3 == True:
        mc "It went great. The shift was easy and went by quickly."

        e "That's great to hear. I'll take the data you collected and you can head out for the night."
        e "Like I said, it's a simple shift!"

        n "You hand your clipboard over Miss Esther. What an interesting day..."

        jump e3first
    
    else:
        mc "It was okay. Nothing happened, really."

        e "Sometimes that's a good thing. Inaction is better than a bad reaction, after all."
        e "I'll take your data for the day and you can head out for the night."

        n "You hand your clipboard over to Miss Esther."

        jump e3first