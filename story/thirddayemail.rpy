screen emailday3():
    vbox:
        style_prefix "emailbtns"

    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        if wkd3 == True:
            textbutton "    from: {color=#25a68c}Kris{/color}\n        Hello, Doctor                                                                        " action Jump("emailsevenkris")
        if whd3 == True:
            textbutton "    from: {color=#7f30e0}Heath{/color}\n        A little more magic from me...                                                                         " action Jump("emailsevenheath")
        if wad3 == True:
            textbutton "    from: {color=#1c710b}Aspen{/color}\n        Thanks for today                                                                        " action Jump("emailsevenaspen")
        if wcd3 == True:
            textbutton "    from: {color=#1140a4}CC{/color}\n        Thank you for your visit.                                                                        " action Jump("emailsevencc")
        if wrd3 == True:
            textbutton "    from: {color=#8a0d0d}Rob{/color}\n        What's up, Doc                                                                        " action Jump("emailsevenrob")

    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        #textbutton "    from: {color=#c9ae16}Gregory{/color}\n        an invite?                                                                                   " action Jump("emaileight")
        textbutton "    from: [[ BLOCKED ]\n        [[ HIGH SCAM LIKELIHOOD ]                                                           " action Jump("tde")
    vbox:
        style_prefix "nextday"
        textbutton "NEXT DAY >>" action Jump("day4")
    use affectionprogress

    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

screen email7kris():
    vbox:
        style_prefix "emltitle"
        text "Hello, Doctor"
    vbox:
        style_prefix "emlfrom"
        text "from: Kris"
    vbox:
        style_prefix "eml"
        text "Doctor,\n\nI'd like to thank you for your visit today. It was very informative. I may,\nin fact, have misjudged you upon our first meeting. I will not make such a\nmistake again.\n\nI believe I may have been a little... informal with you today. Please ignore\nthis in our future briefings. It was not intentional and I am not sure what\npossessed me to divulge such sensitive information to you. Thank you,\ndespite that, for your listening ear today. Have a good night.\n\nRegards,\n\nKris, Business Core"
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("tde")

screen email7heath():
    vbox:
        style_prefix "emltitle"
        text "A little more magic from me..."
    vbox:
        style_prefix "emlfrom"
        text "from: Heath"
    vbox:
        style_prefix "eml"
        text "Heyyy Doctor!\n\nGlad you came to see my show today, haha. I haven't had someone give\nme that much attention since I was activated, like, 6 years ago!\n\nIt's unfortunate we had to cut it short to accomodate your busy, busy\nschedule. I'll be sure to make it up to you in the future with even more\nsurprises! Don't be shocked if I'm on fire the next time ya catch me!\n\nCheers,\nHeath, MAGIC CORE!!"
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("tde")

screen email7aspen():
    vbox:
        style_prefix "emltitle"
        text "Thanks for today"
    vbox:
        style_prefix "emlfrom"
        text "from: Aspen"
    vbox:
        style_prefix "eml"
        text "Hi Doctor!\n\nI was looking through my contacts and saw you were recently added to\nmy email database, so I figured I'd send you a message. Nothing special!!\nJust wanted to thank you for today.\n\nNot a lot of other scientists show that much interest in botany! They're\ntoo excited about the robots and the teleportation and all the fancy sci-fi\nstuff, they forget where they came from, haha. So yeah. Thanks for\nletting me talk about it! Sorry to keep you, and have a good night. I should\nsee you tomorrow on your route!!\n\nThanks again,\nAspen, Botanical Core"
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("tde")

screen email7cc():
    vbox:
        style_prefix "emltitle"
        text "Thank you for your visit."
    vbox:
        style_prefix "emlfrom"
        text "from: CC"
    vbox:
        style_prefix "eml"
        text "Hello Doctor.\n\nI wanted to thank you for visiting me today. Though you could have\nchosen any other core in your section, you chose me, and I'm flattered,\nespecially considering how boring I must have been for you.\n\nI hope you do not consider me a fool - I do realize the reason for your\npick is most likely the easy-going shift you recieved in turn. Regardless,\nI am very glad you chose to stop in.\n\nThank you.\n\nRest well,\nCC"
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("tde")

screen email7rob():
    vbox:
        style_prefix "emltitle"
        text "What's up, Doc"
    vbox:
        style_prefix "emlfrom"
        text "from: Rob"
    vbox:
        style_prefix "eml"
        text "What's up, Sport? Great job on that elliptical today! Really working out\nthose SCIENCE MUSCLES, hahaha! Don't forget to rest up - you're gonna\nbe sore tomorrow, that's for certain. Hell, I wouldn't be surprised if\nyou're sore the day after that too!\n\nThanks for stoppin' in today. Don't get a lot of company here n' all, so I'll\ntake whatever I can get! Haha, just kiddin'. I appreciate it, in complete \nseriousness.\n\nAnyway! Stock up on that protein, cuz I ain't done with you yet!\n\nKeep it real,\nRob ( GO HAWKS!! )"
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("tde")

    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#screen email8():
    #vbox:
        #style_prefix "emltitle"
        #text "an invite??"
    #vbox:
        #style_prefix "emlfrom"
        #text "from: Gregory"
    #vbox:
        #style_prefix "eml"
        #text "hey doc!!\n\nglad you opened this email up, didn't know if you would! haha.\n\nlisten, i've been thinking about two days ago, when we bumped into each\nother? you might've gotten some ideas about me that aren't\nparticularly true, so i just wanna clear things up. if you're interested, i'm \ngonna be at the gym this saturday!\n\ni don't know if you'll be on-campus, but i figured it's worth a shot,\nright? so yeah, maybe we grab a coffee, i can clear up any question\nyou might have, yeah?? anyway. think about it!!\n\n- gregory"
    #use affectionprogress
    #vbox:
        #style_prefix "emlback"
        #textbutton "<<< back" action Jump("tde")
    
label tdefirst:

    scene blankemail
    with fade
    call screen emailday3

label tde:

    scene blankemail
    call screen emailday3

label emailsevenkris:

    scene blankemail
    call screen email7kris

label emailsevenheath:

    scene blankemail
    call screen email7heath

label emailsevenaspen:

    scene blankemail
    call screen email7aspen

label emailsevencc:

    scene blankemail
    call screen email7cc

label emailsevenrob:

    scene blankemail
    call screen email7rob

#label emaileight:
    
    #scene blankemail
    #call screen email8