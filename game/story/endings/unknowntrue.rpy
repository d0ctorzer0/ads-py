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
    n "He tends to be quieter recently - lots of introspection to do."
    n "You put down your bag, take off your shoes, and round the corner."
    mc "Hey, Ryland."
    show ry happy with easeinbottom at bounce
    ry "Ah! Sorry, I, uh..."
    show ry look
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
    ry "I was a... a maintenance technician, funny 'nough."
    ry "Lower system stuff, though. Pipes and water systems..."
    ry "Makin' sure there wasn't any cracks, y'know?"
    mc "Sounds rough."
    ry "Y-Yeah, I think that mighta had somethin' to do with... how I got to... {i}that{/i} point."
    mc "Ryland, you don't have to talk about that if you -"
    show ry happy
    ry "Nah, nah. It's fine. It... helps. To talk about it."
    ry "Reminds me how far I've come."
    mc "That's good."
    n "You sit down next to him."
    n "Life's been slow since the two of you escaped Aperture."
    n "It was tough at first -"
    n "The lack of Aperture-brand lighter fluid made Ryland's recovery difficult."
    n "He'd only recently stopped having withdrawal symptoms."
    n "You look down at him."
    mc "How are you feeling? Anything internally?"
    show ry look
    ry "Mmm... not that I can tell. No new systems breaks, if that's what you're askin'."
    ry "Can't believe you still remember all that training..."
    mc "I {i}was{/i} in Manufacturing for, what, nine months?"
    mc "I built so many cores down there."
    mc "You're honestly surprised I know them inside and out?"
    show ry happy
    ry "Hah... guess not."
    ry "Still... it prolly ain't easy caring for me all the time."
    mc "It's worth it."
    mc "You've grown so much, Ryland."
    ry "And it's only been two months."
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
    ry "You... and me. Y'know. Human and robot."
    ry "Whaddaya tell people at work? \"My boyfriend\"?"
    mc "I just say my \"partner.\""
    ry "And what about when they ask what I look like?"
    mc "I tell them the truth."
    mc "Or... a version of it."
    mc "Is it really a lie to tell them you've got coffee-colored eyes and a few scars on your body?"
    ry "I mean... kinda. Optics and metal patch plates, but..."
    show ry happy
    ry "I guess it's kinda the same, huh?"
    mc "..."
    ry "..."
    mc "Do you want to go out to the balcony?"
    show ry look
    ry "Yeah. I think I'd like that."
    mc "Let me go grab a drink and we'll go out together."

    scene black with fade
    scene apt balcony with fade
    n "The sun is still nicely over the horizon -"
    n "- but not so far that it's too bright out."
    n "It's a perfect summer afternoon."
    show ry happy
    ry "Ain't it beautiful out here?"
    mc "It sure is."
    show ry look
    ry "..."
    mc "Do you wanna play our little game?"
    ry "Mmm... sure."
    mc "Alright."
    mc "What's your name?"
    ry "Ryland."
    mc "Activation year?"
    ry "Uhh..."
    ry "1973."
    mc "That's what you said last time, too. That's good."
    mc "Activation {i}month?"
    ry "Ugh, that's a tough one."
    ry "J... J something..."
    ry "January?"
    mc "Last time you said June."
    ry "Well, we've narrowed it down to a J month, at least."
    mc "Any progress is good."
    ry "You're a sweetheart, y'know?"
    ry "It's prolly tough. Taking care of me an' all."
    mc "You're right. It's not always the most... easy thing, but..."
    mc "It's worth it. For you."
    n "The two of you sit in silence for a bit, looking out over the balcony."
    n "Your apartment is located in a very nice part of Adrian."
    n "Summers thankfully don't get too hot in Michigan, which lets you enjoy the balcony more often."
    n "Much to Ryland's delight."
    n "Occasionally, he'll even ask you to leave him out there for a few hours..."
    n "...just to watch the sky."
    ry "Hey..."
    mc "What's up?"
    ry "This is gonna sound like it came from nowhere..."
    mc "You tend to come up with some pretty crazy things."
    mc "Whatever it is, I probably won't be surprised."
    ry "Hah... you really do know me pretty well, huh?"
    ry "..."
    ry "Do you think... there's a robot heaven?"
    mc "Dang. That really did come from nowhere."
    ry "I-I've just been thinkin' about the other robots back at Aperture..."
    ry "They definitely didn't all make it out from that, y'know."
    ry "I mean... CC's the prime example, but..."
    menu:
        extend ""
        "I think there's a robot heaven.":
            ry "That's... good."
            ry "I hope they're happy up there."
            mc "Me too."
        "I doubt something like that exists, though.":
            ry "Hah. You're prolly right."
            ry "Still... wonder what happens when our systems shut down..."
        "I'm not sure."
            ry "Me either."
    n "The two of you go quiet again."
    ry "I guess it doesn't really matter, huh?"
    mc "What do you mean?"
    ry "I mean. As long as I'm with you, I'd rather enjoy the time I have, y'know?"
    ry "Can't get to stressin' about all that."
    mc "I agree."
    ry "I-I remember - well, not many details 'bout it, but I remember - they told me about android hell."
    ry "Where ya go if you fail."
    ry "I thought I'd be sent there for sure eventually."
    mc "Why?"
    ry "Well, I... hah..."
    ry "I was breakin' into rooms, stealin' product from the company..."
    ry "I wasn't workin' at all. I mean..."
    mc "I can see why you might've thought that."
    ry "I think... no matter what happens when I shut down..."
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
        achievement.progress("ach_picture", persistent.cutscenes_seen)
        achievement.sync()
    ry "I just remembered something else."
    mc "What's that?"
    ry "My alias."
    ry "Y'know... how CC was Cancer Core, that Kris fellow was the Business Core..."
    mc "Really?"
    ry "Yeah. Hah. You're gonna laugh when you hear it."
    mc "Maybe, maybe not."
    ry "Philosophy Core."
    ry "That was my title."
    ry "At least, it was when I was first activated."
    mc "That makes a lot of things click."
    ry "They started callin' me the Alcoholic Core instead like, I dunno, 4 years ago?"
    ry "And it kinda stuck..."
    mc "I didn't expect all this from you when we first met, but..."
    mc "I don't mind it."
    ry "I'm glad."
    ry "You're really somethin' special."
    ry "I knew that when we first met, y'know?"
    ry "Something about you..."
    # mc "Hmm. Maybe it's because I'm the main character?"
    mc "You're pretty special yourself, Ryland."
    ry "I love it when you say my name like that."
    ry "I-I love you."
    menu:
        extend ""
        "I love you too.":
            ry "Finally said it, huh?"
            ry "Took ya long enough!"
            mc "Haha, yeah, yeah."
        "I'll have to say your name more, then.":
            ry "I don't think I'd mind that at all."
    n "The two of you watch as the sun sets in the distance."
    n "Ryland still has a long way to go, but..."
    n "Progress is progress, regardless."
    n "And he seems a lot happier."
    n "And you're a lot happier, too."
    stop music fadeout 2.0
    window hide
    $ cutscenechoice = False
    show screen creditsfadeout with fade
    $ renpy.pause(2.0, hard=True)
    hide screen creditsfadeout
    python:
        if persistent.endings_got["unknowntrue"] == False:
            persistent.endings_count += 1
            persistent.endings_got["unknowntrue"] = True
        achievement.progress("ach_seenitall", persistent.endings_count)
        achievement.sync()
        achievement.grant("ach_unknowntrue")
        achievement.sync()
    $ renpy.movie_cutscene("ENDCREDIT_ccunknown.webm")
    $ MainMenu(confirm=False)()