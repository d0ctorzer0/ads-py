label day7:
    $ audio_crossFade(1, "music/fourteen.ogg")
    scene mcroom night with fade
    n "You enter back into your room and lay down in your bed."
    n "You set the wakeup time for 11:00, and lay down."
    
    jump day7cont

label day6stayend:
    $ day6stay = True
    n "You decide to stay in."
    n "You read, sleep a little, and go through your paperwork a few times."
    n "It's generally fairly boring."
    n "Eventually, the time comes to go to bed."
    n "You set the wakeup time for 11:00, and lay down."

    jump day7cont

label day7cont:
    scene black
    with fade
    $ daynum = "7"
    $ dayday = "Sunday"

    if renpy.is_skipping() == False:
        show screen daytransition
        $ renpy.pause(2.0, hard=True)

    scene mcroom day with fade
    n "You wake up to a knocking on your door."
    ac "Disruption detected. Automatic waking sequence initiated."
    n "You groan and lean over. The clock reads 09:43."
    mc "Who could possibly..."
    n "The knocking continues."
    n "You get up, go over to the door, and open it with a sigh."

    show e with easeinright
    n "Miss Esther greets you."
    e "Doctor! Doctor, so sorry to wake you."

    mc "...Miss Esther? What are you doing here?"

    show e laugh
    e "Oh yes, I'm sorry - I was just wondering if you'd be interested in a day out with me?"
    show e
    e "Nothing terribly formal, simply an invite from a friend."

    menu:
        extend ""
        "Uh... sure. Let me just get ready.":
            jump day7esther
        "Uh... I don't know. I'm very tired.":
            jump day7alone

label day7esther:
    show e laugh
    e "Oh! Yes. Sorry, sorry."

    show e
    mc "Give me just a minute."
    hide e with easeoutright

    n "You close the door and change out of your pajamas, brush your teeth and put on your shoes."
    n "You open the door once more. Miss Esther is still waiting."

    show e with easeinright
    e "Doctor, fashionable as always. Shall we head out?"

    mc "Yes, I'm ready now."

    show e laugh
    e "Excellent!"
    
    scene hall with fade
    $ audio_crossFade(2, "music/twelve.ogg")
    show e with easeinright
    n "Miss Esther guides you down the hall, out of residential."
    e "Most parts of recreation are closed on Sundays. I suppose it's to give {i}everyone{/i} a day off."

    show e annoy
    e "Rob and Heath, for example. They're usually on a 24/7 recreational schedule, but..."
    show e
    e "Sunday affords them a day off."

    mc "That's good."
    show e shock
    e "Anyway, Doctor, I just wanted to invite you out, because..."
    show e
    e "...well, we don't get all too much time to chat between all the places we have to go during your shift."
    e "This way, we can just talk. You and I."

    mc "Uh... yeah."
    mc "Where are we headed, anyway?"

    show e laugh
    e "Oh, just the cafeteria. I figured you might want something to eat."

    mc "Ah, yeah. I am kind of hungry."

    show e
    e "Great! We're almost there."

    scene cafe with fade
    n "You walk into the cafeteria. There's actually quite a few people in here."
    n "There's no other cores besides Miss Esther, although that's to be expected with the mostly human fare."

    show e with easeinright
    e "Go ahead and grab yourself some food. I'll be here in the corner - not a lot of management rails to follow! Haha."
    hide e with easeoutright
    
    n "You head over to the buffet-style island in the middle of the cafeteria."
    n "It's not very full - it seems a lot of your coworkers are early risers."
    n "You take a look at the food."

    menu:
        extend " You decide to grab..."
        "(A vegetable omelette.)":
            n "You grab a vegetable omelette and take it with you over to Miss Esther."
            mc "I wonder where they get the eggs..."
            n "You decide not to question it further."
        "(A hefty serving of sausage.)":
            n "You scoop some sausages onto your plate."
            mc "Need my protein."
            mc "This is probably artificial meat, but..."
            n "You walk over to Miss Esther."
        "(A lemon pastry.)":
            mc "Something sweet to start the day."
            n "You grab the lemon tart and head over to Miss Esther."
    
    show e with easeinright
    e "Ah, Doctor. Find something you like, I presume?"

    mc "Yes, I did."

    show e laugh
    e "Haha. Good, good."
    show e annoy
    e "So... how was yesterday?"

    if day6stay == True: # Why would you ever do this? Seriously? You disappointment.
        mc "Oh, I just stayed in my room and read some books."
        mc "Nothing much happened, honestly."

        show e shock
        e "You had a whole campus to explore, and instead you decided to stay inside?"
        show e annoy
        e "Well then."
        e "Fair enough."
    if day6stay == False:
        mc "I explored the campus a little. Just wandered, honestly."
        
        show e  
        e "Fun! I'm glad you got out, Doctor."
        e "Did you leave the section at all?"

        mc "Not really. I'm kind of a homebody, so that's sort of out of my comfort zone."

        e "Fair enough."

    show e annoy
    show screen vignette with vigswitch
    stop music fadeout 1.0
    stop music1 fadeout 1.0
    e "Doctor... I have something important to tell you."
    e "Please listen carefully."

    mc "Uh... yes. I'm listening."

    e "Do not get too close to the cores in your section."
    e "It is against your contract to form strong relationships with them."
    e "Of course, friendly banter, speaking outside of working hours... that is fine."
    e "But any more than that and it may become an issue."
    e "It won't turn out well for you."
    e "Do you understand?"

    mc "Uh..."
    mc "Yes. I understand, Miss Esther."

    play music thirteen
    show e
    hide screen vignette with vigswitch
    e "Great! I'm glad we got that sorted out."
    show e shock
    e "Anyway, sorry for dragging down the mood..."
    show e

    n "Miss Esther suddenly goes back to her normal self."
    show e laugh
    n "She speaks to you about her work and how she became a Supervisor Core."
    n "One of many, she says, though you find it hard to believe there's truly that many at Aperture."
    
    show e
    e "Supervisor Core XA3. That's me."
    mc "{i}X{/i}-A-3?! You number all the way to the end of the alphabet?"
    show e laugh
    e "Well, many of those codes are being used for other arbitrary reasons, but..."
    show e
    e "Yes, generally, we do. Or we did."
    show e shock
    e "I'm not quite sure exactly how many of us are actually still Supervisor Cores, but..."
    show e
    e "That's neither here nor there."
    e "Eat! What are you waiting for?"

    mc "Uhh... I've kind of lost my appetite."

    show e
    e "Oh, that's not good. I hope that wasn't my fault."

    menu:
        extend ""
        "It kind of was.":
            $ esther_affection -= 1
            show e annoy
            e "Oh. I'm sorry, Doctor."
        "No, I'm just not hungry anymore.":
            $ esther_affection += 1
            show e laugh
            e "Fair enough!"
    
    show e
    e "Anyways. Your work is going incredibly well. Management seems to be happy with your reports."

    mc "Well, to be honest, the work isn't very hard."

    e "True enough, though it's one of the few jobs they only want a human to do..."
    show e annoy
    e "A robotic supervisor is fine, but apparently I'm not effective enough on my own."

    mc "Interesting."

    show e
    e "Thinking about it, though, we do sometimes tend to have a... bias towards members of our own species."
    e "I suppose it only makes sense to have a robot-human team working together..."

    if esther_affection >= 5:
        show e laugh
        e "It's a good thing I like you, then, right?"

        menu:
            extend ""
            "I like you too, Miss Esther. A lot.":
                jump esthershootdown
            "I like you too.":
                show e
                e "I'm glad."
                jump day7plate
    
    mc "Yes, I suppose so."

    jump day7plate


label day7plate:
    n "You clear your throat and get up to put your plate away."

    mc "Thanks for inviting me out, Miss Esther, but I'm incredibly tired."

    show e
    e "Oh yes, absolutely. Please get some rest."
    show e laugh
    e "Work starts again tomorrow, after all!"
    show e
    e "See you then, Doctor."

    mc "See you then."

    hide e with easeoutright

    n "You leave the cafeteria and head back to your room."

    jump day7end

label esthershootdown:
    show e shock
    e "Oh, Doctor, you're not -"
    e "You're not insinuating -"
    show e annoy
    e "I'm terribly sorry, Doctor, but if you're saying what I think you're saying -"
    e "I'm afraid I just can't reciprocate."
    show e
    e "For one, I just warned you not to get too close to us..."
    show e shock
    e "But more importantly, I just... I just don't feel that way about anything... any{i}one{/i}, honestly."
    show e laugh
    e "I am flattered, though. I hope this won't make working together difficult."

    show e
    mc "No, I understand, Miss Esther. I apologize."
    mc "I won't bring it up again."

    e "Thank you, Doctor."

    jump day7plate

label day7alone:
    show e shock
    e "Ah no, I understand. So sorry to bother you, Doctor."
    e "I'll let you be, but..."
    show e annoy
    show screen vignette with vigswitch
    stop music fadeout 1.0
    stop music1 fadeout 1.0
    e "First..."
    e "Doctor... I have something important to tell you."
    e "Please listen carefully."

    mc "Uh... yes. I'm listening."

    e "Do not get too close to the cores in your section."
    e "It is against your contract to form strong relationships with them."
    e "Of course, friendly banter, speaking outside of working hours... that is fine."
    e "But any more than that and it may become an issue."
    e "It won't turn out well for you."
    e "Do you understand?"

    mc "Uh..."
    mc "Yes. I understand, Miss Esther."

    play music fourteen
    show e
    hide screen vignette with vigswitch
    e "Great! I'm glad we got that sorted out."
    
    show e shock
    e "Anyways, I'll leave you be now - get some rest for work tomorrow!"
    show e
    e "Goodbye, Doctor!"

    mc "Um... goodbye."

    hide e with easeoutright
    n "And she's gone, as quickly as she came."
    n "Did she really only come to give you that warning?"
    n "You feel a chill run down your spine."
    n "You shake it off and think about going back to bed..."
    n "...but for some reason, it just looks so... uncomfortable."

    n "Instead, you decide to try to focus your mind on other things."
    n "You read, sift through your paperwork... not a lot to do when you're holed up in your room like this."

    jump day8