label day2:

    scene mctemproom
    with fade

    n "You arrive at your new quarters. They're humble, really only meant to house you while you sleep and no more."
    n "You sigh."

    mc "What a weird first day..."

    n "You drop off your bag and lay down on your stasis chamber, which will wake you up in the morning."
    n "You wonder if this thing actually makes sleep more efficient or not."
    n "With that, you gently close your eyes."

    scene black
    with fade

    n "You don't dream. But then again, no one does in stasis."

    scene mctemproom
    with fade

    n "You gently wake up and look at the clock. It's 08:00 on the dot."
    n "Groaning, you get up and head towards your office."

    scene office
    with pixellate

    n "Miss Esther isn't here yet. You organize your files while you wait."
    n "Suddenly, there's a knock on the door."

    mc "Yes? Who is it?"

    u "I'm havin' some trouble here, can't seem to activate these here door mechanisms..."

    n "You get up and go over to the office entrance."

    menu:
        extend ""
    
        "This room is only accessible to maintenance staff.":
            $ romance_points["???"] -= 3
            jump lockout
        
        "I'll open the door, but just this once.":
            $ romance_points["???"] += 3
            jump letin

        "(Stay silent.)":
            $ romance_points["???"] -= 1
            jump silence

label lockout:
    u "Well, y-yeah, but I was thinkin', y'know, you'd make an exception?"

    mc "And why would I do that?"

    u "'Cuz I'm so charmin'?"

    mc "And risk losing my job?"

    u "Alrigh', now, no need to get so serious on me..."

    mc "Get out of here before Miss Esther comes and reprimands you."

    u "I'm goin', I'm goin'."

    n "You scoff and return back to your desk."
    
    jump estherday2

label letin:
    n "You unlcok the door using the keypad, and a familiar face comes \"stumbling\" in."

    show u
    with easeinright
    u "Why hello there, pretty little thing."

    mc "What do you want?"

    u "I jus' wanted to come 'n say hi."

    u "Oh, and also invite you out to my place after work, of course..."

    mc "Haha, and why's that?"

    show u upset
    u "Well, s'not everyday now that a beautiful human like yourself shows their face 'round here."

    show u
    u "I'm takin' a chance while I still got it, now."

    mc "I appreciate the gesture, but I'm very busy. I have a lot of work to get done."

    u "Yea, yea, I know. You scientists are always busy."

    n "The core glanced around himself nervously."

    show u upset
    u "Listen, I should scram 'fore that little pink core of yours shows up again."

    mc "Miss Esther, you mean?"

    u "Yeah, yeah, her. So. I'll send you a little message tonight."
    show u
    u "Keep an eye on your inbox, yeah?"

    hide u
    with easeoutright
    n "The core gave a little bow and exited the room."

    mc "If nothing else, he's certainly interesting..."

    n "You return back to your desk."

    jump estherday2

label silence:
    n "You stay quiet."

    u "Uhhh... hello?"

    mc "..."

    u "I swear I coulda heard you answer me. I know you're in there."

    mc "..."

    u "Or maybe not..."

    u "Maybe I'll try again later."

    n "You hear the core zoom away from your door. You sigh."

    n "You return to your desk."

    jump estherday2

label estherday2:
    n "Just as you sit back down, the door opens and Miss Esther comes barreling in extremely fast."

    show e shock
    with easeinright
    e "Sorry! Sorry I'm late! I got caught up in rail traffic..."

    show e annoy
    n "She shakes her head."

    e "You'd think with the increase in robots working at Aperture, they'd at least {i}try{/i} to expand the rail system..."

    show e
    e "Regardless! Welcome back. Since we're a little behind, we should get started right away. Do you have everything you need?"

    mc "Yes, I believe so."

    e "Perfect. Come along, now."

    jump krisday2

label krisday2:
    scene temphall
    with pixellate
    show e
    with easeinright
    n "You and Miss Esther approach the conference room, just as yesterday."

    e "I know maintenance can be a tedious job, but don't get discouraged."
    e "A lot of other employees in this department would kill to have a route like yours."
    show e annoy
    e "Epecially considering the majority of personality cores aren't... great."

    scene kristemproom
    with pixellate
    show k
    with easeinright
    k "Why hello, and welcome back. I'm assuming your route went well yesterday if you're still here now."

    mc "I'd say so. Any changes in the stock today?"

    show k flirt
    k "Not that I've seen, no. Ever since the new CEO took over, things have mostly been quiet."

    mc "She maintains the finance department well, then?"

    show k
    k "Yes, I'd say so. Smart one, that."

    menu:
        extend ""
        
        "You know, I manage my funds pretty nicely myself.":
            $ romance_points["Kris"] += 3
            jump impresskris2

        "It's pretty easy to not spend recklessly.":
            $ romance_points["Kris"] -= 3
            jump offendkris2
        
        "I agree. She's doing well for the company.":
            $ romance_points["Kris"] += 1
            k "Better than the last one, for sure."
            jump krisday2cont
    
label impresskris2:
    show k flirt
    k "Is that so?"

    mc "Why yes. I watch my spending carefully, especially after the turmoil the company recently went through."

    show k angry
    k "Do you have any investments?"

    mc "Of course. I'm not an idiot."

    show k
    k "That's not what I was implying."
    show k flirt
    k "It's important to invest. I'm glad you see that."

    jump krisday2cont

label offendkris2:
    show k angry
    k "What do you mean by that?"

    mc "The former CEO. His reckless spending put the company deep in the gutter."

    k "I'm aware, but I don't like your tone."
    k "Finances are not easy to manage."
    show k
    k "The fact you think they are speaks measures about how well you truly manage your own."

    jump krisday2cont

label krisday2cont:
    hide k
    with easeoutright
    show e annoy
    with easeinright

    e "We've really ought to be going, now."

    if romance_points["Kris"] >= 5:
        hide e with easeoutright
        show k flirt with easeinright

        k "I hope I'll see you tomorrow."
        n "Miss Esther rolls her optic."

        hide k flirt with easeoutright

    elif romance_points["Kris"] <= 4:
        hide e with easeoutright
        show k with easeinright

        k "Yes, you have more to attend to."

        hide k with easeoutright

    n "You check Kris off your list and head out."
    jump heathday2

label heathday2:
    scene temphall
    with pixellate

    show e annoy with easeinright
    e "Heath likes to show a new \"trick\" every day, so don't be suprised if she tries to do one again."

    mc "Does she actually think what she does is \"magic\"?"

    e "I have no clue. I'm not particularly interested in... uh..."
    e "...getting to know any of them."

    mc "Why not?"

    e "\"Connection\"... it's just not my thing. I don't understand how you humans can do it."

    scene heathtemproom
    with pixellate

    n "You enter the stage room to find Heath already waiting for you."

    show h with easeinright
    h "Welcome, welcome! Apologies for the delay yesterday, it won't happen again! I'm ready this time!"

    n "You wait with baited breath."

    show h sad
    h "Now... choose a card... any card..."

    show h
    h "Well, any card that I have on me, preferably, but..."

    jump heathmenuday2

label heathmenuday2:
    menu:
        extend ""

        "Heath, I don't really have time for this.":
            $ romance_points["Heath"] -= 3
            jump offendheath2

        "Uhh... the three of clubs?":
            $ romance_points["Heath"] += 3
            jump impressheath2
        
        "Ace of Spades." if spades == True:
            $ romance_points["Heath"] += 1
            jump neutralheath

label offendheath2:

    show h sad
    h "Oh. Yeah. You've got important science stuff to get to, huh?"

    mc "Sorry. I just don't really like magic all too much."

    h "That's alright."

    mc "You're doing everything to need to, yes? Keeping morale high and all that?"

    h "I think so."

    mc "Great."

    jump heathday2cont

label impressheath2:

    show h laugh
    h "HAHA! Is {b}THIS{/b} your card?"

    n "She pulls out exactly what you thought of - the three of clubs."

    show h
    mc "Wow! Yes, that's exactly it! Amazing."

    h "Hahaha, thank you, thank you very much."
    n "Miss Esther groans."

    h "Is your morale improved? Your spirits lifted?"

    mc "Definitely. And on top of that, I'm impressed, too."

    show h sad
    h "O-Oh, really? It's nothing, honestly, haha."

    jump heathday2cont

label neutralheath:
    $ spades = False
    show h sad
    h "Oh, um, actually, I don't have that card with me. Can you... choose again?"

    jump heathmenuday2

label heathday2cont:
    hide h with easeoutright
    n "You check Heath off your list. Aspen is next."

    show e annoy with easeinright
    e "I hope that disgusting core we saw yesterday doesn't make another appearance..."

    scene temphall
    with pixellate

    n "testend"