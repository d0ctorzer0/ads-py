# GAME
label start:

    play music cma fadein 0.5 fadeout 0.5

    show screen daytransition
    $ renpy.pause(2.0, hard=True)

    scene office
    with fade

    n "You sigh. Another day, another dollar. But today's gonna be different."
    n "An issue in another department has forced you to take over another employee's position for a few days."

    begmc "What a downgrade... from manufacturing to maintenance..."

    n "As you carry your box to your new temporary desk, you check out your surroundings."
    n "It's a lot different from the development level. Less messy, for sure. There's no bits of machinery strewn about the floor, no blueprints and plans sprawled across the desks."
    n "It's a little unsettling."
    n "You reach your new \"headquarters.\" On the edge of the desk, there's a nametag."

    default name = "Polly"
    $ name = renpy.input("What does it read?", length=14)
    $ name = name.strip()
    n "The tag has \"[name]\" drawn on it in very hasty handwriting."
    
    mc "Well, at least they tried to be welcoming."

    n "Suddenly, you hear the unmistakable sound of a personality core on a management rail. You turn to your right to see a bright, pink-eyed core zooming toward you."

    show e
    with easeinright

    #voice "e/e01-001.ogg"
    e "Why, hello there. I'm Miss Esther. I'm assuming you're the temp replacement for our missing employee, correct?"

    menu:
        extend ""
        "Missing?":
            $ esther_affection += 1
            jump missing
        
        "Yes, that's me.":
        
            $ esther_affection -= 1
            jump introcont

label missing:

    #voice "e/e01-002.ogg"
    e "No, Miss Esther."

    mc "Oh no, I meant -"

    show e laugh
    #voice "e/e01-003.ogg"
    e "Oh! Yes, yes, my mistake. You were asking me what I meant by \"missing employee\"."

    show e
    #voice "e/e01-004.ogg"
    e "You must have not heard, then. The employee who held this position hasn't shown up for a week."

    mc "No, I didn't hear anything about that. They just told me they needed a position filled until they could find a replacement."

    show e laugh
    #voice "e/e01-005.ogg"
    e "Well it's of no real concern, darling. People disappear from here all the time, after all."

    show e
    #voice "e/e01-006.ogg"
    e "You're here now, so..."

    jump introcont

label introcont:

    #voice "e/e01-007.ogg"
    e "That's perfect. Go ahead and get your new desk set up while I go through our itinerary for today."

    n "You begin unloading your box. You leave a space on the corner for your most prized possession..."

    menu:
        extend ""

        "A potted plant you call \"Bertha\".":

            $ plant = True

            n "You set down Bertha and pat down her soil slightly. She somehow survives, even with the lack of real sunlight this far down."
        
        "A baseball signed by your favorite player.":

            $ ball = True

            n "You place the ball carefully on a round stand so that the autograph is facing toward you."
        
        "A picture of Multnomah Falls, Oregon.":

            $ picture = True

            n "You place the picture down gently and turn it slightly towards you."
    
    #voice "e/e01-008.ogg"
    e "Alright. Your job is simple. We will tour Section C8 of the facility - that's the section you're overseeing - and ensure that all Aperture Science Personality constructs are functioning properly."
    #voice "e/e01-009.ogg"
    e "\"Please ensure that the employee does not-\""

    show e shock
    #voice "e/e01-010.ogg"
    e "Oh, sorry! That's for my eyes only. Whoops, haha."

    show e
    #voice "e/e01-011.ogg"
    e "We have five stops for today. And for... everyday, actually. It's the same route almost every morning."

    mc "Great, routine."

    #voice "e/e01-012.ogg"
    e "Check-up number 1..."

    show e annoy
    #voice "e/e01-013.ogg"
    e "Ugh. It's Kris."

    mc "What's wrong with Kris?"

    #voice "e/e01-014.ogg"
    e "Nothing. He's just... you'll see. Come along."

    jump krisday1