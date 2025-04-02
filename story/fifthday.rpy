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
    else:
        "ERROR. If you are seeing this message you either skipped the beginning of Day 5 or there is something wrong. If you are seeing this message, please report it as an issue."