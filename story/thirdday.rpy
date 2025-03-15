label day3:
    scene mctemproom
    with fade

    n "You make your way to your quarters. After organizing your paperwork, you lay down in your stasis chamber."
    n "Before you fall asleep, you wonder what Miss Esther meant by tomorrow being \"different\"."

    scene black
    with fade

    n "No dream, once more."

    scene mctemproom
    with fade

    n "You wake up, slowly but surely, and turn to the clock. 08:00, again."
    n "Work in manufacturing doesn't begin until 11, and it's going to take a bit to get used to this new schedule."
    n "You get up and go towards your office."

    scene office
    with pixellate

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
    with pixellate

    n "You enter the conference room to see Kris staring at the screen. You can't understand what's happening, but that's his job, not yours."

    mc "Kris?"

    show k with easeinright

    n "Kris turns to face you, smug as ever."
    k "Well, well. Esther sent me a notification that you'd be overseeing my work today."

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
    show k
    k "Me? Exciting? Well now. I try not to be {i}too{/i} exciting."
    show k angry
    k "Especially after the disaster that was our former management."

    mc "What was wrong with the former management?"

    show k
    k "Oh, that's right. Esther did say you were a... newer employee."
    k "You must have not been here when Mr. Johnson was still at the head of the company."

    mc "No, I wasn't. I was part of the first new hire wave about 9 months ago."

    k "Mr. Johnson was an... interesting man. You might hear some... {i}lesser{/i} cores refer to him by his first name, \"Cave\"."
    show k angry
    k "I still have some semblance of respect for the man, regardless of his ridiculous financial policies."
    k "He just... did not handle the company very well in terms of our monetary investments."

    mc "Were you working during the time?"

    show k
    k "In a way, yes. I was activated in 1979, but I was originally just a consultant. As Mr. Johnson lost more and more employees due to mandatory testing, he began replacing them with... us."
    k "That's why there's so many personality cores around now. We're remnants."

    show k angry
    k "The man never stopped spending Aperture's money. And it led him to his death."

    mc "You seem bitter about it, still."

    show k
    k "Hmm. I suppose I am. I enjoyed my consulting work. After Miss Caroline took over as CEO, a lot of things happened."
    k "Projects got shut down. Employees were fired. Personality cores became... less important."

    # FIRST KRIS CUTSCENE HERE!! YAY!!
    if romance_points["Kris"] >= 7:
        $ cutscenetextbox = True
        scene kris cutscene 1 with fade
        $ kc1 = True
        k "{color=#fff}I'm stubborn for that reason."
        k "{color=#fff}My job is... simple. Perhaps not every personality core can read a stock market graph, but... it's a useless job."
        k "{color=#fff}Thankless, too."

        mc "{color=#fff}I think what you do is very important."

        k "{color=#fff}Not as important as it should be. Miss Caroline, she..."
        k "{color=#fff}She doesn't trust us. And I'm not sure why."
        k "{color=#fff}She is excellent at what she does. She's dragged Aperture out of the ditch it was in, but..."
        k "{color=#fff}The company now... it's different. Mr. Johnson was fascinated with us. Miss Caroline is not."
        scene kristemproom with fade
        show k
        $ cutscenetextbox = False
        jump krisday3goodpt2
    else:
        jump krisday3goodpt2

label krisday3goodpt2:
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
    with pixellate

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
    h "Well, you're in for a treat. My whole job is entertainment, so I'll be sure to keep you on your toes!"
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
        scene heath cutscene 1 with fade
        $ hc1 = True
        n "{color=#fff}You're stunned by what you see - a hidden-away, wooden room, lined with fairy lights, shelves stocked with magic paraphenalia."
        h "{color=#fff}Tada!! This is my magic room. It's where I keep all the stuff I use to perform my tricks."

        mc "{color=#fff}Wow, Heath. I can't believe this. It's amazing."

        h "{color=#fff}Yes, yes, I know."
        h "{color=#fff}There's my magic 8 ball, my stuffed rabbit, my bowling pins - for juggling."

        mc "{color=#fff}You can juggle?"

        h "{color=#fff}Hahaha, no. But you could!"
        h "{color=#fff}I haven't shown anyone else this room, so you should consider yourself lucky!"

        n "{color=#fff}Heath comes back out and closes the curtains."
        scene heathtemproom with fade
        show h with easeinright
        $ cutscenetextbox = False
        jump heathday3goodpt2
    else:
        h "Oh, just some miscellaneous props and such. Nothing too special."
        h "Aha! I found it!"
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
    e "Good choice. He's a nice kid."
    e "I'm sure he'll appreciate the company."

    e "I'll put it in my database that you'll be supervising Aspen today. Do you remember the way to the greenhouse?"

    mc "Yes, I do."

    e "Good. Off you go!"

    scene aspentemproom
    with pixellate

    n "You enter the greenhouse. Aspen is humming to himself while he waters the plants."

    mc "Aspen?"

    n "He jumps and spins around rapidly."
    
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

    show a look
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
    show a
    a "Oh! Well then, I'm happy to oblige. What are you interested in?"

    mc "How many of you are in Botany?"

    show a look
    a "Let me think..."

    show a
    a "I believe there's a total of about 70 of us. That's researchers, scientists, gardeners like me."

    mc "That's not a lot."

    a "Haha, you're right - it's really not!"
    a "I kind of like it though. It keep us accountable. If even one of us falters, the whole team will suffer."

    mc "That's a lot of pressure."

    a "Tell me about it."

    mc "So, uh... do you have a favorite plant? Out of all of these?"

    if romance_points["Aspen"] >= 7:
        a "Oh yes! Absolutely! Come over here, and I'll show you."

        n "You follow Aspen on his management rail as he leads you to a back corner."

        $ cutscenetextbox = True
        scene aspen cutscene 1 with fade
        $ ac1 = True
        a "This is Penelope. She's an \"Adiantum\" - a maidenhair fern."
        a "She's extremely tempermental. Doesn't listen to anyone but me."
        a "I swear, if any other greenhouse employee tries to water her or test on her, she throws a fit."
        a "Haha, not literally, of course. She'll just wilt. But she's my favourite."

        mc "She's beautiful."

        a "Thank you. I know."

        n "You suddenly realize how close you are to Aspen. He realizes, too."

        scene aspentemproom with fade
        show a look with easeinright
        $ cutscenetextbox = False
        a "Oh! Ahem, uh, sorry. I was excited to show you my - uh... favorite plant."

        mc "No worries."
        jump aspenday3goodpt2
    else:
        a "Oh, not really. I like all my plants equally."
        a "Can't be picking favorites - what if it dies? Haha."
        jump aspenday3goodpt2

label aspenday3goodpt2:
    show a
    n "The rest of your shift is very informative."
    n "Aspen spends his time watering the plants and rattling off botanical facts."
    n "You learn more about botany than you ever thought you'd care to."

    n "He seems to love his job."
    n "You're happy for him."

    n "Before you know it, it's 16:00 and time to go home."
    n "You finish off your checklist and head out."
    jump day3end

label aspenday3bad:
    a "Oh... yeah. I suppose. All I do is water plants, after all."

    n "The rest of your shift is easy, yes, but boring."
    n "You spend most of your time sitting there while Aspen focuses whole-heartedly on his job."
    n "You have no idea what to say to him."
    n "Perhaps you shouldn't have been so harsh."

    n "The time ticks by incredibly slowly. Eventually, it's 16:00, and it's time for you to go."
    n "You finish your checklist and leave."

    jump day3end

# DAY END
# ==================
label day3end:
    scene office
    with pixellate
    show e with easeinright
    e "Welcome back, Doctor! How did your shift go?"

    if goodday3 == True:
        mc "It went great. The shift was easy and went by quickly."

        e "That's great to hear. I'll take the data you collected and you can head out for the night."
        e "Like I said, it's a simple shift!"

        n "You hand your clipboard over Miss Esther. What an interesting day..."

        jump tde
    
    else:
        mc "It was okay. Nothing happened, really."

        e "Sometimes that's a good thing. Inaction is better than a bad reaction, after all."
        e "I'll take your data for the day and you can head out for the night."

        n "You hand your clipboard over to Miss Esther."

        jump tde