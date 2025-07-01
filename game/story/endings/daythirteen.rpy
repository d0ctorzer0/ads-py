label day13:
    window hide
    scene black
    with fade
    $ daynum = "13"
    $ dayday = "Saturday"

    if renpy.is_skipping() == False:
        show screen daytransition
        play music "sfx/alarm.ogg"
        $ renpy.pause(2.0, hard=True)
    if renpy.is_skipping() == True:
        pass
        play music "sfx/alarm.ogg"

    scene mctemproom with fade
    show flash
    window auto

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
    window hide
    show flash
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
    window auto
    
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
    window auto
    $ emv_aspen = True
    scene bioroom with fade
    show flash
    n "You approach the door to the greenhouse."
    n "You peer into the window. It looks like it's flooding, and the sprinklers are on..."
    n "And Aspen is on the ground."

    mc "Aspen!"

    n "You force the door open."
    $ cutscenetextbox = True
    show screen cuttextbox
    scene aspen cutscene 4 with fade
    show flash
    python:
        if persistent.ac4 == False:
            persistent.cutscenes_seen += 1
            persistent.ac4 = True
        achievement.progress("ach_picture", persistent.cutscenes_seen)
        achievement.sync()
    n "{color=#fff}Instantly, you're soaked to the bone. Shaking off the cold, you look down to see Aspen off their management rail."

    a "{color=#fff}Doctor! Oh, I'm so happy to see you! The... the management rail got slippery, and I fell off, I..."
    a "{color=#fff}What's going on out there?"

    mccut "{color=#fff}I'm not really sure, but they're evacuating everyone."

    a "{color=#fff}Wh... why didn't my coworkers come back for me, then?"

    mccut "{color=#fff}I think... I think they're only evacuating human employees."

    a "{color=#fff}What?"

    mccut "{color=#fff}That's not important right now, though. This room is flooding and soon enough we won't be able to get this door open."

    a "{color=#fff}Y-You're right, Doctor. We should get out of here."

    hide screen cuttextbox
    window auto
    scene aspentemproom with fade
    show flash
    $ cutscenetextbox = False
    show a look offrail with easeinbottom

    n "You grab Aspen by the handles and lift them up to you. They're slippery."

    a "O-Oh, I didn't expect you to... haha... oh my."

    mc "Do you know a way out other than the surface elevators?"

    show a offrail

    a "There's a set of stairs right behind the greenhouse - it's how they bring in fresh samples."
    a "It's only used in rare cases though so it's not in the best condition, but..."

    mc "Doesn't matter. It's our only chance. Let's go."

    a "O-Okay. I trust you."

    show a look offrail
    a "My... my plants, they..."

    mc "I know."

    n "Struggling to keep a hold of Aspen, you push your way out of the greenhouse doors."

    jump escape_aspen

label noaspen:
    window auto
    $ emv_aspen = True
    scene bioroom with fade
    show flash
    n "You approach the door to the greenhouse."
    n "You can't get it open - it's jammed."
    n "You peer into the window. It looks like it's flooding, and the sprinklers are on..."
    n "But you don't see Aspen anywhere."

    mc "It seems someone from the greenhouse might've gotten them already..."

    jump emmap

# ###################################### GREGORY
# ######################################

label savegreg:
    
    if lock_gregory == False:
        jump nogreg
    else:
        pass
    show bioroom with fade
    show flash
    window auto
    n "You approach the door to the lounge to find a frightening sight."
    n "Gregory's caught on the door - it seems like it's jammed shut on his trench coat."

    mc "Gregory!"
    $ cutscenetextbox = True
    show screen cuttextbox
    scene greg cutscene 3 with fade
    show flash
    python:
        if persistent.gc3 == False:
            persistent.cutscenes_seen += 1
            persistent.gc3 = True
        achievement.progress("ach_picture", persistent.cutscenes_seen)
        achievement.sync()
    g "{color=#fff}O-Oh, Doctor! Can you - oh my god, can you help me?! Please!"

    mccut "{color=#fff}Where are you caught on?"

    g "{color=#fff}The... the door's jammed shut."
    g "{color=#fff}I was trying to get everyone else out first, but the servos failed while I was leaving..."
    g "{color=#fff}My coat is caught in the door."

    mccut "{color=#fff}We might have to take the coat off, then."

    g "{color=#fff}B-But - what if someone sees?! You're the only person I've ever told, I -"

    mccut "{color=#fff}Everyone else is gone. They're evacuating."

    g "{color=#fff}I..."

    mccut "{color=#fff}We don't have much time."

    g "{color=#fff}O-Okay. I trust you, Doctor."

    n "{color=#fff}You attempt to unbutton the trench coat to free them, but it's very tight."
    
    mccut "{color=#fff}I think the only way to free you is to rip this off."

    g "{color=#fff}My favorite coat..."

    n "{color=#fff}With all your strength, you grab the coat's fabric and rip it off them."
    n "{color=#fff}Gregory comes cascading down - and when they land..."

    hide screen cuttextbox
    window auto
    scene hall with fade
    show flash
    $ cutscenetextbox = False
    show g nocoat with easeinright
    g1 "W-What? What's... what's going on?"
    g2 "Who..."
    g3 "Where am I? Who are you?"

    mc "Oh my god. Gregory, are you okay?!"

    gall "Yeah, I'm fine."
    g2 "Wait a minute - are we... separated?!"
    g1 "Oh no. Oh no. This can't be happening."
    g3 "Great. This is just great."

    mc "I thought you... all... said you {i}couldn't{/i} be separated?"

    g2 "That's what I thought, but... I suppose I was wrong."
    g1 "{i}You{/i} thought? That was {i}my{/i} idea!"
    g3 "It was {i}our{/i} idea. We thought that together."

    mc "I - ugh. We don't have time for this, we need to get out of here."
    mc "Everyone else has left. The surface elevators are probably full of people, and I don't think they'd like it if you came with me."

    g1 "Probably not."
    g2 "Agreed."
    g3 "Stealing Aperture property."

    n "You take off your lab coat and scoop the three small cores into it."

    mc "Any of you have any ideas?"

    g2 "Hmm..."
    gall "The stairs!"
    g1 "They're stairs behind Kris' conference room."
    g2 "Sometimes our stockholders will come down that way, but rarely."
    g3 "It's our only choice."

    mc "Great idea, you three. Let's go."

    n "You hurriedly adjust your grip on your coat and run back up towards the conference rooms."

    jump escape_gregory

label nogreg:
    $ emv_greg = True
    scene bioroom with fade
    show flash
    window auto
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

    window hide
    jump emmap


# ###################################### ROB
# ######################################

label saverob:
    
    if lock_rob == False:
        jump norob
    else:
        pass
    n "You push the door open into the gym. There's a fire near one of the machines in the back."
    n "All the TVs are flashing a warning signal - except for one."

    mc "Oh my god - Rob!!"

    $ cutscenetextbox = True
    show screen cuttextbox
    scene rob cutscene 4 with fade
    show flash
    python:
        if persistent.rc4 == False:
            persistent.cutscenes_seen += 1
            persistent.rc4 = True
        achievement.progress("ach_picture", persistent.cutscenes_seen)
        achievement.sync()
    n "{color=#fff}Rob has fallen off his management rail, trapped under the TV that used to be hung up behind him."
    n "{color=#fff}One of his handles is broken off and his eye is twitching."

    mccut "{color=#fff}Oh my god. Rob, are you okay?!"

    r "{color=#fff}D-Doc? Oh, haha, it {i}is{/i} you..."
    r "{color=#fff}I'm not doing... great, no..."

    mccut "{color=#fff}Hold on. I'll get you out of there."

    n "{color=#fff}The fire behind him flares up threateningly."

    r "{color=#fff}Wait... it's dangerous. And this TV... i-it's heavy."

    mccut "{color=#fff}If you've taught me anything, I think I'll be able to lift it just fine."

    n "{color=#fff}You wrap your arms under the TV and push it up. Rob's right - it's incredibly heavy."
    n "{color=#fff}Somehow, though, you manage to get it up and push it off him."

    mccut "{color=#fff}Oh my god."

    hide screen cuttextbox
    scene cctemproom with fade
    show flash
    $ cutscenetextbox = False
    window auto
    show r offrail with easeinbottom
    r "Doc... you came for me. You didn't need to do that."

    mc "Of course I did."

    n "You pick his broken handle up off the floor."

    show r look offrail
    r "Eh... I don't need that, hah. I got you here. That's all I need."

    mc "No, right now you need to get out of here. But that's sweet of you."
    mc "We can't take the surface elevators - I'm almost positive they won't let you up with me."

    show r offrail
    r "I... I think I know a different way. Y'know where Heath's break room is, yeah?"
    r "There's a staircase behind it. I've gotten complaints from visitors that they can hear me yelling from over there..."
    r "It's not a very popular entrance. Maybe 'cuz of me, haha."
    r "But I know it leads to the surface."

    mc "Great idea, Rob. Let's get out of here."

    jump escape_rob

label norob:
    $ emv_rob = True
    scene robtemproom with fade
    show flash
    window auto
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
    scene bioroom with fade
    show flash
    window auto
    $ renpy.sound.play("sfx/fire.ogg", channel='fire', loop=True)
    n "You approach the door to CC's room. You hear fire from inside."

    mc "CC?! Are you in there?!"

    u "Doc?! Holy cow, is that you?"

    mc "What the -"

    u "There should be a spot to crawl into on the edge of the door - it's where I squeezed in."

    n "Sure enough, there's a core-sized indent in the door that looks just big enough to fit through."
    n "You take a quick breath, compose yourself, and climb through."

    $ cutscenetextbox = True
    show screen cuttextbox
    scene cc cutscene 4 with fade
    show flash
    python:
        if persistent.cc4 == False:
            persistent.cutscenes_seen += 1
            persistent.cc4 = True
        achievement.progress("ach_picture", persistent.cutscenes_seen)
        achievement.sync()
    c "{color=#fff}Doctor..."
    n "{color=#fff}As soon as you enter, you're met with a very peculiar sight."
    n "{color=#fff}Multiple walls are on fire and all of CC's monitoring systems are off."
    n "{color=#fff}In addition, what's-his-name is trying - desperately - to wrangle CC off his management rail and into..."

    if cctv == True:
        mccut "{color=#fff}Is that the CCTV? The one I took from your room?"
        
        u "{color=#fff}Uh - yeah. I broke into the office and stole it back from ya. Sorry, Doc."
        u "{color=#fff}Figured out after some snooping around that it used to be used for transporting CC around."

        c "{color=#fff}He's right. I-I had no idea it was with him this whole time, haha..."
    elif cctv == False:
        mccut "{color=#fff}What is that thing?"

        u "{color=#fff}It's the... uh, CCTV. Cancer Core Transportation Vehicle, or somethin' like that."
        u "{color=#fff}Used to be used for hauling CC around campus. Guess it got stuffed into my old closet a while back."

        c "{color=#fff}I'm glad it was left with you and not thrown in an incinerator..."
    
    mccut "{color=#fff}Here, let me help you."

    if lock_cc:
        c "{color=#fff}No, Doctor, wait. It's dangerous - the whole room is unstable."
        mccut "{color=#fff}Neither of you have hands. I'm your only hope."

        c "{color=#fff}I..."
        c "{color=#fff}Okay. I trust you. But please... be careful. I wouldn't want anything to happen to you."
    if lock_unknown:
        u "{color=#fff}You better not, Doc. It's dangerous. The whole place could come crashing down any minute."
        mccut "{color=#fff}Neither of you have hands. I'm your only hope."

        u "{color=#fff}But..."
        u "{color=#fff}Ugh. You're right, as usual. C'mere. But be careful - if ya got hurt, I wouldn't forgive myself."
    
    n "{color=#fff}You approach the two of them carefully."
    n "{color=#fff}With gentle manuvering, you successfully detach CC from both his tubes and his management rails."
    n "{color=#fff}Water leaks out of the tubes as you remove them from his systems."
    n "{color=#fff}He's heavy."
    n "{color=#fff}Thankfully though, you eventually get him down into the CCTV."

    if lock_cc:
        c "{color=#fff}You should handle me like that more often, haha..."
        n "{color=#fff}The other core looks at CC with a smirk."
    if lock_unknown:
        u "{color=#fff}Wish you were handlin' {i}me{/i} like that, haha..."
        n "{color=#fff}CC looks at him with a suspicious smile of sorts."
    
    n "{color=#fff}You plug the canister on the back into CC's ports and lock them in place."

    hide screen cuttextbox
    scene cctemproom with fade
    show flash
    $ cutscenetextbox = False
    window auto
    show u c with easeinright
    u "Okay, Doc. Is he in alright?"

    mc "I think so. No guarantees, but this is our only choice."

    hide u c with easeoutright

    show c offrail with easeinright
    c "I... I'll be okay, you two. We need to leave. This room isn't safe."

    mc "One second."
    hide c with easeoutright

    n "You move over to the door and try to pry it open."
    n "Thankfully, it gives way easily - seems it was just stuck from the outside."

    show u c with easeinright
    mc "I'm gonna need to get you off that management rail."

    u "You're right. I don't think Aperture cares too much about keepin' us alive anymore..."

    hide u c with easeoutright

    show c offrail with easeinright
    c "Did they ever?"
    hide c with easeoutright

    n "The core drops off his rail and into your arms."

    show u offrail with easeinbottom
    if lock_unknown:
        u "Well, Doc, this is certainly one way to get acquainted..."
    else:
        u "Good catch."

    mc "Anyone got any escape plans? The elevators are probably a no-go."
    u "It... won't be easy, with CC's chair and all, but... I do know one way."
    u "Behind the break room, there's a set of stairs... I see people come down that way sometimes, but not often."
    u "It's not a very well-known exit. Prolly our best bet."

    mc "Great idea. Let's go."
    hide u offrail with easeoutbottom

    n "Broken-down core in one hand and a wheelchair-bound one in the other, you rush hurriedly to the break room area."

    jump escape_ccunknown

label nocc:
    $ emv_cc = True
    scene bioroom with fade
    show flash
    window auto
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
    scene heathroom with fade
    show flash
    window auto
    n "You enter the break room."
    n "The stage is concave, and the curtains are on fire."
    n "Tables are flipped over and chairs are thrown across the floor."
    n "Heath is close to the stage, staring at the curtains."

    mc "Heath!"
    $ cutscenetextbox = True
    show screen cuttextbox
    scene heath cutscene 4 with fade
    show flash
    python:
        if persistent.hc4 == False:
            persistent.cutscenes_seen += 1
            persistent.hc4 = True
        achievement.progress("ach_picture", persistent.cutscenes_seen)
        achievement.sync()
    h "{color=#fff}Oh... Doctor..."
    h "{color=#fff}I-I... my magic supplies, my... livelihood, it's..."

    mccut "{color=#fff}Heath, are you okay?"

    h "{color=#fff}I'm fine physically, Doctor. I think. But I..."
    h "{color=#fff}Look at my emporium. It's..."
    h "{color=#fff}No amount of magic could fix something this devastating..."

    mccut "{color=#fff}Heath, I'm so sorry. I know this is really difficult."

    h "{color=#fff}Yeah..."

    mccut "{color=#fff}But you'll burn alive if we don't get you out of here."

    h "{color=#fff}Oh. Yes."

    mccut "{color=#fff}Here. Drop off your rail. I'll catch you."

    h "{color=#fff}But - I'm too warm for you to hold on to. You'll burn yourself."

    mccut "{color=#fff}I can't get you out of here otherwise."

    n "{color=#fff}You take your lab coat off your shoulders and hold it in front of you."

    mccut "{color=#fff}Here - the coat will protect me. Let's get you out of here."

    h "{color=#fff}Okay. I trust you."

    n "{color=#fff}Heath takes a deep breath..."
    n "{color=#fff}...and jumps off her rail, into your coat."
    hide screen cuttextbox
    scene heathroom with fade
    show flash
    $ cutscenetextbox = False
    show h look offrail with easeinbottom

    h "I'm sorry, Doctor, I'm... I don't know what to think."

    mc "You're plenty magic without your supplies, Heath."

    h "You certainly make me feel that way, regardless..."

    mc "Let's get out of here."
    mc "I'm not sure they'll let me out with you in the surface elevators..."
    mc "From what I've seen so far, I expect the exact opposite, in fact."

    show h offrail
    h "OH! Doctor! I have an idea!"
    h "The stairs! They're just behind Kris' conference rooms!"
    show h look offrail
    h "I sometimes hide behind the panels near it to surprise people, haha."
    h "They lead to the surface. And they aren't that well-known. It's perfect!"

    show h offrail

    mc "You're a genius, Heath. Guide me there."

    h "Aye aye, captain!"

    jump escape_heath

label noheath:
    $ emv_heath = True
    scene heathroom with fade
    show flash
    window auto
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
    window auto
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
    python:
        if persistent.kc4 == False:
            persistent.cutscenes_seen += 1
            persistent.kc4 = True
        achievement.progress("ach_picture", persistent.cutscenes_seen)
        achievement.sync()
    k "{color=#fff}Doctor! Thank god you're here, I..."
    k "{color=#fff}I don't know what's going on. I got to work, started doing my normal thing -"    
    k "{color=#fff}You know what?! I bet I was right! This is it! The \"Operation ACRI\" that's happening right now -"
    k "{color=#fff}That's how they're getting rid of us, Doctor! I was right! I told you, I..."

    mccut "{color=#fff}Kris, that isn't important right now."
    mccut "{color=#fff}We need to get you out of here."

    k "{color=#fff}Y-You're right, Doctor. I'm..."

    mccut "{color=#fff}I know you're scared. I'm right here."

    k "{color=#fff}I've never been off my management rail before. I'm terrified."

    mccut "{color=#fff}I've got you."

    n "{color=#fff}Kris takes a deep breath..."
    n "{color=#fff}...and drops off his rail."
    window auto
    hide screen cuttextbox
    scene kristemproom with fade
    show flash
    $ cutscenetextbox = False
    show k look offrail with easeinbottom
    n "You quickly catch him. He looks up at where he came from, worriedly."

    k "I don't... it feels so strange to be off it, but..."

    mc "We really don't have a choice."
    show k offrail
    mc "If you're right, and they're truly trying to get rid of you..."
    mc "...they won't let me out with you via the surface elevators."

    k "Wait - I know a different way to the surface."
    k "There's a back way. Stairs."

    mc "How do you know..."

    show k look offrail

    k "Gregory told me. They sometimes bring special guests in that way for conferences."
    k "Quick - I'll direct you."

    jump escape_kris

label nokris:
    $ emv_kris = True
    scene kristemproom with fade
    show flash
    window auto
    n "You push your way into Kris' conference room."
    n "It's a little difficult to get through the jammed door, but you make it in."
    n "Kris isn't here, though. The screen is turned off, too."
    n "The management rail is less dusty - seems it's been used recently."

    mc "That's good - he probably got out okay."

    jump emmap