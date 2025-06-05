label day11:
    $ audio_crossFade(2, "music/fourteen.ogg")
    scene mctemproom with fade
    n "You enter your chambers once more."
    if lock_kris:
        mc "Well... Kris certainly gave me a run for my money today... haha!"
    elif lock_heath:
        mc "I wonder where Heath got that dove from... haha."
    elif lock_aspen:
        n "You place the cactus Aspen gave you, [cactusname], beside your \"bed\"."
        n "The flowers look as bright as ever."
    elif lock_cc:
        mc "I never expected CC to recite poetry to me..."
    elif lock_rob:
        n "You place your Topps baseball card by your \"bed\"."
        mc "It's honestly a little shocking he would give this to me... haha."
    else:
        n "A fairly... normal day, all things considered."
    n "Throwing your paperwork down for the day, you sigh."
    n "You lay down in your stasis chamber for the night."

    scene black
    with fade
    $ daynum = "11"
    $ dayday = "Thursday"

    if renpy.is_skipping() == False:
        show screen daytransition
        $ renpy.pause(2.0, hard=True)
    if renpy.is_skipping() == True:
        pass

    scene mctemproom
    with fade

    n "You wake up at 7:30, more ready for the day than ever."
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
    scene kristemproom with fade
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
    if positive["Kris"] == 0:
        if lock_kris == True:
            jump romancekrisday11
        if lock_kris == False:
            jump p_krisday11
    if positive["Kris"] == -1:
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
    k "You do have paperwork to turn in still, after all."

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
    k "You do have paperwork to turn in still, after all."

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
    scene heathtemproom with fade
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

    if positive["Heath"] == 0:
        if lock_heath == True:
            jump romanceheathday11
        if lock_heath == False:
            jump p_heathday11
    if positive["Heath"] == -1:
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
    scene temphall with fade
    n "The walk up to the greenhouse is incredibly long and boring."

    # if lock_kris and lock_aspen and lock_cc and lock_heath and lock_rob == False:
    #     if romance_points["???"] == romance_points["Greg"]:
    #         $ day11lock_randomizer = renpy.random.choice(['???', 'Greg'])
    #         if day11lock_randomizer == "Greg":
    #             jump gregday11
    #         elif day11lock_randomizer == "???":
    #             jump unknownday11

    if romance_points["???"] < romance_points["Greg"]:
        jump gregday11
    elif romance_points["???"] > romance_points["Greg"]:
        jump unknownday11
    else:
        jump aspenday11

label gregday11:
    n "Suddenly, you hear a familiar sound - weighed-down wheels."
    $ audio_crossFade(2, "music/seven.ogg")
    show g aaa
    n "Gregory comes around the corner and nearly runs into you."
    g "Doctor! O-Oh. Hi!"

    mc "Gregory? What are you doing down here?"

    show g look
    g "I was just on my way to see Kris - there's a... a meeting in his conference room. They ran out of space upstairs."
    g "So I have to go get it ready."

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

    $ cutscenechoice = True
    show screen cuttextbox
    scene greg cutscene 3 with fade
    $ cutscenetextbox = True
    $ persistent.gc2 = True
    n "Gregory moves his bottom handle slightly, unbuttoning his trench coat. It falls to the ground."
    n "What stands before you is not a personality core - but three of them, just as you thought."
    n "The top one - Gregory's voice, you assume - looks down nervously at the other two."
    n "The middle one looks up at you curiously, and the bottom one glares at you in turn."

    g "I-I'm not... really... a personality core. I'm... three of them."
    g "I know I've been trying to hide it, and this is really difficult - no one knows this but my creators, and..."
    g "I figured you should know the truth before I ask you to accept me any further."

    mc "Accept you?"

    g "Well, Doctor... we... have constantly been running into you, and... you treat me - uh, us so well."
    g "No one's done that for us before."
    g "I don't want you to think we're weird, or awkward, but..."
    g "Can you give me a chance? To be closer to you?"

    menu:
        extend ""
        "I'll accept you no matter what.":
            g "Oh, Doctor... I..."
            g "Thank you. So much."
            jump gregacceptance
        "This is too weird for me.":
            jump gregrejection

label gregacceptance:
    $ cutscenechoice = False
    hide screen cuttextbox
    scene temphall with fade
    $ cutscenetextbox = False
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
    g "I - the one with the yellow eye - I do most of the talking. And appearing, of course."
    g "The one right below me - it does a lot of the thinking. Since we're really small physically, we don't have as much processing power..."
    show g nocoataaa
    g "We gotta divide our jobs, y'know?"

    mc "And the bottom one?"

    show g nocoat
    g "It controls the movement - the cart we're on, and our handles, our eyes..."

    show g nocoatlook
    g "But we can't be separated. From what I know. We'd be incomplete, we'd..."
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

label unknownday11:
    "endtest_???"