label END_aspentrue:
    window auto
    scene black
    with fade
    $ daynum = "49"
    $ dayday = "On the road..."

    if renpy.is_skipping() == False:
        show screen truedaytransition
        $ renpy.pause(2.0, hard=True)
    if renpy.is_skipping() == True:
        pass
    
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
    a "And I get to spend time with my favourite human ever."
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