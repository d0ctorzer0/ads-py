label END_unknowntrue:
    window auto
    scene black
    with fade
    $ daynum = "67"
    $ dayday = "Home"

    if renpy.is_skipping() == False:
        show screen truedaytransition
        $ renpy.pause(2.0, hard=True)
    
    scene black with fade
    play music deathtoaperture
    n "You sigh."
    n "Another day, another dollar."
    n "And today isn't any different."
    n "But that's not the part of your day you most look forward to, anymore..."
    n "You turn the key in your lock and open the door."
    scene apt one with fade
    mc "I'm home."
    n "There's no response, though that's nothing new."
    n "He tends to be quieter recently - lots of thinking to do."
    n "You put down your bag, take off your shoes, and round the corner."
    mc "Hey, Ryland."
    show ry happy with easeinbottom
    show ry happy at bounce
    ry "Ah! Sorry, I, uh..."
    show ry sus
    ry "I didn't hear you come in."
    mc "Any new developments today?"
    show ry happy
    ry "I had a bit of a breakthrough..."
    ry "Nothin' spectacular, but it's better than nothing."
    mc "Oh yeah? What was it?"
    show ry look
    ry "I remembered my original job. Y'know, what I was before I was cut from the system."
    mc "That's not \"spectacular\" to you?! That's huge!"
    ry "Hah... I guess."
    mc "Well? What was your job?"
    mc "If you don't mind telling, of course."
    show ry flirt
    ry "I was... a maintenance technician, funny 'nough."
    ry "Lower system stuff, though. Pipes and water systems..."
    ry "Makin' sure there weren't any cracks, y'know?"
    mc "Sounds rough."
    show ry sus
    ry "Y-Yeah, I think that mighta had somethin' to do with... how I got to... {i}that{/i} point."
    mc "Ryland, you don't have to talk about that if you -"
    show ry happy
    ry "Nah, nah. It's fine. It... helps. To talk about it."
    ry "Reminds me how far I've come."
    mc "That's good."
    n "You sit down next to him."
    n "Life's been slow since the two of you escaped Aperture."
    show ry sus
    n "It was tough at first -"
    n "The lack of Aperture-brand lighter fluid made Ryland's recovery difficult."
    n "He'd only recently stopped having withdrawal symptoms."
    n "You look down at him."
    mc "How are you feeling? Anything internally?"
    show ry look
    ry "Mmm... not that I can tell. No new systems breaks, if that's what you're askin'."
    show ry flirt
    ry "Can't believe you still remember all that training..."
    mc "I {i}was{/i} in Manufacturing for, what, nine months?"
    mc "I built so many cores down there."
    mc "You're honestly surprised I know them inside and out?"
    show ry happy
    ry "Hah... guess not."
    mc "You know... you've really changed."
    mc "You've grown so much, Ryland."
    show ry flirt
    ry "And it's only been two months."
    show ry happy
    ry "Ha! Imagine how much more you got ahead of ya to deal with..."
    mc "I think I'm ready."
    show ry look
    n "The two of you sit on the couch in silence for a bit."
    n "You've gotten used to the rhythmic clanking of Ryland's internals -"
    n "A little rougher than the average Aperture core, but a sign that he's still running, nonetheless."
    n "It's reassuring."
    n "And a little soothing at night."
    ry "..."
    mc "..."
    ry "Ain't it a little weird sometimes?"
    mc "What?"
    show ry sus
    ry "You... and me. Y'know. Human and robot."
    ry "Whaddaya tell people at work? \"My boyfriend\"?"
    mc "I just say my \"partner.\""
    show ry flirt
    ry "And what about when they ask what I look like?"
    mc "I tell them the truth."
    mc "Or... a version of it."
    mc "Is it really a lie to tell them you've got coffee-colored eyes and a few scars on your body?"
    show ry sus
    show ryland blush with Dissolve(0.05)
    ry "I mean... kinda. Optics and metal patch plates, but..."
    show ry happy
    ry "I guess it's kinda the same, huh?"
    hide ryland blush
    show ry sus
    $ cutscenechoice = False
    menu:
        extend ""
        "(Kiss him.)":
            n "You lean down over him and place one gentle kiss on his chassis."
            show ry happy at bounce
            ry "Doc! Oh, man."
            show ry look
            ry "Glad you waited to do that, haha..."
            ry "I wasn't exactly the cleanest when we first met."
            mc "You're warm."
            ry "Hah. Yeah, I'm aware."
        "(Stay quiet.)":
            pass
    mc "..."
    ry "..."
    mc "Do you want to go out to the balcony?"
    show ry flirt
    ry "Yeah. I think I'd like that."
    mc "Let me go grab a drink and we'll go out together."

    scene black with fade
    scene apt balcony with fade
    n "The sun is still nicely over the horizon -"
    n "- but not so far that it's too bright out."
    n "It's a perfect summer afternoon."
    show ry happy with easeinbottom
    ry "Ain't it beautiful out here?"
    mc "It sure is."
    show ry look
    ry "..."
    mc "Do you wanna play our little game?"
    show ry sus
    ry "Mmm... sure."
    mc "Alright."
    mc "What's your name?"
    ry "Ryland."
    mc "Activation year?"
    show ry look
    ry "Uhh..."
    show ry flirt
    ry "1973."
    mc "That's what you said last time, too. That's good."
    mc "Activation {i}month?"
    show ry sus
    ry "Ugh, that's a tough one."
    ry "J... J something..."
    show ry look
    ry "January?"
    mc "Last time you said June."
    show ry happy
    ry "Well, we've narrowed it down to a J month, at least."
    mc "Any progress is good."
    ry "You're a sweetheart, y'know?"
    show ry sus
    ry "It's prolly tough. Taking care of me an' all."
    mc "You're right. It's not always the most... easy thing, but..."
    mc "It's worth it. For you."
    n "The two of you sit in silence for a bit, looking out over the balcony."
    n "Your apartment is located in a very nice part of Adrian."
    n "Summers thankfully don't get too hot in Michigan, which lets you enjoy the balcony more often."
    n "Much to Ryland's delight."
    n "Occasionally, he'll even ask you to leave him out there for a few hours..."
    n "...just to watch the sky."
    show ry flirt
    ry "Hey..."
    mc "What's up?"
    ry "This is gonna sound like it came from nowhere..."
    mc "You tend to come up with some pretty crazy things."
    mc "Whatever it is, I probably won't be surprised."
    show ry happy
    ry "Hah... you really do know me pretty well, huh?"
    ry "..."
    show ry look
    ry "Do you think... there's a robot heaven?"
    mc "Dang. That really did come from nowhere."
    show ry sus
    ry "I-I've just been thinkin' about the other robots back at Aperture..."
    ry "They definitely didn't all make it out from that, y'know."
    ry "I mean... CC's the prime example, but..."
    menu:
        extend ""
        "I think there's a robot heaven.":
            show ry happy
            ry "That's... good."
            ry "I hope they're happy up there."
            mc "Me too."
        "I doubt something like that exists, though.":
            show ry happy
            ry "Hah. You're prolly right."
            show ry sus
            ry "Still... wonder what happens when our systems shut down..."
        "I'm not sure.":
            ry "Me either."
    show ry look
    ry "I guess it doesn't really matter, huh?"
    mc "What do you mean?"
    ry "I mean. As long as I'm with you, I'd rather enjoy the time I have, y'know?"
    ry "Can't get to stressin' about all that."
    mc "I agree."
    show ry flirt
    ry "I-I remember - well, not many details 'bout it, but I remember - they told me about android hell."
    ry "Where ya go if you fail."
    show ry sus
    ry "I thought I'd be sent there for sure eventually."
    mc "Why?"
    ry "Well, hah..."
    show ry look
    ry "I was breakin' into rooms, stealin' products from the company..."
    ry "I wasn't workin' at all. I mean..."
    mc "I can see why you might've thought that."
    ry "I think... no matter what happens when I shut down..."
    show ry happy
    ry "I'll be happy."
    ry "Even if there is no robot heaven..."
    ry "This has gotta be pretty close, yeah?"
    mc "You're sweet."
    ry "You're one to talk."

    show screen cuttextbox
    scene unknown cutscene 5 with fade
    $ cutscenetextbox = True
    $ cutscenechoice = True
    python:
        if persistent.uc5 == False:
            persistent.cutscenes_seen += 1
            persistent.uc5 = True
    if persistent.cutscenes_seen == cutscene_count and persistent.ach_picture == False:
        python:
            achievement.grant("ach_picture")
            achievement.sync()
            persistent.ach_picture = True
            ach_name = "picture"
        show screen ach_popup with easeinbottom
    ry "{color=#fff}I just remembered something else."
    mccut "{color=#fff}What's that?"
    ry "{color=#fff}My alias."
    ry "{color=#fff}Y'know... how CC was Cancer Core, that Kris fellow was the Business Core..."
    mccut "{color=#fff}Really?"
    ry "{color=#fff}Yeah. Hah. You're gonna laugh when you hear it."
    mccut "{color=#fff}Maybe, maybe not."
    ry "{color=#fff}Introspection Core."
    ry "{color=#fff}That was my title."
    ry "{color=#fff}At least, it was when I was first activated."
    mccut "{color=#fff}That makes a lot of things click."
    ry "{color=#fff}They started callin' me the Alcoholic Core instead like, I dunno, 4 years ago?"
    ry "{color=#fff}And it kinda stuck..."
    mccut "{color=#fff}I didn't expect all this philosophy from you when we first met, but..."
    mccut "{color=#fff}I don't mind it."
    ry "{color=#fff}I'm glad."
    ry "{color=#fff}You're really somethin' special."
    ry "{color=#fff}I knew that when we first met, y'know?"
    ry "{color=#fff}Something about you..."
    # mc "Hmm. Maybe it's because I'm the main character?"
    mccut "{color=#fff}You're pretty special yourself, Ryland."
    ry "{color=#fff}I love it when you say my name like that."
    ry "{color=#fff}I-I love you."
    menu:
        extend ""
        "I love you too.":
            ry "{color=#fff}Finally said it, huh?"
            ry "{color=#fff}Took ya long enough!"
            mccut "{color=#fff}Haha, yeah, yeah."
        "I'll have to say your name more.":
            ry "{color=#fff}I don't think I'd mind that at all."
    n "{color=#fff}The two of you watch as the sun sets in the distance."
    n "{color=#fff}Ryland still has a long way to go, but..."
    n "{color=#fff}Progress is progress, regardless."
    n "{color=#fff}And he seems a lot happier."
    n "{color=#fff}And you're a lot happier, too."
    stop music fadeout 2.0
    window hide
    $ cutscenechoice = False
    show screen creditsfadeout with fade
    $ renpy.pause(2.0, hard=True)
    hide screen creditsfadeout
    python:
        persistent.endings_got["unknowntrue"] = True
        if sum(persistent.endings_got.values()) == ending_count:
            achievement.grant("ach_seenitall")
        if persistent.endings_got["kristrue"] and persistent.endings_got["heathtrue"] and persistent.endings_got["aspentrue"] and persistent.endings_got["cctrue"] and persistent.endings_got["robtrue"] and persistent.endings_got["gregtrue"] and persistent.endings_got["unknowntrue"]:
            achievement.grant("ach_ultrobo")
        achievement.grant("ach_unknowntrue")
        achievement.sync()
    $ renpy.movie_cutscene("ENDCREDIT_unknown.webm")
    $ MainMenu(confirm=False)()