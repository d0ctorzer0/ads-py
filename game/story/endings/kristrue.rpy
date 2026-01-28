label END_kristrue:
    window auto
    scene black
    with fade
    $ renpy.pause(2.0, hard=True)
    $ daynum = "47"
    $ dayday = "New York City, Evening"

    if renpy.is_skipping() == False:
        show screen truedaytransition
        $ renpy.pause(2.0, hard=True)

    scene nyc with fade
    play music deathtoaperture
    n "You step off the transit and take a deep breath." 
    n "It's loud. The air is bustling with the noise of cars, people, and footsteps."
    n "It's crowded."
    n "You clutch your luggage closer to you."
    mc "Wait just a second - we're almost there."
    n "You check your map - the hotel is just a few blocks away." 
    n "You hurriedly start down the street, pushing past people on their way home from work."
    n "You've never been to New York before. It's certainly something."
    mc "Might have to check out Times Square if we can."
    n "Eventually, you come up on your hotel."
    n "You enter."
    scene nyc hotel front with fade 
    mc "I have a reservation for one for [name]."
    dc "Ah yes, I see you right here. Give me just a sec..."
    n "After some brief formalities, the desk clerk hands you your room key."
    dc "Checkout time is 11am on the 5th. If you need an extension, just call the front desk."
    mc "Thank you."
    n "You head up to your room."
    scene nyc hotel with fade
    n "Carefully closing the door behind you, you lay your luggage on the single bed."
    mc "Okay. I think we're good now. You ready?"
    n "A muffled voice comes through your suitcase -"
    k "Ugh. I would never, EVER do this under any other circumstances..."
    mc "I know, I know. I didn't really have a choice, though."
    k "I'm surprised I wasn't too heavy..."
    n "You unzip the suitcase and pull Kris out, dusting off his chassis."
    show k sus offrail with easeinbottom
    k "Mmm. I'm not scuffed, am I?"
    mc "Just a bit. Nothing we can't polish out."
    show k offrail
    k "You're sweet."
    n "He looks around the room."
    k "This is a lot different from your apartment..."
    mc "Our apartment, Kris."
    show k look offrail
    k "Yes. I keep forgetting. Apologies. {i}Our{/i} apartment."
    k "New York City, huh? Or, at least, that's what the gate attendant said..."
    mc "Yes, New York. The Big Apple."
    show k offrail
    k "The city of business, they say. One of our shareholders back at Aperture was from New York. He was very... arrogant."
    mc "That tends to be the case. And you're one to talk."
    show k look offrail
    k "Me? Arrogant? Why, I'm the picture of humility."
    mc "Are you aware you have somewhat of a... superiority complex?"
    show k sus offrail
    k "Complex? I find my superiority quite simple."
    mc "Oh, hush."
    show k offrail
    k "Whatever you say, sweetheart."
    n "You lay down on the bed next to Kris." 
    show k offrail
    k "Where are you taking me, anyway?"
    mc "Like I said, that's a secret."
    show k look offrail
    k "Oh, you're no fun."
    mc "You know, we'll have to be careful out there, Kris."
    mc "I may have been able to buff off that Aperture logo you had on you, but you're still pretty high-tech property."
    show k offrail
    k "I know, I know. I'm just so unique and spectacular that I'll draw attention if I'm not careful..."
    mc "Sure. Let's go with that."
    mc "Most people in New York don't really care, though. Too busy with their own stuff to notice."
    mc "If anyone asks, though, just play dead. I'll say you're a prop from some obscure TV show."
    show k sus offrail
    k "A prop?! Well then. I think I'm definitely more to you than that."
    mc "Of course you are."
    show k offrail
    k "So... are we going anywhere today?"
    mc "Pfft. No. I'm exhausted from the flight. Maybe we can order dinner or something..."
    k "Fair enough. You should rest."
    mc "Tomorrow you'll see why we flew all the way out here."
    k "I'm excited."
    k "Although..."
    show k look offrail
    show kris blush with Dissolve(0.1)
    k "Going anywhere with you is exciting."
    hide kris blush
    mc "You're such a flirt, Kris."
    show k offrail
    k "You love it."

    scene black
    with fade
    $ daynum = "48"
    $ dayday = "New York City, Morning"

    if renpy.is_skipping() == False:
        show screen truedaytransition
        $ renpy.pause(2.0, hard=True)

    scene nyc hotel with fade
    show k sus offrail with easeinbottom
    k "Mmm. Good morning."
    mc "Good morning, Kris."
    show k offrail
    k "Rest well?"
    mc "Yes, thank you. Next time, though, maybe don't roll onto my leg halfway through the night?"
    show k look offrail
    k "Sorry about that."
    mc "You're heavier than you think you are."
    show k offrail
    k "That just means there's more of me to love."
    show k sus offrail
    k "So... where are we going?"
    mc "Oh, shush. Patience is a virtue, you know."
    k "Fine."
    n "You get up off the bed and get dressed."
    show k look offrail
    n "Kris looks away from you diligently."
    mc "Such a gentleman." 
    k "I try to be."
    n "Once dressed, you grab your bag from the corner."
    show k offrail
    mc "Alright. Let's go."
    n "You pick Kris up gently and tuck him under your shoulder, against your waist."
    show k sus offrail
    n "You click a small button on your bag, revealing a thick strap attached to it."
    n "You wrap it around Kris and click it back into place behind your back."
    show k offrail
    mc "Secure?"
    k "Secure."
    mc "Perfect."
    n "You grab your room key and head out into the big city."

    scene black with fade
    "The trains are busy once more."
    k "I suppose this is what we get for taking our vacation on a weekend..."
    "Thankfully, Kris' size gives the two of you quite a bit of space."
    k "Can I know where we're going yet?"
    mc "No. We're almost there, anyway."
    mc "You used to stare at a screen for 12 hours a day. Where's that patience now?"
    n "Kris mumbles to himself, but doesn't say anything more."
    n "Eventually, the train reaches the station you're looking for."
    mc "We're here, Kris. Are you ready?"
    k "Am I ever."
    n "You step off the train and face the thing you came here to show him -"
    scene nyc wall street with fade
    n "Wall Street."
    show k sus offrail with easeinbottom
    k "You wouldn't -"
    show k offrail
    k "{fast}- oh, you did."
    k "This is... this is Wall Street, isn't it?"
    k "The heart of all things finance."
    mc "You bet it is."
    show k look offrail
    show kris blush with Dissolve(0.05)
    k "I can't believe you flew us all the way out to New York... just to show me this."
    k "What a generous gift."
    hide kris blush
    show k offrail
    n "You walk down the street slowly, letting Kris twist in your arm to see everything around him."
    k "I've only ever seen the stock market from afar."
    show k sus offrail
    k "It feels so... so strange to be here, so far from Aperture, so far from that screen I dedicated so much of my life to..."
    show k look offrail
    k "I'm in the middle of it now. This is where it all happens."
    show k offrail
    k "Wow."
    n "You approach a big building with columns and statues adorning its roof."
    n "American flags decorate the top, and four golden words adorn its face: NEW YORK STOCK EXCHANGE."
    show k happy offrail
    k "This is it! Haha, this is {i}the{/i} building, this - oh, wow."
    k "One of the oldest and largest stock exchanges in the world! And I'm right here outside of it."
    mc "You're really gonna love the next bit, then."
    show k sus offrail
    k "W-What do you mean?"
    mc "Well. Yours truly got us tour tickets to see the actual trading floor."
    k "Wh - no you didn't, haha. You're pulling my... uh, leg."
    mc "I'm not messing with you, Kris."
    show k offrail
    mc "It took some string pulling and a little bit of cash, but I managed to get us a sneak peek inside."
    k "You're just one surprise after the other."
    show k happy offrail
    k "God, I love you."
    scene nyc trade with fade
    tg "And here we are, ladies and gentlemen - the New York Stock Exchange trading floor."
    tg "You may notice it looks quite hectic down there! And you'd be right - trading isn't easy, and it's often a very fast-paced job."
    n "You lean down to your side slightly, keeping your voice low."
    mc "Can you see alright?"
    k "A little higher?"
    show k sus offrail with easeinbottom
    "You lift yourself up slightly."
    show k offrail
    k "Oh wow."
    mc "I personally don't think I'd survive down there. Too many people. Too much chaos."
    k "Looks like my cup of tea."
    mc "You're crazy."
    show k look offrail
    k "Maybe a little."
    k "..."
    k "Thank you."
    mc "Hm?"
    show kris blush with Dissolve(0.05)
    k "For doing this for me."
    k "For... being here for me."
    k "I love you."
    mc "I..."
    menu:
        extend ""
        "Thank you, Kris.":
            hide kris blush
            show k offrail
            k "I hope we can make a lot more memories together."
            mc "We will."
            jump END_kristrue2
        "I love you too.":
            hide kris blush
            show k happy offrail
            k "Oh, you finally said it, did you?"
            mc "I've been thinking it for a while."
            show k offrail
            k "You're stubborn."
            mc "So are you."
            jump END_kristrue2

label END_kristrue2:
    scene black with fade
    $ renpy.pause(1.0, hard=True)
    scene nyc park with fade
    n "The sun is shining. The birds are chirping... it's peaceful."
    n "Central Park is fairly busy today, but everyone's generally worried about their own activities to notice you and your weird spherical device."
    n "It's a beautiful day."
    n "You lay down in the grass, near a swath of small daisies."
    show k offrail with easeinbottom
    n "Unbuckling Kris from your bag, you lay him down next to you, looking at the sky."
    k "What are these? Daisies?"
    mc "Something like that. They're very prevalent in parks during the summer."
    k "Huh. Interesting."
    $ cutscenetextbox = True
    show screen cuttextbox
    scene kris cutscene 6 with fade
    python:
        if persistent.kc6 == False:
            persistent.cutscenes_seen += 1
            persistent.kc6 = True
    if persistent.cutscenes_seen == cutscene_count:
        python:
            achievement.grant("ach_picture")
            achievement.sync()
            persistent.ach_picture = True
            ach_name = "picture"
        show screen ach_popup with easeinbottom
    k "{color=#fff}I'm still getting used to... not being... down there, you know."
    k "{color=#fff}It's still strange sometimes."
    k "{color=#fff}Not waking up in a charging port..."
    k "{color=#fff}...not staring at that screen all the time..."
    k "{color=#fff}But when I see you, it's... easier."
    mc "{color=#fff}You're a lot more sappy than you pretend to be, you know."
    k "{color=#fff}I know, I know."
    k "{color=#fff}Can't help it... my attitude's deep in my programming."
    k "{color=#fff}You don't seem to mind it, though."
    mc "{color=#fff}I like a man who's confident."
    k "{color=#fff}I'm not really a man."
    mc "{color=#fff}I'm well aware."
    k "{color=#fff}Haha... you're interesting, that's for sure."
    k "{color=#fff}If that brought us together, though..."
    stop music fadeout 2.0
    k "{color=#fff}I'm all the happier for it."
    window hide
    show screen creditsfadeout with fade
    $ renpy.pause(2.0, hard=True)
    hide screen creditsfadeout
    python:
        persistent.endings_got["kristrue"] = True
        if sum(persistent.endings_got.values()) == ending_count:
            achievement.grant("ach_seenitall")
        if persistent.endings_got["kristrue"] and persistent.endings_got["heathtrue"] and persistent.endings_got["aspentrue"] and persistent.endings_got["cctrue"] and persistent.endings_got["robtrue"] and persistent.endings_got["gregtrue"] and persistent.endings_got["unknowntrue"]:
            achievement.grant("ach_ultrobo")
        achievement.grant("ach_kristrue")
        achievement.sync()
    $ renpy.movie_cutscene("ENDCREDIT_kris.webm")
    $ MainMenu(confirm=False)()