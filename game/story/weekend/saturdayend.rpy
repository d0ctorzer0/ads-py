label satend:
    scene black with fade
    n "It's getting late. What's your plans for tonight?"
    menu:
        "Dinner with Kris at the lounge." if inv_kris == True:
            $ satchoose_kris == True
            jump satend_kris
        "Watching Heath's performance." if inv_heath == True:
            $ satchoose_heath == True
            jump satend_heath
        "Visit CC to see what he's prepared." if inv_cc == True:
            $ satchoose_cc == True
            jump satend_cc
        "See the glowing algae with Aspen." if inv_aspen == True:
            $ satchoose_aspen == True
            jump satend_aspen
        "Watching the SuperBowl with Rob." if inv_rob == True:
            $ satchoose_rob == True
            jump satend_rob

        "I think I'll just go to bed early.":
            jump satend_mc

label satend_mc:
    play music fourteen
    scene mcroom night with fade
    n "You decide to just head in for the night."
    n "It was fun to explore the facility, though."
    n "You change into your pajamas and head to bed."

    jump day7

label satend_kris:
    play music two
    scene lounge with fade
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
    k "Ah, Doctor."
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
    show screen cuttextbox
    python:
        if persistent.kc2 == False:
            persistent.cutscenes_seen += 1
            persistent.kc2 = True
        achievement.progress("ach_picture", persistent.cutscenes_seen)
        achievement.sync()
    if persistent.advcap == True:
        "{i}{color=#fff}The scene fades to Kris looking at you, lit by candlelight."
    k "{color=#fff}Mmm. Quite simple, Doctor."
    k "{color=#fff}You're incredibly intriguing. I don't get to know much about you in our day-to-day."
    k "{color=#fff}Plus, it's not like we have much time to chat throughout the week, given your busy schedule."
    k "{color=#fff}And, on top of all this, you'll be gone in another week."
    k "{color=#fff}I'm simply taking the opportunity I've been given."
    k "{color=#fff}You wouldn't fault me for that, would you?"
    scene lounge with fade
    hide screen cuttextbox
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
    play music three
    scene lounge with fade
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
    python:
        if persistent.hc2 == False:
            persistent.cutscenes_seen += 1
            persistent.hc2 = True
        achievement.progress("ach_picture", persistent.cutscenes_seen)
        achievement.sync()
    show screen cuttextbox
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
    scene lounge with fade
    hide screen cuttextbox
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

label satend_aspen:
    play music four
    scene aspentemproom with fade
    n "You enter into the greenhouse, which much darker inside than usual."
    n "It's almost dead-silent - no hissing of sprinklers or whirring of Aspen's management rail."
    n "It's a little terrifying."

    mc "Aspen?"

    n "Silence. You wonder if they decided to just call it a night."

    mc "Aspen, I'm -"
    
    n "You step forward and look to your left. The door that's usually closed on the far side of the room is now open, and a soft blue light is emanating from within."
    n "You approach the door cautiously."

    mc "Aspen?"

    show a look with easeinright
    n "You step into the room to see Aspen looking down at a water pool."
    n "Manufactured waves ebb and flow across the surface, moving the algae."
    show a
    a "Doctor! Glad you could make it."
    a "Isn't it beautiful? Haha."

    mc "Wow."

    n "The algae glow a vibrant blue-green light, unlike anything you've ever seen."
    $ cutscenetextbox = True
    scene aspen cutscene 2 with fade
    show screen cuttextbox
    python:
        if persistent.ac2 == False:
            persistent.cutscenes_seen += 1
            persistent.ac2 = True
        achievement.progress("ach_picture", persistent.cutscenes_seen)
        achievement.sync()
    acg "{color=#fff}I mean, I'm sure you've seen things glow before, but... this is different, yes?"
    acg "{color=#fff}{i}Pyrodinium bahamense{/i}. That's their binomial name."
    acg "{color=#fff}But a lot of us just refer to them as their superclass."
    acg "{color=#fff}I personally think using their full name can be important..."
    acg "{color=#fff}They're on loan to us from Marine Studies. We generally don't carry much sea life in Botany."
    acg "{color=#fff}It's a rare treat."
    acg "{color=#fff}I'm glad you're here."

    mccut "{color=#fff}Aspen, this... is beautiful."
    scene aspentemproom with fade
    show a look with easeinright
    hide screen cuttextbox
    $ cutscenetextbox = False

    a "I'm really happy you could make it. I was excited to show you this."
    a "You've shown a lot of interest in plant life, something I'm really passionate about..."
    show a
    a "I just hope you know that I really appreciate you, Doctor."

    mc "I appreciate you too, Aspen. It's been wonderful to learn what little you've shown me."
    mc "I'd honestly be interested in hearing even more."
    
    show a look
    a "It's such a shame that you're only here for one more week."
    a "I have so much I could tell you..."

    show a
    mc "I promise I'll come by and visit. Then you can tell me as much as you'd like."

    a "No, that can't work. Once you're back in Manufacturing, you won't be permitted to come into the greenhouse."
    show a look
    a "And I'm not permitted to leave..."
    show a laugh
    a "Which just means I'll need to take every opportunity I can to teach you!"

    show a
    n "Under the light of the algae, Aspen begins rattling off about every botany fact they can think of."
    show a laugh
    n "It's a lot. How they know so much, you'll never understand."
    n "You suppose it's just the passion they have for the craft."
    n "Before long, you've been here for over an hour, just listening to them."

    show a look
    a "Oh, uh, Doctor, I'm incredibly sorry, it seems I've kept you here way too late."

    mc "Ah, yes. I didn't realize how tired I was until just now, haha."

    a "I know you need your rest and everything, so..."
    show a
    a "Thank you. Again. For visiting me. It's always... so good to be with you."
    a "I can't wait to see you again on Monday."

    mc "Likewise."

    n "You hesistate, but leave the greenhouse behind and head to bed."

    jump day7

label satend_rob:
    play music six
    scene bioroom with fade
    n "You approach the door to the gym. It's mostly dark through the window, although you can see a faint light through the frosted glass."
    n "On the door is a sign that says \"CLOSED FOR REPAIRS\"."
    mc "Yeah, right."

    n "You knock."

    r "Uh, sorry, we're closed!! The sign?? Hello?"

    mc "Rob, it's me."

    r "Agh!! Doctor! One sec, one sec..."

    n "There's a bit of light crashing before you hear the whirring of a door lock."
    r "Should be open now, come on in!"

    n "You open the door and step in."
    n "Just like you thought, the faint light you saw from outside the window was, in fact, the TV."

    show r with easeinright
    r "Glad ya came, Doc. I was just about to start the game."
    r "Take a seat! Take a seat."

    n "You sit down and look up at the TV."
    mc "I've been meaning to ask why your TVs are in such a weird aspect ratio."
    mc "Isn't that the same size most of the new monitors are?"

    show r angry
    r "Ah, yeah. The boss wanted this newly-invented \"widescreen\" put into everything - our TVs, monitors..."
    r "That man loved anything with \"science\" in it..."
    r "Another reason barely anyone comes in here. Everyone's too obsessed with science thanks to that brute."

    mc "Well, not everyone. I'm more interested in engineering than whatever they do up in testing."

    show r
    r "Prolly why you and I get along so well."
    r "Anyway, the people up on the surface still haven't all switched over to widescreen, so..."
    r "...all my programs are still in the usual 4 by 3. Sorry."

    mc "Oh no, it's okay."

    n "You hear a click sound, and the playback on the television starts."

    ann "Do you want the heavy favorite, the San Francisco 49ers, going for their third Super Bowl win this decade..."
    ann "...or the underdogs by 7 points, the Cincinnati Bengals, trying to celebrate their 200th year as an American city with their first Super Bowl win?"
    n "The announcer welcomes you to the Superbowl XXIII."

    show r angry
    r "Y'know, Doc, I don't think anyone's ever sat down to watch a game with me."
    r "So... in a way, this is kind of a date, huh?"

    mc "Haha. Maybe."

    show r
    r "Well. Hope my temper doesn't scare ya too bad."
    r "Oh - check it out, the game's startin'."

    n "You don't understand a lot about what you're watching, but it doesn't bother you too much."

    show r yell
    r "GO! GO! COME ON, YOU GOT THIS!"
    
    n "Rob's energy is contagious. Before you know it, you've joined in."

    mc "YOU'RE ALMOST THERE, COME ON!"
    show r
    r "HELL YEAH!"
    mc "Touchdown!!"
    $ cutscenetextbox = True
    scene rob cutscene 2 with fade
    python:
        if persistent.rc2 == False:
            persistent.cutscenes_seen += 1
            persistent.rc2 = True
        achievement.progress("ach_picture", persistent.cutscenes_seen)
        achievement.sync()
    show screen cuttextbox
    if persistent.advcap == True:
        "{i}{color=#fff}The scene fades to a dark room lit by a TV screen. Rob turns back to look at you."
    r "{color=#fff}Now you're getting into it, Doc."
    r "{color=#fff}Never thought you'd be one to yell."
    mccut "{color=#fff}What can I say? You got me pumped up."
    r "{color=#fff}Hahaha! I'm so glad. Thanks for joinin' me tonight."
    r "{color=#fff}You really didn't have to, but..."
    r "{color=#fff}S'been a long time since I last had some proper company."
    r "{color=#fff}So I appreciate it."
    hide screen cuttextbox
    scene robtemproom with fade
    show r with easeinright
    $ cutscenetextbox = False

    n "The game's exciting. Rob explains the basics of football to you so you can keep up with what's going on."
    n "Before you know it, the game's over."

    show r yell
    r "YEAH!! 49ERS TAKE IT!"
    show r
    r "That's my team right there. I've been so hyped for the Superbowl 'cuz they made it all the way this year."
    r "Anyway. That's all, Doc. Game's over."

    mc "Aw, that's too bad. I was having fun."

    r "There's always more - you can stop in any time to join me."
    show r angry
    r "Please don't hesitate, Doc. I really enjoy your company."
    mc "Yours too, Rob. Your energy's infectious."
    show r
    r "Haha! I'm glad."
    r "Welp. I guess I'll catch you on Monday, then."
    mc "Guess so."
    n "You get up to leave the gym."
    show r angry
    r "Wait - Doc."
    mc "What's up?"
    r "Thanks for not judging me. A lot of the other cores... they think I'm too loud. Too crazy..."
    r "Hell, my ex-wife left me cuz of that."
    r "Sports are my passion, and she just... couldn't really accept that."
    r "It feels good to have someone who does around now."
    mc "Of course, Rob."
    r "Goodnight, Doc."
    mc "Goodnight."

    n "You leave the gym and head back to your room."

    jump day7

label satend_cc:
    play music five
    scene bioroom with fade
    n "You approach CC's door. It's quiet. You knock."
    mc "CC, it's me."
    c "Doctor. Come in, please."
    n "You slowly open the door."
    $ cutscenetextbox = True
    show screen cuttextbox
    scene cc cutscene 2 with fade
    python:
        if persistent.cc2 == False:
            persistent.cutscenes_seen += 1
            persistent.cc2 = True
        achievement.progress("ach_picture", persistent.cutscenes_seen)
        achievement.sync()
    n "{color=#fff}CC greets you with a raised optic. In between his chassis and his handlebars is a bouquet of red roses."
    ccg "{color=#fff}I hope this isn't too... forward, Doctor."
    ccg "{color=#fff}Aspen assisted me in acquiring the flowers, so... it wasn't entirely my work."
    ccg "{color=#fff}They remind me of you, though. In a way."
    ccg "{color=#fff}Please... accept them."
    mccut "{color=#fff}Oh, CC..."
    scene ccroom with fade
    hide screen cuttextbox
    show c look with easeinright
    $ cutscenetextbox = False
    n "You take the bouquet from between his handlebars."
    mc "Thank you, CC. These are beautiful."
    mc "I can't believe you went out of your way just for me."
    show c
    c "Aha... it wasn't all that easy, especially because Aspen and I can't leave our rooms, but..."
    c "We made it work."
    show c close
    c "Thank you for coming back to see me, Doctor. I was afraid you wouldn't."
    show c look
    c "Miss Esther is kind, but... I've never had any of the human scientists show me as much grace as you have."
    c "It is truly unfortunate that you will only be here one more week."
    mc "I agree. I've really enjoyed my time in maintenance."
    show c
    c "Doctor, please... will you stay a little longer?"
    show c look
    c "I could use your company."
    mc "Of course, CC."
    show c
    c "Thank you."

    show c close
    n "You spend the evening with CC, mostly in quiet contemplation."
    n "Occasionally, he'll have a thought or idea he brings up to you, but otherwise you sit in silence."
    
    c "I sometimes feel like my room is in a world separate from the rest of Aperture."
    c "Because I'm so isolated, I rarely see anyone other than Miss Esther and the maintenance attendant."
    c "It feels like I live in my own little bubble."

    mc "I understand that."

    show c look
    c "It's always a little more lively when you visit, though."

    show c close
    n "Before you know it, it's very late, and you're beginning to get tired."

    show c
    c "Please, Doctor. If you're tired, you should go to bed."
    mc "Ah. Yes. I should."
    c "Thank you again for coming by tonight."
    show c look
    c "I will see you on Monday."

    jump day7