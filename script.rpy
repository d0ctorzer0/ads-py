define cutscenetextbox = False

#SPECIAL DEFAULTS
default plant = False
default ball = False
default flowers = False
default spades = True
default emailfromrobday2 = False
default askforu = False
default askforg = False

#GOODBYES
default krisgoodbye = False
default heathgoodbye = False
default unknownhumor = False
default aspengoodbye = False
default haveaheart = False

#DAY 3 SETUPS
default goodday3 = False

#CUSTCENE T/F
default kc1 = False
default hc1 = False
default ac1 = False
default cc1 = False
default rc1 = False

#define shorter_easein = MoveTransition(0.3, enter=offscreenright, enter_time_warp=_warper.easein)
#define shorter_easeout = MoveTransition(0.3, exit=offscreenright, enter_time_warp=_warper.easein)

#ROMANCE SETUP
default romance_points = {
    "Kris" : 0 ,
    "Heath" : 0 ,
    "???" : 0 ,
    "Aspen" : 0 ,
    "CC" : 0 ,
    "Greg" : 0 ,
    "Rob" : 0 ,
}
default romance_minimum_for_good_ending = 10
default romance_minimum_for_perfect_ending = 15

#ESTHER EVIL SETUP
default esther_affection = 0
default esther_affection_minimum = 10

# GAME
label start:

    play music cma fadein 0.5 fadeout 0.5

    scene office
    with pixellate

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

    e "No, Miss Esther."

    mc "Oh no, I meant -"

    show e laugh
    e "Oh! Yes, yes, my mistake. You were asking me what I meant by \"missing employee\"."

    show e
    e "You must have not heard, then. The employee who held this position hasn't shown up for a week."

    mc "No, I didn't hear anything about that. They just told me they needed a position filled until they could find a replacement."

    show e laugh
    e "Well it's of no real concern, darling. People disappear from here all the time, after all."

    show e
    e "You're here now, so..."

    jump introcont

label introcont:

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
        
        "A vase full of fake lilies.":

            $ flowers = True

            n "You place the vase down gently and fluff up the plastic petals slightly."
    
    e "Alright. Your job is simple. We will tour Section C8 of the facility - that's the section you're overseeing - and check that all Aperture Science Personality constructs are functioning properly."
    e "\"Please ensure that the employee does not-\""

    show e shock
    e "Oh, sorry! That's for my eyes only. Whoops, haha."

    show e
    e "We have five stops for today. And for... everyday, actually. It's the same route every morning."

    mc "Great, routine."

    e "Check-up number 1..."

    show e annoy
    e "Ugh. It's Kris."

    mc "What's wrong with Kris?"

    e "Nothing. He's just... you'll see. Come along."

    jump krisday1