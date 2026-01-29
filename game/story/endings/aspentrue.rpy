label END_aspentrue:
    window auto
    scene black
    with fade
    $ daynum = "49"
    $ dayday = "On the road..."

    if renpy.is_skipping() == False:
        show screen truedaytransition
        $ renpy.pause(2.0, hard=True)
    
    scene black with fade
    play music deathtoaperture
    n "The car is quiet - just the way the two of you like it."
    n "The radio's off."
    n "The only sounds are the gentle whirring of the car engine and the wind passing by the windows."
    n "The scenery changes from wheat fields to forest and back again."
    n "The sun shines through an overcast sky."
    n "You pass by a sign -"
    n "UNIVERSITY OF MICHIGAN - 5 MILES"
    a "University? What are we going to a university for?"
    mc "Well, it's not really the uni we're going to..."
    a "You're really good at keeping secrets."
    mc "I think you're just a little dense."
    a "Hey!"
    a "You're not wrong, haha..."
    n "The car goes quiet again, but you don't mind it."
    n "You've learned over the past few weeks that Aspen tends to be very quiet unless there's plants nearby -"
    n "- in which case they'll gladly talk for hours."
    n "You chuckle to yourself. They'll be very talkative today for sure."

    scene black with fade
    $ renpy.pause(2.0, hard=True)
    n "You pull into the lot and put the car into park."
    mc "You ready?"
    show a look offrail with easeinbottom
    a "I think so. I still don't know what's happening, though."
    a "Hard to prepare for something I don't know anything about..."
    n "You laugh."
    mc "Oh, you're ready."
    n "You pick up your tote bag from the backseat."
    mc "I'm going to pick you up now, alright?"
    show a offrail
    a "A-Alright."
    n "You gently scoop your hands underneath Aspen's chassis and lift them up and into the tote bag."
    mc "Snug, I hope?"
    show a look offrail
    a "Yeah. I'm still not used to it, but what can you do? Haha."
    mc "Perfect."
    scene mat entrance with fade
    n "You walk up to the entrance."
    mc "Aspen - why don't you read that sign next to us?"
    show a left offrail with easeinbottom
    a "Matthaei... Botanical..."
    show a offrail
    a "Oh my goodness! The Matthaei Botanical Gardens!"
    a "I've heard about these - they're the closest gardens to Aperture!"
    show a look offrail
    a "Or... the closest to where Aperture used to be, haha..."
    show a offrail
    a "I can't believe I'm actually here!"
    a "They have so many different species here... so many different types of plants... I..."
    show a left offrail
    show aspen blush with Dissolve(0.05)
    a "Oh wow. Thank you. I-I don't even know what to say."
    mc "You're welcome, Aspen."
    mc "I've been wanting to take you here for a while now."
    hide aspen blush
    show a offrail
    a "You know me so well."
    mc "I certainly hope I do."

    scene mat two with fade
    n "The gardens are beautiful - brightly-colored flowers spot the landscape of dark green bushes and trees." 
    show a offrail with easeinbottom
    n "Aspen is enthralled, completely in their element."
    a "Morning glories! I believe this one's specifically {i}Ipomoea nil...{/i}"
    a "And flowering tobacco! {i}Nicotiana alata!{/i}"
    show a left offrail
    a "Oh wow... they never brought any of these down into my greenhouse."
    a "We had very few flowers... mostly ferns and bushes."
    mc "About that..."
    mc "I'm sorry we couldn't save Penelope, Aspen."
    a "Yes... I know."
    a "It's okay."
    show a offrail
    a "Besides... I got out of there thanks to you."
    a "You saved me. I couldn't have gotten out alone."
    a "You sacrificed so much for me."
    show a look offrail
    a "And you brought me here. To this beautiful place."
    a "I loved my job in Aperture. I loved the plants I cared for."
    a "But Aperture... didn't care for me very much."
    show a offrail
    a "You probably know this, but I never got a break."
    a "I would spend 2 hours per night in my charging port at the back of the greenhouse..."
    a "...then wake up and water the plants the entire day."
    a "And as much as I loved it..."
    show a left offrail
    a "I was so, so tired."
    a "Thanks to you, though, I get to enjoy this freely..."
    a "And I get to spend my time with my favorite human ever."
    mc "You're so sweet, Aspen."
    show a look offrail
    show aspen blush with Dissolve(0.05)
    a "Ah... ahaha... sorry. I may have gotten a little sappy there."
    mc "I love it when you talk like that."
    a "Y-You can stop now. Your compliments overheat my systems too much."

    scene mat one with fade
    show a offrail with easeinbottom
    a "Wow..."
    a "{i}Allium schoenoprasum!{/i}"
    a "These are chives! Like the ones humans use for cooking!"
    show a left offrail
    a "Sometimes I wish I could smell them... or taste them!"
    a "But they're pretty just to look at."
    a "It's pretty crazy how much botany relies on scent..."
    show a look offrail
    a "Made my job harder sometimes! Hah... haha..."
    a "Glad I wasn't one of the scientists."
    mc "How were your coworkers, anyway?"
    show a offrail
    a "Well... the greenhouse supervisor, Dr. Olive... she was nice."
    a "I think she was one of the only people there who actually cared about me."
    show a look offrail
    a "She only really worked {i}inside{/i} the greenhouse once or twice a week..."
    a "Most of her time was spent overseeing plant testing, haha."
    show a offrail
    a "We had a few nanobots on staff as well. Usually in the pipes, making sure the water pressure levels were consistent."
    a "It was a small team! But hardworking."
    show a left offrail
    a "They just... didn't supply us with enough people to... supplement for me."
    a "Hence my lack of breaks."
    mc "I'm sorry, Aspen. That sounds difficult."
    a "It was, but..."
    show a offrail
    a "Hey! {i}Zinnia elegans{/i}!"
    n "The next few hours is spent listening to Aspen reciting botany facts."
    n "Thankfully, the garden is relatively empty, so Aspen spends most of the day out of their tote bag."
    n "Slowly, the two of you make your way over to the garden's sprawling trails."
    
    scene mat trail with fade
    show a left offrail
    a "It feels like we've been here for hours!"
    mc "Probably because we have been, Aspen."
    show a look offrail
    a "Oh... I didn't even realize."
    mc "You were too busy enjoying yourself to realize, Aspen."
    mc "There's a human phrase - time flies when you're having fun."
    show a offrail
    a "I am having fun."
    mc "I'm glad."
    show a left offrail
    show aspen blush with Dissolve(0.05)
    n "Suddenly, Aspen looks away from you, down at the wood-paneled trail you're currently walking."
    mc "Is something wrong?"
    a "N-No. Nothing. I just..."
    show a look offrail
    a "I-I'm just so lucky to have you."
    a "Can you imagine if you had never taken that maintenance position?"
    a "I would've... I probably would've..."
    n "They take a deep breath."
    a "I would've died down there."
    a "A-And I would've never experienced all of... this."
    hide aspen blush
    show a offrail
    a "I just don't think I thank you enough."
    a "You're... so kind to me."
    mc "Aspen..."
    a "Yes?"
    mc "You're rambling again."
    show a look offrail
    a "O-Oh! I'm so sorry! I... I really didn't mean to, I'm..."
    mc "No. I like it, remember?"
    mc "It's my favorite thing about you."
    mc "How passionate you get. How excitable you are."
    a "I..."
    show a offrail
    a "I-I really love you, you know."
    menu:
        extend ""
        "You're so sweet.":
            pass
        "I love you too.":
            show a left offrail
            show aspen blush with Dissolve(0.05)
            a "O-Oh. I didn't expect..."
            a "I didn't think you were going to say it back, haha..."
            mc "Why wouldn't I?"
            a "I... I don't know, I just..."
            a "Wow."
    
    scene black with fade
    scene mat trail with fade
    show a offrail with easeinbottom
    mc "You know, you haven't called me Doctor since we left."
    if name.lower() == 'dr. rowan':
        a "Would you prefer I call you... Rowan?"
    elif name.lower() == 'dr. cait':
        a "Would you prefer I call you... Cait?"
    elif name.lower() == 'ross':
        a "Would you prefer I call you... Ross?"
    elif name.lower() == 'avery':
        a "Would you prefer I call you... Avery?"
    elif name.lower() == 'hazel':
        a "Would you prefer I call you... Hazel?"
    elif name.lower() == 'len':
        a "Would you prefer I call you... Len?"
    elif name.lower() == 'evelyn':
        a "Would you prefer I call you... Evelyn?"
    elif name.lower() == 'lynne':
        a "Would you prefer I call you... Lynne?"
    elif name.lower() == 'mo':
        a "Would you prefer I call you... Mo?"
    elif name.lower() == 'bemb':
        a "Would you prefer I call you... Bemb?"
    elif name.lower() == 'unny':
        a "Would you prefer I call you... Unny?"
    elif name.lower() == 'cass':
        a "Would you prefer I call you... Cass?"
    elif name.lower() == 'tyler':
        a "Would you prefer I call you... Tyler?"
    elif name.lower() == 'john':
        a "Would you prefer I call you... John?"
    elif name.lower() == 'brian':
        a "Would you prefer I call you... Brian?"
    elif name.lower() == 'caz':
        a "Would you prefer I call you... Caz?"
    elif name.lower() == 'izzy':
        a "Would you prefer I call you... Izzy?"
    else:
        jump END_aspentrue2
    n "You laugh."
    mc "Haha. Maybe."
    show a look offrail
    a "That was so embarrassing."
    mc "On the contrary. I thought it was cute."
    a "Stop."
    jump END_aspentrue2

label END_aspentrue2:
    show a offrail
    a "Wait!"
    a "Look at those daisies, just off the path!"
    show a look offrail
    a "Do you think we can... go over there?"
    mc "I don't see why not."
    $ cutscenetextbox = True
    show screen cuttextbox
    scene aspen cutscene 6 with fade
    python:
        if persistent.ac6 == False:
            persistent.cutscenes_seen += 1
            persistent.ac6 = True
    if persistent.cutscenes_seen == cutscene_count and persistent.ach_picture == False:
        python:
            achievement.grant("ach_picture")
            achievement.sync()
            persistent.ach_picture = True
            ach_name = "picture"
        show screen ach_popup with easeinbottom
    n "{color=#fff}You set Aspen down in the daisy patch and lay down next to them."
    acg "{color=#fff}Oh wow... the sun's already starting to set..."
    acg "{color=#fff}It's so beautiful."
    acg "{color=#fff}Today's been perfect."
    acg "{color=#fff}You've..."
    acg "{color=#fff}You've been perfect."
    mc "{color=#fff}I hope I can keep that stellar reputation up."
    acg "{color=#fff}I-I'm sure you will."
    acg "{color=#fff}You're so... you're so kind to me."
    acg "{color=#fff}So gentle."
    acg "{color=#fff}Something a lot of people back in Aperture... weren't."
    acg "{color=#fff}I was so lonely in there."
    acg "{color=#fff}Not being able to leave the greenhouse... stuck in that one room my entire life..."
    acg "{color=#fff}I-It really got to me sometimes."
    acg "{color=#fff}And now I get to look up at the sky..."
    acg "{color=#fff}And it feels like I could fall up into it any second!"
    acg "{color=#fff}I-It's crazy!"
    acg "{color=#fff}I wake up every morning next to you and every morning I'm amazed all over again."
    mc "{color=#fff}You haven't even seen the half of it, Aspen."
    acg "{color=#fff}I hope you'll show me everything."
    acg "{color=#fff}I want to see everything."
    mc "{color=#fff}I want to show you everything."
    acg "{color=#fff}I love you."
    acg "{color=#fff}This..."
    acg "{color=#fff}This is perfect."
    stop music fadeout 2.0
    window hide
    show screen creditsfadeout with fade
    $ renpy.pause(2.0, hard=True)
    hide screen creditsfadeout
    python:
        persistent.endings_got["aspentrue"] = True
        if sum(persistent.endings_got.values()) == ending_count:
            achievement.grant("ach_seenitall")
        if all_achievements_unlocked():
            achievement.grant("ach_lore")
        if persistent.endings_got["kristrue"] and persistent.endings_got["heathtrue"] and persistent.endings_got["aspentrue"] and persistent.endings_got["cctrue"] and persistent.endings_got["robtrue"] and persistent.endings_got["gregtrue"] and persistent.endings_got["unknowntrue"]:
            achievement.grant("ach_ultrobo")
        achievement.grant("ach_aspentrue")
        achievement.sync()
    $ renpy.movie_cutscene("ENDCREDIT_aspen.webm")
    $ MainMenu(confirm=False)()