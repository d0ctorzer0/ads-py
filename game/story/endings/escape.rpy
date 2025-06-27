define blindplayer = Fade(0.1, 0.0, 0.5, color="#fff")

label escape_kris:
    scene stairs with fade
    show flash
    show k offrail with easeinbottom
    n "Overly-snobby core in hand, you approach the stairs to the surface."

    mc "That's a long way up..."

    k "I'm not too heavy for you, am I?"

    mc "Not at all. You're a lot lighter than I thought you'd be, actually."

    show k look offrail
    k "The doors are open at the top..."
    k "That must be sunlight, then."

    mc "Yeah. You've never seen the doors open before?"

    k "Never."
    k "I'm..."

    stop music fadeout 1.0
    stop music1 fadeout 1.0
    stop sound fadeout 3.0

    n "Kris looks away nervously."

    show k offrail
    k "Doctor, I'm not built for the surface. I'm not even sure what to expect."
    k "I have no idea what's up there."
    k "And I..."

    show k look offrail
    n "He sighs."

    k "...all the equipment and resources required to keep me running, it's all down here with Aperture."
    k "Even if we do escape... and make it out alive..."
    k "I'm not sure I'll be able to adapt."

    mc "Kris..."
    mc "We'll figure it out. Together."

    k "I..."
    show k offrail
    k "Y-You're right. We should... stop stalling now. It's a... a waste of resources."

    n "Clutching Kris tightly under your arm, you begin the ascent up the stairs."

    hide flash
    scene black with fade
    $ renpy.pause(2.0, hard=True)
    $ cutscenetextbox = True
    show screen cuttextbox
    $ renpy.music.play("music/outsidereveal.ogg")
    $ renpy.music.queue("music/outside.ogg", clear_queue=False)
    scene white with blindplayer

    k "{color=#fff}My optics - agh, they're..."
    k "{color=#fff}Oh my god..."

    scene kris cutscene 5 with dissolve
    $ persistent.kc5 = True
    n "{color=#fff}Your vision is blinded by the bright light of the outside world."
    n "{color=#fff}It's only been about two weeks since you were last outside, but..."

    k "{color=#fff}This... this is incredible."
    k "{color=#fff}I-I've been staring at a screen my whole life, when {i}this{/i} was right above me?"

    n "{color=#fff}...Kris has never seen the surface."

    k "{color=#fff}I can see why Aperture would choose to build their headquarters here. It's... it's..."
    k "{color=#fff}Beautiful. I..."
    n "{color=#fff}He turns to look at you."

    k "{color=#fff}The only thing more amazing than what's happening right now..."
    k "{color=#fff}Is that you're here, experiencing it with me."

    # mc has to stay normal here because the cutscene is quite bright, white text may not work,
    # do not edit for now and we'll come back to it later
    mc "{color=#fff}Kris, I..."

    k "{color=#fff}I-I think I love you."

    mc "{color=#fff}Wh-"

    k "{color=#fff}You've been so kind to me, despite my... attitude."
    k "{color=#fff}You risked your life, gave up your job, and possibly endangered your future..."
    k "{color=#fff}All for me."
    k "{color=#fff}I..."

    n "{color=#fff}He laughs softly."

    k "{color=#fff}I'm so selfish."
    k "{color=#fff}I hope you can learn to love me as well."

    mc "{color=#fff}Kris..."
    mc "{color=#fff}I think I've already started to."

    k "{color=#fff}Doctor, you..."
    k "{color=#fff}Oh, thank you. This is... just incredible."

    mc "{color=#fff}I'm glad, Kris."

    hide screen cuttextbox
    scene black with fade
    $ cutscenetextbox = False
    
    n "Without much choice, you run down the road leading away from the complex."
    n "No one notices you, thankfully."
    n "Your home city isn't far away from here, but it's by no means a short walk. Plus, you left your car in the parking garage..."

    mc "Damn it."

    n "Eventually, night comes, and you need to rest."
    n "You stop near a hidden clearing just a few miles away from the city limits."

    k "Doctor, are you okay?"

    mc "Yes, I'm fine. I just... I just need to sit down for a bit."
    mc "What about you? Systems still feeling alright? Everything functioning as it should?"

    k "Still doing your job, even off the clock? My, Doctor, be careful. You know, time is money."

    mc "Ha, ha."

    k "You should rest, Doctor. It's getting late."

    mc "Thank you, Kris."

    k "I'm a little terrified of the future..."
    k "You {i}did{/i} just steal \"Aperture property\", you know."

    mc "You're no one's property, Kris. Not anymore."

    k "Haha... I suppose so."
    k "With you by my side, I'm certain everything will work out just fine."

    mc "We'll make it work. It won't be easy, but..."
    mc "We'll make it work."

    if romance_points["Kris"] < 30:
        stop music fadeout 1.0
        window hide
        show screen creditsfadeout
        $ renpy.pause(2.0, hard=True)
        hide screen creditsfadeout
        $ renpy.movie_cutscene("ENDCREDIT_kris.webm")
        $ MainMenu(confirm=False)()
    if romance_points["Kris"] >= 30:
        jump END_kristrue

label escape_heath:
    jump endtest

label escape_ccunknown:
    jump endtest

label escape_rob:
    jump endtest

label escape_gregory:
    jump endtest

label escape_aspen:
    jump endtest