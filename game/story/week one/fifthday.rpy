label day5:
    play music fourteen
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

    if renpy.is_skipping() == False:
        show screen daytransition
        $ renpy.pause(2.0, hard=True)
    if renpy.is_skipping() == True:
        pass
    scene mctemproom with fade

    n "You wake with a start." 
    n "You think you were dreaming, but that's not possible in stasis."
    n "You get up and check your wardrobe. What should you wear for Casual Friday?"

    menu:
        extend ""
        "A t-shirt and jeans.":
            python:
                tshirt = True
                romance_points["Aspen"] += 1
                romance_points["Greg"] += 1
            n "You put on a regular old t-shirt and blue jeans, and head out the door to work."
        "Your best formalwear.":
            python:
                formal = True
                romance_points["Kris"] += 1
                romance_points["Heath"] += 1
            n "You put on your best date-night attire, and head out the door to work."
        "A Hawaiian shirt and khakis.":
            python:
                vaca = True
                romance_points["Rob"] += 1
                romance_points["???"] += 1
            n "You put on your vacation clothes, and head out the door to work."
        "Just your regular uniform.":
            python:
                uniform = True
                romance_points["CC"] += 1
                esther_affection += 1
            n "You decide to just wear your uniform as regular, sling the lab coat over your shoulders, and head out the door to work."

    scene office
    with fade
    $ audio_crossFade(2, "music/one.ogg")
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
        "Gregory invited me to go meet him. I might do that.":
            e "Interesting. Well, it's your time off. You're free to do whatever you please."
        "I have absolutely no clue.":
            show e laugh
            e "Fair enough. I suppose you aren't used to being on-campus on your days off."
    
    show e
    e "Well, we should be on our way, then. Grab your clipboard, and let's get going."
    n "You get your paperwork and follow Miss Esther out the door."

    jump krisday5

label krisday5:
    scene kristemproom with fade
    $ audio_crossFade(2, "music/two.ogg")

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
        k "Frankly, as I've told you before, I believe this is just another way to get us out of the picture..."
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
    k "I have been doing this for nearly 5 years now - almost half my lifespan!"
    k "I will not tolerate this disgrace to my intelligence..."

    if romance_points["Kris"] <= 0:
        $ positive["Kris"] = -1
        show k flirt
        k "You've been incredibly rude to me over the past week, Doctor..."
        k "I'm not sure what I did to upset you, but..."
        show k
        k "I don't appreciate it in the slightest."
    jump krisday5cont

label krisday5cont:
    mc "I... should be going now. I have a schedule to keep."

    hide k with easeoutright
    show e annoy with easeinright

    e "Wow, I didn't even have to tell you to hurry it up this time..."

    n "You check Kris off your list for the last time this week and head out the door."

    jump heathday5

label heathday5:
    scene heathroom with fade
    $ audio_crossFade(2, "music/three.ogg")
    
    n "You enter into the break room. Heath isn't in the doorway this time - instead, she's waiting patiently up on the stage."

    show h with easeinright
    h "Doctor! Apologies for yesterday. Are you ready for yet another trick?"

    n "You hear what sounds like mechanics whirring, a puff of air, and then -"
    n "A cloth starts coming out of Heath's chassis. A load of differently-colored scarves."

    show h laugh
    h "Tada!"

    show e b annoy at bounce
    e "I don't see what the appeal of this \"trick\" is."
    hide e 

    show h sad
    h "Just you wait, Miss Esther..."

    show h
    n "At least 10 meters of scarf has now exited Heath's chassis, and it's still going."
    n "Cores aren't {i}that{/i} large, all things considered - just slightly bigger than a small yoga ball."
    n "Regardless, they're certainly not big enough to fit that much cloth in..."
    n "How she managed this, let alone while avoiding her circuitry, {i}and{/i} without hands..."
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
    h "Concerned about me, are you?"
    h "Why Doctor, if you're not careful..."

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
    e "I swear, as much as I like her, that girl gets on my nerves sometimes..."

    n "You check Heath off your checklist once more and head out of the break room."

    jump aspenday5

label aspenday5:
    scene hall with fade
    $ audio_crossFade(2, "music/eleven.ogg")
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

    scene aspentemproom with fade
    $ audio_crossFade(2, "music/four.ogg")

    show a look with easeinright

    a "Doctor, Doctor, now's not a really good time!"

    n "You look around the room. It's darker than usual - not a good sign for an underground greenhouse."

    mc "Is something going on?"

    show a laugh

    a "Ahh, yeah, kind of? Haha... the artificial sunlight, pumped in from the surface..."
    show a
    a "It turned off overnight."
    show a look
    a "When I got in this morning, things were completely dark... I had to quickly report the problem to Facilities so they could fix it."

    n "Aspen is rushing from specimen to specimen as they speak to you, frantically checking their work."

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
    a "Oh, no, Doctor, this is my job. Plus, you aren't really cleared to work on this."
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
        show a look
        a "And... thank you. For your treatment of me this week."
        a "You've been very respectful and... very kind."
        a "I'm not used to it. It's a little strange..."
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
    a "Oh, that's funny - no, no. They look okay from the outside, but on the inside, they're dying."
    show a look
    a "Without the sunlight for that long, and this deep into the facility..."
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
    scene hall with fade
    $ audio_crossFade(2, "music/eleven.ogg")
    show e with easeinright
    e "Doctor, welcome back. Let's head back down."

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
    
    n "You reach CC's room. Standing outside the door, you can hear muffled talking."

    show e shock
    e "Is someone in there with him?"
    e "There shouldn't be anyone in there at this time -"

    show e annoy
    e "Doctor, open the door. Carefully."

    n "You do exactly that."

    scene cctemproom with fade
    $ audio_crossFade(2, "music/eight.ogg")

    show u upset with easeinright
    u "I ain't doin' anything wrong, here, am I?"
    hide u with easeoutright

    show c close with easeinright
    c "Technically, you are. This is a private room. You're invading my space."
    hide c with easeoutright

    show u with easeinright
    u "But the Doc's in here. And her little friend."

    show e b annoy at bounce
    e "Who are you calling \"little\"?!"
    hide e b
    hide u with easeoutright

    show c with easeinright
    c "Doctor, can you please remove this core from my room?"
    c "I have nothing against him, but he is trespassing."

    menu:
        extend ""
        "Alright, sir, you're going to have to leave.":
            $ esther_affection += 1
            jump ccanduleave
        "I'm sure there's a way to resolve this. Why are you here?":
            python:
                romance_points["???"] += 3
                romance_points["CC"] += 1
                esther_affection -= 1
            jump ccanduresolve

    # 8 points for pos on ???

label ccanduleave:
    hide c with easeoutright
    show u upset with easeinright

    u "Fine, fine, I'm leavin'."
    show u
    u "None of you even give a rat's ass about me..."

    show e b annoy at bounce
    e "Obviously."
    hide e b 

    if romance_points["???"] >= 8:
        show u upset
        u "You're usually pretty... soft to me, Doc. I'm sure this is a one-off."
        show u
        u "I'll see ya... this weekend, right?"
        hide u with easeoutright
        n "And with that, he leaves."

    elif romance_points["???"] <= 0:
        $ positive["???"] = -1
        show u upset
        u "Seems no matter how hard I try, you simply ain't interested, Doc."
        show u look
        u "S'fine. But I take back my invite for this weekend..."
        hide u with easeoutright
        n "And with that, he leaves."

    elif 1 <= romance_points["???"] <= 7:
        hide u with easeoutright
        n "And with that, he leaves."
    
    jump ccday5cont

label ccanduresolve:
    hide c with easeoutright
    show u look with easeinright
    u "S'pretty simple, honest. I thought this was my own room..."

    mc "The \"place\" you keep inviting me back to?"

    show u
    u "Yeah, exactly that. And I don't quite remember {i}why{/i} I thought this was my room, but..."

    hide u with easeoutright
    show c close with easeinright
    c "I sympathize, sir, I really do, but this is technically a research area."
    show c
    c "You can't just go rolling into every room you see."
    c "Aspen told me you've rammed into the greenhouse door before as well."

    show e b annoy at bounce
    e "Oh, so this is a {i}recurring{/i} problem?"
    hide e b annoy
    hide c with easeoutright

    show e annoy with easeinright
    e "Doctor, I suggest we escalate this to Encoding. There seems to be something horribly wrong with this... {i}\"core.\"{/i}"

    mc "Now wait a moment, Miss Esther. I don't think that's necessary."
    hide e with easeoutright
    show u with easeinright

    mc "I don't know your name, or your job, or your designation..."
    mc "But you need to watch where you're going."
    mc "My first day here, you nearly ran into Miss Esther."
    mc "And she's right - if this continues to be a problem, I'll have to report it."
    mc "I don't want to do that."

    show u upset
    u "Yeah..."
    u "Yeah, I understand, Doc."
    show u look
    u "I apologize, uh... CC, right?"
    hide u with easeoutright

    show c look with easeinright
    c "Haha. Yes, that's my name."
    c "You're forgiven."
    hide c with easeoutright

    show u with easeinright
    
    if romance_points["???"] >= 8:
        u "I'll get goin' now, Doc."
        show u upset
        u "You've been unusually, uh, patient with me this week."
        show u look
        u "I do reckon you'll visit me tomorrow. Hopefully."
        hide u with easeoutright
        n "And with that, he leaves."

    elif romance_points["???"] <= 0:
        $ positive["???"] = -1
        u "Uhh... Doc, I wanna apologize to you too, for uh..."
        show u look
        u "Tryin' so hard. Pushin' you too much."
        u "I take back my invite for t'morrow. You don't gotta come."
        hide u with easeoutright
        n "And with that, he leaves."

    elif 1 <= romance_points["???"] <= 7:
        u "I reckon I oughta be goin', then."
        u "See y'all."
        hide u with easeoutright
        n "And with that, he leaves."
    
    jump ccday5cont

label ccday5cont:
    show c with easeinright
    $ audio_crossFade(2, "music/five.ogg")
    c "Ahh. Thank you, Doctor."
    
    show e b at bounce
    e "Are you alright, CC?"
    hide e b 
    c "Yes, Miss Esther."
    c "He was not a bother. Simply breaking the rules - that was all."
    show c close
    c "I honestly regret he could not stay. I enjoy any company, regardless of the type."

    mc "How are you feeling today?"

    show c
    c "The same as usual, I would say."
    c "Maybe a little better?"

    n "You turn to Miss Esther."

    mc "Is that a good thing?"

    show c close
    show e b annoy at bounce
    e "For him, yes. For us, no. A \"positive\" report on CC is either one where his condition has not changed or has worsened."

    menu:
        extend ""
        "What heartless bastard wrote this goddamn report, anyway?":
            $ romance_points["CC"] += 3
            jump impresscc5
        "They're not going to be happy about this one, then?":
            jump neutralcc5

label impresscc5:
    hide e B
    show c
    c "Haha... excuse my language, but..."
    show c look # cc gets agitated here
    c "Aperture bastards, that's who."
    show c
    c "Can't leave well enough alone..."
    c "Test, test, test, that's all they do..."

    show e b sad at bounce
    e "Now, CC, calm down. Don't get too stressed. It's bad for you."
    hide e b

    show c look
    c "Well then. If it's bad for me, I should keep it up, yes?"
    show c
    c "Give those idiot scientists what they want..."

    show c close
    c "Ahem. Apologies, Doctor, I believe I may have gotten... out of hand, there."

    jump ccend5

label ccend5:
    if romance_points["CC"] >= 10:
        show c look
        c "Before you go..."
        c "You have been incredibly kind to me, despite that not being necessary."
        c "I will not forget that."
        
        mc "Thank you, CC."

    elif romance_points["CC"] <= 0:
        $ positive["CC"] = -1
        show c look
        c "Before you go..."
        c "I'm not sure what the issue is, but..."
        c "It seems you don't like me very much, Doctor."
        show c
        c "That's alright though. That's a common occurence."

        mc "CC -"

    show c
    c "You should be going, now. You've been here far longer than your scheduled time."

    mc "Yes."

    hide c with easeoutright
    n "You finish your report and quietly leave the room."

    jump robday5

label neutralcc5:
    e "Most likely not."
    hide e b 

    jump ccend5


label robday5:
    scene hall with fade
    n "As you approach the door to the gym, you notice a surprising lack of yelling from inside it."

    show e annoy with easeinright
    e "Rob's surprisingly quiet today. I don't hear the television active, either."

    mc "Hmm..."

    n "You open the door carefully."

    scene robtemproom with fade
    $ audio_crossFade(2, "music/six.ogg")
    show r close with easeinright
    n "Rob is sound asleep at his desk."

    show e b annoy at bounce
    e "You've got to be kidding me."
    hide e b

    n "The TV above him is turned off, as well."
    n "There's no one else in here, though by now that seems to be the default state of things."

    hide r with easeoutright
    show e shock with easeinright
    e "ROB! WAKE YOUR SORRY ASS UP!"
    hide e with easeoutright

    show r close with easeinright
    show r at bounce
    r "Oh! Shit! Essie!"
    show r angry
    r "Sorry, I... uh."

    hide r with easeoutright
    show e shock with easeinright
    e "You were SLEEPING? Do you realize we have to report this now?"
    show e annoy
    e "Why I {i}never...{/i}"
    hide e with easeoutright

    show r yell with easeinright
    r "Look! Look, I'm sorry, Essie. It gets boring as hell in here sometimes..."
    show r angry
    r "And I got no games to watch on Fridays 'cuz they redirect my electricity to hold meetings upstairs!"
    r "So I fell asleep. What's the big deal?"

    menu:
        extend ""
        "We have to report that you weren't doing your job.":
            $ romance_points["Rob"] -= 3
            $ esther_affection += 1
            jump offendrob5
        "Nothing too much. I just need you to stay awake from now on.":
            $ romance_points["Rob"] += 3
            jump impressrob5
        "Miss Esther?":
            $ esther_affection += 1
            jump neutralrob5

label offendrob5:
    show r yell
    r "Not doing my job?!"
    r "All I do is sit here and watch the TV all day!"
    show r angry
    r "What \"job\" do I even do?! Hahaha..."
    show r yell
    r "I swear!! I'm alone in here all day, no one comes into this goddamn gym, and -"
    hide r with easeoutright

    show e shock with easeinright
    e "I DO NOT CARE! Your JOB is to watch and maintain the company gym. SLEEPING prevents you from doing that!"
    show e annoy
    e "Do NOT talk back to the Doctor. They are your supervisor."
    e "This is ridiculous, Rob."
    hide e with easeoutright

    show r close with easeinright
    r "Yeah, yeah. Whatever."
    show r angry
    show e b annoy at bounce
    e "Now. If you're awake, the Doctor and I need to get going."
    hide e b
    show r close
    r "Sure."

    if romance_points["Rob"] >= 10:
        show r angry
        r "Doc, listen..."
        r "You've been takin' me seriously. Not a lot of other doctors do that."
        r "Sorry I fell asleep today. Won't happen again."
        
        mc "No problem, Rob."
    elif romance_points["Rob"] <= 0:
        $ positive["Rob"] = -1
        r "I don't know what your problem is, Doc, but..."
        r "The way you talked to me this past week, I..."
        r "I dunno."

        show r close
        r "See ya."
    
    jump day5end

label impressrob5:
    r "Ahh, yeah. I suppose I shouldn't have dozed off like that."
    r "It just gets real boring, y'know? Hardly anyone comes in here."
    r "And they've recently started shutting off my electricity on Fridays for meetings, so I don't got any TV at the moment."

    mc "Yeah, I understand."
    mc "But I have to report this if it happens again."

    r "I get it, Doc. Thanks."

    show e b annoy at bounce
    e "Now. If you're awake, the Doctor and I need to get going."
    hide e b
    show r close
    r "Sure."

    if romance_points["Rob"] >= 10:
        show r
        r "Doc, listen..."
        r "You've been takin' me seriously. Not a lot of other doctors do that."
        r "And you've been nice. On top of that. So... thanks, yeah?"
        
        mc "No prob, Rob." # LMAO
    elif romance_points["Rob"] <= 0:
        $ positive["Rob"] = -1
        show r angry
        r "But... I really don't know how to feel about you yet."
        r "Seems you're flip-floppin'. Gotta make up your mind."

        show r close
        r "See ya."
    
    jump day5end

label neutralrob5:
    hide r with easeoutright
    show e annoy with easeinright
    e "Well, we have to report this. You sleeping is you not doing your job..."
    e "Regardless of the reasons behind it."
    show e
    e "And frankly, maybe you'll take it in stride. Do your work, Rob."
    hide e with easeoutright
    
    show r with easeinright
    r "Hmm. Yes'm."

    show e b annoy at bounce
    e "Now. If you're awake, the Doctor and I need to get going."
    hide e b
    show r close
    r "Sure."

    if romance_points["Rob"] >= 10:
        show r
        r "Doc, listen..."
        r "You've been takin' me seriously. Not a lot of other doctors do that."
        r "So... thanks, yeah?"
        
        mc "No problem, Rob." 
    elif romance_points["Rob"] <= 0:
        $ positive["Rob"] = -1
        show r
        r "Doc, listen."
        r "It seems you don't really care for me, or the gym, or any of that shit."
        r "That's alright, but... don't think I don't know that, yeah?"

        mc "Yeah. Got it."
    
    jump day5end

label day5end:
    if positive["Rob"] == 0:
        n "You end the day with your final checkmark of the week and head back towards your office."
    elif positive["Rob"] == -1:
        n "You end your day with a note by Rob's name - \"(sleeping)\". You head back towards your office."
    
    scene office with fade
    show e with easeinright
    $ audio_crossFade(2, "music/one.ogg")
    e "Alright, Doctor, I believe that's all!"
    e "You may have some end-of-week emails to go through, though. Other than that..."
    e "I'll see you on Monday!"

    mc "Thank you for all your help, Miss Esther."

    show e laugh
    e "You're welcome. It's my job, after all."

    jump e5first
