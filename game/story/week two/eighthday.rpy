label day7end:
    $ audio_crossFade(2, "music/fourteen.ogg")
    scene mcroom day with fade
    n "You enter back into your room."
    n "You weren't out for very long - the clock reads 12:35."
    n "You think back to Miss Esther's warning."
    mc "That was strangely out-of-character for her..."
    n "You shrug it off, for now."

    n "You have to prepare your paperwork for tomorrow."

    $ renpy.pause(1.0)

    jump day8

label day8:
    scene mcroom night with dissolve
    n "Before you know it, your eyes are getting heavy."
    n "For a job with not a lot to do, there sure are a lot of emails to respond to..."

    n "You take a breath, mentally prepare yourself to start work again tomorrow, and lay down in your bed."

    scene black
    with fade
    $ daynum = "8"
    $ dayday = "Monday"

    if renpy.is_skipping() == False:
        show screen daytransition
        $ renpy.pause(2.0, hard=True)

    scene mcroom day
    with fade

    n "You wake up at 07:30. It's not so bad this time."
    n "Seems your body is getting used to the new sleep schedule - something it'll regret when you go back to work in Manufacturing."
    n "You sigh, change, grab your paperwork, and head out the door."

    $ audio_crossFade(2, "music/one.ogg")
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
    $ audio_crossFade(2, "music/two.ogg")
    scene krisroom with fade
    n "You enter into the conference room. It seems everything is back to normal."
    n "The screen is lit up once more, and Kris is back to watching it."

    show e annoy with easeinright
    n "Miss Esther sighs. You can't tell if it's out of annoyance or relief."
    e "Happy Monday, Kris."
    n "Annoyance. It's probably annoyance."
    hide e with easeoutright
    show k with easeinright

    if positive["Kris"]:
        jump p_krisday8
    else:
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
    k "Oh, don't worry. I will."

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
    k "I spoke to Financial about it and they assured me that it wouldn't happen again, but..."
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
    hide e b

    k "And Miss Esther. Good morning to you, too."

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
    scene hall with fade
    n "The short trip from the conference room to the break room is once again uneventful."

    stop music fadeout 1.0
    stop music1 fadeout 1.0
    scene heathroom with fade
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
    play music three
    h "....I GOT YOU!"

    n "She suddenly whirls out of in-between the knives in an impressive feat of dexterity."

    show h
    h "You thought I was {i}actually{/i} stuck?"
    h "The GREAT AND AMAZING Heath would NEVER find herself in a predicament that she couldn't escape from..."
    show h laugh
    h "Lowly knives cannot contain me!"

    show e b annoy at bounce
    e "Not really {i}magic,{/i} but..."
    hide e b

    if positive["Heath"]:
        jump p_heathday8
    else:
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
    h "And Miss Esther? You seemed worried!"

    show e b annoy at bounce
    e "Yes. Worried I'd be stuck with even more paperwork tonight..."
    hide e b

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

    show h sad
    h "Although... when you stop by the gym today, could you ask Rob to turn his TV down?"
    h "It keeps breaking my concentration! I'm trying to plan my next show, and..."
    show h laugh
    h "It sometimes surprises me how thin these walls are..."
    show h
    h "...although it {i}is{/i} pretty much just management rails back there. And empty space."

    mc "Yes, I'll take care of it."

    show h
    h "You should be on your way now - you've got more cores to check in on, after all!"

    mc "Ah, yes. You're right."

    show e b happy at bounce
    e "Thank you, Heath."
    hide e b 

    n "You check another box off your paperwork and leave the break room."

    jump gregday8

label gregday8:
    $ audio_crossFade(2, "music/eleven.ogg")
    scene hall with fade
    n "You begin heading upstairs towards the greenhouse."
    show e with easeinright
    n "Miss Esther follows close behind."

    mc "I couldn't help but notice that you don't seem to... get along with many other cores here."

    show e laugh
    e "Yes, I suppose you're right."
    show e annoy
    e "Honestly, I'm not sure why..."
    show e
    e "I like Aspen. They're a good kid - incredibly kind to everyone they meet."
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
    $ audio_crossFade(2, "music/seven.ogg")
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
            $ priority["Greg"] += 2
            jump impressgreg8
        "That's all you do? Set up rooms?":
            $ romance_points["Greg"] -= 3
            $ priority["Greg"] -= 2
            jump offendgreg8

label impressgreg8:
    show g look
    g "Aha, yes, it does, uh... thanks!"
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

    scene aspenroom with fade
    $ audio_crossFade(2, "music/four.ogg")
    n "You enter the greenhouse once more. Nothing seems out of the ordinary."
    n "Aspen is turned away from you, watering in the back left corner."
    mc "Aspen?"

    n "They turn around."

    if positive["Aspen"]:
        jump p_aspenday8
    else:
        jump n_aspenday8

label p_aspenday8:
    show a laugh with easeinright
    a "Doctor! Come over here, please."

    n "You walk over to the back corner and stand next to them."

    show a look
    a "Check it out - chrysanthemums!"
    a "{i}Chrysanthemum × morifolium.{/i} Or, y'know, just... florist's daisy."

    mc "Oh my."

    show a
    a "They're testing micropropogation. Thankfully, a pretty harmless procedure."
    a "So they're doing really good at the moment."

    show a look
    a "They {i}should{/i} have bloomed earlier, but things get weird underground."
    a "I'm not sure how half of them still bloom at the right time of the year anymore."

    show a laugh
    a "Regardless - aren't they beautiful?"

    menu:
        extend ""
        "Almost as beautiful as you.":
            $ romance_points["Aspen"] += 3
            $ priority["Aspen"] += 1
            jump p_aspenday8positive
        "They really are very pretty.":
            $ romance_points["Aspen"] += 2
            $ priority["Aspen"] -= 1
            jump p_aspenday8neutral

label p_aspenday8positive:
    show a look
    a "O-Oh, I... um, uh..."
    a "Ahem. Uh..."
    a "Thank you, Doctor, I uh..."
    a "Don't know what to say to that."
    a "You're... quite beautiful yourself."

    show a laugh
    a "Anyways! Um, everything's working fine in here right now."

    mc "Sprinkler isn't malfunctioning at all? Moss staying far away from your internal mechanisms?"

    show a
    a "Yep! All of that!"

    show a look
    a "So you should, uh... get going. I think I need to go..."
    a "...dunk myself in the aqueduct."

    hide a with easeoutright
    n "You laugh and leave the greenhouse behind."
    jump ccday8

label p_aspenday8neutral:
    show a
    a "Anyways, that's what I wanted to show you. They just bloomed yesterday!"
    a "Everything else is working fine. Nothing to report, no concerns."
    show a laugh
    a "It seems most of the specimens have recovered from that brief power loss a few days ago, so that's good!"
    
    mc "Glad to hear."

    show a
    a "Anyways, you should probably be on your way, Doctor. Miss Esther is waiting for you."

    mc "Ah, yes. I'll be going now."

    a "See you tomorrow!"

    n "You say your goodbyes to Aspen and leave the greenhouse behind."

    jump ccday8

label n_aspenday8:
    show a with easeinright
    a "Oh, Doctor. Welcome back."
    a "Here for my check-in, right?"

    mc "Yes, that's correct."

    a "Well, everything's proceeding as normal. I don't have any complaints."
    a "We are in a delicate testing cycle right now though, so... if you could limit your time here, that would be great."

    mc "I just need to make sure you're not malfunctioning in any way."
    mc "When I started, I was told your sprinkler can cause issues, so..."

    show a look
    a "I did already say I didn't have any complaints, Doctor."
    a "If there was something wrong with my sprinkler I would have said it then."

    mc "Ah. Yes."
    mc "Uh... thank you, Aspen. I'll be going now."

    show a
    a "Thank you, Doctor. I'll see you tomorrow."

    n "You shake your head and leave the greenhouse behind."

    jump ccday8

label ccday8:
    $ audio_crossFade(2, "music/eleven.ogg")
    scene hall with fade
    show e with easeinright
    n "Miss Esther is waiting for you outside."

    e "Hello again, Doctor. Hope everything went well in there!"
    e "Let's be on our way back down to CC, now."

    show e annoy
    e "I swear..."
    e "Sometimes it feels like the trip from the main section to this upper part takes up half our shift..."

    scene hall with fade
    n "You don't run into anyone on your way to CC's room."
    show e with easeinright
    n "Miss Esther seems very happy about that."
    e "Here we are now. No noises inside the room today..."
    e "Let's go in."

    scene ccroom with fade
    $ audio_crossFade(2, "music/five.ogg")
    n "You enter into CC's room. He's staring out the window beside him."
    n "You don't know what he's looking at, considering all you can see outside it is a blank white void."

    show e with easeinright
    e "Good afternoon, CC. How has your day been?"

    hide e with easeoutright
    show c with easeinright
    c "Good, all things considered."
    c "The usual."
    show c look
    c "If you were worried I was getting better, Miss Esther..."
    show c
    c "No need to anymore. I feel worse than ever."

    show e b at bounce
    e "Oh, CC..."
    hide e b

    if positive["CC"]:
        jump p_ccday8
    else:
        jump n_ccday8
    
label p_ccday8:
    show c look
    c "Oh, and Doctor. Good to see you again."
    show c
    c "I hope you do not find my pessimism off-putting."
    c "As you're well aware, it's difficult to be positive sometimes."

    mc "I know. I understand."

    show c look
    c "Seeing your face always brightens my day, though."

    mc "Is there anything you need? Anything I can help with?"

    show c close
    c "Not that I can think of, no. I appreciate your concern, though."
    show c
    c "You make me feel like I'm not just an experiment anymore."

    menu:
        extend ""
        "You've always been more than that.":
            $ romance_points["CC"] += 3
            $ priority["CC"] += 1
            jump p_ccday8positive
        "I'm happy to help, CC. You deserve better.":
            $ romance_points["CC"] += 2
            $ priority["CC"] -= 1
            jump p_ccday8neutral

label p_ccday8positive:
    show c look
    c "I... oh."
    c "Doctor, you're... too kind to me."
    show c close
    c "Thank you."
    c "Um, you... should be going, now. More check-ins to do, yes?"
    show e b at bounce
    e "Thank you, CC."
    hide e b
    show c
    c "...please come and see me tomorrow."

    mc "I will."

    n "You check CC off your list and leave the room with Miss Esther."

    jump robday8

label p_ccday8neutral:
    show c
    c "Haha. Thank you, Doctor."
    show c close
    c "Even if you're only here for one more week, I will remember your kindness."
    show c
    c "You should go, now. I think I need some rest."

    mc "Yes. Of course. Have a good day, CC."

    show c close
    c "You as well."

    n "You check CC off your list and leave the room with Miss Esther."

    jump robday8

label n_ccday8:
    show c
    c "Oh... Doctor. My apologies, I didn't see you there."
    c "I'm assuming you two have come for my check-up."

    mc "Yes, that's correct."

    c "Well, as I just mentioned, I'm still sick, I assure you. Very much so."
    show c close
    c "No matter how much I rest, it doesn't get any better..."
    show c
    c "Of course, I know it shouldn't, but..."

    show e b at bounce
    e "I'm sorry, CC."
    hide e b 

    c "It's alright, Miss Esther. But you two should be going. I'm sure you have more to attend to."

    mc "Yes. Thank you, CC."

    n "You check CC off your list and leave the room with Miss Esther."

    jump robday8

label robday8:
    scene hall with fade
    show e annoy with easeinright
    n "Miss Esther is quiet on the way to the gym."
    n "Her mood seems to flip on a dime - incredibly happy and energetic at one point, solemn and quiet the next."
    n "It makes her hard to read."
    n "You approach the gym door without any interruptions."

    scene robroom with fade
    $ audio_crossFade(2, "music/six.ogg")
    show r with easeinright
    if positive["Rob"]:
        jump p_robday8
    else:
        jump n_robday8

label p_robday8:
    r "Doc! Essie! How's it hanging?"
    r "Good to see you both alive."

    show e b annoy at bounce
    e "Why wouldn't we be alive?"
    hide e b 

    show r angry
    r "Ah, you never know what could happen, yeah?"
    show r
    r "Can't ever be too careful!"

    mc "Nice to see you again, Rob. Everything's alright in here?"

    r "Yep! All good, as per -"
    show r yell
    if persistent.streammode == True:
        r "ARE YOU KIDDING ME? WHY WOULD YOU DO THAT?! {k=-5}————{/k}!!"
    else:
        r "ARE YOU KIDDING ME? WHY WOULD YOU DO THAT?! DUMBASS!!"
    show r
    r "...as per usual, yeah."

    show e b annoy at bounce
    e "I really wish you'd stop yelling so much, Rob."

    show r angry
    r "Agh, sorry, Essie."

    show e b at bounce
    e "And stop calling me Essie. That's {i}Miss Esther{/i} to you."
    hide e b

    show r
    r "Habits! What can ya do, yeah?"
    r "Anyway, Doc, it's all good."

    mc "Oh - Heath asked me to tell you to turn your TV down."

    show r angry
    r "She can hear it all the way over there?"
    r "Yikes. She must hate me, haha."

    show r close
    r "Ah, I gotcha. I'll turn it down. My bad."

    menu:
        extend ""
        "Thank you, Rob.":
            $ romance_points["Rob"] += 2
            $ priority["Rob"] -= 1
            jump p_robday8neutral
        "You're a good man. Thank you.":
            $ romance_points["Rob"] += 3
            $ priority["Rob"] += 1
            jump p_robday8positive

label p_robday8neutral:
    show r
    r "'Course, Doc."
    r "Now you should prolly -"
    show r yell
    r "GO! GO!! COME ON! WHAT THE HELL, JACOB?"
    show r angry
    r "- get goin'. S'almost four, yeah?"

    mc "Ah yeah, you're right. Thanks again, Rob."

    show r
    r "Yeah, s'no problem. See ya tomorrow!"
    
    n "You finish off your checklist and head back towards the office."

    jump day8end

label p_robday8positive:
    show r angry
    r "Ah, uh, thank you, Doc. Kind of you to say that."
    show r
    r "Even though I ain't really a man and all that, but..."
    r "I'm pickin' up what you're puttin' down."

    show e b annoy at bounce
    e "Eugh."
    hide e b

    r "Now you should prolly -"
    show r yell
    r "GO! GO!! COME ON! WHAT THE HELL, JACOB?"
    show r angry
    r "- get goin'. S'almost four, yeah?"

    mc "Ah yeah, you're right. Thanks again, Rob."

    show r
    r "Anytime, Doc. Always willing to do ya some good."
    r "If there's anything else I can do for you..."

    show r angry
    r "...just let me know."

    mc "Will do."

    show r
    r "See ya tomorrow!"

    n "You finish off your checklist and head back towards the office."

    jump day8end

label n_robday8:
    r "Essie! And you brought the Doc with you."

    mc "Just here for the regular routine checkup."

    show r angry
    r "Ah, yeah. Why else would you be here?"
    show r close
    r "Not like you care 'bout ol' Rob, anyhow."

    show r
    show e b at bounce
    e "Now, Rob, let's be professional, here."
    hide e b 

    r "Kinda hard when I'm not treated with respect, Essie."

    show e b annoy at bounce
    e "To be entirely fair, you don't show me much respect, either."
    hide e b 

    show r angry
    r "Got me there."
    show r
    r "Anyway. Everything's runnin' fine, so you don't gotta put any little notes on your clipboard there."

    mc "Oh - Heath did ask me to tell you to turn your TV down."

    show r angry
    r "She can hear it all the way from down there?"
    r "Yikes. She must hate me, haha. That makes two of ya, I suppose."

    show r close
    r "I'll turn it down. She's got nothing to worry about."

    mc "Thank you."

    show r angry
    r "Alrigh', now, you should get goin'. I don't wanna miss any of my game for this."

    mc "We'll be leaving."

    n "And with that, you finish off your checklist and head back to your office."

    jump day8end

label day8end:
    $ audio_crossFade(2, "music/one.ogg")
    scene office with fade
    show e with easeinright
    e "Well! Uneventful day, all things considered."
    show e laugh
    e "That's the way I like it! Haha."

    show e
    e "Now - expect the normal routine. You should check your email before heading to bed."
    e "Thank you for your work today, Doctor. I will see you tomorrow."

    jump e8first