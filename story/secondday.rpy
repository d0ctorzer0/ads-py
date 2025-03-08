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