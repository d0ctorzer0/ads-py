label krisday1:

    play music sa fadein 0.5
    scene kristemproom
    with pixellate

    n "As you enter the room of your first checkup, you look up at the wall in front of you to see a stock market display. Green and red lines dance across the screen rapidly."
    n "In the corner of the room, intensely staring at the wall and muttering to itself, is a core, hanging by a management rail that looks like it hasn't been used in ages."

    show e annoy
    with easeinright

    e "Ahem. Kris."

    n "The core, startled by your entrance, spins around rapidly."
    hide e annoy
    with easeoutright

    show k
    with easeinright
    k "Ahh, Miss Esther. I assume you're here for my checkup?"

    show e b sad at bounce 
    e "{i}I'm{/i} here for no such thing. {i}They,{/i} however..."
    hide e b sad
    show k flirt
    n "Kris turns down to face you."

    k "A new employee? Hmm. Interesting. Whatever happened to the other human?"

    n "He scrutinizes you."

    show k
    k "A little plain, isn't it?"

    mc "Excuse me?"

    show k flirt
    k "You. You're a little... boring, I suppose the word is."

    mc "Is he always this rude?"

    show e b sad at bounce
    n "Esther sighs. You glance down at your clipboard."
    hide e b sad

    mc "I see here your job is to make sure Aperture stock doesn't get too low. Is that correct?"

    show k
    k "Ahem. Yes, that's me. I'm constantly monitoring this board here."
    k "I own fifteen Fortune-500 companies, you know. I'm an expert in all things business."

    menu:
        extend ""

        "Uh-huh. A personality core, running a business.":

            $ romance_points["Kris"] -= 3
            jump offendkris
        
        "Wow. That must be difficult.":

            $ romance_points["Kris"] += 3
            jump impresskris
        
        "Interesting.":

            $ romance_points["Kris"] += 2
            jump krisday1cont

label offendkris:

    show k angry
    k "Excuse me?! I don't appreciate your... implications."
    k "Does this look easy to you? All these lines and colors and numbers??"

    show e b at bounce
    e "Now, Kris. I'm sure they meant nothing by their comment."
    hide e b

    k "Hmmph. Regardless, check me off your list. I'm doing everything I need to here."
    
    jump krisday1cont

label impresskris:

    $ krisgoodbye = True

    show k flirt
    k "Why... yes. It is quite hard."
    k "Glad {i}someone{/i} here has some common sense."

    show e b sad at bounce
    n "Esther scoffs. Kris pauses."
    hide e b sad
    show k
    k "I apologise... for calling you... \"boring\"."
    k "Don't get me wrong, though. You could be doing a lot more."

    jump krisday1cont

label krisday1cont:

    show k

    n "You check \"KRIS (BUSINESS CORE)\" off your list. Seems like, despite the attitude, he does his job well enough."

    hide k
    with easeoutright
    show e
    with easeinright
    e "Let's go, now. We have more to attend to."

    if krisgoodbye == True:

        hide e
        with easeoutright
        show k flirt
        with easeinright
        k "I suppose I'll see you tomorrow, then."

        mc "I suppose so."

        hide k flirt
        with easeoutright
    
    n "Miss Esther guides you out of the business sect and towards recreation. On your clipboard, it lists \"HEATH\" as your next checkup..."
    
    jump heathday1

label heathday1:

    scene heathtemproom
    with fade

    n "As you proceed along your route, you notice you've never been down to recreation before. You rarely have time to, and once work is over, well, you've always just gone home."
    n "The boring, plaster-white tile walls give way to gentler, kinder beige colors, and the floor transitions softly to carpet."

    show e
    with easeinright
    e "We're nearing our next checkup. Her name is Heath. She's... a little eccentric, but nowhere near as rude as Kris."

    mc "Eccentric? How so?"

    show e annoy
    e "Just humor her, if you can."

    mc "Alright."

    show e
    n "Miss Esther guides you into the next room, which holds a small stage with a closed curtain. Behind the drapes, you can hear crashing, banging, and..."

    hide e
    with easeoutright

    h "Where is that goddamn rabbit?!"

    n "The unmistakable voice of a personality core."

    show e
    with easeinright

    e "Heath? Heath! It's time for your check-in."

    h "Ah, shit. I'm on my way. One second. Is the human here yet?"

    show e annoy
    e "Yes."

    h "Oh. Um. Human? Pretend you didn't hear anything."

    n "Esther shakes her chassis in a sort of disappointed way."

    hide e annoy
    with easeoutright

    h "Prepare yourself... for the great and amazing {i}{b}HEATH!{/i}{/b}"

    show h
    with easeinright
    n "The curtains part as a core with a purple optic and ribbon-wrapped handlebars comes barreling out. A flurry of confetti comes up from the floor and lands around it."

    h "Mystery... intrigue... the unknown... what do all these things have in common?"

    show h laugh
    h "{i}{b}ME, OF COURSE!{/i}{/b}"

    show h
    h "Are you ready for the most amazing trick you'll ever see in your feeble human existence?"

    show h sad
    n "Heath turns away temporarily, seemingly fiddling with something behind the curtain."
    n "Suddenly, fire shoots up from the floor."

    show h laugh
    h "{i}{b}BOOM!! HAHA!!{/i}{/b} I just summoned FIRE with my MIND!!"

    menu:
        extend ""

        "OH MY GOD!! That was incredible! HOW'D YOU DO THAT?":

            $ romance_points["Heath"] += 3
            jump impressheath
        
        "Haha, very funny. What's your job, exactly?":

            $ romance_points["Heath"] -= 3
            jump offendheath
        
        "Wow! Impressive.":
        
            show h
            h "Haha, yes, thank you, thank you."
            $ romance_points["Heath"] += 2
            jump heathday1cont

label impressheath:

    $ heathgoodbye = True

    show h
    h "Haha!! I KNEW you had taste from the moment I laid eye on you!"
    h "I'm a true magician. It's in my wiring. And you SAW THAT!"

    mc "That was inspiring, Heath. Amazing."

    h "Mmhmm. Thank you, thank you. Not everyone appreciates my great talents."

    show e b sad at bounce
    n "Miss Esther groans."
    hide e b sad

    mc "You do this all day?"

    show h laugh
    h "Yes! I'm the staff entertainer... it's my job to keep morale high and IMPRESS THE MASSES!"

    mc "Well, you certainly impressed me."

    hide h laugh
    with easeoutright
    show e annoy
    with easeinright
    e "Sorry to interrupt... this, but we {i}do{/i} have more work to do..."

    jump heathday1cont

label offendheath:

    show h sad
    h "O-Oh. I'm... the entertainer. I keep staff morale high."

    mc "I see. Is this how you achieve that?"

    h "Well, I would hope so. I'm the GREAT AND AMAZING Heath, after all."

    jump heathday1cont

label heathday1cont:

    n "You check \"HEATH (MAGIC CORE)\" off your list. Miss Esther was right - she certainly is eccentric, but morale seems high enough with her around."

    if heathgoodbye == True:

        hide e annoy
        with easeoutright
        show h
        with easeinright
        h "Come back again tomorrow for another AMAZING SHOW!!"
        
        mc "Haha, I certainly will!"

    hide h
    with easeoutright
    show e
    with easeinright
    e "We'll have to take a shortcut to the next location, as it's a bit far up."

    n "Next on your clipboard is an \"ASPEN\"."

    jump unknownday1

label unknownday1:

    scene temphall
    with fade

    show e
    with easeinright
    n "Miss Esther guides you to the next area, following you closely on her management rail."

    e "Section C8 is mostly a recreational area."
    e "Deep down in manufacturing and encoding, where you were, you might not have all the amenities afforded to more... surface-level scientists."

    n "As she speaks, you look at your surroundings. Boring, dull offices are instead replaced with vibrant conference rooms."
    
    e "As I'm sure you're well aware, many of our staff resides on-campus in case of an emergency. On their days off, they'll often come here."
    e "You'll be assigned a room tonight. Maintenance staff is always on-call."

    n "You groan."

    show e laugh
    e "Oh, hush. It's not all bad. Your sustenance is provided for you. No hunting required."

    mc "Sorry, hunting?"

    show e
    e "Why yes. Don't humans have to hunt for their food?"

    mc "That was... hundreds of years ago. We have slaughterhouses and processing plants now."

    e "Huh."

    n "Suddenly, Miss Esther stops."

    show e shock
    e "What the -"

    n "Coming towards her is a dirty, obviously-damaged core, not paying attention to where he's going."

    show e annoy
    e "Hey!"

    hide e annoy
    with easeoutright
    n "The core comes screeching to a halt."
    
    show u
    with easeinright
    u "Uhh... huh?"

    hide u
    with easeoutright
    show e annoy
    with easeinright
    e "Who is your supervisor?!"
    e "This management rail is only approved for use by maintenance staff!!"

    hide e annoy
    with easeoutright
    show u
    with easeinright
    u "Uhh, sorry, miss... ma'am. I don't rightly know how I... *hic* ...got here."

    show e b annoy at bounce
    e "What is this... disgrace to my position!?"

    menu:
        extend ""

        "Let's take a minute to calm down and figure things out.":

            $ romance_points["???"] += 3
            jump impressunknown
        
        "Shouldn't you be in the repair bay?":

            $ romance_points["???"] -= 3
            jump offendunknown

        "I suggest you listen to Miss Esther.":

            $ romance_points["???"] -= 2
            jump unknownday1cont

label impressunknown:

    $ unknownhumor = True

    hide e b annoy
    show u upset
    u "Yeah, calm down, lady. Issalright."

    mc "Are you lost?"

    show u
    u "Mmm, I guess I am, if I'm on an unapproved rail here."

    mc "Where were you headed?"

    u "Heheh, to your place, of course..."

    n "The core winks at you. Or... something adjacent to that, having only one eye."

    show e b annoy at bounce
    e "Eugh. Disgusting. Vile."
    hide e b annoy

    u "Why don't you come drink some... *hic* lighter fluid with me, honey?"

    mc "I'm... flattered, but I have to get back to work."

    u "Your loss, but the invite's allllways available for such a pretty human..."

    jump unknownday1cont

label offendunknown:

    hide e b annoy
    show u upset
    u "Pfft. No. I'm... fit as a fiddle."

    mc "You have sparks flying out of you."

    u "And what do you know?! You're just a lousy human!"

    show e b annoy at bounce
    e "EXCUSE ME, sir? This \"human\" has very important business to attend to and does not need the likes of YOU interrupting them."
    hide e b annoy

    show u
    u "Fine. Jesus, y'think people would have some manners..."

    jump unknownday1cont

label unknownday1cont:

    hide e b annoy with None

    hide u
    with easeoutright
    n "The unnamed core spins around and hums happily to itself as it disappears back into the maze of rails behind the walls."

    show e annoy
    with easeinright
    if unknownhumor == True:
        e "I have no idea why you even humoured such a... creature as {i}that.{/i}"

        n "You shrug."
    
    n "Miss Esther, visibly shaken (perhaps with anger, perhaps with confusion), continues slowly on her management rail."

    show e
    e "Regardless. Our next stop is the greenhouse."

    mc "Greenhouse? Why do we need a greenhouse down here?"

    show e shock
    e "Why do we--"

    n "She scoffs."

    show e annoy
    e "We test more than robots here, thank you very much. Botany is just as much science as any other path."

    show e
    n "She continues to rant about botany's importance to Aperture as you approach an unusually well-lit room."
    n "Once you reach the entrance to the greenhouse, Miss Esther stops you."

    e "Due to the fragile nature of our greenery, I must remain here. Only approved spheres may go past this point, and I am not one."

    menu:
        extend ""

        "Will you be alright out here?":
            
            $ esther_affection += 1
            show e laugh
            e "Haha, yes, Doctor, I'll be fine. It won't be for long."
            jump aspenday1
        
        "I'll handle it, no worries.":

            $ esther_affection -= 1
            jump aspenday1
    
label aspenday1:

    show aspentemproom
    with pixellate

    n "You enter the greenhouse and are almost instantly blinded by the bright lights above you."
    n "You look around in shock. Hundreds of plants, including some specimens you've never seen, line the floors, the walls, and the ceiling."
    n "In the back corner, a mossy, dirt-covered core sprays the greenery with what is most likely water."

    mc "Hello?"

    n "The core stops spraying, turns around in shock, and quickly zooms back over to the entrance."

    show a look with easeinright
    a "Sorry, sorry, didn't see you there!"

    mc "That's alright."

    show a
    a "I'm assuming you're the temp for the maintenance position, yeah?"
    a "Miss Esther can't come in here, but she briefed me on your arrival this morning."

    mc "Yes, that's me. I've just come to check up on you."

    a "Well, no need for concern. My sprinkler system's working great as always."

    show a look
    a "The day it fails will be a horrible day for Aperture!"

    show a
    n "He laughs nervously."

    menu:
        extend ""

        "Good to hear. Keep up the great work.":

            $ romance_points["Aspen"] += 2
            a "I certainly will."
            jump aspenday1cont

        "The work you do here is certainly very important, then.":
            
            $ romance_points["Aspen"] += 3
            jump impressaspen
        
        "What do all these plants even do for Aperture, anyway?":

            $ romance_points["Aspen"] -= 3
            jump offendaspen

label impressaspen:

    $ aspengoodbye = True

    show a look
    a "Aha, yes, it is. I'm glad you can, uh, see that."

    mc "Are you the only one maintaining these specimens?"
    
    show a
    a "Oh, not at all. Well, kind of. I'm the only personality core working in here. We've got a few nanobots on the greenhouse staff."
    a "And of course, the scientists. But I would say I definitely work the {i}most{/i}."

    mc "Wow, that's awesome."

    a "Haha. Thanks."

    jump aspenday1cont

label offendaspen:

    a "What? What do you mean?"

    mc "I just don't see what use Aperture could have for botany."

    a "Lots of things! They test on other organics before they ever test on themselves, you know. And there's some kinds of science that can only be done on plants."

    mc "Mmm. I guess so."

    jump aspenday1cont

label aspenday1cont:

    mc "I'll be leaving now. I'm sure Miss Esther is waiting for me."

    if aspengoodbye == True:

        a "Alright. Stay safe! I'll see you tomorrow."

    if aspengoodbye == False:

        show a look
        a "Hmm. I'm sure."

    hide a with easeoutright
    n "You check \"ASPEN (BOTANICAL CORE)\" off your list. Despite the rather unusual subsection he oversees, he seems content enough with it."
    n "As you exit the greenhouse, Miss Esther greets you."

    show e
    show e
    with easeinright
    e "Glad to see you're back. We should move along - that... {i}encounter{/i} earlier put us behind schedule."

    n "You glance down. Next on your list is something simply labeled \"CC\"."

    jump ccday1

label ccday1:

    scene temphall
    with pixellate
    show e
    with easeinright

    n "Miss Esther guides you down the hall, slightly quicker than before."

    show e annoy
    e "Before we reach our next checkup, I have to warn you... it's a little strange."

    mc "All of them have been pretty strange."

    show e laugh
    n "Miss Esther laughs."

    show e annoy
    e "Yes, but... CC is different. Not eccentric or interesting... just a little sad."

    mc "What does CC stand for, anyway?"

    e "...You'll see."

    scene cctemproom
    with pixellate

    n "The two of you approach a room that is definitely not very well-maintained. The door looks like it's barely hanging on, and the window is so dusty you can't see through it."
    n "You open the door gently. Inside, hanging from the ceiling by a cut-off management rail, is a core."

    show e annoy
    with easeinright
    e "CC, it's time for your checkup."

    hide e
    with easeoutright
    show c close
    with easeinright
    cu "Oh, what's the use? The diagnosis will be the same, regardless."

    show e b sad at bounce
    e "Yes, I know."
    hide e b sad
    show c
    n "The core slowly opens its optic and turns to face you. It looks... tired, somehow."

    cu "Oh. This one's new, isn't it?"

    hide c
    with easeoutright
    show e annoy
    with easeinright
    e "Yes. This is the new temp."

    hide e
    with easeoutright
    show c
    with easeinright
    mc "What's wrong with you?"

    cu "What's wrong with me? Haha..."

    show c close
    n "The core laughs, then coughs harshly."

    show c look
    c "I have cancer."

    n "You look at the core, then at Miss Esther, then back at the core again."

    mc "Sorry. What?"

    show c
    c "I know, it sounds ridiculous. A robot, having a human disease. But I do."

    mc "Isn't that impossible?"

    c "Everything Aperture does is impossible."

    hide c
    with easeoutright
    show e annoy 
    with easeinright
    e "You're just here to ensure he's still sick."

    mc "That's... that's it? No job to do, no task to maintain? I'm just making sure he's suffering?"

    e "Yes."

    jump ccchoice

label ccchoice:
    if haveaheart == True:
        e "Yes."

    menu:
        extend ""

        "That's horrible. I can't believe someone would do this.":
            
            $ romance_points["CC"] += 3
            $ esther_affection += 1
            jump impresscc
        
        "Oh my god, that's hilarious.": # player choosing this option absolutely DESTROYS their chance at CC

            menu:

                n "Are you sure you want to choose this option? It is unnecessarily cruel and horrible."
                "Yes, I am a horrible person.":
                    $ romance_points["CC"] -= 100
                    $ esther_affection -= 1
                    jump offendcc
                
                "Actually, no. I have a heart.":
                    $ haveaheart = True
                    jump ccchoice
        
        "Why would they do this?":

            $ romance_points["CC"] += 2
            $ esther_affection += 1
            hide e
            with easeoutright
            show c
            with easeinright
            c "Don't ask me. Humans can be cruel. Especially... Aperture ones."
            jump ccday1cont

label impresscc:

    hide e
    with easeoutright
    show c
    with easeinright
    c "Yes. Horrible indeed."

    mc "Does that mean you're dying?"

    show c close
    c "Haha... they aren't sure. That's what they're testing."

    mc "If they wanted to test... robotic disease, or whatever... why didn't they use one of the non-sentient machines?"

    c "Don't ask me. You humans are cruel."

    show c look
    c "Well. Maybe not all of you."

    show c
    show e b sad at bounce
    e "CC, get some rest. Doctor, we should be going, now."
    hide e b

    mc "I hope you feel better."

    c "I won't."

    jump ccday1cont

label offendcc:

    hide e
    with easeoutright
    show c close
    with easeinright
    c "That's what they said when they turned me on, too."

    mc "Well, at least this makes this part of the job easy."
    mc "You're still suffering, so... mission accomplished."

    show c
    c "You're not like the... previous employee at all."

    hide c
    with easeoutright
    show e annoy 
    with easeinright
    e "CC, get some rest."

    jump ccday1cont

label ccday1cont:

    n "You check \"CC\" off your list. So {i}that's{/i} what the C's stand for..."
    n "The last name on your list is a \"ROB\"."

    hide c
    with easeoutright
    hide e
    with easeoutright

    jump gregday1

label gregday1:

    scene temphall
    with pixellate

    n "You and Miss Esther leave CC's room and start heading back towards your office."

    show e
    with easeinright
    e "The nice thing about your route is that it circles back around to your desk, which helps prevent too much time wasted walking."

    mc "Yes, I can see how that would be useful."

    e "Our final stop of the day is the company gym."

    mc "We have a gym?"

    show e annoy
    e "Yes. Rarely used, but yes, we have one."
    hide e with easeoutright

    n "Suddenly, a strangely-shaped figure comes barreling around the corner on a cart. It's headed straight towards you."
# help he looks SO FUNNY IN GAME OMG
    show g aaa with easeinright
    gu "Aah!! I'm so so sorry! Watch out watch out!!"

    n "You try to move in time, but it's too late. The cart crashes into you."
    show g aaa at bounce
    n "Thankfully it's extremely lightweight, and you don't fall over."
    show g
    n "You look down at the cart to see what is very clearly three cores in a trench coat."

    show g look
    gu "Sorry, sorry. It's hard to control this thing."

    mc "Are you - are you alright?"

    show g
    gu "Me? Why, y-yes, of course, why do you ask?"

    mc "It just looks like there's three -"

    show g aaa
    gu "Whoops! Got to go!!"
    show g look
    gu "Late for a, um, very important meeting! Yes, that's it!"

    n "With a few clicks of what's probably some sort of control panel, the cart turns and speeds off past you."

    hide g with easeoutright
    show e shock
    with easeinright

    mc "What... what was that?"
    
    e "That... was Gregory. He's - or, they're... or, uh..."

    show e
    e "You know what? We have more important business. Come along!"

    jump robday1

label robday1:

    show e
    n "Still left with more questions than answers, you follow Miss Esther."

    scene robtemproom with pixellate
    n "Eventually, you approach a door with \"GYM\" written on it. Not a sign of any other human employees, though."
    n "You open the door to see a core behind a desk, red pupil twitching as it watches a TV screen above it."

    show r yell with easeinright
    r "GO! GO!! What are you DOING?! THROW IT!!"

    if ball == True:
        n "The screen seems to be playing back an old recording of an American football game."
    else:
        n "The screen seems to be playing back a game of some kind, but you don't know enough about sports to tell which one."
    show r angry
    r "Sorry, with you in a sec."
    show r yell
    r "THROW THE GODDAMN BALL, WHAT ARE YOU WAITING FOR?!"

    hide r with easeoutright
    show e annoy with easeinright
    e "Rob, it's 3 minutes of your day. That's all we ask for every time we come by."

    hide e with easeoutright
    show r angry with easeinright
    r "Yes, yes, Essie. One sec."
    show r yell
    r "AHH, DAMN IT!! CAN'T YOU DO ONE GODDAMN THING RIGHT?"

    show r angry
    n "The core shakes his chassis."

    r "Sorry, sorry, yeah, I'm here, I'm present."

    show e b annoy at bounce
    e "We're here for your check-in."
    hide e b

    show r
    r "Yea, that's what I figured. This the new temp?"

    mc "Yes, that would be me. I'm assuming you're Rob?"

    r "At your service. I'm in charge of maintaining this here gym. If it was ever used..."

    mc "Do you not get a lot of people in here?"

    show r angry
    r "Not really. Too busy with their fancy science to get some exercise in."

    menu:
        extend ""

        "That's too bad. This place is pretty well-kept.":

            $ romance_points["Rob"] += 3
            jump impressrob
        
        "Not much time for exercise when you're changing the world.":

            $ romance_points["Rob"] -= 3
            jump offendrob
        
        "I mean, as long as someone uses it every now and then, right?":

            $romance_points["Rob"] -= 1
            r "Yeah, I suppose so."
            mc "Keep it up."
            jump robday1cont

label impressrob:

    show r
    r "Why, thank you. I try to keep in nice just in case someone needs it."
    r "I do get the occasional customer, but it's only about once a week."
    r "So I spend my shifts watching the game instead."

    mc "Sounds fun."

    r "You should come try out the machines some time."

    mc "I just might."

    jump robday1cont

label offendrob:


    r "It's still important. Not much time for saving the world when you're DEAD."

    mc "I don't think a lack of exercise will {i}kill{/i} you-"

    show r yell
    r "It CAN! Trust me, I've seen it happen. Like those humans in the stasis pods right now."
    show r angry
    r "They're gettin' no exercise while they're sleepin'. And when they wake up? They'll wither away."

    hide r with easeoutright
    show e shock with easeinright
    e "You really shouldn't get him started. He likes to rant."
    e "Just... slowly back away."

    jump robday1cont

label robday1cont:

    hide r with easeoutright

    n "You check off \"ROB (SPORTS CORE)\" from your list. That's the whole route done!"

    with easeoutright
    show temphall
    with pixellate
    n "As you and Miss Esther proceed back to the offices, she conrgatulates you on a job well-done."

    show e
    with easeinright
    e "Despite all the interruptions, you made it through your whole route. And in record time, too."

    mc "Certainly an interesting cast of characters."

    show e annoy
    e "Yes. They tend to throw the more... eccentric cores into recreation, so they're not managing critical systems."

    mc "That makes sense."

    show e
    e "It'll be the same thing tomorrow, same route, same check-ins."
    
    scene office
    with pixellate

    show e
    with easeinright
    e "Remember to check your e-mail for any important information. I'll send you your room number and code now."
    e "Have a good night. Rest well."

    jump fdefirst

    return