label day7end:
    scene mctemproom with fade
    n "You enter back into your room."
    n "You weren't out for very long - the clock reads 12:35."
    n "You think back to Miss Esther's warning."
    mc "That was strangely out-of-character for her..."
    n "You shrug it off, for now."

    n "You have to prepare your paperwork for tomorrow."

    $ renpy.pause(1.0)

    jump day8beg

label day8beg:
    n "Before you know it, your eyes are getting heavy."
    n "For a job with not a lot to do, there sure are a lot of emails to respond to..."

    n "You take a breath, mentally prepare yourself to start work again tomorrow, and lay down in your stasis chamber."

    scene black
    with fade
    $ daynum = "8"
    $ dayday = "Monday"

    if renpy.is_skipping() == False:
        show screen daytransition
        $ renpy.pause(2.0, hard=True)
    if renpy.is_skipping() == True:
        pass

    scene mctemproom
    with fade

    n "You wake up at 07:30. It's not so bad this time."
    n "Seems your body is getting used to the new sleep schedule - something it'll regret when you go back to work in Manufacturing."
    n "You sigh, change, grab your paperwork, and head out the door."

    scene office with fade
    n "You arrive just before shift-start. Miss Esther is waiting for you."

    show e with easeinright
    e "Doctor! It's a brand-new day. A brand-new week, even."
    show e laugh
    e "Excited to get to work?"
    mc "I guess you could say I am."
    
    n "She seems unconcerned. Perhaps the warning she gave you yesterday was nothing to worry about, after all..."

    show e
    e "Excellent. Grab your paperwork - Kris is first, as usual."

    jump krisday8

label krisday8:
    scene kristemproom with fade
    n "You enter into the conference room. It seems everything is back to normal."
    n "The screen is lit up once more, and Kris is back to watching it."

    show e annoy with easeinright
    n "Miss Esther sighs. You can't tell if it's out of annoyance or relief."
    e "Happy Monday, Kris."
    n "Annoyance. It's probably annoyance."
    hide e with easeoutright
    show k with easeinright

    if positive["Kris"] == 0:
        jump p_krisday8
    elif positive["Kris"] == -1:
        jump n_krisday8

label p_krisday8:
    k "Doctor. Good to see you. Welcome back."

    if satchoose_kris == True:
        show k flirt
        k "Couldn't get enough of me, even after this weekend, hm?"
        show e b annoy at bounce
        n "Miss Esther looks at him suspiciously, but says nothing."
        hide e b
    
    show k
    k "As you can most likely tell, things are back to normal for me."
    k "Something I'm... very grateful for."

    mc "It seems that way, yes."

    show k flirt
    k "Miss Esther, you're... in high spirits today."

    show e b happy at bounce
    e "I suppose I am. Not entirely sure why, but..."
    e "...take what you can get, Kris."
    hide e b

    show k
    k "Oh, do not worry. I will."

    menu:
        extend ""
        "Is the stock doing okay today?":
            $ romance_points["Kris"] += 2
            $ priority["Kris"] -= 1
            jump p_krisday8neutral
        "I'm glad you can resume your work, Kris.":
            $ romance_points["Kris"] += 3
            $ priority["Kris"] += 1
            jump p_krisday8positive

label p_krisday8neutral:
    show k angry
    k "Yes... I did not appreciate the glitch last week that caused my panic."
    k "I spoke to Finanical about it and they assured me that it shouldn't happen again, but..."
    k "I doubt their truthfulness."

    mc "Why's that?"

    show k
    k "They've lied to me in the past. Perhaps they see me as a shell of my former glory?"
    show k angry
    k "They forget who I used to be."
    show k flirt
    k "Regardless. I do not mean to be bitter, Doctor. Forgive me."
    k "You help to... brighten my outlook, despite my pessimism."

    show k
    show e b annoy at bounce
    e "Doctor, you should -"
    
    mc "Ah, yes, Miss Esther. Finish my checklist and leave."
    show e b happy at bounce
    e "Why... yes. Exactly that."
    hide e b

    k "Go on, Doctor. As always, it was a pleasure to have you."
    
    if romance_points["Kris"] >= 13:
        show k flirt
        k "I look forward to seeing you tomorrow."

        mc "Thank you, Kris."

    n "You finish your checklist and leave the conference room."

    jump heathday8

label p_krisday8positive:
    show k flirt
    k "As am I. I may not be... entirely {i}content{/i} with what I do, but..."
    k "I feel quite... useless when I am not working."
    show k
    k "Especially considering this is my sole purpose."

    mc "Ah, yeah. I understand."

    show k flirt
    k "I knew you would."
    show k
    k "But, uh... yes. Everything is back to normal. Perfect, even. Now that you're here."

    show e b annoy at bounce
    e "Kris... watch yourself."
    hide e b 

    show k angry
    k "Ah. Yes ma'am."

    mc "You're sweet, Kris. I should be going, though."

    show k
    k "Mmm. No worries. Thank you for your concern."
    k "Have an excellent day, Doctor."

    mc "Thank you."

    n "You finish your checklist and leave the conference room."

    jump heathday8

label n_krisday8:
    k "Doctor. There you are. I was worried you'd be late again."

    show e b annoy at bounce
    e "You'll be well aware when we're late, Kris."
    hide e B

    k "And Miss Esther. Good morning to you."

    mc "I see your screen is back to being online."

    show k angry
    k "Excellent powers of observation. Yes, Financial re-activated my screen."
    
    mc "I'm assuming everything's back to normal, then?"

    show k
    k "Yes. There are some aspects of my routine I enjoy..."

    n "He looks you up and down."

    show k angry
    k "Others... not so much."

    show e b at bounce
    e "Now, Kris. Don't be rude."
    hide e b 

    show k
    k "Mmm. Forgive me."

    mc "I'm glad to see everything's alright in here, now."

    k "Mhm."

    mc "I'll... uh, be going."

    show k angry
    k "Yes. Thank you."

    n "You finish your checklist and leave the conference room."

    jump heathday8

label heathday8:
    scene temphall with fade
    n "The short trip from the conference room to the break room is once again uneventful."

    scene heathtemproom with fade
    n "You enter into the breakroom to find a frightening sight."

    show e shock with easeinright
    e "Oh my - Heath, are you alright?!"
    hide e shock with easeoutright

    show h sad with easeinright
    h "Uh..."
    h "Kind of?"

    n "Heath is pinned to the wall of the stage by 4 different knives."

    mc "How did you even -"

    h "I-I'm honestly not sure, Doctor, I..."
    show h laugh
    h "....I GOT YOU!"

    n "She suddenly whirls out of in-between the knives in an impressive feat of dexterity."

    show h
    h "You thought I was {i}actually{/i} stuck?"
    h "The GREAT AND AMAZING Heath would NEVER find herself in a predicament she couldn't escape from..."
    show h laugh
    h "Lowly knives cannot contain me!"

    show e b annoy at bounce
    e "Not really {i}magic,{/i} but..."
    hide e b

    if positive["Heath"] == 0:
        jump p_heathday8
    if positive["Heath"] == -1:
        jump n_heathday8

label p_heathday8:
    show h
    h "So... what did you think, Doctor?"
    h "Yet another amazing trick by yours truly..."
    show h sad
    h "O-Or, not {i}yours,{/i} uhh..."

    menu:
        extend ""
        "You definitely surprised me.":
            $ romance_points["Heath"] += 2
            $ priority["Heath"] -= 1
            jump p_heathday8neutral
        "I'm so glad you're okay.":
            $ romance_points["Heath"] += 3
            $ priority["Heath"] += 1
            jump p_heathday8positive

label p_heathday8neutral:
    show h laugh
    h "Hahaha! I'm so glad, Doctor."

    show h
    h "And Miss Esther? You seemed so worried!"

    show e b annoy at bounce
    e "Yes. Worried I'd be stuck with even more paperwork tonight..."
    hide e B

    h "She's so harsh."

    mc "Everything's working fine in here, Heath?"

    show h laugh
    h "Oh, yes. No complaints!"

    show h sad
    h "Although... when you stop by the gym today, could you ask Rob to turn his TV down?"
    h "It keeps breaking my concentration! I'm trying to plan my next show, and..."
    show h laugh
    h "It sometimes surprises me how thin these walls are..."
    show h
    h "...although it {i}is{/i} pretty much just management rails back there. And empty space."
    h "So I guess it's not that surprising."

    mc "Yes, I'll make sure to tell him."

    h "Great! Thank you, Doctor."
    h "Now. You should be going."
    h "Miss Esther's glaring at me. Haha!"

    n "You check the box off on your clipboard and leave the break room."

    jump gregday8

label p_heathday8positive:
    show h laugh
    h "As am I! Haha."
    show h sad
    h "Don't worry, Doctor. I'm well aware of what I can and can't do!"
    show h laugh
    h "Plus, who would've thrown the knives at me, anyway?"

    mc "You have a point."

    show h
    h "I appreciate the concern, though."
    show h sad
    h "I find I don't really take my... {i}\"safety\"{/i} into consideration when I come up with my tricks."

    show e b at bounce
    e "Oh, that much is obvious, Heath."
    hide e b 

    show h laugh
    h "But I got you both because of it!"
    show h

    mc "Everything's working fine in here?"

    h "Oh, yes. No complaints!"

    show h sad
    h "Although... when you stop by the gym today, could you ask Rob to turn his TV down?"
    h "It keeps breaking my concentration! I'm trying to plan my next show, and..."
    show h laugh
    h "It sometimes surprises me how thin these walls are..."
    show h
    h "...although it {i}is{/i} pretty much just management rails back there. And empty space."
    h "So I guess it's not that surprising."

    mc "Yes, I'll make sure to tell him."

    h "Great! Thank you, Doctor."
    h "Now. You should be going."
    h "Miss Esther's glaring at me. Haha!"

    n "You check the box off on your clipboard and leave the break room."

    jump gregday8

label n_heathday8:
    show h laugh
    h "Haha... ridiculous. Me, getting stuck!"
    show h
    h "I can't believe I finally got you, Miss Esther!"

    show e b annoy at bounce
    e "Don't oversell yourself, now."
    hide e b annoy

    h "Well then, Doctor. Come to check in on me as per usual?"

    mc "Yes, that's right."

    h "As you can see, everything's in ship-shape. Me, my equipment, my impeccable skill..."
    show h laugh
    h "So there's no need for concern!"

    mc "That's good."

    show h
    h "You should be on your way now - you've got more cores to check in on, after all!"

    mc "Ah, yes. You're right."

    show e b happy at bounce
    e "Thank you, Heath."
    hide e b 

    n "You check another box off your paperwork and leave the break room."

    jump gregday8

label gregday8:
    scene temphall with fade
    n "You begin heading upstairs towards the greenhouse."
    show e with easeinright
    n "Miss Esther follows close behind."

    mc "I couldn't help but notice that you don't seem to... get along with many other cores here."

    show e laugh
    e "Yes, I suppose you're right."
    show e annoy
    e "Honestly, I'm not sure why..."
    show e
    e "I like Aspen. He's a good kid - incredibly kind to everyone he meets."
    show e annoy
    e "And I feel for CC. His plight is an... indicator of how Aperture treats us."
    e "But I'm not sure why I can't seem to... {i}connect{/i} with any of the others."
    show e
    e "It was the same while I was in Testing. The scientists would have favorite test subjects or coworkers or supervisors..."
    show e annoy
    e "But for me, they were all the same."
    e "I was there to do my job, not much else."
    show e
    e "It's honestly only after starting this job that I began to truly... feel for others, in some aspects."
    show e laugh
    e "They used to call me the \"Sociopath Core\" while I worked in Testing... as a joke, of course."
    show e shock
    e "But I - wait a minute..."
    hide e with easeoutright
    show g with easeinright
    g "Doctor! Miss Esther! Good to see you."

    mc "Gregory? What are you doing here?"

    show g look
    g "I'm just on my way to the lounge - finished my work up top, so I'm headed down for a quick drink."

    mc "What do you do in your section, anyway?"

    show g
    g "Oh! Uhh..."
    show g look
    g "Well, C7 is mostly for meetings and visits from shareholders..."
    show g
    g "I'm an event coordinator! Kind of. I make sure that the meeting rooms are set up and all the tech's working fine."
    show g aaa 
    g "Then I leave before the important business people see me! Haha."
    show g

    menu:
        extend ""
        "That's impressive. Must take a lot of work.":
            $ romance_points["Greg"] += 6
            $ priority["Greg"] += 1
            jump impressgreg8
        "That's all you do? Set up rooms?":
            $ romance_points["Greg"] -= 3
            $ priority["Greg"] -= 1
            jump offendgreg8

label impressgreg8:
    show g look
    g "Aha, yes, it is, uh... thanks."
    g "I didn't have many meetings to set up today, so I got to clock out early."
    show g
    g "But hey! I got to run into you because of it, so, uh..."
    g "I'm glad."

    show e b annoy at bounce
    show g aaa
    g "Now, Miss Esther is starting to scare me with that glare of hers, so..."
    g "...I gotta run!"
    hide e b 

    show g
    g "I'll see you later, Doctor!"

    hide g with easeoutright

    n "And he's off."

    show e annoy with easeinright
    e "They're certainly interesting, though the slightest bit annoying..." # NEEDS REPHRASING

    jump aspenday8

label offendgreg8:
    show g look
    g "W-Well, yes, but it's not as easy as it sounds..."
    g "Every shareholder wants something different, and every manager likes a different setup..."
    show g
    g "Not only is it my job to get things ready, but it's also my job to remember everyone's preferences."
    g "Thank goodness I have thrice the processing power of a -"
    show g aaa
    g "Oh, I mean... uh..."
    show g look
    g "Ahem. I work thrice as fast as -"
    show g
    g "Y'know what? Nevermind. I've gotta go!"

    hide g with easeoutright

    n "And he's off."

    show e annoy with easeinright
    e "They're certainly interesting, though the slightest bit annoying..." # NEEDS REPHRASING

label aspenday8:
    n "The two of you finally approach the greenhouse doors."

    show e
    e "Go on now, Doctor. I'll be waiting for you."

    scene aspentemproom with fade
    n "You enter the greenhouse once more. Nothing seems out of the ordinary."