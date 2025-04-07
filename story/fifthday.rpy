label day5:
    scene mctemproom
    with fade

    n "You make it to your room, change into your bedclothes, and prepare to sleep."
    n "Tomorrow's the last day of the week, and maintenance doesn't work on the weekends, other than being on-call."
    n "You're excited for your first day off, though a little curious what you'll do if you can't leave the campus."
    n "Before you know it, you're fast asleep."

    scene black
    with fade
    $ daynum = "5"
    $ dayday = "Friday!"

    show screen daytransition
    $ renpy.pause(2.0, hard=True)

    scene mctemproom with fade

    n "You wake with a start." 
    n "You think you were dreaming, but that's not possible in stasis."
    n "You get up and check your wardrobe. What should you wear for casual friday?"

    menu:
        extend ""
        "A t-shirt and jeans.":
            $ tshirt = True
            n "You put on a regular old t-shirt and blue jeans, and head out the door to work."
        "Your best formalwear.":
            $ formal = True
            n "You put on your best date-night attire, and head out the door to work."
        "A Hawaiian shirt and khakis.":
            $ vaca = True
            n "You put on your vacation clothes, and head out the door to work."
        "Just your regular uniform.":
            $ uniform = True
            n "You decide to just wear your uniform as regular, sling the lab coat over your shoulders, and head out the door to work."

    scene office
    with pixellate

    n "Miss Esther is waiting for you patiently when you enter."

    show e with easeinright

    if tshirt == True:
        e "Ahh, Doctor. I see you went with the classic \"casual\" outfit today! Very nice."
    if formal == True:
        e "Ahh, Doctor. \"Casual\" doesn't mean \"black-tie event\", but I suppose it works regardless. Dashing."
    if vaca == True:
        e "Ahh, Doctor! Planning on going on a cruise? Whatever that is..."
    if uniform == True:
        e "Ahh, Doctor. Went the simple route I see? No worries. It's not for everyone."

    show e
    e "Today's the last day of the week! Any exciting plans for the weekend?"

    menu:
        extend ""
        "I was thinking I'd just stay in my room and do some reading.":
            show e shock
            e "There's plenty more to do around here than sit and read!"
            show e
            e "But it's your time off, so feel free to do whatever you wish."
        "Gregory invited me to go meet him at the gym. I might do that.":
            e "Interesting. Well, it's your time off. You're free to do whatever you please."
        "Honestly, I was just planning on wandering. Maybe finding a bar?":
            show e laugh
            e "A bar? Haha, that's hilarious, Doctor."
        "I have absolutely no clue.":
            show e laugh
            e "Fair enough. I suppose you aren't used to being on-campus on your days off."
    
    show e
    e "Well, we should be on our way, then. Grab your clipboard, and let's get going."
    n "You get your paperwork and follow Miss Esther out the door."

    jump krisday5

label krisday5:
    scene kristemproom with pixellate

    n "You enter the conference room to find things much calmer than yesterday."
    n "In fact, the screen that is usually moving so vibrantly and quickly is turned off."

    mc "Kris? Is something wrong?"

    show k with easeinright
    k "Oh... Doctor."
    k "No. Not at all. Everything is alright."

    show e b sad at bounce
    e "Kris, your screen. It's off."
    hide e b

    k "Yes, I'm aware. Financial thinks I... need to take a day away from it."

    mc "Why?"

    show k flirt
    k "I'm not sure. Perhaps it has something to do with my... panicking yesterday."

    menu:
        extend ""
        "But you calmed down from that.":
            $ romance_points["Kris"] += 3
            jump impresskris5
        "I suppose that makes some sense.":
            $ romance_points["Kris"] -= 3
            jump offendkris5