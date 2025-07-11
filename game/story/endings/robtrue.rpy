label END_robtrue:
    window auto
    scene black
    with fade
    $ renpy.pause(2.0, hard=True)
    $ daynum = "50" # people can reverse-engineer this to find out the exact day MC escapes from Aperture
    $ dayday = "Detroit"

    if renpy.is_skipping() == False:
        show screen truedaytransition
        $ renpy.pause(2.0, hard=True)

    scene det car with fade
    play music deathtoaperture
    n "The radio's playing."
    n "The sun is shining."
    n "There's not a cloud in the sky."
    n "It's a perfect day for a ball game."
    rd "And today, in just two hours, our very own Detroit Tigers will hit off against the Milwaukee Brewers..."
    rd "We're expecting another loss for our boys, but we'll have to wait and see how things turn out."
    mc "They don't sound very optimistic."
    show r look offrail with easeinbottom
    r "From what I've heard, the Tigers aren't the best team."
    show r offrail
    r "Oh man, though, am I excited!"
    r "My first real game!"
    r "And nearby, no less."
    mc "I'm glad we didn't have to drive too far."
    if ball == True:
        mc "You know, this is my first baseball game in ages."
        mc "I think the last time I went to see a baseball game was... 1981."
        show r look offrail
        r "Jeez, it really has been a while."
        show r offrail
        r "Well, if you need me to remind ya of anything, just let me know!"
    else:
        mc "You know, this is my first baseball game ever."
        mc "In person, at least."
        r "Jeez, you've never seen one before?"
        r "There's a first time for everything, then!"
    mc "..."
    mc "You know... I left that card you got me behind."
    mc "Back at Aperture."
    show r look offrail
    r "Ah, the Jose Canseco one?"
    r "It's no biggie. It was only really special 'cuz it was the first one I'd ever gotten."
    r "Getting out of that place... these last couple weeks with you..."
    show r offrail
    show rob blush with Dissolve(0.05)
    r "That's the real prize, y'know."
    mc "Now {i}that{/i} I can relate to."

    scene black with fade
    $ renpy.pause(1.0)
    scene det stadium with fade
    n "The stadium's packed."
    n "You clutch your backpack close to your chest and squeeze into your two seats in the back."
    n "Thankfully, it looks like the seats beside you are fairly empty."
    n "You lean over to your bag and whisper into it."
    mc "Looks like it'll be safe to take you out in just a little bit."
    r "Alright, Doc, but hurry, yeah?"
    r "It's hot as hell in here!"
    mc "Oh, shush. You can handle it a little longer."
    r "Ugh..."
    n "It's a beautiful day. The sky is clear and, for once, the grass is actually green."
    n "You decided to skip out on front-row tickets."
    n "It was difficult enough getting Rob through the front gates..."
    n "His small size gives him some leeway - from a distance, you could even mistake him for a weirdly-colored basketball -"
    n "- but he still looks quite strange regardless, and the last thing you need is some curious stranger asking where he came from."
    n "And why he talks so much."
    mc "You won't be able to yell this time around."
    r "I can't make any guarantees, y'know."
    mc "That's why I got us seats away from everyone else."
    r "Ah, you anticipated this, didya?"
    mc "Of course I did."
    mc "I think I know you well enough by now."
    r "Yeah... you're right, hah."
    n "You look around you carefully."
    mc "Alright... I think it's safe to take you out now."
    mc "You ready?"
    r "Boy, am I."
    show r offrail with easeinbottom
    n "You pull Rob out of your bag cautiously."
    n "He looks around excitedly."
    r "Holy cow! This place is huge!"
    r "It looks so much bigger in person!"
    show r look offrail
    r "Oh wow. I can't believe I'm here right now, Doc."
    r "So far from that dumb little gym I used to spend my whole life in..."
    show r offrail
    r "I'm right in the middle of it now! Ha!"
    r "The stadiums I've seen so many times through those stupid screens... right in front of me!"
    r "This is wild!"
    r "A-And the players - hah! They're... {i}there!{/i}"
    mc "I knew you'd love this."
    show r look offrail
    show rob blush with Dissolve(0.05)
    r "Not as much as I love you for bringing me here."
    hide rob blush
    r "Seriously, Doc."
    r "None of this woulda been possible without ya, y'know."
    r "Getting outta that place..."
    r "Hell, even getting out from under that damn TV..."
    r "And seeing all this?"
    show r offrail
    r "That's all on you."
    r "I love ya. Serious."
    menu:
        extend ""
        "You're so sweet.":
            show r look offrail
            r "Hah. I know."
        "I love you too.":
            r "'Bout time you reciprocate!"
            show r look offrail
            r "I knew my unbeatable charm would get to ya eventually."
    show r offrail
    ann "Welcome, baseball fans!"
    ann "Today's game is between the Milwaukee Brewers and our very own Detroit Tigers!"
    ann "Let's have a good game, folks!"
    mc "Looks like it's starting, Rob."
    r "Hell yeah! LET'S GO TIGERS!"
    n "You laugh."
    show r look offrail
    n "Rob looks away from you sheepishly."
    r "Sorry. I know you said no yelling."
    mc "Ah, I really don't care."
    mc "I'll just pretend I'm the one yelling if anyone looks."
    show r offrail
    r "You're funny."
    mc "You're one to talk."

    scene black with fade
    scene det stadium with fade
    n "The game's exciting."
    n "The Tigers take a surprising lead over the Brewers - something neither of you saw coming -"
    n "- and apparently, something the announcer didn't see coming, either."
    ann "What an upset! Lou Whitaker hits a home run!"
    n "The crowd goes wild."
    n "Rob included."
    show r offrail with easeinbottom
    r "HELL YEAH! GREAT HIT!"
    r "Aww, this is awesome!! Best day of my life!"
    mc "It's definitely up there for me as well."
    r "It ain't at the top?"
    mc "No. That spot goes to the day you confessed to me."
    show r look offrail
    show rob blush with Dissolve(0.05)
    r "Hah... don't make me blush, Doc."
    mc "Don't be ridiculous. You can't blush."
    hide rob blush
    show r offrail
    r "Mmm. Got me there."
    r "Don't make me... overheat."
    mc "I don't make any promises, Rob."
    ann "And the bases are loaded! This might be it, folks - can the Tigers take this one home?"
    r "Oh man, I'm on the edge of my seat."
    r "This is so much more exciting in person."

    if ball == True:
        mc "The bases being \"loaded\" - remind me what that means again?"
    else:
        mc "The bases being \"loaded\" - what does that mean?"
    
    show r look offrail
    r "Ah, it's just slang for when all three bases have a player on 'em."
    show r offrail
    r "Essentially, it means the other team is screwed! Hah!"
    r "If the next player up to bat hits a home run, they get a whole load of points 'cuz everyone goes to the home plate."
    r "One of my favorite parts of baseball."
    show r look offrail
    r "Honestly, I like baseball more than football..."
    r "Personal preference, 'course, but..."

    mc "You know, I never hear you talk like this."

    show r offrail
    r "Whaddaya mean?"
    mc "Going off on these little tangents. It's cute."
    mc "All I used to hear was you yelling at the TV."
    mc "Still hear that sometimes in our living room, but... it's different."

    show r look offrail
    r "I really hope that doesn't bother you too much, Doc."
    r "I just get so pumped while the game's on, I..."
    mc "I like having you in the house, Rob."
    mc "I enjoy your presence."
    mc "I want you with me."
    show r offrail
    r "I..."
    r "Well. For once, Doc, you've left me speechless."
    mc "What an achievement."

    scene black with fade
    scene det park with fade
    n "The sun's beginning to set."
    n "With the game over, the two of you decided to end the day with a walk through the park before heading home."
    n "Rob looks content."
    show r offrail with easeinbottom
    r "I can't believe they actually won. That was crazy."
    mc "Definitely exciting."
    show r close offrail
    n "Crickets chirp gently in the distance."
    n "The tree branches sway in the wind..."
    n "It's a beautiful summer night, but..."
    n "Rob is strangely quiet."
    mc "Rob?"
    show r offrail with Dissolve(0.2)
    r "{cps=7}Hmm?"
    show r look offrail
    r "Ah, sorry. Did I doze off again?"
    mc "No, I'm sorry. I didn't mean to wake you."
    show r close offrail
    r "Mmm... Doc, can you lay me down in the grass?"
    r "I wanna look up at that sky again."
    show r look offrail
    r "Feels like I can never get enough of that thing..."
    mc "Of course, Rob."
    show screen cuttextbox
    scene rob cutscene 6 with fade
    $ cutscenetextbox = True
    python:
        if persistent.rc6 == False:
            persistent.cutscenes_seen += 1
            persistent.rc6 = True
        achievement.progress("ach_picture", persistent.cutscenes_seen)
        achievement.sync()
    r "{color=#fff}Ahh... that feels so nice."
    mc "{color=#fff}I'm surprised you can even feel the grass under your chassis."
    r "{color=#fff}It ain't \"feeling\" like how most humans define it, but..."
    r "{color=#fff}I've got some sensation."
    r "{color=#fff}Glad they didn't install those pain receptors in me, though..."
    r "{color=#fff}Some cores get that. Sounded horrible."
    r "{color=#fff}This broken handle and optic of mine would prolly hurt like hell if I had those things."
    r "{color=#fff}..."
    r "{color=#fff}Man, today was just perfect."
    r "{color=#fff}I couldn't imagine anything better than bein' out here with you right now."
    r "{color=#fff}I had no idea what I was missing down in Aperture..."
    r "{color=#fff}Screw Celine. I should've been lookin' for a human sooner, huh?"
    mc "{color=#fff}Haha. I think we got a little lucky."
    r "{color=#fff}Tell me about it! Who woulda thought a little core like me would have such a beautiful human for a partner..."
    r "{color=#fff}{i}I'm{/i} the lucky one here, Doc."
    r "{color=#fff}God..."
    r "{color=#fff}You're beautiful."
    r "{color=#fff}Thanks for bringin' me out here."
    r "{color=#fff}This was everything I coulda hoped for..."
    r "{color=#fff}And more."
    stop music fadeout 2.0
    window auto
    show screen creditsfadeout with fade
    $ renpy.pause(2.0, hard=True)
    hide screen creditsfadeout
    python:
        if persistent.endings_got["robtrue"] == False:
            persistent.endings_count += 1
            persistent.endings_got["robtrue"] = True
        achievement.progress("ach_seenitall", persistent.endings_count)
        achievement.sync()
        achievement.grant("ach_robtrue")
        achievement.sync()
    $ renpy.movie_cutscene("ENDCREDIT_rob.webm")
    $ MainMenu(confirm=False)()