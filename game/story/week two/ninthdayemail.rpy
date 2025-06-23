screen emailday9():
    $ romance_highest_name = max(romance_points, key=romance_points.get)
    vbox:
        style_prefix "emailbtns"
            # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        if romance_points["Kris"] or romance_points["Heath"] or romance_points["Aspen"] or romance_points["CC"] or romance_points["Rob"] or romance_points["???"] or romance_points["Greg"] >= 8:

            if romance_highest_name == "Kris":
                textbutton "    from: {color=#25a68c}Kris{/color}\n        Concerning tomorrow                                                                        " action Jump("ekrisconf")
            if romance_highest_name == "Heath":
                textbutton "    from: {color=#7f30e0}Heath{/color}\n        A surprise for you!                                                                       " action Jump("eheathconf")
            if romance_highest_name == "Aspen":
                textbutton "    from: {color=#1c710b}Aspen{/color}\n        About tomorrow                                                                        " action Jump("easpenconf")
            if romance_highest_name == "CC":
                textbutton "    from: {color=#1140a4}CC{/color}\n        I hope you'll stop by.                                                                        " action Jump("eccconf")
            if romance_highest_name == "Rob":
                textbutton "    from: {color=#8a0d0d}Rob{/color}\n        Hoping to see ya tomorrow!                                                                        " action Jump("erobconf")
            if romance_highest_name == "???":
                $ emailfromunknownday9 == True
                textbutton "    from: {color=#725e42}UNKNOWN{/color}\n        Hey, Doc                                                                        " action Jump("eunknownconf")
            if romance_highest_name == "Greg":
                $ emailfromgregday9 == True
                textbutton "    from: {color=#c9ae16}Gregory{/color}\n        seeing if you're interested...                                                                        " action Jump("egregconf")

        else:
            pass

    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        textbutton "    from: {color=#db35a9}Miss Esther{/color}\n        One-on-One Observation                                                             " action Jump("emailone_9")
        textbutton "    from: Len\n        Miss ya down here!!                                                                      " action Jump("emailtwo_9")
    vbox:
        style_prefix "nextday"
        textbutton "NEXT DAY >>" action Jump("day10")
    use affectionprogress

screen email1_9():
    vbox:
        style_prefix "emltitle"
        text "One-on-One Observation"
    vbox:
        style_prefix "emlfrom"
        text "from: Miss Esther"
    vbox:
        style_prefix "eml"
        text "Hello Doctor,\n\nI am just sending you this simple e-mail to remind you of etiquette\nconcerning tomorrow. I am aware this is your last one here, but I would\njust like to remind you not to let the influences of the cores in our section\naffect your decision.\n\nThe one-on-one day is meant to be a surprise to them, so we can catch\nthem not doing their job - this means they cannot anticipate your arrival.\nI hope you will take this into consideration before tomorrow's shift.\n\nExcellent work today. Have a good night.\n\nMiss Esther"
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("e9")

screen email2_9():
    vbox:
        style_prefix "emltitle"
        text "Miss ya down here!!"
    vbox:
        style_prefix "emlfrom"
        text "from: Len"
    vbox:
        style_prefix "eml"
        text "Hey! Hope you're doing alright up there in maintenance, lol. David won't\nshut up about how much harder his job is now that you're doing\nsomething else for once.\n\nI know you only got a couple more days left up there, so don't give up\nyet! Things are almost back to normal! We miss you down here. Hope you\nhaven't forgotten us yet, LMAO\n\nStay cool. Chill. Whatever adjective you like. Just don't die.\n\nSee ya,\nLen"
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("e9")

screen krisconfemail():
    vbox:
        style_prefix "emltitle"
        text "Concerning tomorrow"
    vbox:
        style_prefix "emlfrom"
        text "from: Kris"
    vbox:
        style_prefix "eml"
        text "Hello, Doctor.\n\nI apologize for my brevity today - I noticed Miss Esther was quite\nexhausted, so I tried to keep our interaction short.\n\nI am aware I am not usually supposed to say such things, but I would like\nyou to seriously consider choosing me as your one-on-one observation\ntomorrow - I have a surprise for you I think you will quite enjoy.\n\nThat is all. Have an excellent night, Doctor.\n\nKris\nBusiness Core"
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("e9")

screen heathconfemail():
    vbox:
        style_prefix "emltitle"
        text "A surprise for you!"
    vbox:
        style_prefix "emlfrom"
        text "from: Heath"
    vbox:
        style_prefix "eml"
        text "Hey Doctor! Hope this email finds you!\n\nListen, you've been giving me a lot of attention lately... and personally, I\ndon't think I've had enough yet! Haha. You should come visit me tomorrow!\nI know I'm not really supposed to tell you that, since... y'know... it's\nsupposed to be a surprise or whatever. But I don't really care. I've never\nbeen much of a rule-follower anyway!\n\nIf you do come tomorrow, I got a big surprise for you. No spoilers, though!\n\nStay real,\nHeath, MAGIC CORE!!"
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("e9")

screen aspenconfemail():
    vbox:
        style_prefix "emltitle"
        text "About tomorrow"
    vbox:
        style_prefix "emlfrom"
        text "from: Aspen"
    vbox:
        style_prefix "eml"
        text "Hi Doctor, I hope you're doing well tonight!\nI'm still tending to the chrysanthemums I've been talking about lately. You\nshould come by tomorrow to see them again, haha. I'm not really allowed\nto tell you to come visit me, but I think it's okay if I, like, subtly imply it.\n\nIf you do come tomorrow I promise I have a surprise for you that you'll\nlike a lot! Maybe. I might not know you as well as I think I do.\n\nAnyway, I'm rambling again, so I'm going to stop typing now. Have a\ngood night, Doctor.\n\nRegards,\n\nAspen, Botanical Core"
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("e9")

screen ccconfemail():
    vbox:
        style_prefix "emltitle"
        text "I hope you'll stop by."
    vbox:
        style_prefix "emlfrom"
        text "from: CC"
    vbox:
        style_prefix "eml"
        text "Hello Doctor. I hope you do not find this email to be a bother.\n\nForgive me if I am stepping outside boundaries by asking this, but I would\nbe very appreciative if you chose to supervise me during your one-on-one\nshift tomorrow.\n\nI know it can be quite boring watching over me (haha), especially\nconsidering my lack of a true purpose, but I hope that does not bother\nyou to a great extent. I have something for you should you choose me,\nbut I promise it will not inconvenience me if you choose otherwise.\n\nThank you for your time.\n\nCC"
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("e9")

screen robconfemail():
    vbox:
        style_prefix "emltitle"
        text "Hoping to see ya tomorrow!"
    vbox:
        style_prefix "emlfrom"
        text "from: Rob"
    vbox:
        style_prefix "eml"
        text "Heya Doc! Glad ya opened my email.\n\nWe didn't get much time together today, seeing how Essie was so tired,\nso... I figured I'd sent you a message just in case you didn't catch my\ndrift earlier.\n\nI'd really like it if ya stopped in to supervise me tomorrow. I know it's, like,\nagainst regulation or whatever, to tell you to do that, but I don't really\ncare. Anyway, you should definitely stop in tomorrow! Trust me, it's in\nyour best interest... I've got a surprise for you.\n\nHave a great night, Doc. Get some sleep!\n\nCya!"
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("e9")

screen gregconfemail():
    vbox:
        style_prefix "emltitle"
        text "seeing if you're interested..."
    vbox:
        style_prefix "emlfrom"
        text "from: Gregory"
    vbox:
        style_prefix "eml"
        text "hi doctor! looks like we've been missing each other lately, haha. i know\nthat tomorrow is your one-on-one shift - or at least, that's what rob\ntold me - so i hope you have fun with that! anyways.\n\ni have something for you that i think you'll be interested in! it's nothing\nmuch so don't be concerned if you don't see me soon, but, just something to\nkeep in mind.\n\nthat's all! have a good night, doctor.\n\n- gregory"
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("e9")

screen unknownconfemail():
    vbox:
        style_prefix "emltitle"
        text "Hey, Doc"
    vbox:
        style_prefix "emlfrom"
        text "from: UNKNOWN"
    vbox:
        style_prefix "eml"
        text "How's it going? Hope you're doing alright. It was good to run into ya today.\n\nI know that tomorrow's your observation day - the one-on-one, where\nyou spend your shift with one of the cores? That's what CC told me.\nYeah, him and me have been talking lately, haha. I've been... trying to get\nbetter, if you get what I mean.\n\nAnyways, Doc, I was messaging you to see if you'd be free sometime soon?\n\nI got a big surprise\nfor ya but I don't really think your little friend would be very nice to me\nif I saw you out and about.\n\nThink about it, will ya? See you, Doc."
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("e9")

label e9first:
    stop music
    stop music1
    play music nine
    scene blankemail
    with fade
    call screen emailday9 with dissolve

label e9:

    scene blankemail
    call screen emailday9

label emailone_9:

    scene blankemail
    call screen email1_9

label emailtwo_9:
    
    scene blankemail
    call screen email2_9

label ekrisconf:
    
    scene blankemail
    call screen krisconfemail

label eheathconf:
    
    scene blankemail
    call screen heathconfemail

label easpenconf:
    
    scene blankemail
    call screen aspenconfemail

label eccconf:
    
    scene blankemail
    call screen ccconfemail

label erobconf:
    
    scene blankemail
    call screen robconfemail

label egregconf:
    
    scene blankemail
    call screen gregconfemail

label eunknownconf:
    
    scene blankemail
    call screen unknownconfemail