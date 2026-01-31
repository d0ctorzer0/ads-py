define blindplayer = Fade(0.1, 0.0, 0.5, color="#fff")

label escape_kris:
    scene stairs with fade
    if persistent.flash == True:
        show flash
    show k sus offrail with easeinbottom
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
    stop music fadeout 3.0

    n "Kris looks away nervously."

    show k sus offrail
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
    show k sus offrail
    k "Y-You're right. We should... stop stalling now. It's a... uh... a waste of resources."

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
    python:
        if persistent.kc5 == False:
            persistent.cutscenes_seen += 1
            persistent.kc5 = True
    if persistent.cutscenes_seen == cutscene_count and persistent.ach_picture == False:
        python:
            achievement.grant("ach_picture")
            achievement.sync()
            persistent.ach_picture = True
            ach_name = "picture"
        show screen ach_popup with easeinbottom
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

    if persistent.streammode == False:
        mc "Damn it."

    n "Eventually, night comes, and you need to rest."
    n "You stop near a hidden clearing just a few miles away from the city limits."

    k "Doctor, are you okay?"

    mc "Yes, I'm fine. I just... I just need to sit down for a bit."
    mc "What about you? Systems still feeling alright? Everything functioning as it should?"

    k "Still doing your job, even off the clock? My, Doctor, be careful. You know, time is money."

    mc "Ha, ha."

    k "You should rest. It's getting late."

    mc "Thank you, Kris."

    k "I'm a little terrified of the future..."
    k "You {i}did{/i} just steal \"Aperture property\", you know."

    mc "You're no one's property, Kris. Not anymore."

    k "Haha... I suppose so."
    k "With you by my side, I'm certain everything will work out just fine."

    mc "We'll make it work. It won't be easy, but..."
    mc "We'll make it work."

    stop music fadeout 1.0

    if romance_points["Kris"] < 29: #tested it myself - it's 29 not 30!
        window hide
        show screen creditsfadeout
        $ renpy.pause(2.0, hard=True)
        hide screen creditsfadeout
        python:
            persistent.endings_got["krisgood"] = True
            if sum(persistent.endings_got.values()) == ending_count:
                achievement.grant("ach_seenitall")
            achievement.grant("ach_krisgood")
            achievement.sync()
        $ renpy.movie_cutscene("ENDCREDIT_kris.webm")
        $ MainMenu(confirm=False)()
    if romance_points["Kris"] >= 29:
        python:
            persistent.endings_got["krisgood"] = True
            if sum(persistent.endings_got.values()) == ending_count:
                achievement.grant("ach_seenitall")
            achievement.grant("ach_krisgood")
            achievement.sync()
        jump END_kristrue

label escape_heath:
    scene stairs with fade
    if persistent.flash == True:
        show flash
    show h offrail with easeinbottom
    h "Aha! I knew it!"
    h "Told ya so, Doctor!"

    mc "You sure did, Heath. You sure this way up is safe?"

    h "Positive! But..."
    show h look offrail
    h "I've never seen the light up there so bright before..."

    mc "That's just sunlight, Heath."

    h "Like... the real stuff?"

    mc "Yeah. The real stuff."

    show h offrail
    h "Wow. I..."
    h "I can't lie, part of me is... definitely excited, haha, but I..."

    stop music fadeout 1.0
    stop music1 fadeout 1.0
    stop music fadeout 3.0
    show h look offrail
    h "My whole life is down here, Doctor."
    h "My magic emporium, my tricks, the parts of the break room I control to make confetti shoot out of the walls..."
    h "It's all down here. And it'll stay down here. And..."

    show h offrail
    h "Well, my overclocking? I-It's really only kept in check by my management rail, hah..."
    show h look offrail
    h "I'm not sure how well I'll do disconnected from it now."

    mc "Heath..."
    mc "I promise you, we'll figure it out."
    mc "And you won't have to go through it alone. I'll be here for you."

    show h offrail
    h "That... makes me feel a little better."

    mc "Plus, you've done plenty of tricks that don't require being connected to the system."

    h "That I have! Haha, you've got me there, Doc."
    show h look offrail
    h "Phew. Alright."
    h "It's not like we got much of a choice, huh?"

    mc "Yeah."

    n "She sighs hesitantly."
    h "Let's go."

    hide flash
    scene black with fade
    $ renpy.pause(2.0, hard=True)
    $ cutscenetextbox = True
    show screen cuttextbox
    $ renpy.music.play("music/outsidereveal.ogg")
    $ renpy.music.queue("music/outside.ogg", clear_queue=False)
    scene white with blindplayer

    h "{color=#fff}It's so bright out here..."
    h "{color=#fff}Oh... {i}wow.{/i}"

    scene heath cutscene 5 with dissolve
    python:
        if persistent.hc5 == False:
            persistent.cutscenes_seen += 1
            persistent.hc5 = True
    if persistent.cutscenes_seen == cutscene_count and persistent.ach_picture == False:
        python:
            achievement.grant("ach_picture")
            achievement.sync()
            persistent.ach_picture = True
            ach_name = "picture"
        show screen ach_popup with easeinbottom
    n "{color=#fff}Your vision is blinded by the bright light of the outside world."
    n "{color=#fff}It's only been about two weeks since you were last outside, but..."

    h "{color=#fff}This... this is better than the brightest spotlight!"
    h "{color=#fff}Hahaha... I've never seen anything so... so..."
    h "{color=#fff}Magical!"
    h "{color=#fff}Wow..."

    n "{color=#fff}...Heath has never seen the surface."

    h "{color=#fff}I-I can't get over this - the trees, it's like they make their own confetti, and..."
    h "{color=#fff}Everything's glowing!"
    h "{color=#fff}Oh, and Doctor! Listen to that music! {i}Real animals!{/i}"

    mc "{color=#fff}Haha, yeah."

    n "{color=#fff}She turns to you with the most joyous look you've ever seen from her."

    h "{color=#fff}And... your face! It's..."
    h "{color=#fff}Oh, it's so much easier to see in the sunlight, Doctor."
    h "{color=#fff}You're beautiful, you're..."
    h "{color=#fff}Oh..."

    n "{color=#fff}She pauses."

    h "{color=#fff}I'm pretty sure I'm in love with you."
    h "{color=#fff}You're just so... wow."
    h "{color=#fff}You went out of your way to save me instead of just saving yourself..."
    h "{color=#fff}Honestly, you say I put myself in danger, but you're one to talk!"
    h "{color=#fff}I-I know it's quite early, and we still have to get to know each other, Doctor..."
    h "{color=#fff}But I... I want you to love me too, one day."

    mc "{color=#fff}I think... I think I will, Heath."

    hide screen cuttextbox
    scene black with fade
    $ cutscenetextbox = False

    n "Without much choice on where to go, you quickly wrap Heath up and rush down the road leading away from Aperture."
    n "You don't dare look back."
    n "Heath is heavy, and you're exhausted from the adrenaline rush..."
    n "And, stupidly, you'd left your car at the complex."

    if persistent.streammode == False:
        mc "Damn it."

    n "Eventually, you reach a clearing just outside the city limits, and decide to rest for a bit."
    
    h "Doctor... you should really sit down, you know."
    h "Not everyone has as much energy as I do! Haha."
    
    mc "Heath, you're... you're smoking."

    h "Oh! Well, I knew I was {i}hot{/i}, but..."

    mc "N-No. Literally."

    h "Oh. Haha, that just happens sometimes."
    h "Nothing to be concerned about. We'll find some water and dunk me in there. That'll probably help cool me off."

    mc "You promise you're going to be alright?"

    h "Yeah. Trust me, Doc, the, uh..."
    h "\"GREAT AND AMAZING HEATH!\" knows her limits!"

    mc "Haha. You're funny."

    h "I know."
    h "..."
    h "...I'm worried, Doctor. Aperture's not going to come looking for me, are they?"

    mc "Doubtful. I don't think they really care what happens to you guys now..."
    mc "But even if they did, I'd be here to protect you."
    mc "I won't let anything happen to you, Heath."

    h "Well then. I hope you're ready for a lot more tricks from yours truly!"

    mc "Oh, don't worry. I know what I got myself into."

    stop music fadeout 1.0

    if romance_points["Heath"] < 29:
        window hide
        show screen creditsfadeout
        $ renpy.pause(2.0, hard=True)
        hide screen creditsfadeout
        python:
            persistent.endings_got["heathgood"] = True
            if sum(persistent.endings_got.values()) == ending_count:
                achievement.grant("ach_seenitall")
            achievement.grant("ach_heathgood")
            achievement.sync()
        $ renpy.movie_cutscene("ENDCREDIT_heath.webm")
        $ MainMenu(confirm=False)()
    if romance_points["Heath"] >= 29:
        python:
            persistent.endings_got["heathgood"] = True
            if sum(persistent.endings_got.values()) == ending_count:
                achievement.grant("ach_seenitall")
            achievement.grant("ach_heathgood")
            achievement.sync()
        jump END_heathtrue

label escape_aspen:
    scene stairs with fade
    if persistent.flash == True:
        show flash
    show a offrail with easeinbottom
    a "Here it is."
    a "I'm not sure we're supposed to use these -"
    a "Actually, we're probably definitely not supposed to use these, haha."
    a "But I don't think we have any other choice, so..."

    mc "No. We really don't."

    a "Doctor - wait. Wait wait."

    mc "What's up?"

    stop music1 fadeout 1.0
    stop music fadeout 3.0
    show a look offrail
    a "I... I don't know what to expect up there."
    a "And I'm terrified."
    a "Hah... I mean... other than when I was activated, this is my first time outside the greenhouse..."
    a "Let alone somewhere even farther than that."
    a "I have no... I have no frame of reference, I have no experience..."
    a "What am I supposed to do?"

    show a offrail
    mc "You {i}do{/i} have a frame of reference, Aspen."
    mc "Plants are your specialty."
    mc "And if I know anything about the surface, there's a hell of a lot of them up there."

    a "I... I suppose you're right, Doctor."

    mc "And I'm going to be here for you the entire time."
    mc "I promise I won't leave your side."

    a "O-Okay. I..."
    show a look offrail
    a "I think I'm ready, then."
    show a offrail
    a "I can't wait to see what real grass looks like."

    n "Steeling yourself, you hold tighter onto Aspen and begin the ascent."

    hide flash
    scene black with fade
    $ renpy.pause(2.0, hard=True)
    $ cutscenetextbox = True
    show screen cuttextbox
    $ renpy.music.play("music/outsidereveal.ogg")
    $ renpy.music.queue("music/outside.ogg", clear_queue=False)
    scene white with blindplayer

    a "{color=#fff}Agh, it's just like when the greenhouse lights turn on..."
    a "{color=#fff}I... oh my god!"

    scene aspen cutscene 5 with dissolve
    python:
        if persistent.ac5 == False:
            persistent.cutscenes_seen += 1
            persistent.ac5 = True
    if persistent.cutscenes_seen == cutscene_count and persistent.ach_picture == False:
        python:
            achievement.grant("ach_picture")
            achievement.sync()
            persistent.ach_picture = True
            ach_name = "picture"
        show screen ach_popup with easeinbottom
    n "{color=#fff}Your vision is blinded by the bright light of the outside world."
    n "{color=#fff}It's only been about two weeks since you were last outside, but..."

    acg "{color=#fff}The sky! The grass! The... oh, {i}Pinus strobus...{/i}"
    acg "{color=#fff}It's all so bright... and so green... and so beautiful!"

    n "{color=#fff}...Aspen has never seen the surface."

    acg "{color=#fff}Wow, this is incredible! I can't..."
    acg "{color=#fff}Doctor, can you set me down in the grass?"

    n "{color=#fff}You lay Aspen down in front of you. They look up and around themselves in wonder."

    acg "{color=#fff}These - these are {i}Taraxacum officinale{/i}, aren't they? Dandelions!"
    acg "{color=#fff}They're so plentiful. And so yellow, and..."
    acg "{color=#fff}Oh, it's all so wonderful. I..."

    n "{color=#fff}Aspen turns to look up at you."

    acg "{color=#fff}You gave me this opportunity, Doctor."
    acg "{color=#fff}You almost got yourself... killed... all for me. You..."
    acg "{color=#fff}You even came to save... me. Even though it was flooding."
    acg "{color=#fff}You rushed through fires and... all because of that, I get to see this."
    acg "{color=#fff}You..."
    acg "{color=#fff}I think I... I think I love you, Doctor."
    acg "{color=#fff}And... I know that's a little strange to hear from a core like me, so I understand if you..."
    
    n "{color=#fff}They sigh."

    acg "{color=#fff}I hope you'll feel the same. One day."

    mccut "{color=#fff}I think I've already started to, Aspen."

    hide screen cuttextbox
    scene black with fade
    $ cutscenetextbox = False

    n "Without much choice, you pick Aspen up and begin running."
    n "The trek from the facility to the neighboring city is a long one."
    n "You regret that you left your car behind."

    if persistent.streammode == False:
        mc "Damn it."

    n "As you're pushing through the forest alongside the road, Aspen points out specimens they recognize."

    a "{i}Cephalanthus occidentalis!{/i} Buttonbush! They said it'd be too expensive to care for down in the greenhouse..."
    a "And {i}Osmundastrum{/i} - cinnamon ferns. Oh, wow. There's so many different species out here."

    n "You chuckle to yourself as they talk. Though you're exhausted, Aspen's excited rambling gives you a little energy."
    n "Eventually, you reach a clearing just on the outskirts of the city."

    mc "Phew... let's rest here for a bit."

    a "Y-Yeah. You look so tired, Doctor."

    mc "Hah. I am."

    a "Then let's rest for a bit."

    n "You close your eyes and place Aspen next to you."

    a "..."
    a "Doctor... I'm still so scared."
    a "This is wonderful... being here with you, and seeing all this natural beauty, and being out of that cramped little room..."
    a "But... Aperture's going to come looking for us, aren't they?"

    mc "I don't think they will. It's not in their interest anymore."
    mc "From what I picked up, that whole emergency - Operation \"ACRI\" - was them trying to get {i}rid{/i} of you."
    mc "Frankly, I don't think they care what happens."

    a "That... makes me feel a little better, I suppose."
    a "What are we supposed to do... now, though?"
    a "Both of us are out of a job..."

    mc "I'll find another one."
    mc "We'll just have to... figure it out, I guess."

    a "Okay."
    a "I think I can handle that."
    a "As long as you're here with me."

    mc "Don't worry, Aspen. I'm not going anywhere."

    stop music fadeout 2.0
    window hide
    scene black with fade

    if persistent.ach_aspengood == False:
        python:
            persistent.endings_got["aspengood"] = True
            ach_name = "aspengood"
            showpopup = True
            achievement.grant("ach_aspengood")
            persistent.ach_aspengood = True
        show screen ach_popup with easeinbottom
        $ renpy.pause(4.0, hard=True)

    if romance_points["Aspen"] < 28:
        $ renpy.movie_cutscene("ENDCREDIT_aspen.webm")
        $ MainMenu(confirm=False)()
    if romance_points["Aspen"] >= 28:
        jump END_aspentrue


label escape_ccunknown:
    scene hall hell with fade
    if persistent.flash == True:
        show flash
    stop fire
    n "They're heavy. Heavier than you thought they would be."
    if lock_cc == True:
        jump leave_unknown
    if lock_unknown == True:
        jump leave_cc

label leave_unknown:
    show c offrail with easeinright
    c "Doctor, are you alright?"

    mc "Y-Yes, I'm just... I'm just exhausted."

    hide c with easeoutright
    show u offrail with easeinbottom
    u "We're almost outta here. The stairs are just around the corner."

    n "You push forward slowly. Eventually, you finally reach the stairs."
    scene stairs with fade
    if persistent.flash == True:
        show flash
    mc "Alright. We're... we're here."
    mc "Okay. How are we gonna get you up, CC?"

    show c annoy offrail with easeinright
    c "My chair has wheels that {i}should{/i} be able to go up stairs..."
    c "But I'm not sure you'll be able to take us both at the same time."

    hide c with easeoutright
    show u offrail with easeinbottom
    u "Take him first, Doc. He's heavier - it'll be easier to carry me up after."
    u "Don't worry. I'll be fine."

    hide u with easeoutbottom
    show c close offrail with easeinright
    c "No - what if they find you? What if they..."
    show c annoy offrail
    c "It's not safe. You should go up first."
    hide c with easeoutright
    show u offrail with easeinbottom
    u "Don't listen to him, Doc. Please - take him first."

    mc "CC - he's right. It'll be easier to come back for him than for you..."
    mc "I'm already... quite exhausted."

    hide u with easeoutbottom
    show c close offrail with easeinright
    n "CC sighs."

    show c offrail
    c "Okay. I trust you, uh..."

    hide c with easeoutright
    show u offrail with easeinbottom
    u "Ryland."

    mc "What?"

    ry "My name. I... I remembered. Yesterday."
    ry "I've just been... scared to tell anyone. 'Case I forget again."

    hide u with easeoutbottom
    show c happy offrail with easeinright
    c "Ryland."
    c "That's an excellent name."
    show c close offrail
    c "I trust you."
    c "I'll see you at the surface."

    hide c with easeoutright
    n "You begin the ascent, slowly pushing CC's chair up, step by step."
    n "It's not easy, and your arms nearly give in with every other push, but eventually, you're already halfway up."
    n "Suddenly, you hear Ryland call out from behind you -"

    ry "Doc! Hurry! They're -"

    vc "HEY! There's still one over here - what do you want me to do with it?"
    vc2 "Orders are to just throw them in the incinerator now. Boss says it's not worth the hassle."
    vc "Roger that."
    
    ry "CC, I -"
    ry "You guys need to get goin'."

    c "RYLAND!"

    ry "I'll be fine."

    n "Grimacing, you push CC up as quickly as you can, trying your best to ignore the scene behind you."

    show c offrail with easeinright
    c "Doctor, do you think -"

    mc "I don't know, CC. I don't... I don't know."
    mc "But we have to keep going. If they discover I have you, they'll do the same thing to you."

    show c annoy offrail
    c "You're... you're right. I..."

    mc "I'm sorry, CC. I know how much you cared about him."

    show c close offrail
    c "Y-Yeah. I guess... hah. I guess that's Aperture for you."

    stop music fadeout 2.0
    n "Before you know it, you've crested the \"horizon\"."

    hide flash
    scene black with fade
    $ renpy.pause(2.0, hard=True)
    $ cutscenetextbox = True
    show screen cuttextbox
    $ renpy.music.play("music/outsidereveal.ogg")
    $ renpy.music.queue("music/outside.ogg", clear_queue=False)
    scene white with blindplayer

    c "{color=#fff}I-It's like the window outside my room..."
    c "{color=#fff}Except..."

    scene cc cutscene 5 with dissolve
    python:
        if persistent.cc5 == False:
            persistent.cutscenes_seen += 1
            persistent.cc5 = True
    if persistent.cutscenes_seen == cutscene_count and persistent.ach_picture == False:
        python:
            achievement.grant("ach_picture")
            achievement.sync()
            persistent.ach_picture = True
            ach_name = "picture"
        show screen ach_popup with easeinbottom
    n "{color=#fff}Your vision is blinded by the bright light of the outside world."
    n "{color=#fff}It's only been about two weeks since you were last outside, but..."
    c "{color=#fff}This is... incredible. Everything's so vibrant and bright and..."
    c "{color=#fff}The air is so... clear."

    n "{color=#fff}...CC's never seen the surface."

    c "{color=#fff}All the poetry I've read, and none of it ever described the surface accurately."
    c "{color=#fff}It's... entirely different in person."
    c "{color=#fff}It's beautiful. It's..."

    n "{color=#fff}He turns to look at you."

    c "{color=#fff}You... you came for me. To show me this."
    c "{color=#fff}You tried your best to save not only me, but my friend, and..."
    c "{color=#fff}You sacrificed your job to do that. For me. So I could see this."
    c "{color=#fff}But..."
    c "{color=#fff}As long as I can see you, I think I'll be okay."
    c "{color=#fff}I think I'm in love with you, Doctor."
    c "{color=#fff}And I know that's a little weird to hear from... a core such as myself. A robot. But..."
    c "{color=#fff}I don't expect reciprocation. Deep down, I guess a part of me hopes..."
    c "{color=#fff}...you'll feel the same way one day."

    mccut "{color=#fff}I think I might, CC."

    hide screen cuttextbox
    scene black with fade
    $ cutscenetextbox = False

    n "Before the people that took Ryland away can get curious, you quickly push CC's chair down and across the field, into the thick of the forest ahead."
    n "He's heavy. The chair weighs almost half as much as you do, and pushing it for even just half an hour is incredibly taxing."
    n "The rough terrain probably doesn't help."
    n "You regret that you hadn't thought to get your car out of the complex."

    if persistent.streammode == False:
        mc "Damn it..."

    n "Eventually, you reach a peaceful clearing just on the outskirts of the big city."
    n "Out of breath, you lay down in the grass."

    mc "Let's... let's rest here, for a bit."

    n "No response."

    mc "CC?"

    c "I'm... I'm here, Doctor, I'm..."
    c "Sorry. I'm just exhausted. And... in awe, still."
    c "And... processing what we just went through. Who I just lost."
    c "Forgive me."

    mc "Don't apologize. It's a lot to take in at once."

    c "Yes. Yes it is."
    c "I'm so happy you're here, Doctor. I just wish..."

    mc "Yeah. Ryland."
    mc "I'm sorry I couldn't save him, I -"

    c "It's not your fault. Please don't blame yourself."
    c "He... he told me he was finally happy, yesterday."
    c "Said it was partially thanks to me. I..."

    mc "This must be hard for you."

    c "It is. And I'm a little scared how I'm going to... well, you understand."
    c "Without Aperture's resources, I'm not sure how much longer I'll have."

    mc "I'll do anything to help you, CC."
    mc "You'll be okay."

    c "Thank you, Doctor. I..."
    c "I'm so lucky."

    if romance_points["CC"] < 30:
        stop music fadeout 1.0
        window hide
        show screen creditsfadeout
        $ renpy.pause(2.0, hard=True)
        hide screen creditsfadeout
        python:
            persistent.endings_got["ccgood"] = True
            if sum(persistent.endings_got.values()) == ending_count:
                achievement.grant("ach_seenitall")
            achievement.grant("ach_ccgood")
            achievement.sync()
        $ renpy.movie_cutscene("ENDCREDIT_cc.webm")
        $ MainMenu(confirm=False)()
    if romance_points["CC"] >= 30:
        python:
            persistent.endings_got["ccgood"] = True
            if sum(persistent.endings_got.values()) == ending_count:
                achievement.grant("ach_seenitall")
            achievement.grant("ach_ccgood")
            achievement.sync()
        jump END_cctrue

label leave_cc:
    show u offrail with easeinright
    u "Hey Doc, you doing good?"

    mc "Y-Yes, I'm just... I'm just exhausted."

    u "We're almost outta here. The stairs are just around the corner."

    n "You push forward slowly. Eventually, you finally reach the stairs."
    scene stairs with fade
    if persistent.flash == True:
        show flash
    mc "Alright. We're... we're here."
    mc "Okay. How are we gonna get you two up?"

    show c annoy offrail with easeinright
    c "My chair has wheels that {i}should{/i} be able to go up stairs..."
    c "But I'm not sure you'll be able to take us both at the same time."

    hide c with easeoutright
    show u offrail with easeinbottom
    u "Take him first, Doc. He's heavier - it'll be easier to carry me up after."
    u "Don't worry. I'll be fine."

    hide u with easeoutbottom
    show c annoy offrail with easeinright
    c "No - what if they find you? What if they..."
    show c offrail
    c "It's not safe. You should go up first."
    c "Plus, you're lighter - the doctor will waste less energy by taking you first."
    hide c with easeoutright
    show u offrail with easeinbottom
    u "Don't listen to him, Doc. Please - take him first."

    mc "No, CC's right. I can carry you up quicker and come back down for CC."
    mc "I'm already... quite exhausted. It'll be better to save my energy for the harder climb."

    n "He sighs."

    u "Okay. I trust you two."
    hide u with easeoutbottom
    show c offrail with easeinright
    c "Thank you, uh..."

    hide c with easeoutright
    show u offrail with easeinbottom
    u "Ryland."

    mc "What?"

    ry "My name. I... I remembered. Yesterday."
    ry "I've just been... scared to tell anyone. 'Case I forget again."

    hide u with easeoutbottom
    show c happy offrail with easeinright
    c "Ryland."
    c "That's an excellent name."
    c "I'll see you on the surface, alright?"
    c "Just don't spoil it for me."

    hide c with easeoutright
    n "You begin the ascent, quickly carrying Ryland up step by step."
    n "It's not easy, and the stairs seem to go on forever... but eventually, you're already halfway up."
    n "Suddenly, you hear voices call out from behind you -"

    vc "HEY! There's still one over here - what do you want me to do with it?"
    vc2 "Orders are to just throw them in the incinerator now. Boss says it's not worth the hassle."
    vc "Roger that."
    
    c "Ryland, I -"
    c "You guys should hurry."

    ry "CC!"

    n "Grimacing, you carry Ryland up as quickly as you can, trying your best to ignore the scene behind you."

    show u offrail with easeinbottom
    ry "Doctor, do you think -"

    mc "I don't know, Ryland. I don't... I don't know."
    mc "But we have to keep going. If they discover I have you, they'll do the same thing to you."

    ry "You're... you're right."

    mc "I'm sorry. I know how much he cared about you, though."

    ry "I don't think he would've wanted it any other way."

    stop music fadeout 2.0
    n "Before you know it, you've crested the \"horizon\"."

    hide flash
    scene black with fade
    $ renpy.pause(2.0, hard=True)
    $ cutscenetextbox = True
    show screen cuttextbox
    $ renpy.music.play("music/outsidereveal.ogg")
    $ renpy.music.queue("music/outside.ogg", clear_queue=False)
    scene white with blindplayer

    ry "{color=#fff}It's so bright out here..."
    ry "{color=#fff}I can barely see a- oh my..."

    scene unknown cutscene 4 with dissolve
    python:
        if persistent.uc4 == False:
            persistent.cutscenes_seen += 1
            persistent.uc4 = True
    if persistent.cutscenes_seen == cutscene_count and persistent.ach_picture == False:
        python:
            achievement.grant("ach_picture")
            achievement.sync()
            persistent.ach_picture = True
            ach_name = "picture"
        show screen ach_popup with easeinbottom
    n "{color=#fff}Your vision is blinded by the bright light of the outside world."
    n "{color=#fff}It's only been about two weeks since you were last outside, but..."
    ry "{color=#fff}What the..."
    ry "{color=#fff}This is insane. I've been hiding away in a closet my whole life?!"
    ry "{color=#fff}This was above me? All this time?!"
    ry "{color=#fff}Haha! Wow!"

    n "{color=#fff}...for all he knows, Ryland has never seen the surface."

    ry "{color=#fff}This fresh air through my circuits, it's like... better than any drink I've had."
    ry "{color=#fff}If only... CC could've seen this."
    ry "{color=#fff}But..."

    n "{color=#fff}He turns to face you."

    ry "{color=#fff}I'm glad you're here."
    ry "{color=#fff}You... hah, Doc, you risked your life for us both."
    ry "{color=#fff}Not just for me, but CC, too."
    ry "{color=#fff}And I... can't thank you enough."
    ry "{color=#fff}You're really somethin' else."
    ry "{color=#fff}And I might love that."
    ry "{color=#fff}I know I ain't been the best to you. I know I've been a flirt, and I've been annoying..."
    ry "{color=#fff}But I hope you'll love me back. One day. If I try hard enough."

    mccut "{color=#fff}I think... it'll take time, Ryland. But I might."

    hide screen cuttextbox
    scene black with fade
    $ cutscenetextbox = False

    n "Steeling yourself for the future, you run away from the complex with Ryland before you can be followed."
    n "You don't dare look back."
    n "Pushing through the brush and the trees, you slowly make your way towards the city."
    n "It's exhausting."
    n "Eventually, you reach a quiet clearing just on the outskirts."

    ry "Wait, Doc. Let's stop here for a bit."
    ry "You look beat."

    mc "Hah. You know what I could really use right now?"

    ry "A drink?"

    mc "Hell yeah."

    ry "Honestly, me too. I may be tryna quit, but sometimes I wish I wasn't."

    mc "I don't think I ever told you how much that means to me."
    mc "That you would try to... get yourself clean for me."

    ry "Well. Like I said, not {i}all{/i} for you, but..."
    ry "You were the... uh, \"catalyst\", I think the word is?"

    mc "Hahaha. Yeah."

    ry "What... what are we gonna do now?"
    ry "I mean. I wasn't doin' much down in Aperture, anyway."

    mc "Now we..."
    mc "Now we {fast}make our own path."

    ry "Think they're gonna come looking for us?"

    mc "No. I don't think they care, frankly."
    mc "I left all my keys and stuff down in the office, so it's not like I have stuff to return..."

    ry "Other than me, 'course."

    mc "I don't plan to return you."

    ry "Good. I like it out here."
    ry "With you."

    if romance_points["???"] < 15:
        stop music fadeout 1.0
        window hide
        show screen creditsfadeout
        $ renpy.pause(2.0, hard=True)
        hide screen creditsfadeout
        python:
            persistent.endings_got["unknowngood"] = True
            if sum(persistent.endings_got.values()) == ending_count:
                achievement.grant("ach_seenitall")
            achievement.grant("ach_unknowngood")
            achievement.sync()
        $ renpy.movie_cutscene("ENDCREDIT_unknown.webm")
        $ MainMenu(confirm=False)()
    if romance_points["???"] >= 15:
        python:
            persistent.endings_got["unknowngood"] = True
            if sum(persistent.endings_got.values()) == ending_count:
                achievement.grant("ach_seenitall")
            achievement.grant("ach_unknowngood")
            achievement.sync()
        jump END_unknowntrue    

label escape_rob:
    scene stairs with fade
    if persistent.flash == True:
        show flash
    show r offrail with easeinbottom
    r "Alright, Doc. Here she is."
    r "Those are some long stairs. Think ya got the leg strength for it?"

    mc "Hah, you kidding me?"

    r "Maybe."
    r "I..."
    show r look offrail
    r "Wait a sec, Doc."

    mc "We don't have a lot of time -"

    r "I know, I know, but..."

    stop music fadeout 3.0
    r "I... I've never been up there, y'know."
    r "We aren't allowed up to the surface. All I know is what I've seen on TV."
    r "Fitness, athletics - that's my specialty."
    r "I don't like change all that much."

    show r offrail
    r "And I'm... frankly, Doc, I'm kinda scared."

    mc "I understand. But there's so much up there to see."
    
    show r look offrail
    mc "It might be scary, but we don't have much of a choice."
    mc "And Rob?"

    show r offrail
    r "Yeah?"

    mc "I'm not leaving your side. I'll be right here the whole time."

    r "I..."
    r "Alright."
    r "Let's get goin'."

    n "You pat Rob's chassis gently and begin the ascent."

    hide flash
    scene black with fade
    $ renpy.pause(2.0, hard=True)
    $ cutscenetextbox = True
    show screen cuttextbox
    $ renpy.music.play("music/outsidereveal.ogg")
    $ renpy.music.queue("music/outside.ogg", clear_queue=False)
    scene white with blindplayer

    if persistent.streammode == True:
        r "{color=#fff}What the - why's it so {k=-5}————{/k} bright out here?!"
    else:
        r "{color=#fff}What the - why's it so goddamn bright out here?!"
    r "{color=#fff}Oh... holy cow..."

    scene rob cutscene 5 with dissolve
    python:
        if persistent.rc5 == False:
            persistent.cutscenes_seen += 1
            persistent.rc5 = True
    if persistent.cutscenes_seen == cutscene_count and persistent.ach_picture == False:
        python:
            achievement.grant("ach_picture")
            achievement.sync()
            persistent.ach_picture = True
            ach_name = "picture"
        show screen ach_popup with easeinbottom
    n "{color=#fff}Your vision is blinded by the bright light of the outside world."
    n "{color=#fff}It's only been about two weeks since you were last outside, but..."
    
    if persistent.streammode == True:
        rcg "{color=#fff}This is insane. Did you know about this? The sky? And... oh, the clouds, {k=-5}————{/k}!"
    else:
        rcg "{color=#fff}This is insane. Did you know about this? The sky? And... oh, the clouds, goddamn!"
    rcg "{color=#fff}I've only seen this stuff through a screen!"

    n "{color=#fff}...Rob's never seen the surface."

    rcg "{color=#fff}This is crazy! It's all real - real grass, real blue and green and..."
    rcg "{color=#fff}Oh, feel that fresh air through your circuits!"
    rcg "{color=#fff}...or lungs, in your case."
    rcg "{color=#fff}It's so much better than that stuffy mess of a gym..."

    mccut "{color=#fff}I told you so."

    rcg "{color=#fff}You sure did! Haha!"
    rcg "{color=#fff}God... I can't believe we made it out of there."

    n "{color=#fff}He turns to look at you."

    rcg "{color=#fff}I can't believe you {i}got{/i} me out of there, I... hah... I can't thank you enough, Doc."
    rcg "{color=#fff}Wow. You're real pretty in this light."

    mccut "{color=#fff}Thank you."

    rcg "{color=#fff}You've got such a... glow around you, Doc. And I don't want to leave it."
    rcg "{color=#fff}I think I love ya. As silly as that sounds."
    rcg "{color=#fff}And I KNOW, I {i}know{/i}, alright, we ain't known each other long..."
    rcg "{color=#fff}I'm just hopin' you'll give me a chance."
    rcg "{color=#fff}I mean... I'm sure we'll have plenty of time now, right?"

    mccut "{color=#fff}Haha. That we will."

    hide screen cuttextbox
    scene black with fade
    $ cutscenetextbox = False

    n "Clutching Rob to your side, you take off towards the city."
    n "You stay close enough to the road to know where you're going, but far enough away that no one will see you."

    r "KEEP GOING, DOC! YOU GOT THIS! PUSH YOURSELF!"
    mc "I'm pushing as hard as I can!!"

    n "The run is difficult, but Rob's encouragement does wonders."
    n "You still regret that you left your car at the complex."
    if persistent.streammode == False:
        mc "Damn it!"
    r "Alright, I think we're far 'nough away from the complex. Let's take a rest... uh, here."

    n "The two of you reach a clearing just on the outskirts of the city."
    n "Breathing heavily, you lean against a tree, Rob on your lap."

    r "How you doin', Doc?"

    mc "I'm alright. Adrenaline's still pumping through my veins, but I'm coming down. Slowly."

    r "Good, good. Take a deep breath."

    n "Rob sighs."

    r "Still can't believe you came back for me. Celine never woulda done somethin' like that."
    r "You're real selfless, Doc."

    mc "Thanks, Rob. I try to be."

    r "Make sure you're lookin' out for yourself, too."

    mc "Yeah, yeah."

    n "..."

    r "D'ya think they're gonna come lookin' for us?"

    mc "No. We honestly probably saved them time by disappearing."
    mc "I don't think they care anymore. Thankfully."

    r "Huh."
    r "What's next, then?"

    mc "Well. I'm not sure."
    mc "It's up to us to figure that out."
    mc "I should probably start by finding a new job..."

    r "That you should."
    r "Heh..."
    r "Thanks, Doc."
    r "I'm glad you're here."
    r "I'm glad we met."

    if romance_points["Rob"] < 29:
        stop music fadeout 1.0
        window hide
        show screen creditsfadeout
        $ renpy.pause(2.0, hard=True)
        hide screen creditsfadeout
        python:
            persistent.endings_got["robgood"] = True
            if sum(persistent.endings_got.values()) == ending_count:
                achievement.grant("ach_seenitall")
            achievement.grant("ach_robgood")
            achievement.sync()
        $ renpy.movie_cutscene("ENDCREDIT_rob.webm")
        $ MainMenu(confirm=False)()
    if romance_points["Rob"] >= 29:
        python:
            persistent.endings_got["robgood"] = True
            if sum(persistent.endings_got.values()) == ending_count:
                achievement.grant("ach_seenitall")
            achievement.grant("ach_robgood")
            achievement.sync()
        jump END_robtrue  

label escape_gregory:
    scene stairs with fade
    if persistent.flash == True:
        show flash with None
    show gre
    show gore
    show rie happy
    with easeinbottom
    g1 "Here we are, Doctor."

    n "You look down at the three cores bundled up in your coat."

    mc "This is still a little weird to me."

    show rie
    g3 "You're not the only one."
    show gore look
    g2 "We have more pressing concerns right now."

    mc "Yes, you're right."
    mc "Alright. Let's -"

    show gre at bounce
    show gore at bounce
    show rie happy at bounce
    gall "Wait!"

    mc "Wh -"

    stop music fadeout 3.0
    show gre look
    g1 "Sorry, Doctor, give us just a second."
    show gore close
    g2 "This is... a new experience."
    show rie look
    g3 "All of this."
    show gre sus
    g1 "Being separated..."
    show gore look
    g2 "Thinking independently..."
    show rie
    g3 "...going to the surface."
    show gre look
    show gore
    show rie happy
    gall "And I'm a little scared."
    g1 "We've had a lot of contact with surface humans before."
    show gore close
    g2 "In particular, the shareholders that come down for meetings."
    show rie look
    g3 "But we've never been to the surface ourselves."
    show gre sus
    g1 "I don't know what to expect up there."
    show gore
    g2 "I'm not used to this... silence in my head."
    show rie
    g3 "How are we supposed to process this?"
    show gre look
    show gore close
    show rie look
    gall "Separately?"

    mc "I can imagine that would be quite terrifying."
    mc "Spending your whole life thinking as one entity - and now you have to think for yourselves."

    show gore look
    g2 "It's not just that. Think about this logically -"
    show rie angry
    g3 "You're basically stealing us from Aperture."
    show gre
    g1 "What if they come after you?"

    show rie
    mc "I don't think they will. I think we'll be just fine."
    mc "We don't have much of a choice, either way."

    show gore
    g2 "That much is accurate..."
    show gre look
    g1 "Okay."
    show rie look
    g3 "I still think this is a bad idea."
    gall "But I'm ready."

    mc "Alright."

    n "You hold the coat close to your stomach and begin the ascent."

    hide flash
    scene black with fade
    $ renpy.pause(2.0, hard=True)
    $ cutscenetextbox = True
    show screen cuttextbox
    $ renpy.music.play("music/outsidereveal.ogg")
    $ renpy.music.queue("music/outside.ogg", clear_queue=False)
    scene white with blindplayer

    g1 "{color=#fff}It's so bright out here!"
    g2 "{color=#fff}Agh, my optics -"
    g3 "{color=#fff}Would you two quit whining?"
    gall "{color=#fff}Oh my god..."

    scene gregory cutscene 4 with dissolve
    python:
        if persistent.gc4 == False:
            persistent.cutscenes_seen += 1
            persistent.gc4 = True
    if persistent.cutscenes_seen == cutscene_count and persistent.ach_picture == False:
        python:
            achievement.grant("ach_picture")
            achievement.sync()
            persistent.ach_picture = True
            ach_name = "picture"
        show screen ach_popup with easeinbottom
    n "{color=#fff}Your vision is blinded by the bright light of the outside world."
    n "{color=#fff}It's only been about two weeks since you were last outside, but..."
    g1cg "{color=#fff}Guys! Oh my god, look at how vibrant the sky is!"
    g2cg "{color=#fff}And the grass... such a beautiful green."
    g3cg "{color=#fff}Pfft, I've seen better..."
    g2cg "{color=#fff}No you haven't."

    n "{color=#fff}...Gregory's never seen the surface."

    g1cg "{color=#fff}This is crazy! I can't believe we've been missing this all this time!"
    g2cg "{color=#fff}Incredible. There's so much to see out here."
    g3cg "{color=#fff}Aperture is nothing compared to this..."
    gallcg "{color=#fff}Wow."

    n "{color=#fff}The three cores turn to look at you."

    g1cg "{color=#fff}Doctor, you brought us up here. You..."
    g2cg "{color=#fff}It's thanks to you we're seeing this right now."
    g3cg "{color=#fff}You're brave. Saving us despite the risk."
    g1cg "{color=#fff}You've never once judged me. You've never questioned me."
    g2cg "{color=#fff}Kept our secret... and when we told you, you accepted us regardless."
    g3cg "{color=#fff}Doctor..."
    g1cg "{color=#fff}I think I love you."
    g2cg "{color=#fff}Me too."
    g3cg "{color=#fff}Me three."
    g1cg "{color=#fff}Hah... this is a little weird, huh?"
    g1cg "{color=#fff}We all still have the same feelings for you despite the separation..."

    mc "{color=#fff}It is a little strange."
    mc "{color=#fff}Especially considering I still feel the same way I did about you before."
    mc "{color=#fff}But we'll... figure it out."

    hide screen cuttextbox
    scene black with fade
    $ cutscenetextbox = False
    n "Looking back at the complex you came from, you tie the sleeves of your coat together around Gregory and sprint off."

    n "You keep to the forest neighboring the road, making sure to stay far enough away that no one will see you."
    n "Thankfully, Gregory's lightweight - the three of them together are still about half the weight of a full core."
    n "It's still a long jog, though."
    n "You regret that you left your car back at the complex."

    if persistent.streammode == False:
        mc "Damn..."

    g1 "Doctor - you should probably rest for a bit."
    g2 "It's dangerous to push yourself too hard."
    g3 "Yeah. Listen to them."

    mc "Alright, alright."

    n "You reach a clearing just on the outskirts of the city."

    mc "Let's rest here a bit."

    n "You lay down on the grass and unfurl your lab coat, letting Gregory see the sky once again."

    g1 "Can't get over that view..."
    g2 "Incredible."
    g3 "I can't believe we aren't in Aperture anymore."
    g1 "I know, right?"
    g2 "It almost feels impossible."
    g1 "What are we going to do now?"
    g2 "What {i}should{/i} we do?"
    g3 "Hah! What {i}shouldn't{/i} we do?!"
    g2 "Don't get ahead of yourself."
    g1 "Doctor?"

    mc "Yeah?"

    g2 "What's next?"
    if persistent.streammode == True:
        g3 "We reach the city, {k=-5}————{/k}."
    else:
        g3 "We reach the city, dumbass."
    g1 "Well yeah. I think he's asking {i}what then?{/i}"

    mc "Who knows. First things first, I get a new job. And then..."
    mc "Well. I don't know."

    g1 "It still feels weird being separated..."
    g2 "Agreed. It's a little uncomfortable."
    g3 "Oh, get over yourselves. We'll get used to it."
    g1 "She's right. It'll just take some time."

    mc "You three are funny."

    g2 "What do you mean?"

    mc "Oh, nothing."
    mc "But don't worry. We'll figure things out."

    g1 "I'm sure things will be just fine with you here, Doctor."
    g2 "Agreed. You're smart."
    g3 "And pretty."

    mc "Haha. Thank you, guys."
    if romance_points["Greg"] < 21:
        stop music fadeout 1.0
        window hide
        show screen creditsfadeout
        $ renpy.pause(2.0, hard=True)
        hide screen creditsfadeout
        python:
            persistent.endings_got["greggood"] = True
            if sum(persistent.endings_got.values()) == ending_count:
                achievement.grant("ach_seenitall")
            achievement.grant("ach_greggood")
            achievement.sync()
        $ renpy.movie_cutscene("ENDCREDIT_greg.webm")
        $ MainMenu(confirm=False)()
    if romance_points["Greg"] >= 21:
        python:
            persistent.endings_got["greggood"] = True
            if sum(persistent.endings_got.values()) == ending_count:
                achievement.grant("ach_seenitall")
            achievement.grant("ach_greggood")
            achievement.sync()
        jump END_gregtrue 

label escape_esther:
    scene stairs with fade
    if persistent.flash == True:
        show flash
    show e offrail shock with easeinbottom
    e "Is... is that... sunlight? At the top?"
    e "The doors are... {i}open!"
    mc "You said they're usually locked, right?"
    show e offrail sus
    e "Usually, yes, but..."
    show e offrail look
    e "Looks like they're... not... this time."
    mc "Miss Esther? Is something wrong?"
    show e offrail close
    n "She sighs."
    e "I... well..."
    stop music fadeout 3.0
    show e offrail look
    e "I've never been to the surface."
    e "Personality constructs... {i}we{/i}... usually aren't permitted."
    show e offrail close
    e "And I... don't know what to expect up there."
    show e offrail sus
    e "I'm used to Aperture, Doctor. I'm used to being connected to the panel systems, I'm used to being in charge of Section C8, I'm..."
    e "Even though Testing played a big part in... most of my life, I've..."
    show e offrail look
    e "Fond of... working with... the others."
    show e offrail close
    e "A-And now I don't know if they're safe, and I... I've lost any connection I had to them, and..."
    show e offrail shock
    e "I-I'm scared, I..."
    show e offrail close
    e "I thought I was finally making {i}progress.{/i}"
    show e offrail
    e "Hell, Kris had invited me to the lounge yesterday, and... he {i}hates{/i} me. Or... so I thought."
    show e offrail look
    e "Now that they're gone, what... what will I do? What's even up there for me?"
    show e offrail sus
    mc "I understand, Miss Esther. That... that must be tough."
    mc "But you have me here. I'm going to get you out of here, and..."
    mc "You'll have plenty of opportunities on the surface that you can't get down here."
    mc "I can't guarantee it'll be easy, or quick..."
    mc "But you've shown me that you're strong."
    mc "I think you'll do just fine up there."
    show e offrail close
    e "O-Okay, Doctor. I trust you, I..."
    show e offrail
    e "It's a little ridiculous to talk about this now, when the facility's falling apart, isn't it?"
    show e offrail close
    n "She sighs."
    show e offrail
    e "Let's go."

    hide flash
    scene black with fade
    $ renpy.pause(2.0, hard=True)
    $ cutscenetextbox = True
    show screen cuttextbox
    $ renpy.music.play("music/outsidereveal.ogg")
    $ renpy.music.queue("music/outside.ogg", clear_queue=False)
    scene white with blindplayer

    e "{color=#fff}O-Oh my god, I can... barely see a thing..."
    e "{color=#fff}I... oh, {i}my.{/i}"

    scene esther cutscene 4 with dissolve
    python:
        if persistent.ec4 == False:
            persistent.cutscenes_seen += 1
            persistent.ec4 = True
    if persistent.cutscenes_seen == cutscene_count and persistent.ach_picture == False:
        python:
            achievement.grant("ach_picture")
            achievement.sync()
            persistent.ach_picture = True
            ach_name = "picture"
        show screen ach_popup with easeinbottom

    n "{color=#fff}Your vision is blinded by the bright light of the outside world."
    n "{color=#fff}It's only been about two weeks since you were last outside, but..."
    
    e "{color=#fff}This is... nothing like the rest of Aperture."
    e "{color=#fff}It's so bright, so full of color, so..."

    n "{color=#fff}...Miss Esther has never seen the surface."

    e "{color=#fff}It's incredible!"
    e "{color=#fff}All those white-paneled walls and perfectly-placed tiling... could {i}never{/i} compare to this."
    e "{color=#fff}I... wow."
    e "{color=#fff}..."
    e "{color=#fff}Doctor..."
    e "{color=#fff}Why'd you come back for me?"
    e "{color=#fff}I-I've done nothing for you in the past two weeks but... boss you around and..."
    e "{color=#fff}Well, you know."
    e "{color=#fff}You could've just saved yourself, but... you came all the way to the offices, not even knowing if I was there, I..."
    e "{color=#fff}You risked so much. And for what?"
    e "{color=#fff}For me?"
    e "{color=#fff}You know better than anyone how much I... struggle to connect with others, and how..."
    e "{color=#fff}I'm not the... {i}kindest{/i} robot out there."
    e "{color=#fff}I-It's in my programming."
    e "{color=#fff}I've always thought..."
    mccut "{color=#fff}I don't know, Miss Esther. You..."
    mccut "{color=#fff}You've been kind to me. And... when I woke up, and the alarms were going off, I..."
    e "{color=#fff}I suppose making enemies out of my most possible friends doesn't help me much in the long run..."
    e "{color=#fff}..."
    e "{color=#fff}Thank you."
    e "{color=#fff}You're... too kind to me."
    e "{color=#fff}We should go now. Before they find us."

    hide screen cuttextbox
    scene black with fade
    $ cutscenetextbox = False
    n "You clutch Miss Esther tightly to your hip and start running."
    n "She's heavier than average core weight, somehow."
    n "You don't dare look back."
    n "Dodging bushes and trees, you run alongside the road leading away from the facility, keeping just far enough away to not be spotted."
    n "Eventually, you reach a clearing just outside the neighboring city."
    e "Doctor - stop. You need to rest."
    e "It won't do you any good to keep running. I think we're far enough away, regardless."
    mc "You're... you're right, Miss Esther. As usual."
    e "Hah. Don't give me too much credit."

    n "You sit down against a tree and lay Miss Esther beside you."

    e "Being... outside... is so strange."
    e "The closest I ever got was the surface tracks."
    e "I was stationed there only 3 months before they scrapped the program."
    e "Turns out sweeping dead leaves and scrubbing moss out of testing tracks is expensive."
    e "Who would've thought?"

    mc "So you've seen the surface before, then?"
    e "Seen it? Yes. But I was never permitted outside the observation rooms, which were completely enclosed."
    e "So this... is new."
    e "..."
    mc "..."
    e "Thank you, again, Doctor."
    e "I don't know what awaits us in the future, but..."
    e "I'm glad to have someone as... understanding as you in my life."

    mc "Actual gratitude? From you?"

    e "Rare, I know. Don't get used to it."

    stop music fadeout 2.0

    jump END_esthertrue