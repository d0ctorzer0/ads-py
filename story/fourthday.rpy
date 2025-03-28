label day4:
    scene mctemproom
    with fade

    n "You put in the code to your room and enter it, dropping your paperwork on the floor."

    if wkd3:
        n "You never expected Kris to act so... sensitively. It seemed almost out-of-character."
    if whd3:
        n "You're glad you spent the day with Heath. She kept you entertained."
    if wad3:
        n "You figure you learned more about botany today than you ever did in your schooling years."
    if wcd3:
        n "CC's conversations can get very deep. It gave you a lot to think about."
    if wrd3:
        n "You're exhausted from your shift today, much more than usual. But it feels good."
    else:
        n "You wonder if maybe you should've done something different today, or asked Miss Esther to come with you despite management's wishes."
    # ^ this line plays regardless of previous variable values. fix later
    n "Regardless, you need your rest for tomorrow's shift. You change out of your work attire and lay down for stasis."

    scene black
    with fade
    $ daynum = "4"
    $ dayday = "Thursday"

    show screen daytransition
    $ renpy.pause(2.0, hard=True)

    scene mctemproom with fade

    n "You wake up at 08:00 as usual, get dressed, and head out the door."

    scene office with pixellate

    n "Miss Esther greets you at the door."

    show e with easeinright
    e "Hello, Doctor!"

    mc "Hello, Miss Esther."

    e "Are you ready for another day? We're back to our regular routine!"

    mc "You're awfully cheery today."

    show e laugh
    e "Oh yes, I suppose I am. It's Thursday, which means we're more than halfway through the week!"
    show e
    e "I'm simply excited for the weekend."

    mc "What do you even do over the weekend, anyway?"

    show e annoy
    e "I have hobbies! I do... things!"
    
    show e
    e "Anyways, we'd better be on our way to Kris. Saturday will come quicker than you expect! Let's go!"
    hide e with easeoutright

    if cc1 == True and picture == True:
        n "You glance at the picture of Multnomah Falls on your desk and remember what CC said yesterday."
        menu:
            extend " You decide to..."

            "Bring it with you.":
                n "You pick up the picture and tuck it in with your paperwork."
                $ giveccpicture = True
            "Leave it behind.":
                n "You leave the picture on the desk. Maybe another day."
    
    n "You follow Miss Esther out of the office and towards the conference room."

    jump krisday4

label krisday4:

    scene kristemproom with pixellate

    n "You enter the conference room to see Kris whizzing across his management rail, back and forth, rapidly."
    n "The screen behind him has a lot more red on it than usual."

    show e with easeinright
    e "Kris, we're here for your..."
    hide e with easeoutright
    
    show k angry with easeinright
    k "No time to talk. I'm trying to find the source."

    mc "The source of what?"

    k "Can't you read? Our stock plummeted overnight. We've had no large experiments lately, no important investments to make..."
    k "It just doesn't make sense!"

    menu:
        extend ""
        "(Reassure him.)":
            $ romance_points["Kris"] += 3
            jump impresskris4
        "(Let him think.)":
            $ romance_points["Kris"] += 1
            k "I've reported it to finanical already, left a note that I believe it may have been a mistake, or something in Testing..."
            k "I've... done everything I have to. I've done my job."
            k "I'm not sure why I'm still panicking."

            show k flirt
            k "Sorry, Doctor. I am... calmer now."
            jump krisday4cont
        "(Criticize him.)":
            $ romance_points["Kris"] -= 3
            jump offendkris4

label impresskris4:
    if wkd3 or romance_points["Kris"] >= 7:
        mc "Woah, Kris. Take a breath. You're the senior officer in charge of watching the stock, right?"

        show k flirt
        k "Yes. That's why -"

        show k angry
        mc "That's why you'll be fine. This is your whole job. You've got this."
        mc "But first you need to slow down."

        show k
        k "Yes. Yes... you're right, Doctor. I apologize."
        jump krisday4cont
    
    else:
        mc "That's interesting. Can you solve it?"

        k "It's not my JOB to solve it. My job is to WATCH the stock, nothing more, and report to Finanical when it drops below a certain threshold."
        k "I've already reported it."

        mc "Then you've done all you can, yes?"

        show k flirt
        k "I... suppose I have."

        mc "Then there's no reason to panic."

        show k
        k "Yes. Yes... you're right, Doctor. I apologize."
        jump krisday4cont

label offendkris4:
    mc "Get a hold of yourself, Kris. This is highly unprofessional."

    show k
    k "Excuse me?"

    mc "You're running all over the place in a panic. This job is not a high-stress one. There is no reason to panic."

    k "Yes, but I've just never seen such -"

    mc "No excuses. Pull yourself together."

    k "Uh... yes, ma'am."

    if wkd3:
        show k angry
        k "Whatever happened to the Doctor I had yesterday?"
    
    jump krisday4cont

label krisday4cont:
    mc "I don't think I need to ask if you're doing your job."

    hide k with easeoutright
    show e annoy with easeinright
    e "Yes, he made it clear right away that he was."
    e "And his rambling put us behind schedule, Doctor."

    mc "Oh. Yes. Sorry."

    hide e with easeoutright
    show k with easeinright

    k "I'll... handle this. You should be on your way."

    mc "Thank you, Kris."

    n "You head out the door and towards the break room."

    jump heathday4

label heathday4:
    scene heathtemproom with pixellate

    n "Before you can enter the break room, Heath stops you at the door."

    show h laugh with easeinright
    h "Ohh! Doctor! Haha, you're here early."

    show e b annoy at bounce
    e "Actually, we're right on time."
    hide e b annoy

    show h
    h "Yes, yes, but, er... I'm not ready for you quite yet."

    show h sad
    h "I'm not prepared! So, you, uh, need to wait."

    menu:
        extend ""
        "Are you getting ready for another show?":
            $ romance_points["Heath"] += 3
            jump impressheath4
        "We do have a schedule to keep, but we can probably wait a little.":
            $ romance_points["Heath"] += 1
            jump neutralheath4
        "Heath, I'm just checking to see if you're doing your job.":
            $ romance_points["Heath"] -= 3
            jump offendheath4

label impressheath4:
    show h laugh
    h "Why yes! Yes I am! And I'm not ready yet, haha. So..."

    mc "So you need us to wait."

    show h
    h "Yes!! Yes, yes."
    hide h with easeoutright

    show e annoy with easeinright
    e "Heath, we do have a tight schedule."
    e "We don't have a lot of time to wait."
    hide e with easeinright

    jump heathday4cont

label neutralheath4:
    hide h with easeoutright
    show e annoy with easeinright
    e "No, Doctor, we can't really afford to wait."

    mc "Not even for a short while?"

    e "No. Kris already put us behind."

    hide e with easeoutright

    jump heathday4cont

label offendheath4:
    h "Oh yes, I understand. You have places to be."
    show h laugh
    h "No show today, then, Doctor!"
    if whd3:
        show h sad
        h "You seemed so interested yesterday..."

    hide h with easeoutright
    show e with easeinright
    
    e "We should get going, doctor. Just mark the second box on your checklist instead of the first."
    n "You check off the box that says \"PREVENTED FROM INVESTIGATION\"."

    if romance_points["Heath"] <= 6:
        mc "This isn't going to make her look bad, is it?"
        e "It shouldn't, but I'll leave a note just in case."
    else:
        pass

    e "Come along now."

    jump estherday4

label heathday4cont:
    hide e with easeoutright
    show h sad with easeinright
    h "Oh yes, I understand. No, you have places to be."
    show h laugh
    h "No show today, then, Doctor! I'm sorry!"

    mc "That's unfortunate."

    if whd3:
        show h sad
        h "I think you saw enough yesterday to make up for it, hopefully!"
        show h laugh
        h "If not, well, I'll just have to do better next time! Hahaha!"
        show e b annoy at bounce
        n "Miss Esther looks at Heath suspiciously."
        hide e b
    else:
        pass

    hide h with easeoutright
    show e with easeinright

    e "We should get going, doctor. Just mark the second box on your checklist instead of the first."
    n "You check off the box that says \"PREVENTED FROM INVESTIGATION\"."

    mc "This isn't going to make her look bad, is it?"

    e "It shouldn't, but I'll leave a note just in case."
    e "Come along now."
    
    jump estherday4

label estherday4:
    n "You and Miss Esther exit the break room and begin heading toward the greenhouse."
    n "You've been around the section enough now that Miss Esther doesn't have to lead you anymore."

    show e with easeinright
    e "Doctor..."

    mc "Yes?"

    e "Are you... enjoying your time here?"

    mc "What do you mean?"

    show e shock
    e "I understand your... regular routine is a lot more extensive than maintenance."

    show e
    mc "That's true. Manufacturing is difficult."

    menu:
        extend ""
        "I think I'd still rather be down there.":
            $ esther_affection -= 1
            show e annoy
            e "I see. Yes, it's probably what you're used to."
            mc "And I don't have to engage with so many... er, characters, either."
            e "Very true."
            jump aspenday4

        "I suppose I am enjoying the change.":
            $ esther_affection += 1
            show e laugh
            e "Well, that's great!"
            show e
            e "I'm glad you've found a... place for you in maintenance, even if it's for a short time."
            jump aspenday4

        "I don't really feel like it's much different, though.":
            jump aspenday4

label aspenday4:
    show e
    n "You approach the door to the greenhouse."

    e "I'll wait out here as usual."
    e "Go ahead."

    scene aspentemproom with pixellate
    show a laugh with easeinright

    a "Doctor! Good to see you."
    show a
    a "How's your shift been?"

    mc "Pretty much the same as usual."

    a "That's better than \"absolutely horrible, thanks Aspen,\" haha."

    mc "Everything alright in here? Sprinklers functioning as normal?"

    a "Yes, actually."

    if romance_points["Aspen"] <= 8:
        show a look
        a "Things are even better now that you're here!"
    else:
        pass

    show a
    a "Ahem. Sprinklers functioning normally, all that, yes, yeah."

    mc "That's great."

    n "You suddenly notice something a little concerning - the moss growing on Aspen is beginning to creep into his inner mechanisms."
    n "This could be a maintenance issue."

    mc "Aspen, that moss on you..."

    menu:
        extend ""
        "Are you going to be alright? It won't interfere with anything, will it?":
            $ romance_points["Aspen"] += 3
            jump aspenday4cont

        "You should probably remove it if possible. It's a hazard.":
            $ romance_points["Aspen"] -= 3
            jump aspenday4cont

label aspenday4cont:
    show a look
    a "Oh, this? It's just sphagnum moss. It really shouldn't be an issue."

    show a
    a "Don't worry. It won't get into anything critical. My core systems are sealed in case something like that were to happen."

    show a laugh
    a "It's all under control! Haha."

    if wad3 == True or romance_points["Aspen"] <= 9:
        show a look
        a "I do appreciate you showing concern, though, Doctor."

        mc "Of course."
    else:
        pass

    show a look
    a "You should probably be going, now. Miss Esther is waiting."

    mc "Yes, you're right. I'll see you tomorrow?"

    show a laugh
    a "Casual Friday! Yes, you'll see me."
    show a
    a "Have a good day, Doctor."

    n "You mark off your checklist and leave the greenhouse."

    jump ccday4

label ccday4:
    scene temphall with pixellate
    n "Miss Esther greets you outside the door."

    show e with easeinright
    e "Well now, checklist marked off, correct? Let's proceed."

    n "The trip to CC's room is uneventful."
    if giveccpicture == True:
        n "You contemplate how you're going to give your picture to him."
    else:
        pass

    scene cctemproom with pixellate

    show e with easeinright
    e "CC! Love, it's time for your check-in."
    hide e with easeoutright

    show c with easeinright
    c "Ahh, Doctor. Welcome back."

    if giveccpicture == True:
        show c
        mc "I've brought something for you. After our conversation yesterday."

        show c look
        c "You have?"

        show c
        mc "Yes."

        n "He doesn't have hands to put the picture in, so instead you hold it up to his optic."

        mc "It's a picture of Multnomah Falls, in Oregon. I went there some time ago while I was visiting my family."

        $ romance_points["CC"] += 3
        show c look
        c "You brought this in... for me?"

        mc "Well, yes. I figured you probably get tired of looking at the same old waterfalls, so here's a new one."

        show c close
        c "Haha... Thank you, Doctor. This means more than you think."

        mc "You're welcome, CC."

        show e b at bounce
        e "This is very sweet of you, Doctor."
        hide e b
        jump ccday4cont

    else:
        pass

    mc "Have there been any changes in your health?"

    show c close
    c "Not that I'm aware of. I'm as sick as usual."
    c "In fact, if anything, I feel worse than yesterday."

    menu:
        extend ""
        "Look on the bright side - you're still here!":
            $ romance_points["CC"] += 3
            jump impresscc4
        "Wouldn't it be more beneficial to not waste resources sustaining you?":
            $ romance_points["CC"] -= 3
            $ esther_affection -= 2
            jump offendcc4

label impresscc4:
    show c look
    c "I suppose that is true, yes."
    c "Your positive attitude is... refreshing."

    mc "I try to be positive. It's hard sometimes, though, I understand."

    show c
    c "Quite."

    jump ccday4cont

label offendcc4:
    hide c with easeoutright
    show e annoy with easeinright
    e "Doctor, that's ridiculous. And rude."
    
    mc "I apologize. I just meant..."

    e "No, I understood what you meant. But you didn't have to say it aloud."

    mc "Uh... yes, ma'am."

    hide e with easeoutright
    show c with easeinright
    c "No, Miss Esther. It's alright."
    show c close
    c "The doctor is correct. Aperture's energy is wasted on me."
    c "I'm unsure as to why they bother."
    
    jump ccday4cont

label ccday4cont:
    show e b sad at bounce
    e "CC, I'm afraid the Doctor and I are behind schedule. We should leave."

    show c
    c "Yes, I understand."

    if romance_points <= 9:
        show c look
        c "I'll see you tomorrow, Doctor, yes?"

        mc "Yes. You will."

        show c
        c "Good."
        hide c with easeoutright
    
    n "You both leave CC behind and exit the room."

    jump robday4

label robday4:
    scene temphall with pixellate
    n "The gym isn't too far from CC's room, thankfully, and you make it there in no time."
    n "Miss Esther is strangely quiet. And she was so chipper this morning..."

    scene robtemproom with pixellate\

    show r with easeinright
    r "Doc! Essie! Welcome back. I'd like ya to meet my friend here, Greg."
    hide r with easeoutright

    show g look with easeinright
    g "Oh... {i}you're{/i} who he was talking about... haha."

    show e b annoy at bounce
    e "Great. More disruptions."
    hide e b

    hide g with easeoutright
    show r with easeinright
    r "Greg here's one-a-my best friends. He's technically not part of recreation, but who cares?"
    show r angry
    r "He also thinks he's one personality core even though he's actually three of 'em."
    show r
    r "And they call me whack! Ha!"
    hide r with easeoutright
    show g with easeinright

    g "I don't know what he's talking about. I {i}am{/i} only one personality core."
    show g look
    g "Haha... who goes around... pretending to be three cores in one?"
    show g aaa
    g "That's ridiculous! Right?"

    menu:
        extend ""
        "Oh, no, for sure. Don't worry, I know you're just one core.":
            $ romance_points["Greg"] += 6
            $ romance_points["Rob"] += 2
            jump impressgreg

        "I mean, I think the trench coat is a little ridiculous.":
            $ romance_points["Greg"] -= 3
            $ romance_points["Rob"] += 2
            jump offendgreg
        
        "I kinda... don't have time for... whatever this is.":
            $ esther_affection += 1
            show g aaa at bounce
            g "And I... should be going. I'll talk to you later, Rob!!"
            jump robday4cont

label impressgreg:
    show g
    g "Haha. See. I knew you had common sense."
    g "I was just talking to Rob about these \"sports\" he loves so much. Something surface humans do."

    mc "Surface humans?"

    show g look
    g "Y'know, humans that live up on the surface. Some of the doctors here never leave."

    show g
    mc "Ah, I see."

    n "Suddenly, Gregory's... \"legs\" wobble."

    show g aaa at bounce
    g "Oh! I need to, uh, go. I think I'm... malfunctioning."

    jump robday4cont

label offendgreg:
    show g look
    g "That's not very nice... trench coats are stylish, okay?"
    show g
    g "And plus. Human fashion is an... interest of mine, kind of."

    g "You wouldn't get that. You doctors... all you wear are those lab coats."

    n "Suddenly, Gregory's... \"legs\" wobble."

    show g aaa at bounce
    g "Oh! I need to, uh, go. I think I'm... malfunctioning."

    jump robday4cont

label robday4cont:
    hide g with easeoutright
    n "Gregory zooms away, gone as quickly as he came."

    show r with easeinright
    r "He's an interesting guy. I like him."
    r "Reminds me of myself, in a way."

    show r angry
    r "Anyway. The techs came by earlier today, fixed up that machine that was broken."
    r "Don't know if it was you who put in the order, but thanks if so."

    show r
    r "Oh, one second."
    show r yell
    r "WHAT THE HELL IS YOUR PROBLEM? MOVE, DAVID, MOVE!"

    show r
    r "Sorry. He's a shitty reciever. Would be much better if they put him in literally any other position..."

    if ball == False:
        mc "I have no idea what that means."
        show e b annoy at bounce
        e "Neither do I."
        hide e b annoy
    
    mc "Everything's alright in here then? Nothing else causing any problems?"

    r "Nope! Spic n' span, as per usual."

    if wrd3:
        show r angry
        r "You must be pretty sore, though. Make sure you rest those muscles."

        mc "Aye aye, captain."
    
    hide r with easeoutright
    show e with easeinright
    e "Sorry to interrupt, but it's almost shift-end, Doctor. We should leave."

    mc "Oh, yes. Absolutely."

    n "You finish your checklist for the night, wave goodbye to Rob, and leave the gym."

    jump day4end

label day4end:
    scene office with pixellate
    show e with easeinright
    e "Good shift today, Doctor. Tomorrow's Casual Friday. Wear whatever you feel is appropriate."
    show e annoy
    e "Just... try not to show too much skin."

    mc "Will do. Thank you, Miss Esther."

    jump e4first