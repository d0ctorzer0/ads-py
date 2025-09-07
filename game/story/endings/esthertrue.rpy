label END_esthertrue:
    window auto
    scene black
    with fade
    $ daynum = "DAY ???"
    $ dayday = "Aperture Laboratories"

    if renpy.is_skipping() == False:
        show screen esdaytransition
        play sound "sfx/esther.ogg"
        $ renpy.pause(2.0, hard=True)
    
    scene black with fade
    dr "Good morning, Esther."
    eold "Morning, Doctor."
    dr "You're supervising your first ever testing track today."
    eold "Yes sir."
    dr "Are you prepared? You passed your exam with flying colors."
    eold "Yes, I'm prepared. I've studied hard for this."
    dr "Good."
    scene es test3 with fade
    eold "Hello, test subject. Welcome to Testing Track X-A."
    "{shader=noise:0.07}  Miss Esther?"
    eold "I - ahem."
    eold "This first chamber involves the Aperture Science Thermal Disencouragement Beam."
    eold "This element was first introduced to Testing in the early 1970s..."
    "{shader=noise:0.07}  Miss Esther, you're -"
    eold "..."
    eold "Proceed through the track as quickly as possible. Your results will be monitored for -"
    "{shader=noise:0.07}  Are you okay?"
    eold "..."
    scene black with fade
    scene es test3 with fade
    eold "Uh... congratulations."
    eold "You've finished this... uh... you've completed this track quicker than 79.3 percent of participants."
    "{shader=noise:0.07}  You keep talking to yourself, I'm -"
    eold "Proceed through the exit door and back to the relaxation chamber."
    "{shader=noise:0.07}  I've been really worried -"
    eold "Thank you again."
    scene black with fade
    dr "Good job, Esther. Management couldn't be happier with your performance."
    eold "Thank you, sir."
    dr "{b}Hah! It was funny watching how you talk to the test subjects, though."
    eold "Sorry?"
    drs1 "{b}{shader=noise:0.005} You're so cold to them. It's like you don't care about them at all."
    eold "Cold?"
    drs2 "{b}{shader=noise:0.01} Do you even like working in Testing?"
    eold "I, uh -"
    drs2 "{b}{shader=noise:0.02} Manufacturing should've named you the \"Sociopath Core\"!\n Hah!"
    eold "..."
    mc "Miss Esther!"
    # SNAP BACK TO REALITY!
    play music deathtoaperture
    scene es apt with Dissolve(0.1)
    show e offrail shock with easeinbottom
    show e offrail shock at bounce
    e "Ahh! Doctor!"
    show e offrail sus
    e "You woke me from my charging cycle."
    mc "You were talking to yourself again."
    show e offrail look
    e "Oh... yes. I apologize. That must have been..."
    mc "I was worried. You've been doing that a lot more lately, you know."
    show e offrail sus
    e "I have?"
    mc "Yes. Nearly every night, now."
    show e offrail look
    e "I-I'm sorry, Doctor."
    mc "Talk to me. What's going on?"
    show e offrail close
    e "It's really not important. You need rest."
    mc "I... okay. But we're going to talk about this in the morning."
    show e offrail look
    e "Mm. Fine."
    mc "I'm not going to just sit here and watch you go through whatever's happening alone."
    e "I..."
    show e offrail
    e "Okay. Thank you."
    e "We'll speak about it in the morning."
    mc "Deal."

    window auto
    scene black
    with fade
    $ daynum = "65"
    $ dayday = "Home"

    if renpy.is_skipping() == False:
        show screen truedaytransition
        $ renpy.pause(2.0, hard=True)
    
    scene apt one with fade
    n "You wake up to the sun just coming over the horizon."
    n "Miss Esther is sitting quietly in her charging port."
    n "After you woke her up, she stopped talking to herself for the rest of the night..."
    n "You get up to make yourself some breakfast, letting her rest a little longer."

    scene black with fade
    scene apt one with fade

    n "Once you've finished eating, you come back to find Miss Esther already awake."
    show e offrail sus with easeinbottom
    e "Good morning, Doctor."
    mc "You know, you don't have to keep calling me that."
    e "It's habitual. I apologize."
    mc "How are you feeling?"
    show e offrail look
    e "Better, I suppose. The rest of the night was... calm."
    n "You pick her up and set her on the bed beside you."
    mc "So. Talk to me. What's going on?"
    show e offrail
    e "I..."
    show e offrail look
    e "Well, I'm sure you're well aware that personality constructs are built with..."
    e "Certain... features that allow us to... {i}\"dream\",{/i} in a sense, yes?"
    if wcd3 == True:
        mc "Yes. I believe CC told me about that, once."
        show e offrail
        e "Oh? He did often tell me about the dreams he used to have..."
    else:
        mc "No, actually, I didn't know that."
        show e offrail
        e "Oh! Well, we can... visualize things, I suppose... they're different than human dreams, as far as I'm aware, but..."
        e "The concept remains basically the same."
    show e offrail look
    e "I've been having... {i}dreams,{/i} lately, about... Aperture."
    e "And... when I was first activated, and..."
    e "The early years of my life."
    mc "You mean when you used to work in Testing?"
    show e offrail
    e "Yes, that time."
    show e offrail sus
    e "I... it's uncomfortable to think about."
    mc "Why's that?"
    show e offrail close
    e "I was never the most... {i}pleasant{/i} Test Supervisor."
    e "They... they used to joke, you know. I've told you this, yes?"
    show e offrail sus
    e "\"Sociopath Core.\""
    mc "You have mentioned that, yes."
    show e offrail look
    e "I-It was a joke, and I'm... well aware of that fact, but..."
    e "It still stings, regardless."
    mc "I'm sure."
    show e offrail close
    e "I-I just don't understand why I can't... why I'm so..."
    show e offrail sus
    e "So {i}mean.{/i}"
    show e offrail look
    e "Every time I use my voicebox simulator, it's like I can never say what I want to..."
    show e offrail close
    e "I sigh involuntarily. I groan at the slightest inconvenience. I'm... not..."
    show e offrail
    e "It's like I {i}want{/i} everyone to hate me, and I don't know {i}why.{/i}"
    e "Does... is this making any sense?"
    mc "You're doing just fine, Miss Esther."
    mc "Thank you for telling me this. I think..."
    mc "I think this was important for me to know."
    mc "As your friend."
    show e offrail look
    e "There you go again, calling us \"friends\"..."
    mc "We are friends, whether you like it or not."

    window auto
    scene black
    with fade
    stop music
    $ daynum = "{shader=noise:0.01} DAY ???"
    $ dayday = "{shader=noise:0.01} Aperture Laboratories"

    if renpy.is_skipping() == False:
        show screen esdaytransition
        play sound "sfx/esther.ogg"
        $ renpy.pause(2.0, hard=True)
    
    scene black with fade
    dr "Esther - we'll be moving you to the new surface tracks tomorrow."
    eold "Surface tracks?"
    dr "Some of our researchers think keeping the test subjects inside all the time might be affecting test results."
    eold "Why would that matter? The tests are the same regardless."
    dr "Well, exposure to the outside world is important to mental health."
    dr "{shader=noise:0.005}Being a robot probably makes that hard to understand."
    eold "Yes..."

    scene black with fade
    eold "Ahem. Welcome to Surface Track E-2."
    eold "In addition to normal testing procedure, we'll also be monitoring your emotional and mental well-being via the\nchip we implanted in your brain."
    eold "Proceed through the chamber as quickly as possible."
    drs2 "{shader=noise:0.05} Sociopath Core..."
    eold "Uh... please. And thank you."
    scene black with fade

    eold "Congratulations, test subject, on completing this assignment."
    eold "Proceed... uh, {i}please{/i} proceed to the exit elevators in a timely manner."
    eold "T-Thank you for your cooperation."

    window auto
    scene black
    with fade
    play music deathtoaperture
    $ daynum = "66"
    $ dayday = "Home"

    if renpy.is_skipping() == False:
        show screen truedaytransition
        $ renpy.pause(2.0, hard=True)
    
    scene apt one with fade
    mc "Good morning, Miss Esther."
    show e offrail with easeinbottom
    e "Morning."
    mc "I've got a surprise for you today."
    show e offrail sus
    e "I'm not the biggest fan of surprises, you know."
    mc "I think you'll enjoy this one."
    show e offrail
    mc "It'll be a {i}bit{/i} of a trip, though. I hope you can bear with me."
    show e offrail look
    e "I've dealt with you this long..."

    scene black with fade
    scene det car with fade
    n "The car rumbles gently underneath you."
    show e offrail close with easeinbottom
    n "Miss Esther is in the passenger seat, optic closed and silent."
    n "You've learned over the past two months that she only really {i}sleeps{/i} when she's charging..."
    n "...which means, even if she may not look it, you know she's wide awake."
    n "You decide to let her be a little longer."
    n "The last couple of months with her have been... interesting."
    n "Some days she'll be almost violent, other days she'll be deathly quiet."
    n "Just like when the two of you were in Aperture, her mood seems to flip on a dime..."
    n "But in addition to that, you've learned to see behind the front she puts on."
    n "You're hoping what you're about to show her will give her some..."
    n "...perspective."

    window auto
    scene black
    with fade
    stop music
    $ daynum = "{shader=noise:0.03} DAY ???"
    $ dayday = "{shader=noise:0.03} Aperture Laboratories"

    if renpy.is_skipping() == False:
        show screen esdaytransition
        play sound "sfx/esther.ogg"
        $ renpy.pause(2.0, hard=True)
    
    dr "Esther. We're moving you downstairs."
    eold "Down... downstairs? To a different testing track again?"
    dr "No. We've... decided to move you to a different department."
    dr "One where you'll be less... available to human interaction."
    eold "I-Is... did something happen? Did I do something wrong?"
    dr "We've tried to be patient, but... we've waited nearly 5 years, now."
    dr "You know, Management's been putting more of an emphasis on employee morale lately since Mr. Johnson passed, and..."
    dr "{shader=noise:0.01} You're just not... beneficial to that... ideal."
    eold "Y-You mean..."
    drs1 "{shader=noise:0.015} We'll be moving you down to Maintenance in the following\n weeks."
    drs2 "{shader=noise:0.015} Management thinks you'll be better suited for a... team\n environment."
    eold "But I... I can do better, I can..."
    drs2 "{shader=noise:0.015} Sorry, Esther. You just don't have the... {i}attitude{/i} they want up\n here."
    eold "Wait!"

    play music deathtoaperture
    scene det car with Dissolve(0.1)
    show e offrail close with easeinbottom
    show e offrail sus at bounce
    e "Doctor..."
    mc "Oh, Miss Esther. We're almost there."
    show e offrail
    e "Where are we going?"
    mc "Patience, and you'll see."
    show e offrail look
    e "This better be good..."

    scene black with fade
    scene es trail with fade
    n "You carry Miss Esther on your hip, attached to your shoulder with a strap."
    n "You cobbled this... contraption together using an old seatbelt and a tote bag."
    n "It works well, but it doesn't negate her weight."

    show e offrail with easeinbottom
    e "You know, Doctor..."
    e "Being outside, the {i}size{/i} of this place..."
    show e offrail look
    e "Aperture was huge, the largest facility in America, as far as I'm aware, but..."
    show e offrail
    e "This sky goes on {i}infinitely{/i}..."

    mc "You got used to it fairly quickly."

    show e offrail close
    e "I'm great at adaptation, Doctor."
    show e offrail

    n "You adjust your weight to hold Miss Esther a little higher."

    mc "Carrying my former supervisor up a mountain..."
    mc "Now that's something I never thought I'd do."

    scene black with fade
    scene black with fade

    $ daynum = "???"
    $ dayday = "Section C8"

    if renpy.is_skipping() == False:
        show screen truedaytransition
        $ renpy.pause(2.0, hard=True)
    
    dr "Here you are, Esther. Section C8. You'll be in charge of this place for a while."
    dr "The maintenance employee will be here shortly. Make sure to introduce yourself."
    drs1 "{shader=noise:0.015}Oh, and... try not to make any new enemies."
    eold "Yeah..."
    scene black with fade
    eold "Hello. I'm Es-"
    e "Ahem. {i}Miss{/i} Esther. I'll be your supervisor here in Maintenance for the foreseeable future."
    e "You're... Thomas, correct?"
    e "{cps=15}I hope we can be..."
    e "I hope we can be...{fast} {i}good friends.{/i}"

    scene es trail with Dissolve (0.5)
    show e offrail with easeinbottom

    mc "Alright, Miss Esther. We're almost at the summit."

    show e offrail sus
    e "The summit?"
    e "Where are you {i}taking{/i} me?"
    mc "Just you wait."

    scene black with fade

    scene es overlook with fade
    show e offrail shock with easeinbottom
    n "Finally, you reach the summit, exhausted."
    n "You hold Miss Esther up to look at the skyline."
    n "It goes on for acres, spreading across swaths of trees and brush, and in the distance, Lake Michigan can be seen."
    n "It makes you feel small."
    n "It gives you..."
    e "Oh my god..."

    $ cutscenetextbox = True
    show screen cuttextbox
    scene esther cutscene 5 with fade
    python:
        if persistent.ec5 == False:
            persistent.cutscenes_seen += 1
            persistent.ec5 = True
        if persistent.cutscenes_seen == cutscene_count:
            achievement.grant("ach_picture")
            achievement.sync()
    e "{color=#fff}Doctor... what {i}is{/i } this place?"
    mccut "{color=#fff}We're at Mount Arvon. Highest point in Michigan."
    e "{color=#fff}It's... oh my god, it goes on forever..."
    e "{color=#fff}It makes me feel..."
    mccut "{color=#fff}Small?"
    e "{color=#fff}Haha! Something like that, I..."
    e "{color=#fff}I can't believe I'm here right now..."
    e "{color=#fff}The expanses in Aperture, the voids between testing tracks, they faded into fog quickly..."
    e "{color=#fff}You could never see everything. Not like this."
    e "{color=#fff}I can see trees hundreds of acres away! This is... this is crazy!"
    e "{color=#fff}I..."
    e "{color=#fff}The outside... it's so... {i}huge.{/i}"
    e "{color=#fff}There's so much here outside of myself, I..."
    e "{color=#fff}I've been so... so {i}selfish.{/i}."
    e "{color=#fff}I don't think I've ever really thanked you for getting me out of that hellhole."
    e "{color=#fff}Isn't that... that's ridiculous, right?"
    e "{color=#fff}I should be..."
    e "{color=#fff}Oh, Doctor."
    e "{color=#fff}I... I want to see more like this, I want to..."
    e "{color=#fff}I feel so {i}stuck.{/i} Inside the house, inside myself, inside..."
    e "{color=#fff}But here. Right now. I feel..."
    e "{color=#fff}I feel..."
    e "{color=#fff}{i}Happy."
    e "{color=#fff}A-And not a manufactured happiness, not a..."
    n "{color=#fff}She sighs, looking out over the horizon."
    e "{color=#fff}Thank you. You're..."
    e "{color=#fff}You've opened doors for me I never thought possible."
    e "{color=#fff}You've been... patient. More than anyone has ever been with me before."
    e "{color=#fff}I wish I could've seen it earlier."
    e "{color=#fff}I..."
    mccut "{color=#fff}It's okay, Miss Esther."
    e "{color=#fff}Please."
    eold "{color=#fff}Call me Esther."
    window auto
    hide screen cuttextbox
    scene black with fade
    $ cutscenetextbox = False
    $ renpy.pause(2.0, hard=True)

    stop music fadeout 2.0
    window hide
    show screen creditsfadeout with fade
    $ renpy.pause(2.0, hard=True)
    hide screen creditsfadeout
    python:
        persistent.endings_got["true"] = True
        if sum(persistent.endings_got.values()) == ending_count:
            achievement.grant("ach_seenitall")
        achievement.grant("ach_true")
        achievement.sync()
    $ renpy.movie_cutscene("ENDCREDIT_esther.webm")
    $ MainMenu(confirm=False)()