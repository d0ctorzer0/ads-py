screen emailday4():
    vbox:
        style_prefix "emailbtns"
        textbutton "    from: {color=#c9ae16}Gregory{/color}\n        an invite?                                                                                   " action Jump("emaileight")
        textbutton "    from: {color=#db35a9}Miss Esther{/color}\n        Friday Etiquette                                                                           " action Jump("emailnine")
        textbutton "    from: Dr. Lillihammer{color=#5d5d5d}, etc.{/color}\n        Operation RPO Update                                                                 " action Jump("emailten")
        textbutton "    from: Management\n        IMPORTANT MESSAGE                                                                 " action Jump("emaileleven")
    vbox:
        style_prefix "nextday"
        textbutton "NEXT DAY >>" action Jump("day5")
    use affectionprogress

screen email8():
    vbox:
        style_prefix "emltitle"
        text "an invite??"
    vbox:
        style_prefix "emlfrom"
        text "from: Gregory"
    vbox:
        style_prefix "eml"
        text "hey doc!!\n\nglad you opened this email up, didn't know if you would! haha.\n\nlisten, i've been thinking about today, when we bumped into each\nother? you might've gotten some ideas about me that aren't\nparticularly true, so i just wanna clear things up. if you're interested, i'm \ngonna be at the lounge this saturday!\n\ni don't know if you'll be on-campus, but i figured it's worth a shot,\nright? so yeah, maybe we grab a coffee, i can clear up any question\nyou might have, yeah?? anyway. think about it!!\n\n- gregory"
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("e4")

screen email9():
    vbox:
        style_prefix "emltitle"
        text "Friday Etiquette"
    vbox:
        style_prefix "emlfrom"
        text "from: Miss Esther"
    vbox:
        style_prefix "eml"
        text "Hello Doctor,\n\nI figured you might be confused about \"Casual Friday\" here in maintenance,\nas I'm fairly sure manufacturing doesn't engage in the practice.\n\nEssentially, tomorrow, there is no need to wear your uniform. You can\nwear whatever \"surface clothes\" your heart desires, as long as they follow\nthese guidelines:\n\n> No cropped or low-cut tops. Stomach and chest covered.\n> No ripped or torn pants.\n> No Black Mesa paraphenalia.\n> No logos/companies that promote drug/alcohol consumption.\n"
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "next >>>" action Jump("emailninept2")

screen email9pt2():
    vbox:
        style_prefix "emltitle"
        text "Friday Etiquette"
    vbox:
        style_prefix "emlfrom"
        text "from: Miss Esther"
    vbox:
        style_prefix "eml"
        text "I'm sure these rules are not too strict and should be easy to follow. I look\nforward to seeing you tomorrow!\n\nRegards,\nMiss Esther"
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("e4")

screen email10():
    vbox:
        style_prefix "emltitle"
        text "Operation RPO Update" #rpo stands for "robot project overhaul"
    vbox:
        style_prefix "emlfrom"
        text "from: Dr. Lillihammer, Dr. Zero, Dr. Chakwas, cont."
    vbox:
        style_prefix "eml"
        text "Attention all high-level employees,\n\nOperation RPO will be underway shortly, possibly by the end of this\nmonth. I know this project has been highly anticipated and we look\nforward to commencing with it. We have been working closely with the\nCEO to ensure the fallout from this project will be minimal at worst, \nnonexistent at best.\n\nWe thank you all for your patience in this tumultuous time.\n\nDr. Lillian S. Lillihammer\nHead of RPO"
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("e4")

screen email11():
    vbox:
        style_prefix "emltitle"
        text "IMPORTANT MESSAGE"
    vbox:
        style_prefix "emlfrom"
        text "from: Management"
    vbox:
        style_prefix "eml"
        text "ATTENTION ALL EMPLOYEES,\n\nIt has been brought to our attention that an email regarding a top-secret \nproject may have accidentally been sent to many low-level human\nemployees, particularly in manufacturing. This was unintended and you\nare required to forget said email's existence if you have received it.\n\nIn addition, all associates who receieved the email are eligible to win up to\n$150 if they choose to undergo a quick and easy memory-erasure\nprocedure.\n\nThank you,\nManagement"

    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("e4")
    
label e4first:
    play music endofday
    scene blankemail
    with fade
    call screen emailday4 with dissolve

label e4:

    scene blankemail
    call screen emailday4

label emaileight:

    scene blankemail
    call screen email8

label emailnine:
    
    scene blankemail
    call screen email9

label emailninept2:
    
    scene blankemail
    call screen email9pt2

label emailten:
    
    scene blankemail
    call screen email10

label emaileleven:

    scene blankemail
    call screen email11