screen emailday8():
    vbox:
        style_prefix "emailbtns"
        textbutton "    from: HR\n        MANDATORY TRAINING                                                                " action Jump("emailone_8")
        textbutton "    from: Aperture News Now\n        Are YOU Smarter Than A Test Subject? >>                                 " action Jump("emailtwo_8")
        if romance_points["Greg"] >= 10:
            textbutton "    from: {color=#c9ae16}Gregory{/color}\n        good to see you again                                                                       " action Jump("emailthree_8")
    vbox:
        style_prefix "nextday"
        textbutton "NEXT DAY >>" action Jump("day9")
    use affectionprogress

screen email1_8():
    vbox:
        style_prefix "emltitle"
        text "MANDATORY TRAINING"
    vbox:
        style_prefix "emlfrom"
        text "from: HR"
    vbox:
        style_prefix "eml"
        text "Our mandatory sexual harrassment training is swiftly approaching.\nWe know many long-term employees may still not be used to this\nprogram, so we would like to remind you of the conduct we expect\nduring these trainings.\n\nDo not, under any circumstances, use this mandatory training as a basis\nfor jokes at the expense of the company or your coworkers.\n\nIn addition, we expect a certain modicum of respect for those giving the\npresentation and providing resources to our employees.\n\nThis email also serves as a reminder that any and all harrassment\nconcerns should be reported immediately to HR. Reports can also be"
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "next >>>" action Jump("emailone_8pt2")

screen email2_8():
    vbox:
        style_prefix "emltitle"
        text "Are YOU Smarter Than A Test Subject?"
    vbox:
        style_prefix "emlfrom"
        text "from: Aperture News Now"
    vbox:
        style_prefix "eml"
        text "Investigations in the Testing department have revealed that the average\ntest subject CANNOT READ!\n\nThis unforseen illiteracy has lead many researchers to ask what the \naverage intelligence of Aperture employees actually is. We spoke to\nDr. Pierce in Neurology with this question.\n\n\"Aperture Laboratories is home to many intelligent scientists and\nresearchers,\" he said. \"The fact that our test subjects tend to be lower on\nthe intelligence scale does not speak to the IQ of our main employee base.\"\n\nRead more on this story {a=https://en.wikipedia.org/wiki/Intelligence_quotient#:~:text=Historically%2C%20many%20proponents%20of%20IQ%20testing%20have%20been%20eugenicists%20who%20used%20pseudoscience%20to%20push%20now%2Ddebunked%20views%20of%20racial%20hierarchy%20in%20order%20to%20justify%20segregation%20and%20oppose%20immigration.%5B25%5D%5B26}here.{/a}"
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("e8")

screen email3_8():
    vbox:
        style_prefix "emltitle"
        text "good to see you again"
    vbox:
        style_prefix "emlfrom"
        text "from: Gregory"
    vbox:
        style_prefix "eml"
        text "hey doc! it was good to see you again today. sorry i couldn't have\nstayed longer - miss esther gives me this glare sometimes and it's really\nhonestly terrifying, haha.\n\nregardless, it's always good to see you around! don't be a stranger. you\ncan always stop by my section to say hi :)\n\n<3 gregory"
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("e8")

screen email1_8pt2():
    vbox:
        style_prefix "emltitle"
        text "MANDATORY TRAINING"
    vbox:
        style_prefix "emlfrom"
        text "from: HR"
    vbox:
        style_prefix "eml"
        text "filed anonymously by calling our 24-hour hotline below.\n\nAperture Reporting Hotline (24 HOURS):\n858-924-0180"
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("e8")

label e8first:
    stop music
    stop music1
    play music nine
    scene blankemail
    with fade
    call screen emailday8 with dissolve

label e8:

    scene blankemail
    call screen emailday8

label emailone_8:

    scene blankemail
    call screen email1_8

label emailtwo_8:
    
    scene blankemail
    call screen email2_8

label emailthree_8:
    
    scene blankemail
    call screen email3_8

label emailone_8pt2:
    
    scene blankemail
    call screen email1_8pt2

#oh my god i cant believe i got this to work
#this shit scuffed AS FUCK!!!