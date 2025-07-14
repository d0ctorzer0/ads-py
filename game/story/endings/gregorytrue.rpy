label END_gregtrue:
    window auto
    scene black
    with fade
    $ daynum = "58"
    $ dayday = "On the road..."

    if renpy.is_skipping() == False:
        show screen truedaytransition
        $ renpy.pause(2.0, hard=True)
    
    scene black with fade
    play music deathtoaperture
    n "The passenger seat is quite loud."
    n "Louder than the radio sometimes."
    n "The three little cores that you took under your wing a month ago rarely stop talking."

    g3e "No. You're just straight-up wrong.. Coco Chanel's influence in the 1920s was undeniable."
    g2e "No need to be rude, Rie. I just think Patou's work was {i}better.{/i}"
    g1e "She has a point, though, Gore. Jean Patou was not nearly as influential as Chanel was."
    g2e "No, she's correct. Chanel's work was certainly more influential."
    g2e "That's not the issue I'm having here."
    g2e "I am just stating, in my personal opinion, that Patou's work was more..."
    g3e "More what?"
    g2e "...{i}exciting.{/i}"
    g3e "Oh, if I had hands, Gore, you'd..."
    g1e "Can you two stop fighting?"
    mc "Agreed. You've been talking about this back and forth for the past hour."
    g2e "I apologize."
    g3e "Sorry."
    mc "I know the three of you love your fashion, but it gets exhausting sometimes..."
    g3e "Sorry, Doc."
    g2e "Yes. We're sorry."
    mc "I forgive you two. Thank you, Greg, for helping."
    g1e "No problem!"
    g2e "Speaking of the past hour -"
    g3e "Are we almost there yet? This ride's taking a LONG time..."
    mc "Patience. We'll get there shortly."
    g1e "Where are we going, anyways?"
    mc "You'll see."

    n "The past month has been interesting."
    n "You still aren't entirely sure where you stand on your relationship with these three, but..."
    n "Exploring it has been exciting."
    n "They had split up the name \"Gregory\" into three separate monikers -"
    n "Greg, Gore, and Rie."
    n "It would incredibly smart if it wasn't just the {i}tiniest{/i} bit silly."