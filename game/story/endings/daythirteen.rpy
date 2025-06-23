label day13:
    scene black
    with fade
    $ daynum = "13"
    $ dayday = "Saturday"

    if renpy.is_skipping() == False:
        show screen daytransition
        $ renpy.sound.play("sfx/alarm.ogg", loop=True)
        $ renpy.pause(2.0, hard=True)
    if renpy.is_skipping() == True:
        pass
        $ renpy.sound.play("sfx/alarm.ogg", loop=True)

    scene mctemproom with fade
    show flash

    n "You wake with a start. Red lights fill your vision, and a grating alarm plays, almost as like it's inside your head."
    stc "Emergency detected. Automatic wake-up sequence initiated."
    stc "Please gather all vital equipment and proceed to the nearest surface elevator."
    stc "Surface elevator nearest SECTION 7, CHAMBER 14: [[ INFORMATION UNKNOWN ]"

    mc "Shit. Shit shit shit. Oh my god."

    n "You get up, quickly grab your essentials, and burst out of your room."

    scene hall with fade
    show flash

    mc "What the hell is happening?!"

    intc "Attention, all Aperture employees. Please do not panic."
    intc "Everything is under control."
    intc "Please turn in all contraband to your nearest Operation ACRI official."
    
    mc "Contraband? Operation ACRI? What -"

    mc "..."

    if lock_kris:
        mc "I need to get to Kris."
    elif lock_heath:
        mc "I need to find Heath."
    elif lock_aspen:
        mc "I need to get to Aspen."
    elif lock_cc:
        mc "I need to get CC out."
    elif lock_rob:
        mc "I need to get to Rob."
    elif lock_gregory:
        mc "I need to find Gregory."
    elif lock_unknown:
        mc "I need to find him."
    else:
        "ERROR CODE [[ 13LC ]\nThis is a bug. If you are seeing this text please report it."
    jump emmap

label emmap:
    show flash
    stop music
    stop music1
    scene black with dissolve
    $ renpy.pause(1.0, hard=True)
    scene emmapbg with dissolve
    call screen emergencymap with easeinbottom

# #######################################################
# #######################################################
# #######################################################
# #######################################################

label unknownmissing:
    $ emv_unknown = True
    scene bioroom with fade
    show flash
    n "You approach the room where what's-his-name usually is."
    n "The whole room is seemingly caved in."
    n "You dig under the rubble but see no core trapped underneath."

    mc "Seems he might've made it out..."
    mc "He might be somewhere else."

    n "You leave the destruction behind."

    jump emmap

# ###################################### ASPEN
# ######################################

label saveaspen:
    if lock_aspen == False:
        jump noaspen
    else:
        pass
    jump endtest

label noaspen:
    $ emv_aspen = True
    scene bioroom with fade
    show flash
    n "You approach the door to the greenhouse."
    n "You can't get it open - it's jammed."
    n "You peer into the window. It looks like it's flooding, and the sprinklers are on..."
    n "But you don't see Aspen anywhere."

    mc "It seems someone from the greenhouse might've gotten him already..."

    jump emmap

# ###################################### ASPEN
# ######################################

label savegreg:
    if lock_gregory == False:
        jump nogreg
    else:
        pass
    jump endtest

label nogreg:
    $ emv_greg = True
    scene bioroom with fade
    show flash
    n "You run up to the door leading to the lounge. One of your coworkers greets you."

    cw "What are you doing here?! There's no -"
    cw "You... you should be going. The nearest exit elevator is by the relaxation center."

    mc "What about the lounge?"

    cw "It - ugh, the roof caved in."

    mc "Is everyone okay?"

    cw "No clue. I'm pretty sure the evacuation was successful, but..."
    cw "It doesn't - it doesn't matter. You need to get out of here."

    mc "I'm just -"
    mc "Okay. Okay, thank you."

    n "You quickly leave the lounge behind."

    jump emmap


# ###################################### ROB
# ######################################

label saverob:
    if lock_rob == False:
        jump norob
    else:
        pass
    jump endtest

label norob:
    $ emv_rob = True
    scene robtemproom with fade
    show flash
    n "You push the door open into the gym. There's a fire near one of the machines in the back."
    n "All the TVs are flashing a warning signal."
    n "Rob is nowhere to be found."

    mc "Seems he got out alright..."

    jump emmap

# ###################################### CC / UNKNOWN
# ######################################

label saveccunknown:
    if lock_cc == False and lock_unknown == False:
        jump nocc
    else:
        pass
    jump endtest

label nocc:
    $ emv_cc = True
    scene bioroom with fade
    show flash
    $ renpy.sound.play("sfx/fire.ogg", channel='fire', loop=True)
    n "You approach the door to CC's room. You hear fire from inside."

    mc "CC?! Are you in there?!"

    n "There's no response."

    n "A large {sc}CRASH{/sc} resonates through the door."

    n "The ceiling above you starts to crack."
    n "You quickly run back and away from it before it caves in."
    stop fire fadeout 0.5

    jump emmap

# ###################################### HEATH
# ######################################

label saveheath:
    if lock_heath == False:
        jump noheath
    else:
        pass
    jump endtest

label noheath:
    $ emv_heath = True
    scene heathroom with fade
    show flash
    n "You enter the break room."
    n "The stage is concave, and the curtains are on fire."
    n "Tables are flipped over and chairs are thrown across the floor."
    n "Heath, however, is nowhere to be seen."

    mc "I hope she got out okay..."

    jump emmap

# ###################################### KRIS
# ######################################

label savekris:
    if lock_kris == False:
        jump nokris
    else:
        pass
    scene kristemproom with fade
    show flash
    n "You push your way into Kris' conference room."
    n "It's a little difficult to get through the jammed door, but you make it in."
    n "The stock market screen is on fire."
    n "Literally."

    mc "Kris!"
    $ cutscenetextbox = True
    show screen cuttextbox
    scene kris cutscene 4 with fade
    show flash
    $ persistent.kc4 = True
    k "{color=#fff}Doctor! Thank god you're here, I..."
    k "{color=#fff}I don't know what's going on. I got to work, started doing my normal thing -"    
    k "{color=#fff}You know what?! I bet I was right! This is it! The \"Operation ACRI\" that's happening right now -"
    k "{color=#fff}That's how they're getting rid of us, Doctor! I was right! I told you, I..."

    mc "{color=#fff}Kris, that isn't important right now."
    mc "{color=#fff}We need to get you out of here."

    k "{color=#fff}Y-You're right, Doctor. I'm..."

    mc "{color=#fff}I know you're scared. I'm right here."

    k "{color=#fff}I've never been off my management rail before. I'm terrified."

    mc "{color=#fff}I've got you."

    n "{color=#fff}Kris takes a deep breath..."
    n "{color=#fff}...and drops off his rail."
    hide screen cuttextbox
    scene kristemproom with fade
    show flash
    $ cutscenetextbox = False
    show k look with easeinright
    n "You quickly catch him. He looks up at where he came from, worriedly."

    k "I don't... it feels so strange to be off it, but..."

    mc "We really don't have a choice."
    mc "If you're right, and they're truly trying to get rid of you..."
    mc "...they won't let me out with you via the surface elevators."

    k "Wait - I know a different way to the surface."
    k "There's a back way. Stairs."

    mc "How do you know..."

    k "Gregory told me. They sometimes bring special guests in that way for conferences."
    k "Quick - I'll direct you."

    jump escape_kris

label nokris:
    $ emv_kris = True
    scene kristemproom with fade
    show flash
    n "You push your way into Kris' conference room."
    n "It's a little difficult to get through the jammed door, but you make it in."
    n "Kris isn't here, though. The screen is turned off, too."
    n "The management rail is less dusty - seems it's been used recently."

    mc "That's good - he probably got out okay."

    jump emmap