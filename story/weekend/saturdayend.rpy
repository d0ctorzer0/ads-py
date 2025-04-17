label satend:
    scene black with fade
    n "It's getting late. What's your plans for tonight?"
    menu:
        "Dinner with Kris at the lounge." if inv_kris == True:
            jump satend_kris
        "Watching Heath's performance." if inv_heath == True:
            jump satend_heath
        "Visit CC to see what he's prepared." if inv_cc == True:
            jump satend_cc
        "{i}Mycena chlorophos{/i} with Aspen." if inv_aspen == True:
            jump satend_aspen
        "Watching the SuperBowl with Rob." if inv_rob == True:
            jump satend_rob

        "I think I'll just go to bed early.":
            jump satend_mc

label satend_mc:
    scene mctemproom with fade
    n "You decide to just head in for the night."
    n "It was fun to explore the facility, though."
    n "You change into your pajamas and head to bed."

    jump day7

label satend_kris:
    scene templounge with fade
    n "You enter into the lounge and look around."
    if v_greg == False:
        n "The place is vibrant. Soft jazz plays over speakers above you and there are many employees milling about."
        n "The room itself is warm and inviting, gentle wooden brown and deep red brick."
        n "It's nothing like the rest of Aperture. It feels like you've just stepped into a different world."
        n "On your left, a stage with dark blue curtains looms over the lounge."
        if inv_heath == True:
            n "That's most likely where Heath will be holding her \"performance\"."
    elif v_greg == True:
        n "The bartender greets you once more."
        bar "Welcome back. Here for the open-mic?"
        mc "Not really - I'm having dinner with a... friend."
        bar "Ah. A friend. The tables are right over that way."
        mc "Thanks."
    n "You make your way over to the tables facing the stage."
    n "Kris is sitting in the corner. It seems there's a separate area for cores."
    n "The entire section has management rails coming out from the walls."
    show k with easeinright
    k "Ah, Doctor. Glad you could join me."
    show k flirt
    k "Please, sit. I've been looking forward to this."
    n "You take a seat. There's a plate and a set of silverware in front of you."
    mc "You got me utensils?"
    show k
    k "Ah. Yes. I asked the waiter to set them up just in case you came. I can't... use forks and such, but I'm aware you have to."
    mc "I can see you got yourself a can of lighter fluid, as well."
    k "A distilled variant. I don't drink often. Only on... special occasions."
    mc "Well, I'm flattered you consider this dinner special."
    show k flirt
    k "Of course I do."
    show k
    k "What do you think of the lounge? It's fairly new, I believe."
    k "I wasn't in this section when I was activated, but this place wasn't here when I was transferred over."
    show k angry
    k "Not {i}entirely{/i} sure when they put it in, but..."
    show k
    menu:
        extend ""
        "It's very cozy in here. Not at all like Aperture.":
            pass
        "It's a little unusual. Very different.":
            pass
    k "Aha, yes, very true."
    mc "So, uh... why'd you invite me out tonight?"

    $ cutscenetextbox = True
    scene kris cutscene 2 with fade
    $ persistent.kc2 = True
    k "{color=#fff}Mmm. Quite simple, Doctor."
    k "{color=#fff}You're incredibly intriguing. I don't get to know much about you in our day-to-day."
    k "{color=#fff}Plus, it's not like we have much time to chat throughout the week, given your busy schedule."
    k "{color=#fff}And, on top of all this, you'll be gone in another week."
    k "{color=#fff}I'm simply taking the opportunity I've been given."
    k "{color=#fff}You wouldn't fault me for that, would you?"
    scene templounge with fade
    show k with easeinright
    $ cutscenetextbox = False

    mc "Of course not. And I think it is very kind of you to invite me out tonight, Kris."
    mc "I honestly don't leave my room much. Manufacturing is... exhausting."

    show k flirt
    k "I'm sure. It must be nice to have a break from that fast-paced environment."

    mc "Yes, but Miss Esther still keeps me moving."
    show k
    k "She was like that with the last employee, as well."
    mc "Whatever happened to my predecessor, anyway?"
    show k angry
    k "No one's really quite sure."
    k "He just disappeared one day. No one seems to know what happened."
    show k 
    k "Come to think of it, though, Beatrice disappeared around the same time..."
    mc "Beatrice?"
    show k angry
    k "Another core that used to be in our section. She managed the swimming pool."
    mc "Swimming pool?!"
    show k
    k "Yes. It's been shut down since she left... I believe they drained all the water, as well."
    k "It's a shame, really. She was very polite."
    mc "Interesting."

    show k flirt
    k "Enough negative talk, though, Doctor. Let's enjoy ourselves, yes?"

    n "The night is exciting - you watch the open-mic performances while conversing with Kris."
    if inv_heath == True:
        n "You even get to see Heath on the stage, although you're a little too busy with Kris to pay much attention."
    elif inv_heath == False:
        n "Heath even makes a surprise appearance, though you're a little too busy with Kris to pay much attention."
    show k
    n "He tells you about Camus' teachings about absurdism. It's interesting."
    n "The night comes to a swift end."

    mc "Thank you, Kris. This was incredible."
    show k flirt
    k "Of course, Doctor. It was a pleasure."
    k "I... enjoy your company."
    show k
    k "Now. I believe my systems are malfunctioning, so I should be going."
    k "I need to check my coolant levels. I think I'm overheating."
    mc "Of course."
    k "I will see you on Monday, Doctor."

    hide k with easeoutright
    n "And with that, he disappears back into the walls behind the lounge."
    n "You get up, thank the bartender and your waiter (even though you didn't order anything), and leave to go to bed."

    jump day7

label satend_heath:
    scene templounge with fade
    n "You enter into the lounge and look around."
    if v_greg == False:
        n "The place is vibrant. Soft jazz plays over speakers above you and there are many employees milling about."
        n "The room itself is warm and inviting, gentle wooden brown and deep red brick."
        n "It's nothing like the rest of Aperture. It feels like you've just stepped into a different world."
        n "On your left, a stage with dark blue curtains looms over the lounge."
        n "That's most likely where Heath will be holding her \"performance\"."
    elif v_greg == True:
        n "The bartender greets you once more."
        bar "Welcome back. Here for the open-mic?"
        mc "Yes, but I'm not performing. Just watching."
        bar "You can take a seat at any of the tables over there."
        mc "Thanks."
    n "You make your way over to the tables facing the stage."
    if inv_kris == True:
        n "Kris is at a table on the other side of the room. Seems like there's a specific section that management rails go to."
        n "It's separated from the rest of the \"human\" tables."
    elif inv_kris == False:
        pass
    n "You sit down fairly close to the stage."
    n "After a short while, an employee enters through the curtains."

    cw "Welcome, Aperture employees!"
    cw "Just a reminder that if you are here and {i}aren't{/i} an Aperture employee, we do have cause to escort you and/or erase your memory of this facility."
    cw "Anyways!"
    cw "Today is the Saturday open mic, and we have several performers here, some new, some returning."
    cw "Please sit back and relax, if you can, and enjoy!"
    cw "Brought to you by the Employee Morale Program."

    n "The room gently applauds him as he exits the stage."
    n "The first few showcases are interesting, though not what you came here for."
    n "Someone brings a turret onstage and does a duet with it."
    n "Another person shows off an infinite backflip using a portal gun."
    n "Yet another performs slam poetry about feeling trapped in their cubicle."
    n "All in all, it's very interesting."

    cw "Next up - Magic Core, Heath!"
    n "The room applauds gently once more, and Heath comes out through the curtains."

    $ cutscenetextbox = True
    scene heath cutscene 2 with fade
    $ persistent.hc2 = True
    "{color=#fff}She approaches the microphone, and a spotlight comes up on her."
    h "{color=#fff}Hello, Aperture! I'm glad to be on this stage once more!"
    h "{color=#fff}Say - I was just in the cafeteria the other day, and - just so you know - I'm allergic to peanuts."
    "{color=#fff}The room is silent. A single cough."
    h "{color=#fff}I asked the chef if the cake they were serving had nuts in it - he said no!"
    h "{color=#fff}When I took a bite, I immediately had to spit it out!"
    h "{color=#fff}I guess you could say... the cake was a lie!"
    "{color=#fff}A single chuckle. You don't get it."
    "{color=#fff}Maybe the joke would make more sense if a human told it?"
    h "{color=#fff}You know, Aperture was built in a giant salt mine."
    h "{color=#fff}I guess they didn't call him \"CAVE\" Johnson for nothing!"
    "{color=#fff}A couple more laughs."
    "{color=#fff}That one was pretty good."
    h "{color=#fff}Okay, okay, give me one more chance - this one's a good one."
    h "{color=#fff}What does a robot do after a one-night stand?"
    "{color=#fff}Silence. Bated breath."
    h "{color=#fff}He nuts and bolts!"
    "{color=#fff}You laugh. A good bit of laughter fills the room."
    "{color=#fff}Heath looks very happy."
    "{color=#fff}She continues for a bit, and her jokes get more laughter each time."
    "{color=#fff}Eventually, she takes her bow."
    scene templounge with fade
    show h with easeinright
    $ cutscenetextbox = False
    h "Thank you, thank you! I'll be here next week with some more!"
    n "Gentle clapping fills the room again. Heath disappears into the curtains."
    hide h with easeoutright
    n "She suddenly appears out from a wall beside you."
    show h sad with easeinright
    mc "Heath! I didn't know the walls in here were panels..."
    show h
    h "Haha, yeah, they're disguised as wood, but they're actually hiding a bunch of management rails back here."
    h "So! What'd you think of my show?"
    mc "I didn't know you told jokes on top of doing magic. I thought you were going to perform some tricks."
    show h laugh
    h "Ah, haha, I like to experiment with what I do each time."
    show h
    menu:
        extend ""
        "Well, I thought it was really funny.":
            pass
        "It started off rocky, but got really good.":
            show h sad
            h "Ah, yeah, I'm always a little nervous to start."
            mc "You? Nervous?"
            show h
            h "Don't tell anyone!"
    h "I'm glad you liked the show. Thanks for coming, Doctor."
    show h sad
    h "As soon as I came out, I looked around for you. I was so happy to see you in the audience."
    mc "Heath, I..."
    show h
    h "Ah! Hahaha! I should go! Need my beauty sleep!"
    show h sad
    h "And I think my chassis is - overheating."
    mc "But -"
    hide h with easeoutright
    n "And she's gone."
    n "You get up, compose yourself, and head back to your room to end the night."

    jump day7