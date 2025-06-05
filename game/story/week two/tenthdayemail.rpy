screen emailday10():
    vbox:
        style_prefix "emailbtns"
        textbutton "    from: HR\n        MANDATORY TRAINING                                                                " action Jump("emailone_10")
        textbutton "    from: Aperture News Now\n        Are YOU Smarter Than A Test Subject? >>                                 " action Jump("emailtwo_10")
        if romance_points["Greg"] >= 10:
            textbutton "    from: {color=#c9ae16}Gregory{/color}\n        good to see you again                                                                       " action Jump("emailthree_10")
    vbox:
        style_prefix "nextday"
        textbutton "NEXT DAY >>" action Jump("day11")
    use affectionprogress

screen email1_10():
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
        textbutton "next >>>" action Jump("emailone_10pt2")

screen email2_10():
    vbox:
        style_prefix "emltitle"
        text "Are YOU Smarter Than A Test Subject?"
    vbox:
        style_prefix "emlfrom"
        text "from: Aperture News Now"
    vbox:
        style_prefix "eml"
        text "Investigations in the Testing department have revealed that the average\ntest subject CANNOT READ!\n\nThis unforseen illiteracy has lead many researchers to ask what the \naverage intelligence of Aperture employees actually is. We spoke to\nDr. Pierce in Neurology with this question.\n\n\"Aperture Laboratories is home to many intelligent scientists and\nresearchers,\" he said. \"The fact that our test subjects tend to be lower on\nthe intelligence scale does not speak to the IQ of our main employee base.\"\n\nRead more on this story {a=https://en.wikipedia.org/wiki/Explosion}here.{/a}"
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("e10")

screen email3_10():
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
        textbutton "<<< back" action Jump("e10")

screen email1_10pt2():
    vbox:
        style_prefix "emltitle"
        text "MANDATORY TRAINING"
    vbox:
        style_prefix "emlfrom"
        text "from: HR"
    vbox:
        style_prefix "eml"
        text "filed anonymously by calling our 24-hour hotline below.\n\nAperture Reporting Hotline (24 HOURS):\n10510-924-01100"
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("e10")

label e10first:
    stop music
    stop music1
    play music nine
    scene blankemail
    with fade
    call screen emailday10 with dissolve

label e10:

    scene blankemail
    call screen emailday10

label emailone_10:

    scene blankemail
    call screen email1_10

label emailtwo_10:
    
    scene blankemail
    call screen email2_10

label emailthree_10:
    
    scene blankemail
    call screen email3_10

label emailone_10pt2:
    
    scene blankemail
    call screen email1_10pt2

#oh my god i cant believe i got this to work
#this shit scuffed AS FUCK!!!