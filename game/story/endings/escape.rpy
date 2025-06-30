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
    stop music fadeout 3.0

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
    scene stairs with fade
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
    $ persistent.hc5 = True
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
    h "{color=#fff}Went out of your way to save me instead of just saving yourself..."
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
    h "...I'm worried, Doc. Aperture's not going to come looking for me, are they?"

    mc "Doubtful. I don't think they really care what happens to you guys now..."
    mc "But even if they did, I'd be here to protect you."
    mc "I won't let anything happen to you, Heath."

    h "Well then. I hope you're ready for a lot more tricks from yours truly!"

    mc "Oh, don't worry. I know what I got myself into."

    if romance_points["Heath"] < 30:
        stop music fadeout 1.0
        window hide
        show screen creditsfadeout
        $ renpy.pause(2.0, hard=True)
        hide screen creditsfadeout
        $ renpy.movie_cutscene("ENDCREDIT_heath.webm")
        $ MainMenu(confirm=False)()
    if romance_points["Heath"] >= 30:
        jump END_heathtrue

label escape_aspen:
    scene stairs with fade
    show flash
    show a with easeinbottom
    a "H-Here it is."
    a "I'm not sure we're supposed to use these -"
    a "Actually, we're probably definitely not supposed to use these, haha."
    a "B-But I don't think we have any other choice, so..."

    mc "No. We really don't."

    a "Doctor - wait. Wait wait."

    mc "What's up?"

    stop music fadeout 1.0
    stop music1 fadeout 1.0
    stop music fadeout 3.0
    a "I... I don't know what to expect up there."
    a "And I'm terrified."
    a "Hah... I mean... other than when I was activated, this is my first time outside the greenhouse..."
    a "Let alone somewhere even farther than that."
    a "I have no... I have no frame of reference, I have no experience..."
    a "What am I supposed to do?"

    mc "You {i}do{/i} have a frame of reference, Aspen."
    mc "Plants are your specialty."
    mc "And if I know anything about the surface, there's a hell of a lot of them up there."

    a "I... I suppose you're right, Doctor."

    mc "And I'm going to be here for you the entire time."
    mc "I promise I won't leave your side."

    a "O-Okay. I..."
    a "I think I'm ready, then."
    a "I... I can't wait to see what real grass looks like."

    n "Steeling yourself, you hold tighter onto Aspen and begin the ascent."

    hide flash
    scene black with fade
    $ renpy.pause(2.0, hard=True)
    $ cutscenetextbox = True
    show screen cuttextbox
    $ renpy.music.play("music/outsidereveal.ogg")
    $ renpy.music.queue("music/outside.ogg", clear_queue=False)
    scene white with blindplayer

    a "{color=#fff}The light - agh, it's just like when the greenhouse lights turn on..."
    a "{color=#fff}I... oh my god!"

    scene aspen cutscene 5 with dissolve
    $ persistent.ac5 = True
    n "{color=#fff}Your vision is blinded by the bright light of the outside world."
    n "{color=#fff}It's only been about two weeks since you were last outside, but..."

    a "{color=#fff}The sky! The grass! The... oh, {i}pseudotsuga menziesii...{/i}"
    a "{color=#fff}It's all so bright... and so green... and so beautiful!"

    n "{color=#fff}...Aspen has never seen the surface."

    a "{color=#fff}Wow, this is incredible! I can't..."
    a "{color=#fff}Doctor, can you set me down in the grass?"

    n "{color=#fff}You lay Aspen down in front of you. They look up and around themselves in wonder."

    a "{color=#fff}These - these are {i}Taraxacum officinale{/i}, aren't they? Dandelions!"
    a "{color=#fff}They're so plentiful. And so yellow."
    a "{color=#fff}And... oh, it's all so wonderful. I..."

    n "{color=#fff}Aspen turns to look up at you."

    a "{color=#fff}You gave me this opportunity, Doctor."
    a "{color=#fff}You almost got yourself... killed... all for me. You..."
    a "{color=#fff}You came to save me, even though it was flooding. You rushed me through fires and..."
    a "{color=#fff}And because of that, I get to see this."
    a "{color=#fff}Y-You..."
    a "{color=#fff}I think I... I think I love you, Doctor."
    a "{color=#fff}A-And I know that's a little strange to hear from a core like me, haha, so I understand if you..."
    
    n "{color=#fff}They sigh."

    a "{color=#fff}I hope you'll feel the same. One day."

    mc "{color=#fff}I think I've already started to, Aspen."




label escape_ccunknown:
    scene hall with fade
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
    show flash
    mc "Alright. We're... we're here."
    mc "Okay. How are we gonna get you up, CC?"

    show c offrail with easeinright
    c "My chair has wheels that {i}should{/i} be able to go up stairs..."
    c "But I'm not sure you'll be able to take us both at the same time."

    hide c with easeoutright
    show u offrail with easeinbottom
    u "Take him first, Doc. He's heavier - it'll be easier to carry me up after."
    u "Don't worry. I'll be fine."

    hide u with easeoutbottom
    show c offrail with easeinright
    c "No - what if they find you? What if they..."
    c "It's not safe. You should go up first."
    hide c with easeoutright
    show u offrail with easeinbottom
    u "Don't listen to him, Doc. Please - take him first."

    mc "CC - he's right. It'll be easier to come back for him than for you..."
    mc "I'm already... quite exhausted."

    hide u with easeoutbottom
    show c offrail with easeinright
    n "CC sighs."

    c "Okay. I trust you, uh..."

    hide c with easeoutright
    show u offrail with easeinbottom
    u "Ryland."

    mc "What?"

    ry "My name. I... I remembered. Yesterday."
    ry "I've just been... scared to tell anyone. 'Case I forget again."

    hide u with easeoutbottom
    show c offrail with easeinright
    c "Ryland."
    c "That's an excellent name."
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

    c "You're... you're right. I..."

    mc "I'm sorry, CC. I know how much you cared about him."

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
    $ persistent.cc5 = True
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
    c "{color=#fff}...you'll feel the same one day."

    mc "{color=#fff}I think I might, CC."

    hide screen cuttextbox
    scene black with fade
    $ cutscenetextbox = False

    n "Before the people that took Ryland away can get curious, you quickly push CC's chair down and across the field, into the thick of the forest ahead."
    n "He's heavy. The chair weighs almost half as much as you do, and pushing it for even just half an hour is incredibly taxing."
    n "The rough terrain probably doesn't help."
    n "You regret that you hadn't thought to get your car out of the complex."

    mc "Damn it..."

    n "Eventually, you reach a peaceful clearing just on the outskirts of the big city."
    n "Out of breath, you lay down in the grass."

    mc "Let's... let's rest here, for a bit."

    n "No response."

    mc "CC?"

    c "I'm... I'm here, Doctor."
    c "I'm sorry. I'm just exhausted. And... in awe, still."
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
    c "Without Aperture's resources, I'm not sure how much longer I'll live."

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
        $ renpy.movie_cutscene("ENDCREDIT_ccunknown.webm")
        $ MainMenu(confirm=False)()
    if romance_points["CC"] >= 30:
        jump END_cctrue

label leave_cc:
    show u offrail with easeinright
    u "Hey Doc, you doing good?"

    mc "Y-Yes, I'm just... I'm just exhausted."

    u "We're almost outta here. The stairs are just around the corner."

    n "You push forward slowly. Eventually, you finally reach the stairs."
    scene stairs with fade
    show flash
    mc "Alright. We're... we're here."
    mc "Okay. How are we gonna get you two up?"

    show c offrail with easeinright
    c "My chair has wheels that {i}should{/i} be able to go up stairs..."
    c "But I'm not sure you'll be able to take us both at the same time."

    hide c with easeoutright
    show u offrail with easeinbottom
    u "Take him first, Doc. He's heavier - it'll be easier to carry me up after."
    u "Don't worry. I'll be fine."

    hide u with easeoutbottom
    show c offrail with easeinright
    c "No - what if they find you? What if they..."
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
    show c offrail with easeinright
    c "Ryland."
    c "That's an excellent name."
    c "I'll see you on the surface, alright?"
    c "Just don't spoil it for me."

    hide c with easeoutright
    n "You begin the ascent, quickly carrying Ryland up step by step."
    n "It's not easy, and the stairs seem to go on forever... but eventually, you're already halfway up."
    n "Suddenly, you hear CC call out from behind you -"

    c "Doctor! Hurry! They're -"

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
    ry "{color=#fff}I can barely see a th- oh my..."

    scene unknown cutscene 3 with dissolve
    $ persistent.uc4 = True
    n "{color=#fff}Your vision is blinded by the bright light of the outside world."
    n "{color=#fff}It's only been about two weeks since you were last outside, but..."
    ry "{color=#fff}What the..."
    ry "{color=#fff}This is insane. I've been hiding away in a closet my whole life?!"
    ry "{color=#fff}This... this was above me? All this time?!"
    ry "{color=#fff}Haha! Wow!"

    n "{color=#fff}...for all he knows, Ryland has never seen the surface."

    ry "{color=#fff}This fresh air through my circuits, it's like... it's better than any drink I've had."
    ry "{color=#fff}If only... CC could've seen this."
    ry "{color=#fff}But..."

    n "{color=#fff}He turns to face you."

    ry "{color=#fff}I'm glad you're here."
    ry "{color=#fff}You... hah, Doc, you risked your life for us both."
    ry "{color=#fff}Not just me, but CC, too. And..."
    ry "{color=#fff}I can't thank you enough."
    ry "{color=#fff}You're really somethin' else."
    ry "{color=#fff}And I might love that."
    ry "{color=#fff}I know I ain't been the best to you. I know I've been a flirt, and I've been annoying..."
    ry "{color=#fff}But I hope you'll love me back. One day. If I try hard enough."

    mc "{color=#fff}I think... it'll take time, Ryland. But I might."

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

    ry "Honestly, me too. I may be tryna quit, but I sometimes wish I wasn't, hah."

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
        $ renpy.movie_cutscene("ENDCREDIT_ccunknown.webm")
        $ MainMenu(confirm=False)()
    if romance_points["???"] >= 15:
        jump END_unknowntrue    

label escape_rob:
    jump endtest

label escape_gregory:
    jump endtest