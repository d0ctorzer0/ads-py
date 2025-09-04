label day11:
    $ audio_crossFade(2, "music/fourteen.ogg")
    scene mcroom night with fade
    n "You enter your chambers once more."
    if lock_kris:
        mc "Well... Kris certainly gave me a run for my money today... haha!"
    elif lock_heath:
        mc "I wonder where Heath got that dove from... haha."
    elif lock_aspen:
        n "You place the cactus Aspen gave you, [cactusname], beside your bed"
        n "The flowers look as bright as ever."
    elif lock_cc:
        mc "I never expected CC to recite poetry to me..."
    elif lock_rob:
        n "You place your Topps baseball card by your bed."
        mc "It's honestly a little shocking he would give this to me... haha."
    else:
        n "A fairly... normal day, all things considered."
    n "Throwing your paperwork down for the day, you sigh."
    n "You lay down in your bed for the night."

    scene black
    with fade
    $ daynum = "11"
    $ dayday = "Thursday"

    if renpy.is_skipping() == False:
        show screen daytransition
        $ renpy.pause(2.0, hard=True)

    scene mcroom day
    with fade

    n "You wake up at 07:30, more ready for the day than ever."
    mc "Only two more days..."
    n "You grab your paperwork, get dressed, and leave your chambers."

    scene office with fade
    stop music fadeout(1.0)
    stop music1 fadeout(1.0)
    n "You enter your office."
    n "Miss Esther isn't here yet."

    mc "Strange..."
    mc "The last time she was late was my second day here."

    play music one
    n "You sit down at your desk and organize while you wait."

    scene black with fade
    scene office with fade

    n "Eventually, it's 08:30, and she still hasn't shown."

    mc "Where {i}is{/i} she?"

    n "You decide to wait a little longer."

    scene black with fade
    scene office with fade 

    n "The clock now reads 09:00. No sign of your supervisor."

    mc "Uh..."
    mc "I suppose I should just... get to work?"

    n "You gather your materials, compose yourself, and head towards Kris."

    jump krisday11

label krisday11:
    scene krisroom with fade
    $ audio_crossFade(2, "music/two.ogg")
    n "You enter Kris' room without Miss Esther behind you. It still feels a little strange."

    show k with easeinright
    k "Doctor? You're late."
    show k angry
    k "Where's Miss Esther?"

    mc "No clue. That's why I'm behind - she never showed up today."

    show k
    k "Strange... that woman is exceedingly punctual."
    show k angry
    k "It's not like her to be late..."
    show k
    k "Anyhow. Things are proceeding as normal here."
    if positive["Kris"]:
        if lock_kris == True:
            jump romancekrisday11
        if lock_kris == False:
            jump p_krisday11
    else:
        jump n_krisday11

label romancekrisday11:
    show k flirt
    k "And you look amazing today, Doctor. As usual."

    mc "Thank you. You don't look too bad yourself."

    k "Don't flatter me too much, now, or people might start to think..."
    
    show k
    n "He sighs."
    k "As much as I'd love for you to stay and... {i}waste time{/i} with me..."
    k "...you're very far behind on schedule."

    mc "Yes, I know."

    show k flirt
    k "Miss Esther may not be here to usher you along, but you must stay disciplined."
    show k angry
    k "You do have paperwork to turn in, after all."

    mc "You're right."
    
    show k
    k "Plus... I'm sure we'll have plenty of time this weekend."

    show k flirt
    k "Go on now! Have a wonderful day, Doctor."

    mc "You too, Kris."

    k "I always have a good day after seeing you."

    n "You finish checking Kris off your list and leave the room."

    jump heathday11

label p_krisday11:
    k "You only have two more days left until you go back to Manufacturing."
    k "Are you looking forward to it?"

    mc "I'm not sure."

    show k flirt
    k "Fair enough."
    k "Change is difficult."

    show k
    k "I'm curious who the permanent employee for this position might be..."
    k "If they're anything like you, I'll be happy. All I ask is for someone kind."
    k "Now. As much as I'd love to have you stay and chat, you're very far behind on schedule."

    mc "Yes, I know."

    show k flirt
    k "Miss Esther may not be here to usher you along, but you must stay disciplined."
    show k angry
    k "You do have paperwork to turn in, after all."

    mc "You're right."

    show k flirt
    k "Go on now! Have a wonderful day, Doctor."

    mc "You too, Kris."

    k "I will."

    n "You finish checking Kris off your list and leave the room."

    jump heathday11

label n_krisday11:
    show k angry
    k "Not like you care all that much. Simply here to do a job, after all."
    
    show k
    k "Not to be hostile or anything, but you {i}do{/i} distract my focus when you're here, Doctor."

    mc "Sorry."

    k "Don't be sorry. Can't control it. What can you do?"
    show k angry
    k "You only have two more days left until you go back to Manufacturing."
    k "I'm curious who the permanent employee for this position might be..."
    k "If they're anything like you, I'll be incredibly disappointed."
    show k
    k "Now. I'd love for you to stay and chat, but you are behind schedule. You should be on your way."

    mc "Yes. Thank you, Kris."

    n "You finish checking Kris off your list and leave the room."

    jump heathday11

label heathday11:
    scene heathroom with fade
    $ audio_crossFade(2, "music/three.ogg")
    n "You enter Heath's break room once again."

    show h with easeinright
    h "Welcome, Doctor! Prepare for an interesting trick..."
    show h sad
    h "...wait, where's Miss Esther?"

    mc "I'm not sure. She never showed up."

    h "Weird..."

    n "There's a metal bucket hanging from her handle."

    mc "What's the bucket for?"
    
    show h laugh
    h "Patience, patience! All shall be revealed."
    show h
    h "First though - look inside the bucket. It's empty, correct?"

    n "You do so. There's nothing in there."

    mc "Yes, it's empty."

    n "As soon as you step back, you hear a metal {i}clank{/i} sound, and the bucket shifts slightly."

    show h laugh
    h "Are you so sure?"

    n "You look inside the bucket - there's an Aperture credit in there."

    mc "What... how did you do that?"

    show h
    h "{i}Magic!{/i}"
    show h sad
    h "...and..."

    n "You hear another {i}clank,{/i} though gentler, and she shows you the bucket again."
    n "The credit is gone."

    show h laugh
    h "...a little bit of showmanship! Haha!"

    n "She tosses the bucket to the side with flair."
    show h sad
    h "Now... for the final part of the trick..."
    show h
    h "Check your left pocket!"

    n "You check. There's a credit in it."

    mc "Oh my god."

    show h laugh
    h "Keep it, Doc! A little gift from me."

    if positive["Heath"]:
        if lock_heath == True:
            jump romanceheathday11
        if lock_heath == False:
            jump p_heathday11
    else:
        jump n_heathday11

label romanceheathday11:
    show h
    h "There's plenty more where that came from!"

    n "She looks at you happily."

    mc "That was incredible, Heath. Just like you."

    h "Why thank you, Doctor. You aren't too bad yourself! Haha."
    h "S-Sorry. I'm still a little nervous after yesterday!"
    show h sad
    h "And Miss Esther's not here to balance the mood out."

    mc "You're alright. It's cute."

    show h laugh
    h "I know I am!"
    show h
    h "I wish you could stay, Doctor, I really do. I love your company, {i}but...{/i}"
    h "From the look of the clock, you're really behind schedule! And my trick today took up a lot of time, haha."

    mc "Oh - yes, I should probably get going."

    show h sad
    h "Don't worry - I'll see you this weekend, right?"

    mc "I hope so."

    show h
    h "Wonderful. Have an excellent day, Doctor!"

    mc "I always do after seeing you."

    n "You check Heath off your list and leave the break room."

    jump subromanceday11

label p_heathday11:
    show h
    h "What'd you think of that trick, Doc?"

    mc "Impressive. I don't know how you did it."

    h "Difficult without hands, but I make it work!"

    show h laugh
    h "Imagine if I {i}did{/i} have hands! I'd be the best magician ever!"

    show h sad
    h "I do find it interesting that Miss Esther didn't show..."
    h "She's usually very tough on herself."

    mc "Yeah, I'm not sure. I just decided I should probably get my job done."

    show h
    h "Speaking of! Looking at the clock, you're far behind schedule - you should probably go!"
    h "Sorry for taking up so much time!"

    mc "You're alright, Heath, no worries."

    h "Have a great day, Doctor. I'll see you tomorrow?"

    mc "Yes."

    n "You check Heath off your list and leave the break room."

    jump subromanceday11

label n_heathday11:
    show h
    h "Who knows? Maybe it'll help you be a little more positive!"

    mc "What does that mean?"

    show h laugh
    h "Oh, nothing, haha."
    show h sad
    h "I do find it interesting that Miss Esther didn't show..."
    h "She's usually very tough on herself."

    mc "Yeah..."

    show h
    h "Anyways! My trick took a lot of time today, and you're behind."
    h "You should get going!"

    mc "Oh. Yes. I will."
    mc "Thank you, Heath."

    n "You check Heath off your list and leave the break room."

    jump subromanceday11

label subromanceday11:
    scene hall with fade
    if not lock_kris and not lock_aspen and not lock_cc and not lock_heath and not lock_rob:
        if romance_points["???"] == romance_points["Greg"]:
            $ day11lock_randomizer = renpy.random.choice(['???', 'Greg'])
            if day11lock_randomizer == "Greg":
                if romance_points["Greg"] >= 8:
                    jump gregday11
                else:
                    jump aspenday11
            elif day11lock_randomizer == "???":
                if romance_points["???"] >= 8:
                    jump unknownday11
                else:
                    jump aspenday11

        elif romance_points["???"] < romance_points["Greg"]:
            if romance_points["Greg"] >= 8:
                jump gregday11
            else:
                jump aspenday11
        elif romance_points["???"] > romance_points["Greg"]:
            if romance_points["???"] >= 8:
                jump unknownday11
            else:
                jump aspenday11
    else:
        jump aspenday11

label gregday11:
    n "Suddenly, you hear a familiar sound - weighed-down wheels."
    $ audio_crossFade(2, "music/seven.ogg")
    show g aaa with easeinright
    n "Gregory comes around the corner and nearly runs into you."
    g "Doctor! O-Oh. Hi!"

    mc "Gregory? What are you doing down here?"

    show g look
    g "I was just on my way to see Kris - there's a... a meeting in his conference room."
    g "They ran out of space upstairs. So I have to go get it ready."

    show g
    g "But..."

    g "Actually, now that you're here, there's... uh... something I need to tell you, Doc -"

    mc "Me? Specifically?"

    show g aaa
    g "Yeah! You! Uh..."

    show g look
    g "It might be a little strange..."
    g "A-And you might think of me differently afterwards, but..."
    g "This is important. To me. To... us."
    g "We've been thinking it over, and we have to do this."

    mc "Us? We?"

    $ gotconfession = True
    $ cutscenechoice = True
    show screen cuttextbox
    scene gregory cutscene 2 with fade
    $ cutscenetextbox = True
    python:
        if persistent.gc2 == False:
            persistent.cutscenes_seen += 1
            persistent.gc2 = True
        if persistent.cutscenes_seen == 44:
            achievement.grant("ach_picture")
            achievement.sync()
    n "{color=#fff}Gregory moves his bottom handle slightly, unbuttoning his trench coat. It falls to the ground."
    n "{color=#fff}What stands before you is not a personality core - but three of them, just as you thought."
    n "{color=#fff}The top one - Gregory's voice, you assume - looks down nervously at the other two."
    n "{color=#fff}The middle one looks up at you curiously, and the bottom one glares at you in turn."

    g "{color=#fff}I-I'm not... really... a personality core. I'm... three of them."
    g "{color=#fff}I know I've been trying to hide it, and this is really difficult - no one knows this but my creators, and..."
    g "{color=#fff}I figured you should know the truth before I ask you to accept me any further."

    mccut "{color=#fff}Accept you?"

    g "{color=#fff}Well, Doctor... we... have constantly been running into you, and... you treat me - uh, us so well."
    g "{color=#fff}No one's done that for us before."
    g "{color=#fff}I don't want you to think we're weird, or awkward, but..."
    g "{color=#fff}Can you give us a chance? To be closer to you?"

    menu:
        extend ""
        "I'll accept you no matter what.":
            g "{color=#fff}Oh, Doctor... I..."
            g "{color=#fff}Thank you. So much."
            jump gregacceptance
        "This is too weird for me.":
            jump gregrejection

label gregacceptance:
    $ cutscenechoice = False
    hide screen cuttextbox
    scene hall with fade
    $ cutscenetextbox = False
    $ lock_gregory = True
    show g nocoatlook with easeinright
    g "I don't want to rush things too much between us, so I'm sorry if it came off that way."

    mc "Oh no. It wasn't like that at all."

    show g nocoat
    g "I'm glad."

    mc "How does... this work, anyway?"

    show g nocoatlook
    g "Well, it's a little complicated..."

    mc "I'd like to know regardless."

    show g nocoat
    g "The one with the yellow eye - that's me. I do most of the talking. And appearing, of course."
    g "That one right below me - it does a lot of the thinking. Since we're really small physically, we don't have as much processing power..."
    show g nocoataaa
    g "We gotta divide our jobs, y'know?"

    mc "And the bottom one?"

    show g nocoat
    g "It controls the movement - the cart we're on, and our handles, our eyes..."

    show g nocoatlook
    g "But we can't be separated. From what I know, we'd be incomplete, we'd..."
    g "We wouldn't be fully functional."

    mc "That sounds hard, Gregory."

    g "It is, but..."

    show g nocoataaa
    g "Oh shoot! Look at the time! I've gotta get down to Kris!"
    g "Can you put the trench coat back on me?"

    mc "Sure."

    show g
    n "You slide the trench coat back over Gregory and fasten it at the top."
    show g look
    g "Thank you, Doctor."
    g "I'll... see you later, right?"

    mc "Absolutely."

    hide g with easeoutright
    n "And they're gone."
    n "How strange."

    jump aspenday11

label gregrejection:
    $ cutscenechoice = False
    hide screen cuttextbox
    scene hall with fade
    $ cutscenetextbox = False
    show g nocoatlook with easeinright
    g "Oh... I'm sorry, Doctor, I-I know it is a little weird, haha."
    g "Can you... put my trench coat back on me?"

    mc "Sure, Gregory."

    show g
    n "You put the trench coat back over his... \"shoulders\"."

    show g look
    g "Well... this certainly got awkward quick."
    show g aaa
    g "On second thought, I should probably leave. I..."
    g "I'll see you later, Doc!"

    hide g with easeoutright

    n "And he's gone."
    n "How strange..."

    jump aspenday11


label unknownday11:
    n "Suddenly, you hear a sound - a faint, but distinct, humming."
    show u c with easeinright
    $ audio_crossFade(2, "music/eight.ogg")
    n "A familiar-looking \"face\" rounds the corner - albeit, a little... different from when you last saw it."

    u "Oh! Doc! Sorry, didn't mean to intrude on your route, I..."
    u "Where's that core that's always following you?"

    mc "Don't know, but... is that really you?"

    show u c look
    u "Yep! It's me. I know, I look a little different..."
    if persistent.streammode == True:
        u "I finally got off my {k=-5}——{/k} and went down to repair to go get fixed."
    else:
        u "I finally got off my ass and went down to repair to go get fixed."

    show u c 
    u "They almost refused me service! Hah."
    u "Thankfully a little core named Virgil backed me up."
    u "Took a lot of work - 'bout 3 hours, but... I feel better than ever."

    mc "You... sound better, too."

    show u c look
    u "Well, it ain't easy... I still got a lot of pain in my chassis, y'know..."
    u "I'm tryin' to be better."
    u "'Cuz, well, Doc..."

    $ gotconfession = True
    $ cutscenechoice = True
    show screen cuttextbox
    scene unknown cutscene 2 with fade
    $ cutscenetextbox = True
    python:
        if persistent.uc2 == False:
            persistent.cutscenes_seen += 1
            persistent.uc2 = True
        if persistent.cutscenes_seen == 44:
            achievement.grant("ach_picture")
            achievement.sync() 
    u "{color=#fff}I really wanted to prove to ya that I'm more than what I look like."
    u "{color=#fff}Now, s'true, I've been on a downwards spiral for years now..."
    u "{color=#fff}Hell, I can't even remember my own name..."
    u "{color=#fff}But I really hope that doesn't dissuade ya."
    u "{color=#fff}I'm tryin' to be better. Fixing myself up like this... that's my proof to ya, Doc."
    u "{color=#fff}You've been awfully patient with me. Through my flirtin' and everything..."
    u "{color=#fff}I wanna keep... what we have... goin'."
    u "{color=#fff}Whaddaya say?"
    menu:
        extend ""
        "I'm in the same boat.":
            u "{color=#fff}Well then..."
            u "{color=#fff}I'd consider myself one lucky guy."
            jump unknownacceptance
        "I appreciate it, but... no thanks.":
            jump unknownrejection

label unknownacceptance:
    $ cutscenechoice = False
    hide screen cuttextbox
    scene hall with fade
    $ cutscenetextbox = False
    show u c with easeinright
    $ lock_unknown = True
    mc "I can't believe you went and fixed yourself up just for me."

    u "Well, it wasn't {i}all{/i} for you, y'know."
    u "Some of it was for myself, too."
    show u c look
    u "Can't stay like that forever..."
    show u c
    u "But yeah. Mostly you."

    mc "You said you can't remember your name? At all?"

    u "Yeah, that's right. I haven't been attached to the system in so long, I don't even know when I was activated..."
    u "I'm sure the memory's somewhere deep in my systems, but..."
    u "I've yet to reach it."

    mc "That must be hard."

    u "Sometimes. I don't know how to introduce myself..."
    u "So I jus' don't."

    mc "Fair enough."

    show u c look
    u "Now, Doc, I have a feeling you're runnin' late, so you should prolly get on your way..."
    show u c 
    u "But don't worry. You'll see me later for sure."

    mc "Can't wait."

    u "See ya, Doc."
    hide u c with easeoutright

    n "And he's gone."
    mc "How interesting."

    jump aspenday11

label unknownrejection:
    $ cutscenechoice = False
    hide screen cuttextbox
    scene hall with fade
    $ cutscenetextbox = False
    show u c look with easeinright
    $ lock_unknown = True
    u "Well... no worries. I get it."
    u "I'm a better man. I can take rejection."

    mc "Sorry, it's just -"

    show u c 
    u "Nah, Doc, I understand. Don't feel guilty."
    u "I can improve myself for me, y'know."

    show u c look
    u "Anyways, you should get goin'. I can tell you're kinda in a hurry."
    u "I'll see ya around."

    hide u c with easeoutright

    n "And he's off."

    jump aspenday11

label aspenday11:
    n "The walk up to the greenhouse is incredibly long and boring."
    
    mc "I wonder where she went..."

    n "Eventually, you reach Aspen's door. You open it carefully."

    scene aspenroom with fade
    $ audio_crossFade(2, "music/four.ogg")
    show a with easeinright
    mc "Hey, Aspen."

    if positive["Aspen"]:
        if lock_aspen == True:
            jump romanceaspenday11
        if lock_aspen == False:
            jump p_aspenday11
    else:
        jump n_aspenday11

label romanceaspenday11:
    mc "Are you okay? You seem awfully concerned."

    show a
    a "Yeah, I'm okay, but..."
    a "There's something in the air. The plants are quiet... too quiet."

    mc "Quiet?"

    show a look
    a "Yeah. Usually they make this soft, gentle sound - you'd know if you spent all day with them..."
    a "But today... they're silent. No crying, no singing, no laughter..."
    a "Silence."

    mc "Huh."

    show a laugh
    a "They usually even sound more beautiful when you're here."
    a "They tend to like the same things I do! Haha... uh..."
    show a look
    a "But yeah. Nothing."

    mc "Is that a bad thing?"

    show a
    a "Not necessarily bad, just... interesting. I don't know."
    show a laugh
    a "It's so good to see you, though. I'm glad you came back after... yesterday, haha."
    
    mc "Why wouldn't I have come back?"

    show a look
    a "Oh, I don't know. I get worried like that."

    mc "Don't worry, Aspen. I'm not going anywhere."

    show a
    a "Good."
    show a look
    a "You should be going, though. A-As much as I'd love to keep you, you {i}are{/i} behind on schedule, haha..."

    mc "Yes, you're right, Aspen."
    mc "I hope the plants... feel better."

    show a
    a "Me too."

    mc "I'll see you tomorrow, Aspen."

    a "Same to you, Doctor. Hah."

    n "You finish your checklist on Aspen and leave the room."

    jump ccday11

label p_aspenday11:
    mc "Is everything alright in here? You seem awfully concerned."

    show a
    a "Yeah. Well, everything's physically fine, but..."
    a "There's something in the air. The plants are quiet... too quiet."

    mc "Quiet?"

    show a look
    a "Yeah. Usually they make this soft, gentle sound - you'd know if you spent all day with them..."
    a "But today... they're silent. No crying, no singing, no laughter..."
    a "Silence."

    mc "Huh."
    mc "Is that a bad thing?"

    show a
    a "Not necessarily bad, just... interesting. I don't know."
    show a laugh
    a "It's good to see you, though."
    show a
    a "I'm glad there's at least one constant in my daily routine."
    
    mc "I can imagine the stress of maintaining these plants could get to someone."

    show a look
    a "Sometimes, yeah. But I... I enjoy it regardless."

    mc "That's good, Aspen."
    show a look
    a "You should be going, though. As much as I like the company, you {i}are{/i} behind on schedule, haha..."

    mc "Yes, you're right, Aspen."
    mc "I hope the plants... feel better."

    show a
    a "Me too."

    mc "I'll see you tomorrow, Aspen."

    n "You finish your checklist on Aspen and leave the room."

    jump ccday11

label n_aspenday11:
    mc "Is everything alright in here? You seem hesitant today."

    show a look
    a "Well, there are some concerns I have about the plants..."
    show a laugh
    a "But that's completely natural. It's my whole job to be worried about them! Haha."

    show a
    mc "If you say so."

    a "Everything's pretty much fine in here, though. No issues with my systems, which is what your real concern is, anyways."

    mc "True. That is my main priority."

    show a look
    a "Since you are behind on schedule, though, you should probably get going."

    mc "Yes, you're right. I'll see you tomorrow."

    show a
    a "Thank you, Doctor."

    n "You finish your checklist and leave the greenhouse."
    jump ccday11

label ccday11:
    scene hall with fade
    n "The walk back down to the main section is uneventful."
    n "After what feels like forever, you finally reach the door to CC's room."
    n "You gently open the door."

    scene ccroom with fade
    $ audio_crossFade(2, "music/five.ogg")
    show c look with easeinright
    n "You find CC looking at you expectantly."
    c "Doctor? Where is Miss Esther?"
    mc "She didn't show up this morning. I have no idea where she is."
    c "Interesting. That's very unlike her."
    mc "That's what everyone's said so far."

    if positive["CC"]:
        if lock_cc == True:
            jump romanceccday11
        if lock_cc == False:
            jump p_ccday11
    else:
        jump n_ccday11

label romanceccday11:
    show c
    c "Regardless, it's... good to see your face."
    c "As you're well aware, it gets lonely in here. I was worried you weren't coming at all."

    mc "Nonsense. I have a job to do."
    mc "And of course, I want to see you."

    show c look
    c "I'm so glad. You are too kind to me, Doctor."

    mc "You deserve it, CC. How are you feeling today?"

    show c
    c "Terrible. The worst I've ever felt, I..."

    mc "It's hard to talk about, I understand."

    show c close
    c "Yes. I know you do."

    show c
    c "I was talking to that core, the damaged one that you apparently keep bumping into..."
    
    mc "Wasn't he in your room the other day?"

    show c look
    c "Yes. We've been talking a lot recently."
    c "Honestly, sometimes I'll sneak him in here so I have some company..."

    mc "Sounds like you guys are getting along well."
    
    show c
    c "Yes. He's kind. And he's been... trying to get better."
    
    mc "That's great to hear."
    
    show c look
    c "Isn't it?"

    show c
    c "I only wish I could say the same about myself."
    
    show c close
    c "Now... Doctor. You're very behind - I'm assuming due to Miss Esther's absence. You should be going, now."

    show c
    mc "Yes, CC, you're right. I'll see you tomorrow?"

    c "I hope so."

    n "You finish your checklist, gently touch CC on the... \"cheek\", and leave his room."

    jump robday11

label p_ccday11:
    show c look
    c "Regardless, it's good to see you. I was worried something had happened."

    mc "Well, technically something did, but... I have a job to do."

    show c
    c "Very true."

    mc "How are you feeling today?"

    c "Terrible. The worst I've ever felt, I..."

    mc "It's hard to talk about, I understand."

    show c close
    c "Yes. I know you do."

    show c
    c "I was talking to that core, the damaged one that you apparently keep bumping into..."
    
    if lock_unknown == True:
        mc "I know who you mean."
    mc "Wasn't he in your room the other day?"

    show c look
    c "Yes. We've been talking a lot recently."
    c "Honestly, sometimes I'll sneak him in here so I have some company..."

    mc "Sounds like you guys are getting along well."
    
    show c
    c "Yes. He's kind. And he's been... trying to get better."
    
    if lock_unknown == True:
        mc "It certainly looks that way. I saw him earlier. It's good for him."
    else:
        mc "That's great to hear."
    
    show c look
    c "Isn't it?"

    show c
    c "I only wish I could say the same about myself."
    
    show c close
    c "Now... Doctor. You're very behind - I'm assuming due to Miss Esther's absence. You should be going, now."

    show c
    mc "Yes, CC, you're right. I'll see you tomorrow."

    c "Yes."

    n "You finish your checklist and leave the room quietly."

    jump robday11

label n_ccday11:
    show c close
    c "You're late today - I was concerned you might not show up at all."

    show c
    mc "I still have two more days before my time here is over. I have a job to do, with my supervisor or without."

    c "Mmm. Very true, Doctor."

    mc "How are you feeling today?"

    show c close
    c "Terrible. The worst I've ever felt, I..."

    show c
    mc "No need to elaborate. That's all the information my report requires."
    mc "Oh, and CC -"

    show c close
    c "I truly hate to rush you along, but you are behind schedule, Doctor. You should be going."

    show c
    mc "Ah. Yes, you're right. Thank you, CC."

    n "You finish your checklist and leave the room quietly."

    jump robday11

label robday11:
    scene hall with fade
    mc "Almost done..."

    n "You slowly trudge your way over to the gym."

    mc "Maybe she'll have sent me an email explaining her absence tonight."

    scene robroom with fade
    $ audio_crossFade(2, "music/six.ogg")
    show r yell with easeinright
    n "Once again, Rob is yelling at the TV above him."

    r "OH, YOU'VE {i}GOT{/i} TO BE KIDDING ME. AM I THE ONLY SMART ONE HERE?"
    if persistent.streammode == True:
        r "FOR ONCE IN YOUR {k=-5}————{/k} LIFE, COACH, COULD YOU MAKE A GOOD CALL?"
    else:
        r "FOR ONCE IN YOUR GODDAMN LIFE, COACH, COULD YOU MAKE A GOOD CALL?"
    show r close
    r "Jeez..."

    show r at bounce
    r "Oh! Doc. Sorry, didn't see ya come in."
    r "I wasn't even sure you were gonna show at all! You're awfully late."
    show r angry
    r "Say, where's Miss Esther?"

    mc "Dunno. She never showed up to work."

    r "Really? Huh..."

    if positive["Rob"]:
        if lock_rob == True:
            jump romancerobday11
        if lock_rob == False:
            jump p_robday11
    else:
        jump n_robday11

label romancerobday11:
    show r
    r "Anyhow! Good to see ya, Doc."
    r "Hope you're taking care of that card I gave you."

    mc "Of course I am. I'd treasure anything you gave me."

    show r angry
    r "Aww, you flatter me."
    show r
    r "Big mistake! I love compliments."

    mc "Who doesn't?"

    r "True, true..."
    show r close
    r "But yeah. Everything's working fine in here."
    show r
    r "I ain't got any complaints."
    show r angry
    r "Other than that you aren't in here with me."

    mc "You flatter me right back, Rob."

    show r
    r "I know!"

    show r yell
    if persistent.streammode == True:
        r "HEY! CAN'T YOU FOCUS? THE BALL IS IN YOUR {k=-5}————{/k} HANDS, RUN WITH IT!"
    else:
        r "HEY! CAN'T YOU FOCUS? THE BALL IS IN YOUR GODDAMN HANDS, RUN WITH IT!"
    show r
    r "Oh shoot! It's almost 4, Doc!"

    mc "Oh God, you're right. I didn't even realize."

    show r angry
    r "You should get goin'. But hey - we'll have plenty of time this weekend, right?"

    mc "Of course."

    show r
    r "Awesome. See ya, Doc."

    n "You finally finish your checklist and head back out to your office."

    jump day11end

label p_robday11:
    show r
    r "Anyhow! Good to see ya, Doc."
    r "Everything's working fine in here. Don't got any complaints."

    mc "That's good. How's business?"

    show r angry
    r "Picking up, actually. Which is fine."
    r "It ain't the best, I can't yell as much, but it's better than being in here alone all day."

    mc "That's good, then."
    mc "Aren't you glad people are finally using these machines?"

    show r
    r "Yeah! Course I am, but -"

    show r yell
    if persistent.streammode == True:
        r "HEY! CAN'T YOU FOCUS? THE BALL IS IN YOUR {k=-5}————{/k} HANDS, RUN WITH IT!"
    else:
        r "HEY! CAN'T YOU FOCUS? THE BALL IS IN YOUR GODDAMN HANDS, RUN WITH IT!"
    show r
    r "Oh shoot! It's almost 4, Doc!"

    mc "Oh God, you're right. I didn't even realize."

    show r angry
    r "You should get goin'. Don't want you to get in trouble for going over."

    mc "Of course."

    show r
    r "See ya tomorrow, Doc."

    n "You finally finish your checklist and head back out to your office."

    jump day11end

label n_robday11:
    show r
    r "Anyhow!"
    r "Everything's working fine in here. Don't got any complaints."

    mc "How's business?"

    show r angry
    r "Picking up. It's whatever."
    r "Keeps me busy."

    mc "Are you alright? You're pretty short with me today, I -"

    show r yell
    if persistent.streammode == True:
        r "HEY! CAN'T YOU FOCUS? THE BALL IS IN YOUR {k=-5}————{/k} HANDS, RUN WITH IT!"
    else:
        r "HEY! CAN'T YOU FOCUS? THE BALL IS IN YOUR GODDAMN HANDS, RUN WITH IT!"
    show r
    r "Oh shoot! It's almost 4, Doc!"

    mc "Oh, you're right. I didn't even realize."

    show r angry
    r "You should prolly get going, huh?"

    mc "Yeah. Probably."

    show r
    r "Don't worry about anything in here. It's all working fine."
    
    mc "Roger that."

    n "You finally finish your checklist and head back out to your office."

    jump day11end

label day11end:
    scene office with fade
    n "Still no sign of Miss Esther."
    n "You sigh."

    mc "Maybe in my emails?"

    n "You sit down at your desk and leave your paperwork on top."
    n "With no one to process it, you aren't sure what to do with it..."

    jump e11first