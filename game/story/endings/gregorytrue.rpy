label END_gregtrue:
    window auto
    scene black
    with fade
    $ daynum = "58"
    $ dayday = "On the road..."

    if renpy.is_skipping() == False:
        show screen truedaytransition
        $ renpy.pause(2.0, hard=True)
    
    scene black with fade
    play music deathtoaperture
    n "The passenger seat is quite loud."
    n "Louder than the radio sometimes."
    n "The three little cores that you took under your wing a month ago rarely stop talking."

    g3e "No. You're just straight-up wrong. Coco Chanel's influence in the 1920s was undeniable."
    g2e "No need to be rude, Rie. I just think Patou's work was {i}better.{/i}"
    g1e "She has a point, though, Gore. Jean Patou was not nearly as influential as Chanel was."
    g2e "No, she's correct. Chanel's work was certainly more influential."
    g2e "That's not the issue I'm having here."
    g2e "I am just stating, in my personal opinion, that Patou's work was more..."
    g3e "More what?"
    g2e "...{i}exciting.{/i}"
    g3e "Oh, if I had hands, Gore, you'd..."
    g1e "Can you two stop fighting?"
    mc "Agreed. You've been talking about this back and forth for the past two and a half hours."
    g2e "I apologize."
    g3e "Sorry."
    mc "I know the three of you love your fashion, but it gets exhausting sometimes..."
    g3e "Sorry, Doc."
    g2e "Yes. We're sorry."
    mc "I forgive you two. Thank you, Greg, for helping."
    g1e "No problem!"
    g2e "Speaking of the past two hours -"
    g3e "Are we almost there yet? This ride's taking a LONG time..."
    mc "Patience. We'll get there shortly."
    g1e "Where are we going, anyways?"
    mc "You'll see."

    n "The past month has been interesting."
    n "You still aren't entirely sure where you stand on your relationship with these three, but..."
    n "Exploring it has been exciting."
    n "They had split up the name \"Gregory\" into three separate monikers -"
    n "Greg, Gore, and Rie."
    n "It would be incredibly smart if it wasn't just the {i}tiniest{/i} bit silly."
    n "There's also been a few complications with the separation -"
    g3e "Oh, Doc, you might wanna pull over."
    g2e "I believe Greg's about to go to sleep again."
    g3e "Jeez, you guys are weak..."
    mc "Alright. One second."
    n "You pull over to the side of the road and pull out the charger attached to your car."
    n "You've had to hotwire your vehicle for longer trips."
    n "Their lower processing power causes them to shut down more often."
    n "In addition, you had to make your very own adapter - Aperture's charging ports aren't really manufactured to standard."
    n "You plug Greg in and pull back onto the road."

    mc "Let him sleep. We'll be there soon anyway."

    scene black with fade
    scene gh town with fade
    mc "Welcome, lady and gentlemen..."
    mc "...to Grand Haven."

    show gre close
    show gore
    show rie happy
    with easeinbottom
    
    if persistent.streammode == False:
        g3e "Damn!"
    g2e "This is a quaint little town."
    show rie angry
    g3e "Greg! Wake up!!"
    show gre shock
    g1e "I'M UP! I'M UP! I -"
    show gre
    show rie look 
    g1e "Oh wow... where are we?"
    mc "Grand Haven."
    mc "This is my hometown. Where I'm from."
    show gore close
    g2e "What, are we meeting your parents?"
    show rie happy
    g3e "Hah, that's a good one."
    mc "Not quite. You'll see what we're here for eventually."
    mc "Right now, we need to find our hotel."

    scene black with fade
    $ renpy.pause(1.0, hard=True)
    scene gh hotel with fade
    n "You enter into the hotel room you've bought out for the next few days -"
    n "It's small, and nothing special, but it'll house the four of you for a while."
    show gre
    show gore
    show rie happy
    with easeinbottom
    g1e "Oh wow! This room is so cute!"
    g2e "This is very thoughtful of you."
    g3e "I call the right side."
    n "You breathe a sigh of relief and set the three cores down on the bed next to you."
    mc "This is where we'll be staying the next few nights, so get comfortable."
    show rie
    g3e "Are we all gonna be squeezing together on this bed?"
    show gore look
    g2e "I doubt the three of us could fit comfortably."
    g1e "You two are so negative! This'll be fun."
    show gre look
    g1e "Frankly, I'm happy for any new experience."
    show rie angry
    if persistent.streammode == True:
        g3e "Every experience is new for us, {k=-5}————{/k}."
    else:
        g3e "Every experience is new for us, dumbass."
    show gore close
    g2e "Why are you {i}so loud,{/i} Rie?"
    show rie happy
    g3e "No, I'm happy for anything new, too."
    g3e "I'm excited."
    show rie look
    g3e "Even if I have to be around you two the whole time..."
    show gore look
    g2e "You love us."
    show gre close
    g1e "I don't believe the act she puts on anymore."
    show gore close
    g2e "Me neither."
    show rie angry
    g3e "Ughh..."
    n "You laugh."
    mc "The three of you..."
    show rie happy
    show gore
    show gre
    mc "You're certainly a handful."
    mc "Honestly, I love it."
    mc "I -"
    show gore close
    show gre sus
    g1e "Oh, Gore's falling asleep."
    mc "I think he has the right idea."
    show rie look
    mc "Let's go to bed. I'll show you what we came here for tomorrow."
    mc "Deal?"
    show gre close
    g1e "Deal."
    g3e "I {i}am{/i} getting pretty tired..."

    n "You get up off the bed to plug the three of them in."
    n "You find an outlet near the bed that'll serve well."
    n "After laying one of the bed's blankets down in front of it, you carefully set the three down."
    menu:
        extend ""
        "(Kiss them.)":
            n "You lean down and kiss each of them, one at a time."
            show rie happy
            g3e "Heh... too bad they weren't awake for that."
            mc "Oh, shush."
        "(Wish them goodnight.)":
            pass
    mc "Goodnight, you three."
    show rie close
    g3e "Mmm... goodnight."

    window auto
    scene black
    with fade
    $ daynum = "59"
    $ dayday = "Grand Haven"

    if renpy.is_skipping() == False:
        show screen truedaytransition
        $ renpy.pause(2.0, hard=True)
    
    scene gh hotel with fade
    n "You wake up gently and turn over to look down at the three cores beside you."
    show rie close
    show gre close
    show gore look
    with easeinbottom
    show gore
    g2e "Oh. Good morning."
    mc "They're still sleeping?"
    g2e "I believe so. Rie was awake a little earlier, but I think she wasn't fully powered yet."
    mc "You might want to get some more rest. The three of you need as much of it as you can get."
    g2e "I'm well aware. What about you?"
    mc "I'm going to go get some breakfast. I'll wake you three up when I get back."
    show rie with Dissolve(0.1)
    g3e "You guys are so loud..."
    mc "Oh, sorry, Rie."
    mc "I'll be back in a bit, you two."
    g2e "Copy that."
    
    scene black with fade
    n "You go downstairs to get some complimentary breakfast."
    n "Briefly, you look outside the doors of the hotel -"
    n "Grand Haven. Where you're from."
    n "It's been ages since you've been back, but you figured..."
    n "If you want to show them the beach, this is the place to do it."
    n "You go back upstairs."

    scene gh hotel with fade
    show rie happy
    show gre 
    show gore
    with easeinbottom
    g1e "You're back!"
    mc "Oh, now you're all awake."
    g2e "I told them to get some more rest, but they wouldn't listen."
    show rie
    g3e "Oh, whatever. I'm perfectly fine with the charge I have."
    mc "Alright. Let's get going then, shall we?"
    show gre look
    g1e "Oh, I'm so excited!"
    g1e "What do you two think? Where are we going?"
    show rie close
    show gore look
    g2e "Logically, we're going somewhere we've never been."
    show gre
    g1e "Oh, I love new things."
    n "You scoop the three cores up and into your bag, and leave the hotel room."

    scene black with fade
    $ renpy.pause(1.0, hard=True)
    scene gh beach with fade
    mc "Alright. We're here. Are you three ready?"
    g1e "Am I ever!"
    g2e "Yes, I'm ready."
    g3e "Can we hurry this up?"
    n "You pull the three cores out of your bag - and reveal the beach."
    show rie
    show gre 
    show gore look
    with easeinbottom
    show rie happy at bounce
    show gre shock at bounce
    show gore at bounce
    g1e "Woah... what {i}is{/i} this place?"
    g3e "I think it's pretty obvious..."
    g2e "We're at the beach."
    g1e "Wow..."
    g2e "Agreed."
    show rie look
    g3e "Eh. It's fine."
    show gre look
    g1e "Rie..."
    show rie happy
    g3e "Okay, okay. It's pretty cool."

    show screen cuttextbox
    scene gregory cutscene 5 with fade
    $ cutscenetextbox = True
    $ cutscenechoice = True
    python:
        if persistent.gc5 == False:
            persistent.cutscenes_seen += 1
            persistent.gc5 = True
        if persistent.cutscenes_seen == cutscene_count:
            achievement.grant("ach_picture")
            achievement.sync()
    g2ecg "{color=#fff}This is incredible."
    g1ecg "{color=#fff}You know, I think I read about this in one of Aperture's records."
    g3ecg "{color=#fff}If this is the ocean, why can I see the shoreline on the other side?"
    mc "{color=#fff}It's not the ocean. We're on Lake Michigan."
    g3ecg "{color=#fff}W-Well. It's nothing special, but..."
    g2ecg "{color=#fff}Rie."
    g3ecg "{color=#fff}Haha, okay, you got me, Gore."
    g3ecg "{color=#fff}This is beautiful."
    g1ecg "{color=#fff}I'm so happy I'm here right now."
    g1ecg "{color=#fff}This is the best day ever."
    g2ecg "{color=#fff}I agree. This is excellent."
    g3ecg "{color=#fff}I..."
    n "{color=#fff}Rie turns to you."
    g3ecg "{color=#fff}I-I'm sorry if I've seemed negative lately. I really am..."
    g3ecg "{color=#fff}I really am grateful."
    g3ecg "{color=#fff}I..."
    g3ecg "{color=#fff}I love you."
    g1ecg "{color=#fff}Awww, Rie."
    g2ecg "{color=#fff}She finally admits it."
    g1ecg "{color=#fff}Same goes for me. I love you, Doctor. Thank you for taking us out here."
    g2ecg "{color=#fff}This was a great idea."
    menu:
        extend ""
        "I love you guys, too.":
            mc "{color=#fff}I-I know things have been weird... getting adjusted to this."
            mc "{color=#fff}I appreciate you all being patient with me..."
            mc "{color=#fff}...while I figured out my feelings."
            g2ecg "{color=#fff}Of course. It only makes sense."
            g2ecg "{color=#fff}The relationship the four of us have..."
            g1ecg "{color=#fff}It's a little different, that's for sure."
        "Thank you guys.":
            pass

    g3ecg "{color=#fff}I wouldn't trade you all, or this moment, for the world."
    g1ecg "{color=#fff}Who knew you were such a sap under that hard shell?"
    g2ecg "{color=#fff}I had a feeling."
    n "{color=#fff}You laugh."
    n "{color=#fff}It's hard not to."
    n "{color=#fff}You look out across the waves."
    n "{color=#fff}There's still some things to figure out..."
    n "{color=#fff}Some hurdles to overcome..."
    n "{color=#fff}But you have a feeling things will be alright."
    stop music fadeout 2.0
    window hide
    $ cutscenechoice = False
    show screen creditsfadeout with fade
    $ renpy.pause(2.0, hard=True)
    hide screen creditsfadeout
    python:
        persistent.endings_got["gregtrue"] = True
        if sum(persistent.endings_got.values()) == ending_count:
            achievement.grant("ach_seenitall")
        if persistent.endings_got["kristrue"] and persistent.endings_got["heathtrue"] and persistent.endings_got["aspentrue"] and persistent.endings_got["cctrue"] and persistent.endings_got["robtrue"] and persistent.endings_got["gregtrue"] and persistent.endings_got["unknowntrue"]:
            achievement.grant("ach_ultrobo")
        achievement.grant("ach_gregtrue")
        achievement.sync()
    $ renpy.movie_cutscene("ENDCREDIT_greg.webm")
    $ MainMenu(confirm=False)()
