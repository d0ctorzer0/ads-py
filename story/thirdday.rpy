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
        "On the contrary. I'm sure it'll be exciting with you here.":
            $ romance_points["Kris"] += 3
            jump krisday3good
        
        "That's why I chose to oversee you. Not a lot of work to do, and I can just relax.":
            $ romance_points["Kris"] -= 3
            jump krisday3bad

label krisday3good:
    $ kday3good = True
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
    $ kday3good = False
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

label day3end:
    scene office
    with pixellate
    show e with easeinright
    e "Welcome back, Doctor! How did your shift go?"

    if kday3good == True:
        mc "It went great. The shift was easy and went by quickly."

        e "That's great to hear. I'll take the data you collected and you can head out for the night."
        e "Like I said, it's a simple shift!"

        n "You hand your clipboard over Miss Esther. What an interesting day..."

        jump tde
    
    if kday3good == False:
        mc "It was okay. Nothing happened, really."

        e "Sometimes that's a good thing. Inaction is better than a bad reaction, after all."
        e "I'll take your data for the day and you can head out for the night."

        n "You hand your clipboard over to Miss Esther."

        jump tde