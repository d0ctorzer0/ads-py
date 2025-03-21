screen emailday3():
    vbox:
        style_prefix "emailbtns"

    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        if ekd3 == True:
            textbutton "    from: {color=#25a68c}Kris{/color}\n        Hello, Doctor                                                                        " action Jump("emailsevenkris")
        if ehd3 == True:
            textbutton "    from: {color=#7f30e0}Heath{/color}\n        A little more magic from me...                                                                         " action Jump("emailsevenheath")
        if ead3 == True:
            textbutton "    from: {color=#1c710b}Aspen{/color}\n        Thanks for today                                                                        " action Jump("emailsevenaspen")
        if ecd3 == True:
            textbutton "    from: {color=#1140a4}CC{/color}\n        Thank you for your visit.                                                                        " action Jump("emailsevencc")
        if erd3 == True:
            textbutton "    from: {color=#8a0d0d}Rob{/color}\n        What's up, Doc                                                                        " action Jump("emailsevenrob")
        else:
            textbutton "    from: {color=#db35a9}Miss Esther{/color}\n        Great work as usual!                                                                        " action Jump("emailsevenesther")

    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        textbutton "    from: {color=#c9ae16}Gregory{/color}\n        sorry about yesterday!                                                                 " action Jump("emaileight")
        textbutton "    from: HR\n        MEMO TO ALL EMPLOYEES                                                           " action Jump("emailnine")
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
        text "I told you I'd send ya a little message. Listen, I keep seein' ya 'round these\nparts, and I'm gonna take a chance while I have it, yeah? Not a lot of\nopportunities for a core such as myself. Y'know...\n\nSo hey, maybe over the weekend, you wanna stop by my place? It's\npretty humble, just a closet with a charging port. Big closet though. Lots\nof room for a human. Whaddaya say?\n\nY'know what, don't respond - I already know the answer is yes. So I'll\nsee ya soon."
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
        text "Heyyy there. You keep blowin' me off now and it's not very kind of ya!\nI'm just tryna make a move on a pretty human, here. Can't fault a core\nfor that. So hey, next time I catch ya 'round, be little nicer, yeah?\n\nAnyway. You should slide on over to my place this weekend. I've got\nenough drinks for the two of us. I might even have some \"human alcohol\"\nin here somewhere."
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
        text "Heyyy there. You keep blowin' me off now and it's not very kind of ya!\nI'm just tryna make a move on a pretty human, here. Can't fault a core\nfor that. So hey, next time I catch ya 'round, be little nicer, yeah?\n\nAnyway. You should slide on over to my place this weekend. I've got\nenough drinks for the two of us. I might even have some \"human alcohol\"\nin here somewhere."
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
        text "Heyyy there. You keep blowin' me off now and it's not very kind of ya!\nI'm just tryna make a move on a pretty human, here. Can't fault a core\nfor that. So hey, next time I catch ya 'round, be little nicer, yeah?\n\nAnyway. You should slide on over to my place this weekend. I've got\nenough drinks for the two of us. I might even have some \"human alcohol\"\nin here somewhere."
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
        text "Heyyy there. You keep blowin' me off now and it's not very kind of ya!\nI'm just tryna make a move on a pretty human, here. Can't fault a core\nfor that. So hey, next time I catch ya 'round, be little nicer, yeah?\n\nAnyway. You should slide on over to my place this weekend. I've got\nenough drinks for the two of us. I might even have some \"human alcohol\"\nin here somewhere."
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("tde")

screen email7esther():
    vbox:
        style_prefix "emltitle"
        text "Great work as usual!"
    vbox:
        style_prefix "emlfrom"
        text "from: Miss Esther"
    vbox:
        style_prefix "eml"
        text "Heyyy there. You keep blowin' me off now and it's not very kind of ya!\nI'm just tryna make a move on a pretty human, here. Can't fault a core\nfor that. So hey, next time I catch ya 'round, be little nicer, yeah?\n\nAnyway. You should slide on over to my place this weekend. I've got\nenough drinks for the two of us. I might even have some \"human alcohol\"\nin here somewhere."
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("tde")

    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

screen email8():
    vbox:
        style_prefix "emltitle"
        text "sorry about yesterday!"
    vbox:
        style_prefix "emlfrom"
        text "from: Gregory"
    vbox:
        style_prefix "eml"
        text "hey there! cc told me this is how i could contact you. im not really\nsupposed to, seeing as youre not a part of my section, but its whatever.\n\ni just really wanted to say sorry for bumping into you yesterday! i was in\na hurry and didnt see you. and also its just really hard to control myself.\nlike... my rail... and stuff. cuz its on the ground as opposed to above me\nlike usual.\n\nso... yeah. im really sorry. you dont have to respond to this email!!\nits okay, i just wanted to apologize.\n\nokay bye!\n\n- gregory"
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("tde")

screen email9():
    vbox:
        style_prefix "emltitle"
        text "MEMO TO ALL EMPLOYEES"
    vbox:
        style_prefix "emlfrom"
        text "from: HR"
    vbox:
        style_prefix "eml"
        text "REFERRAL BONUSES ARE NOW AVAILABLE!\n\nDue to the recent decrease of healthy employees here at Aperture, we\nhave decided to enact our very own employee referral program.\n\nHere at Aperture, we are always looking for top scientists and\nresearchers to join our team. Any employee may submit a referral form\nto HR, excluding:\n\n> Any and all HR employees\n> Any and all employees engaged in the hiring process\n> Upper-level management\n\nThis is to ensure our referral process remains unbiased and scientific."
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "next >>>" action Jump("emailninept2")

screen email9pt2():
    vbox:
        style_prefix "emltitle"
        text "MEMO TO ALL EMPLOYEES"
    vbox:
        style_prefix "emlfrom"
        text "from: HR"
    vbox:
        style_prefix "eml"
        text "Employees whose referral is selected will be eligible to recieve up\nto $200. We will NOT, under ANY CIRCUMSTANCES, accept any former\nBlack Mesa employees.\n\nPlease send an email to PEB regarding any questions or referral\nsubmissions.\n\nThank you,\nHR"

    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("tde")
    
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

label emailsevenesther:

    scene blankemail
    call screen email7esther

label emaileight:
    
    scene blankemail
    call screen email8

label emailnine:
    
    scene blankemail
    call screen email9

label emailninept2:

    scene blankemail
    call screen email9pt2