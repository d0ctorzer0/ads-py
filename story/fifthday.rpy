label day5:
    scene mctemproom
    with fade

    n "You make it to your room, change into your bedclothes, and prepare to sleep."
    n "Tomorrow's the last day of the week, and maintenance doesn't work on the weekends, other than being on-call."
    n "You're excited for your first day off, though a little curious what you'll do if you can't leave the campus."
    n "Before you know it, you're fast asleep."

    scene black
    with fade
    $ daynum = "5"
    $ dayday = "Friday!"

    show screen daytransition
    $ renpy.pause(2.0, hard=True)

    scene mctemproom with fade

    n "You wake with a start." 
    n "You think you were dreaming, but that's not possible in stasis."
    n "You get up and check your wardrobe. What should you wear for casual friday?"

    menu:
        extend ""
        "A t-shirt and jeans.":
            $ tshirt = True
            $ romance_points["Aspen"] += 1
            $ romance_points["Greg"] += 1
            n "You put on a regular old t-shirt and blue jeans, and head out the door to work."
        "Your best formalwear.":
            $ formal = True
            $ romance_points["Kris"] += 1
            $ romance_points["Heath"] += 1
            n "You put on your best date-night attire, and head out the door to work."
        "A Hawaiian shirt and khakis.":
            $ vaca = True
            $ romance_points["Rob"] += 1
            $ romance_points["???"] += 1
            n "You put on your vacation clothes, and head out the door to work."
        "Just your regular uniform.":
            $ uniform = True
            $ romance_points["CC"] += 1
            $ esther_affection += 1
            n "You decide to just wear your uniform as regular, sling the lab coat over your shoulders, and head out the door to work."

    scene office
    with pixellate

    n "Miss Esther is waiting for you patiently when you enter."

    show e with easeinright

    if tshirt == True:
        e "Ahh, Doctor. I see you went with the classic \"casual\" outfit today! Very nice."
    if formal == True:
        e "Ahh, Doctor. \"Casual\" doesn't mean \"black-tie event\", but I suppose it works regardless. Dashing."
    if vaca == True:
        e "Ahh, Doctor! Planning on going on a cruise? Whatever that is..."
    if uniform == True:
        e "Ahh, Doctor. Went the simple route I see? No worries. It's not for everyone."

    show e
    e "Today's the last day of the week! Any exciting plans for the weekend?"

    menu:
        extend ""
        "I was thinking I'd just stay in my room and do some reading.":
            show e shock
            e "There's plenty more to do around here than sit and read!"
            show e
            e "But it's your time off, so feel free to do whatever you wish."
        "Gregory invited me to go meet him at the gym. I might do that.":
            e "Interesting. Well, it's your time off. You're free to do whatever you please."
        "Honestly, I was just planning on wandering. Maybe finding a bar?":
            show e laugh
            e "A bar? Haha, that's hilarious, Doctor."
        "I have absolutely no clue.":
            show e laugh
            e "Fair enough. I suppose you aren't used to being on-campus on your days off."
    
    show e
    e "Well, we should be on our way, then. Grab your clipboard, and let's get going."
    n "You get your paperwork and follow Miss Esther out the door."

    jump krisday5

label krisday5:
    scene kristemproom with pixellate

    n "You enter the conference room to find things much calmer than yesterday."
    n "In fact, the screen that is usually moving so vibrantly and quickly is turned off."

    mc "Kris? Is something wrong?"

    show k with easeinright
    k "Oh... Doctor."

    if tshirt or vaca == True:
        k "You look... comfortable today."
    if formal == True:
        show k flirt
        k "You look... incredible today."
    
    show k
    k "Uh... No. Nothing is wrong. Everything is alright."

    show e b sad at bounce
    e "Kris, your screen. It's off."
    hide e b

    k "Yes, I'm aware. Financial thinks I... need to take a day away from it."

    mc "Why?"

    show k flirt
    k "I'm not sure. Perhaps it has something to do with my... panicking yesterday."

    menu:
        extend ""
        "But you calmed down from that.":
            $ romance_points["Kris"] += 3
            jump impresskris5
        "I suppose that makes some sense.":
            $ romance_points["Kris"] -= 3
            jump offendkris5
        "They think you can't handle it?":
            $ romance_points["Kris"] += 1
            jump neutralkris5

label impresskris5:
    show k
    k "Haha, I'm well aware."

    show k angry
    k "I'm unsure exactly why they decided I needed a break, seeing as I don't work tomorrow regardless, but..."
    k "I suppose it's of no consequence."

    show k
    k "The stock's back to normal after all..."

    show k flirt
    k "Turns out it was a bug in the system. Go figure."

    mc "That's unfortunate, Kris. You were so worried."

    show k
    k "Yes. Yes I was."

    # set positive for the next week
    if romance_points["Kris"] >= 10:
        $ positive["Kris"] = 1
        show k flirt
        k "Uh, before you leave, Doctor..."
        k "You've been very kind to me this week. I'd just like to... extend my gratitude to you."
        show k
        k "The man who worked your position before you, he..."
        show k angry
        k "Was not as... gentle as you are."

        show k
        mc "Thank you, Kris. You've been very kind yourself."
    elif romance_points["Kris"] <= 9:
        pass

    jump krisday5cont

label neutralkris5:
    show k angry
    k "Again, I'm not sure. Perhaps that's the reasoning behind it."
    if wkd3 == True:
        k "Frankly, as I've told you before, I believe this just another way to get us out of the picture..."
    k "Regardless. I won't complain about having a day off."
    show k
    k "I just hope this doesn't become a theme."

    show e b at bounce
    e "As do I..."
    hide e b 
    jump krisday5cont

label offendkris5:
    show k angry
    k "Sense? It makes no sense at all! In fact, the idea is frankly ridiculous."
    k "I have been doing this for nearly 3 years now - almost half my lifespan!"
    k "I will not tolerate this disgrace to my intelligence..."

    if romance_points["Kris"] <= 0:
        $ positive["Kris"] = -1
        show k flirt
        k "You've been incredibly rude to me over the past week, Doctor..."
        k "I'm not sure what I did to upset you, but..."
        k "I don't appreciate it in the slightest."
    elif romance_points["Kris"] > = 1:
        pass  
    jump krisday5cont

label krisday5cont:
    show k flirt
    k "You should go now, Doctor. I know you have a schedule to keep." # this line needs to be recorded twice - once negatively and once positively

    mc "Yes, you're very right."

    hide k with easeoutright
    show e annoy with easeinright

    e "Wow, I didn't even have to tell you to hurry it up this time..."

    n "You check Kris off your list for the last time this week and head out the door."

    jump heathday5

label heathday5:
    scene heathtemproom with pixellate
    
    n "You enter into the break room. Heath isn't in the doorway this time - instead, she's waiting patiently up on the stage."

    show h with easeinright
    h "Doctor! Apologies for yesterday. Are you ready for yet another trick?"

    n "You hear what sounds like mechanics whirring, a puff of air, and then -"
    n "A cloth starts coming out of Heath's chassis. A load of differently-colored scarves -"

    show h laugh
    h "Tada!"

    show e b annoy at bounce
    e "I don't see what the appeal of this \"trick\" is."
    hide e 

    show h sad
    h "Just you wait, Miss Esther..."

    show h
    n "At least 10 meters of scarf has now exited Heath's chassis, and it's still going."
    n "Cores aren't very large - a little bigger than a basketball, at most."
    n "How she fit this much cloth into such a tiny compartment, let alone while avoiding her circuitry, {i}and{/i} without hands..."
    n "You're not sure."

    show e b happy at bounce
    e "What the -"
    hide e b 

    show h laugh
    n "Finally, the cloth ends. In total, it's probably around 25 meters in length."

    menu:
        extend ""
        "Oh my god! How in the world did you do that?!":
            $ romance_points["Heath"] += 3
            jump impressheath5
        "I've seen better, but that was impressive!":
            $ romance_points["Heath"] -= 3
            jump offendheath5
        "Is stuffing all that cloth in you... safe?":
            $ romance_points["Heath"] -= 1
            jump neutralheath5

label impressheath5:
    h "Why, a magician never reveals her secrets, Doctor."

    show h
    h "It isn't easy, though, that's something I can guarantee!"

    mc "That was very impressive, Heath. As usual."

    h "Thank you, thank you, Doctor. Your applause is ALWAYS appreciated!"

    show e b happy at bounce
    e "I'm not going to lie, Heath. That actually surprised me."
    hide e b 

    show h laugh
    h "Ha! I even got ice queen Miss Esther to applaud me!"

    if romance_points["Heath"] >= 10:
        $ positive["Heath"] = 1
        show h sad
        h "By the way, Doctor..."
        h "Thank you for being so kind to me this week."
        h "I've never had such a captive audience before."

        show h
        h "I hope you'll keep coming by to see me."
        
        mc "Don't worry, Heath. I will."
    elif romance_points["Heath"] <= 9:
        pass

    jump heathday5cont

label offendheath5:
    show h sad
    h "You've seen better?!"
    h "Ah, I suppose human magicians have more appendages to use..."

    show h
    h "No worries! I guarantee I'll get you next time!"
    
    show h sad
    h "Maybe..."

    if romance_points["Heath"] <= 0:
        $ positive["Heath"] = -1
        h "Y'know, Doc... I've really tried this week..."
        h "Pulled out all the stops so you'd enjoy my performances."
        h "I guess not every person likes magic, though."
    elif romance_points["Heath"] >= 1:
        pass

    jump heathday5cont

label neutralheath5:
    show h
    h "Ah, yes. It should be fine - I've done this trick many times over."

    show h laugh
    h "Concerned about me, are you? Why Doctor, if you're not careful..."

    show e b annoy at bounce
    e "Ugh. Heath..."
    hide e b 

    show h
    h "Yes, yes, Miss Esther, haha."

    jump heathday5cont

label heathday5cont:
    show e b at bounce
    e "Doctor, are you ready to head out?"
    hide e b

    mc "Ah, yes, Miss Esther. Let's go."

    # it would be really funny if i added a smoke.mp4 here LMAO
    n "Suddenly, a puff of smoke comes up from the stage. After you finish coughing, you look up to find..."

    hide h with easeouttop
    n "...Heath has disappeared."

    show e annoy with easeinright
    e "I swear, that girl gets on my nerves sometimes..."

    mc "You check Heath off your checklist once more and head out of the break room."

    jump aspenday5

label aspenday5:
    scene temphall with pixellate
    show e with easeinright
    n "You begin to head up towards the greenhouse with Miss Esther."

    mc "So... tomorrow. What am I allowed to do on-campus when I'm not working, anyway?"

    e "Well, there's a few locations you wouldn't be allowed into."
    e "Storage facilities, for one. Or anywhere in the residential block."

    show e laugh
    e "Other than your own room, of course!"

    show e
    e "You could always check out the sect below this one. I believe the relaxation center is down there... somewhere."

    mc "That's where they keep the test subjects in stasis, yes?"

    show e annoy
    e "Yes, although I believe they've begun to phase that program out..."
    show e shock
    e "Don't quote me on that, though."

    show e
    e "Oh! There's also a lounge down there, I believe. For the humans, after they get out of stasis."
    e "I believe the new CEO installed that only recently, with the new funds Aperture's been pulling in."

    mc "Interesting. Manufacturing is also below us, I believe, but I've never heard of there being a lounge..."

    e "Manufacturing {i}is{/i} quite large. Perhaps you've simply never encountered it."

    e "We're here now. Go on in."

    scene aspentemproom with pixellate

    show a look with easeinright

    a "Doctor, Doctor, now's... really not a good time, haha..."

    n "You look around the room. It's darker than usual - not a good sign for an underground greenhouse."

    mc "Is something going on?"

    show a laugh

    a "Ahh, yeah, kind of? Haha... the artificial sunlight, pumped in from the surface..."
    show a
    a "It turned off overnight. I'm not quite sure why."
    show a look
    a "When I got in this morning, things were completely dark... I had to quickly report the problem to Facilities so they could fix it."

    n "Aspen is rushing from specimen to specimen as he speaks to you, frantically checking his work."

    a "I'm afraid it was too late. And now I'm just doing clean-up before night shift gets here..."

    menu:
        extend ""
        "Is there anything I can do to help you?":
            $ romance_points["Aspen"] += 3
            jump impressaspen5
        "All the plants look just fine to me.":
            $ romance_points["Aspen"] -= 3
            jump offendaspen5

label impressaspen5:
    show a
    a "Oh, no, Doctor, this is my job. Plus, you aren't cleared to work on this."
    show a look
    a "I appreciate it, though."
    show a
    a "I've already sent an email to Facilities asking them to increase the sunlight output for a while, but..."
    a "...can you send them one as well? Your input might be more convincing for them."
    show a laugh
    a "I don't think they respect me very much..."

    mc "Yes, I'll do that, Aspen."

    show a
    a "Thank you, Doctor."

    if romance_points["Aspen"] >= 10:
        $ positive["Aspen"] = 1
        show a look
        a "And... thank you. For your treatment of me this week."
        a "You've been very respectful and, uh... very kind."
        a "I'm not used to it. It's a little strange."
        a "But thank you."

        mc "You're welcome, Aspen."
    elif romance_points["Aspen"] <= 9:
        pass

    show a
    mc "I should be going now. Good luck in here."
    mc "I'll make sure to send that email tonight."

    a "Yes. I'll see you on Monday, Doctor."

    jump ccday5

label offendaspen5:
    show a laugh
    a "Oh, that's funny - no, no. They look okay from the outside, but on the inside..."
    show a look
    a "They're dying. Without the sunlight for that long, and this deep into the facility..."
    show a
    a "It's dangerous. We might lose half of these specimens because of this."

    mc "Well, you're the expert, I suppose."

    show a laugh
    a "Yes, I am, I guess."

    if romance_points["Aspen"] <= 0:
        $ positive["Aspen"] = -1
        show a look
        a "You're a lot like the previous maintenance employee..."
        a "He didn't care much for botany, either."
        a "It's alright, though. It's not for everyone."
    elif romance_points["Aspen"] >= 1:
        pass

    show a
    mc "I should be going now. Good luck in here."

    a "Yes. I'll see you on Monday, Doctor."

    jump ccday5

label ccday5:
    scene temphall with pixellate
    show e with easeinright
    e "Doctor, welcome back out. Let's head back down."

    n "You head toward the residential block with Miss Esther."

    if askestherday2 == True:
        n "You turn to her."

        mc "Miss Esther - you said you used to work in Testing? What was your job there?"
    
        show e shock
        e "Oh, haha, I forgot I told you that..."

        show e
        e "Yes, I was a research assistant. I helped oversee the subjects we tested on."
        show e annoy
        e "Unfortunately, Testing underwent budget cuts... that funding went toward \"employee satisfaction\" or some nonsense."
        e "After that, a lot of personality cores were phased out of the department..."
        e "Given new titles... I'm a Supervisor Core now, for example."

        mc "Interesting. Part of the new CEO's ideal, I assume?"

        e "Most of the recent changes are exactly that."
        show e
        e "I don't doubt her, though. She has done plenty good for Aperture."
        
        mc "I see."

    elif askestherday2 == False and esther_affection >= 4:
        n "You turn to her."

        mc "So... have you always worked in maintenance?"

        show e annoy
        e "Mmm... no. I was a research assistant in the Testing department, when it was still at its peak."

        mc "Testing?! That's a high-level department! And they threw you down here?"

        e "Yes, but they did give me a supervisor title, so..."
        show e
        e "I suppose I can't complain too much."