label day9:
    play music fourteen
    if renpy.random.randint(0, 1000) == 0:
        $ secretchance = "secret"
    else:
        $ secretchance = "night"
    scene mcroom nightchance
    with fade
    n "You enter your chambers for what feels like the 8th time."
    n "...probably because this is the 8th time."

    n "Only 4 more days till you're out of here..."

    menu:
        extend ""
        "I can't wait to go back.":
            pass
        "I don't really want to leave, but...":
            pass
    
    n "You lay down in your bed for the night and close your eyes."

    scene black
    with fade
    $ daynum = "9"
    $ dayday = "Tuesday"

    if renpy.is_skipping() == False:
        show screen daytransition
        $ renpy.pause(2.0, hard=True)

    scene mcroom day
    with fade

    n "You wake up at 07:30, ready for the day."
    n "Well, as ready as you can be."
    n "You get dressed and head out the door."

    scene office with fade
    $ audio_crossFade(2, "music/one.ogg")
    show e annoy with easeinright
    e "Hello... Doctor."

    mc "Miss Esther? Are you okay?"

    e "Yes, just... incredibly tired."

    mc "How can a core be tired?"

    e "I'm not even sure. I just know I'm exhausted for some reason."
    e "Anyways, let's get started on our shift, Doctor."

    mc "Yes ma'am."

    jump krisday9

label krisday9:
    $ audio_crossFade(2, "music/two.ogg")
    scene krisroom with fade
    n "It takes you no time at all to get to the conference room."
    show e annoy with easeinright
    e "Kris, it's time... for your check-in."
    hide e with easeoutright
    show k flirt with easeinright
    k "Er, Miss Esther... is everything alright?"

    mc "She's tired, apparently."

    show e b at bounce
    e "Very much so."
    hide e b 

    show k
    k "Well. I have good news for you, then - everything's alright in here."
    k "I don't have anything to report today."
    k "The stock is looking better than ever, and I'm running smoothly as well."
    if romance_points["Kris"] >= 13:
        show k flirt
        k "Do you want to see how smoothly I'm running, Doctor?"
        mc "I-I'm okay. Thank you. Haha."
        show k
        k "Your loss."
        mc "Anyways..."
    if positive["Kris"]:
        jump p_krisday9
    else:
        jump n_krisday9

label p_krisday9:
    mc "That's great to hear, Kris. I'm glad things are going well."
    k "As am I."
    if romance_points["Kris"] >= 15:
        k "Doctor, I know you have your one-on-one supervising shift tomorrow, and..."
        show k flirt
        k "...well, I know I can't ask you to choose me, but..."
        k "It would be well in your interest to supervise me tomorrow."
        k "That's all I'll say."
        show e b annoy at bounce
        e "Kris... what are you saying?"
        hide e b 
        k "Nothing, Miss Esther. I apologize."
    k "Always good to see your face, Doctor."
    show k flirt
    k "Sunshine on a cloudy day."
    show k angry
    k "...whatever that means."

    menu:
        extend ""
        "That's sweet of you, Kris.":
            $ romance_points["Kris"] += 2
            $ priority["Kris"] -= 1
            jump p_krisday9neutral
        "You shine quite a bit yourself.":
            $ romance_points["Kris"] += 3
            $ priority["Kris"] += 1
            jump p_krisday9positive

label p_krisday9neutral:
    show k
    k "Well. You should be going. I know you have plenty to do today."
    if romance_points["Kris"] >= 13:
        show k flirt
        k "I hope I see you here tomorrow."
    
    show k
    mc "Goodbye, Kris. I'll see you later."

    n "You check Kris off your list and leave the conference room."

    jump unknownday9

label p_krisday9positive:
    show k
    k "Ah. Ahem. Thank you, Doctor."
    k "It's most likely because I polished my chassis last night, but... umm..."

    show k flirt
    k "You should be going. I know you have plenty to do today."

    if romance_points["Kris"] >= 13:
        k "I... hope I see you tomorrow."
    
    show k
    mc "Goodbye, Kris. I'll see you later."

    n "You check Kris off your list and leave the conference room."

    jump unknownday9

label n_krisday9:
    mc "I'm glad things are going well. That's good to hear."

    show k flirt
    k "Thank Aperture, right? Now you don't have to check off a different box than usual."
    show k angry
    k "Such an exhausting task."

    show e b annoy at bounce
    e "Now, Kris, just because I'm tired -"
    hide e b 

    show k
    k "I apologize, Miss Esther."
    show k angry
    k "Haha... truly, I do not know what's gotten into me lately."
    k "Forgive me."

    mc "Uh... well, if everything's okay in here, we should probably be going."

    show k
    k "Mmm. That's an excellent idea, Doctor."
    k "Have a good day."

    mc "You too."

    n "You hesitantly check Kris off your list and leave the conference room."

    jump unknownday9

label unknownday9:
    scene hall with fade
    show e annoy with easeinright
    e "I apologize for not being my... usual self, Doctor."
    e "I hope this shift goes by quickly."
    hide e with easeoutright
    $ audio_crossFade(2, "music/eight.ogg")
    show u with easeinright
    u "Doc! And..."
    show u upset
    u "...Miss Esther, yeah?"
    show u
    u "Shocker bumpin' into you two here."

    show e b at bounce
    e "Shocker?! {i}You're{/i} in the way of {i}our{/i} route."
    show e b annoy
    e "Not that much of a surprise that we're doing our job on a Tuesday morning, is it?"
    hide e b 

    menu:
        extend ""
        "It's good to see you again.":
            $ romance_points["???"] += 3
            $ priority["???"] += 2
            jump impressunknown9
        "I'm a little... busy here.":
            $ romance_points["???"] -= 3
            $ priority["???"] -= 2
            jump offendunknown9

label impressunknown9:
    show u look
    u "Oh, uh... you too, Doc."
    u "Sorry you ain't seen me yesterday, I uh... I was busy."

    show u
    u "Glad I bumped into ya now, though."

    show e b annoy at bounce 
    e "Ugh. Doctor, can we move on? Please."
    hide e b 

    if romance_points["???"] >= 13:
        show u look
        u "Ah, yeah, sorry, should prolly get out of your way now, but..."
        show u
        u "Hey Doc, if you see me later, I got something important to tell ya, alright?"
        show u look
        u "L-Later though, not now, hah."

        mc "Alright. I'll keep that in mind."

        show u
        u "Catch ya later. Hopefully."
        hide u with easeoutright

    elif romance_points["???"] <= 12:
        show u look
        u "Ah, yeah, sorry, should prolly get out of your way now."
        show u
        u "I'll catch ya later, Doc."
        hide u with easeoutright
    
    jump heathday9

label offendunknown9:
    show u upset
    u "Agh, sorry, yeah, I'm movin'."
    if positive["???"] == False:
        u "Jeez, you're {i}real{/i} rude."
    
    show u
    u "See ya, Doc."
    hide u with easeoutright

    jump heathday9

label heathday9:
    show e annoy with easeinright
    e "Ah, thank god. That core annoys me to such an incredible extent, I..."
    show e shock
    e "Oh, we're here."
    show e annoy
    e "I forget how close Kris and Heath are to each other..."

    scene heathroom with fade
    $ audio_crossFade(2, "music/three.ogg")
    show h with easeinright
    h "Doctor! I've got another trick for you today!"
    show h sad
    h "...and I'm not putting myself in danger this time!"
    show h
    n "She turns around briefly, then turns back with four metal rings hanging from her handles."

    h "Now... pay close attention."
    h "You see here - all four rings are connected, yes?"

    mc "Yes."

    h "Are you so sure about that?"

    show h laugh
    n "With an upwards flick of her handle, the rings seem to disconnect from one another mid-air -"
    show h
    n "And by the time they land back down, they're split into two and two."

    h "TADA!!"
    h "Just a little... sleight-of-handle."
    
    if positive["Heath"]:
        jump p_heathday9
    else:
        jump n_heathday9

label p_heathday9:
    mc "Wow! That's incredible, Heath."

    show h laugh
    h "Yes, yes, I know, I know, haha."
    show h
    h "You're always my best audience, Doctor."
    if romance_points["Heath"] >= 15:
        h "I know you have places to be - but hear me out for one second!"
        h "You have your one-on-one shift tomorrow, yeah?"
        show h
        h "If you choose me, I have a very special show to put on for you!"
        show h sad
        h "No pressure of course, but..."
        show e b annoy at bounce
        e "Heath... watch yourself."
        hide e b
        show h
        h "Aha, yes, Miss Esther. Anyways, Doc, I hope you'll stop by to see it!"
    h "You definitely pay more attention than the last guy did! Hahaha."

    menu:
        extend ""
        "It's hard {i}not{/i} to pay attention to you.":
            $ romance_points["Heath"] += 3
            $ priority["Heath"] += 1
            jump p_heathday9positive
        "It seems like that's not hard to achieve.":
            $ romance_points["Heath"] += 3
            $ priority["Heath"] -= 1
            jump p_heathday9neutral

label p_heathday9positive:
    show e b at bounce
    e "Doctor..."
    hide e b 
    show h sad
    h "Oh - ahem. Well..."
    show h 
    h "That must make me the best magician EVER!"
    show h sad
    h "Or you meant it, as in like, I'm annoying..."
    h "...but I don't think you did."
    show h laugh
    h "Glad I can bring a smile to your face, Doctor!"
    hide h with easeoutright
    show e annoy with easeinright
    e "Doctor, we should continue our route, now."
    hide e with easeoutright
    show h with easeinright
    h "Ah, yes. You should leave!"
    if romance_points["Heath"] >= 15:
        show h sad
        h "I'm sure I'll see you tomorrow!"
        hide h with easeoutright
    
    mc "Thank you, Heath."

    n "You check Heath off and leave the break room with Miss Esther."

    jump estherday9

label p_heathday9neutral:
    show h sad
    h "Ah, true. He really didn't care much for me, haha."
    show h
    h "Which is why I'm glad you're here! If only temporarily."
    h "Now - Miss Esther's giving me that look, Doc... y'know, the \"shut up before I yell at you\" look?"
    h "So you should probably be going."
    show e b annoy at bounce
    e "Great power of observation, Heath."
    hide e b

    mc "Yes, we'll be going now. Thank you, Heath."
    
    n "You check Heath off and leave the break room with Miss Esther."

    jump estherday9

label n_heathday9:
    mc "I genuinely don't know how you did that."

    show h sad
    h "I know you feel this is a waste of time, Doctor, but this is my passion."
    show h laugh
    h "Forgive me if I can't resist the urge to show off!"
    show h
    h "As you can see, though, everything here is working just fine."
    h "I know you have a schedule to keep, so..."

    mc "...Yes, I'll be going."

    show h laugh
    h "Wonderful! I mean..."
    show h
    h "Have a great day, Doctor!"

    n "You check Heath off and leave the break room with Miss Esther."

    jump estherday9

label estherday9:
    scene hall with fade
    $ audio_crossFade(2, "music/eleven.ogg")
    show e annoy with easeinright
    e "You know, running along these management rails all day takes a lot more out of me than you might think..."

    mc "I still can't understand how you get tired."

    e "As I've said, I'm not sure either. Perhaps it's something Aperture programmed into us, to make us more..."
    e "...\"human\"."
    show e laugh
    e "Frankly, I don't see the appeal of being human..."
    show e annoy
    e "Other than the legs, of course."

    menu:
        extend ""
        "Sometimes I wish I {i}wasn't{/i} a human.":
            $ esther_affection += 2
            jump estherday9positive
        "I don't know. I take pride in it.":
            $ esther_affection += 1
            jump estherday9neutral

label estherday9positive:
    show e
    e "See! There's the spirit."
    show e annoy
    e "Ugh. I can't put in that much energy right now."
    jump aspenday9

label estherday9neutral:
    e "That's good, I suppose."
    e "Sorry if I seem a little... off today, Doctor."
    e "I really can't put in that much energy today."
    jump aspenday9

label aspenday9:
    n "Before you know it, you've reached the greenhouse upstairs."

    e "I'll just be out here... resting my optic."

    n "You enter the greenhouse."

    scene aspenroom with fade
    $ audio_crossFade(2, "music/four.ogg")

    n "Everything seems to be normal from the outside."
    n "You're well aware by now, of course, that the only person that could tell something is off would be -"

    mc "Aspen? I'm here for your check-in."

    show a with easeinright
    n "Aspen turns around to face you."
    if positive["Aspen"]:
        jump p_aspenday9
    else:
        jump n_aspenday9

label p_aspenday9:
    n "They greet you with a smile. Or something like it."
    a "Doctor! Ah, it's great to see you. How are you?"

    mc "I'm doing good, Aspen. How are you?"

    show a laugh
    a "Great! Everything's going smooth. The chrysanthemums I showed you yesterday are blooming even bigger than before."
    show a look
    a "You know, chrysanthemums are used in tea sometimes, and it's generally believed it has several health benefits..."
    a "In addition, they can reduce air pollution in some cases!"
    show a laugh
    a "Oh shoot, I'm rambling again, aren't I?"
    show a
    a "S-Sorry, Doctor, sorry."

    menu:
        extend ""
        "I like listening to you, Aspen.":
            $ romance_points["Aspen"] += 3
            $ priority["Aspen"] += 1
            jump p_aspenday9positive
        "It's okay. I know you're passionate about botany.":
            $ romance_points["Aspen"] += 2
            $ priority["Aspen"] -= 1
            jump p_aspenday9neutral

label p_aspenday9positive:
    show a look
    if priority["Aspen"] == 2:
        a "Aha... that's twice in a row now, you've said... something..."
        a "...like that."
    elif priority["Aspen"] < 2:
        a "Doctor, I..."
        a "Well, uh..."
        a "...uh, thank you."
    
    if romance_points["Aspen"] >= 15:
        show a
        a "Look, I know I'm not really supposed to ask you this..."
        show a laugh
        a "And I'm stepping way over my programming here, but..."
        show a look
        a "...If you could, do you think you could supervise me during your one-on-one tomorrow?"
        a "I have something... important to tell you."

        mc "I'll think about it, Aspen."

        show a laugh
        a "Ah, good. I know it's... strange of me to ask, haha..."
    
    elif romance_points["Aspen"] <= 14:
        show a
        a "I-I really don't know what to say to that, haha."
        show a look
        a "But yes! Everything's working fine. We're all - I mean, I'm... uh."
        a "Well."
    
    mc "As much as I hate to say it, I should probably be going now."
    mc "Miss Esther is most likely waiting for me."

    show a
    a "Oh! Um. Yes."
    show a laugh
    a "Have a good day, Doctor!"
    if romance_points["Aspen"] >= 15:
        show a look
        a "I hope you'll choose me tomorrow."
    
    n "You check Aspen off your list and leave the greenhouse."

    jump estherday9pt2

label p_aspenday9neutral:
    show a
    a "Thank you, thank you, Doctor."
    a "I knew you'd understand."
    show a look
    a "But yes, uh... you have nothing to worry about."

    mc "That's good."
    mc "I should probably be on my way, then - Miss Esther's waiting for me."

    show a
    a "Of course Doctor! I'll see you on Thursday for sure!"

    n "You check Aspen off your list and leave the greenhouse."

    jump estherday9pt2

label n_aspenday9:
    n "They greet you with... actually, you're not quite sure what that look is."

    a "Oh, Doctor! Hello again."

    mc "Hi, Aspen. Is everything going well in here?"

    show a laugh
    a "Yes, as usual, everything is fine."
    show a
    a "I'm glad to be working in here. The plants keep me company. And they're very kind."
    show a look
    a "Especially when most people {i}aren't.{/i}"
    show a laugh
    a "Anyways!"
    show a
    a "You've got nothing to worry about, Doctor! Haha. So you can go."

    mc "Uh... alright."

    n "You hesitantly check Aspen off your list and leave the greenhouse."

    jump estherday9pt2

label estherday9pt2:
    scene hall with fade
    $ audio_crossFade(2, "music/eleven.ogg")
    show e annoy with easeinright
    e "Ah. Doctor. Welcome back."
    e "Let's be on our way to CC, now."

    n "You follow Miss Esther as she tiredly leads you on her rail."

    menu:
        extend ""
        "Are you alright, Miss Esther?":
            $ esther_affection -= 1
            pass
        "(Let her rest.)":
            $ esther_affection += 1
            jump ccday9
    
    show e laugh
    n "She laughs softly."
    
    show e
    e "I'm doing wonderful, Doctor! Simply excellent."

    show e annoy
    e "...no, Doctor, I'm not okay. As I said, I'm very tired."
    e "Please... a little silence would be nice."

    mc "Ah. Yes. I'm sorry."

    jump ccday9

label ccday9:
    n "Eventually, you two approach the door to CC's room."
    n "You hear... \"coughing\" from inside. It seems CC is already awake."
    n "You open the door."

    scene ccroom with fade
    $ audio_crossFade(2, "music/five.ogg")
    show c with easeinright

    if positive["CC"]:
        jump p_ccday9
    else:
        jump n_ccday9
    
label p_ccday9:
    c "Doctor... Miss Esther."

    n "He sounds much... rougher than usual."

    c "Forgive me for my brevity. I am..."
    show c close
    n "He coughs harshly."
    show c
    c "...not feeling my best."
    show e b at bounce
    e "CC... you sound terrible."
    hide e b
    show c close
    c "Haha... yes, I'm aware."

    menu:
        extend ""
        "I'm here for you, CC.":
            $ romance_points["CC"] += 3
            $ priority["CC"] += 1
            jump p_ccday9positive
        "I'm sorry it's gotten worse.":
            $ romance_points["CC"] += 2
            $ priority["CC"] -= 1
            jump p_ccday9neutral


label p_ccday9positive:
    show c look
    c "Mmm. Thank you, Doctor."
    c "I know. I appreciate that. Genuinely."
    show c close
    c "Honestly, how I feel is up and down on the best of days..."
    show c
    c "I just hope it isn't worse tomorrow."

    mc "As do I."

    c "Everything's as it should be, though, Doctor."
    show c close
    c "You know... seeing you is one of the only things keeping me going right now."
    show c look
    c "..."
    $ renpy.pause(1.0, hard=True)
    show c
    c "Forgive me. That came... out of nowhere."
    c "A-Apologies, Doctor."

    mc "Don't apologize, CC. It's alright."

    show e b at bounce
    e "Doctor, we should be leaving - CC needs his rest."
    hide e b 

    mc "Ah. Yes. Very true."
    mc "Please rest, CC."

    c "I will."
    if romance_points["CC"] >= 15:
        show c look
        c "Wait - Doctor. Before you leave."
        c "I know it seems quite... boring in here, but..."
        c "...if you could choose me for your supervising shift tomorrow, that would be wonderful."
        c "I know it's not my place to ask, but..."

        mc "We'll see."

        show c
        c "Thank you."
    
    n "You check CC off your list and quietly close the door behind you."

    jump robday9

label p_ccday9neutral:
    show c
    c "Ah, it's alright."
    c "Nothing I haven't been through before."

    mc "Still."

    show c close
    c "Everything's as it should be in here, though."
    c "I'm worse than usual, of course. That's the only change."
    show c look
    c "Should be good for your paperwork though, yes?"
    show c

    mc "I guess."

    c "Thank you for your consideration, Doctor."
    c "You should be on your way, though - I know you have a schedule to keep."

    mc "Ah. Yes."
    mc "Thank you, CC."

    n "You check him off your list and gently close the door behind you."

    jump robday9

label n_ccday9:
    c "Miss Esther... Doctor."

    n "He sounds much... rougher than usual."

    c "I am..."
    show c close
    n "He coughs harshly."
    show c
    c "...not feeling my best."
    c "Apologies."
    show e b at bounce
    e "CC... are you okay?"
    hide e b
    show c close
    c "Haha... no, but it's alright."
    c "Honestly... I just need some rest at the moment."
    hide c with easeoutright
    show e annoy with easeinright
    e "I understand, CC. Don't worry, we'll be brief."
    e "I think we have all the information we need, anyways."
    e "We'll be going."
    hide e with easeoutright
    show c with easeinright
    c "Thank you, Miss Esther."
    c "Have a good day."

    n "You check CC off your list and leave the room."

    jump robday9

label robday9:
    scene hall with fade
    $ audio_crossFade(2, "music/eleven.ogg")
    show e annoy with easeinright
    e "Oh thank god. Our route's almost done."
    e "I am so ready to crash into my... charging... port."
    show e laugh
    e "...I guess that phrase doesn't really make sense if I don't have a bed, huh?"
    show e annoy
    e "Anyways. Let's be on our way. Quickly now."

    hide e with easeoutright
    n "Miss Esther advances rapidly on her rail while you try to keep up."
    n "You make it to the gym in no time."
    show e annoy with easeinright
    e "I do hope I won't have a reason to yell at him today..."
    
    scene robroom with fade
    $ audio_crossFade(2, "music/six.ogg")
    show r yell with easeinright
    r "Go go go go GO GO GO!! COME ON..."
    n "You wait patiently."
    r "GOAL!! YEAH, HAHAHA!"
    show r
    r "Oh, Doc. Didn't see you there."

    if romance_points["Rob"] == 0:
        jump p_robday9
    if romance_points["Rob"] == -1:
        jump n_robday9

label p_robday9:
    show r angry
    r "Sorry, sorry, haha."
    show r
    r "Good to see ya, Doc. How's your shift been so far?"

    mc "Not bad. Miss Esther's very tired today, so we've kind of been rushing through it."

    r "Essie? Tired?"
    show r angry
    r "Was bound to happen eventually."

    n "He turns to Miss Esther."
    show r close
    r "You work yourself too hard."

    show e b annoy at bounce
    e "Yes, yes... I'm aware."
    hide e b  

    show r
    r "Anyways, Doc. Real good you're here."
    r "You're the highlight of my day. Other than the game, 'course."

    mc "That's sweet. Everything working out alright in here?"

    r "Yeah. All the machines are up n' running. I even had someone come in earlier today, which is always a pleasant surprise."

    mc "I'm glad to hear that. Keeps you busy."

    show e b at bounce
    e "...and awake."
    hide e b 

    if romance_points["Rob"] >= 15:
        show r angry
        r "...Now, I'm not really s'posed to say this, but... before you go..."
        r "You should totally come by during your one-on-one tomorrow."
        r "I got a surprise for ya if you do."

        show e b annoy at bounce
        e "Watch yourself, Robert."
        hide e b 
        show r yell
        r "DON'T CALL ME THAT!"
        show r
        r "Anyway. Yeah."
    
    hide r with easeoutright
    show e annoy with easeinright
    e "Doctor, are you ready to leave now? I am exhausted."

    mc "Oh, yes, Miss Esther. Let's go."

    if romance_points["Rob"] >= 15:
        menu:
            extend ""
            "I'll see you tomorrow, Rob. Stay safe.":
                $ romance_points["Rob"] += 3
                $ priority["Rob"] += 1
                hide e with easeoutright
                show r with easeinright
                r "Will do."
            "I'll see you later, Rob.":
                $ romance_points["Rob"] -= 3
                $ priority["Rob"] -= 1

    n "You check Rob off your list once more and head back to your office."

    jump day9end

label n_robday9:
    show r close
    r "Would prefer if I didn't see ya at all, haha."

    mc "Wow. Rude."

    show r
    r "Anyway. Everything's working fine. Things are normal, you've got nuthin' to worry about here."

    show r yell
    r "GO! GO! WHAT THE HELL ARE YOU - oh my GOD..."
    show r 
    r "Now I... I'm sure you have work to do -"
    show r close
    r "Oh no, it's the end of your shift, huh..."
    show r angry
    r "Well, an employee is bound to come in here any time now... haha..."
    r "Y'all should prolly get going."

    mc "Alright then."

    n "You check Rob off your list once more and head back to your office."

    jump day9end

label day9end:
    scene office with fade
    show e with easeinright
    e "Alright! Great job, blah blah blah, check your emails..."
    show e annoy 
    e "I'm going to bed. Or... you know what I mean."
    e "I'll see you tomorrow, Doctor."

    mc "Rest well, Miss Esther."

    jump e9first