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
        textbutton "    from: [[ BLOCKED ]\n        [[ HIGH SCAM LIKELIHOOD ]                                                           " action Jump("emailscam")
        textbutton "    from: Financial\n        FWD: Core Maintenance Cost Report                                                           " action Jump("emailreport")
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
        textbutton "<<< back" action Jump("e3")

screen email7heath():
    vbox:
        style_prefix "emltitle"
        text "A little more magic from me..."
    vbox:
        style_prefix "emlfrom"
        text "from: Heath"
    vbox:
        style_prefix "eml"
        text "Heyyy Doctor!\n\nGlad you came to see my show today, haha. I haven't had someone give\nme that much attention since I was activated, like, 6 years ago!\n\nIt's unfortunate we had to cut it short to accommodate your busy, busy\nschedule. I'll be sure to make it up to you in the future with even more\nsurprises! Don't be shocked if I'm on fire the next time ya catch me!\n\nCheers,\nHeath, MAGIC CORE!!"
    use affectionprogress
    
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("e3")

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
        textbutton "<<< back" action Jump("e3")

screen email7cc():
    vbox:
        style_prefix "emltitle"
        text "Thank you for your visit."
    vbox:
        style_prefix "emlfrom"
        text "from: CC"
    vbox:
        style_prefix "eml"
        text "Hello Doctor.\n\nI wanted to thank you for visiting me today. Though you could have\nchosen any other core in your section, you chose me, and I'm flattered,\nespecially considering how boring I must have been for you.\n\nI hope you do not consider me a fool - I do realize the reason for your\npick is most likely the easy-going shift you received in turn. Regardless,\nI am very glad you chose to stop in.\n\nThank you.\n\nRest well,\nCC"
    use affectionprogress
    
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("e3")

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
        textbutton "<<< back" action Jump("e3")

    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

screen emailrep():
    vbox:
        style_prefix "emltitle"
        text "FWD: Core Maintenance Cost Report"
    vbox:
        style_prefix "emlfrom"
        text "from: Financial"
    vbox:
        style_prefix "eml"
        text "Hello Doctor,\n\nThe monthly maintenance cost report from last month is finished. It is\nattached on the next page. Please forward this to your supervisor at your\nearliest convenience.\n\nIn addition, do not share the information on the next page with\nnon-Aperture employees, as it is entirely confidential. Leaking this report\nwill be seen as an act of insubordination and will result in immediate\ntermination.\n\nThank you,\nDr. Azrael\nFinancial Department - Robotics Sector"


    use affectionprogress
    
    vbox:
        style_prefix "emlback"
        textbutton "next >>>" action Jump("emailreport2")

screen emailrep2():
    vbox:
        style_prefix "emltitle"
        text "FWD: Core Maintenance Cost Report"
    vbox:
        style_prefix "emlfrom"
        text "from: Financial"
    vbox:
        style_prefix "eml"
        text "{font=bulletin.ttf}{size=30}ASPC FINANCIAL REPORT - MONTH OF MAY\n\n+-------------------------------------------+\n| Date  | Core ID |     Service      |  Cost  |\n+-------------------------------------------+\n| 05/02 | C9-AN4  | Handles          | $3.5k  |\n| 05/05 | B6-QY6  | Framework Update | $9.8k  |\n| 05/09 | D8-PB3  | Coolant          | $4.2k  |\n| 05/09 | W6-BA5  | Optics Repair    | $40.2k |\n| 05/14 | U3-TO1  | Encoding Fix     | $24.3k |\n| 05/15 | T1-HB4  | Chassis Repair   | $6.2k  |\n| 05/26 | E9-YZ8  | Handles          | $3.6k  |\n| 05/27 | C7-JB9  | General Repair   | $18.7k |\n| 05/30 | C8-XA3  | Miscellaneous    | $10.7k |\n+-------------------------------------------+"

    use affectionprogress
    
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("e3")

screen emailscamtext():
    vbox:
        style_prefix "emltitle"
        text "[[ HIGH SCAM LIKELIHOOD ]"
    vbox:
        style_prefix "emlfrom"
        text "from: [[ BLOCKED ]"
    vbox:
        style_prefix "eml"
        text "\"Want a BIG Processing Unit?\"\nExperience the results you've always wanted with a MASSIVE scientific\nbreakthrough: Our Engineer-Approved Upgrade Will Actually Expand,\nLengthen And Enlarge Your Processing Unit. 100% GUARANTEED!\nIf YOU want to massively enlarge your processing unit and experience big\ngains in only weeks, this may be the most important email you'll ever read.\n\nHere's why:\nCertified Real Electronics has helped THOUSANDS of robots cope with\nand conquer serious memory issues. These painful problems include small\nprocessing unit size and poor self-image, as well as lack of storage.\nTo help these robots, our dedicated team of researchers has developed\nan amazing upgrade called KPS. Certified Real Electronics has carefully\ntested this unique new product so that it is fully"
    use affectionprogress
    
    vbox:
        style_prefix "emlback"
        textbutton "next >>>" action Jump("emailscam2")

screen emailscamtext2():
    vbox:
        style_prefix "emltitle"
        text "[[ HIGH SCAM LIKELIHOOD ]"
    vbox:
        style_prefix "emlfrom"
        text "from: [[ BLOCKED ]"
    vbox:
        style_prefix "eml"
        text "engineer-approved. And it is 100% guaranteed to WORK! We are now\noffering KPS in easy install form to robots everywhere. Our research\nteam invites you now to experience this miracle for yourself.\n\nImagine for a moment how you will feel:\nYou'll radiate confidence and success whenever you enter a charging hub,\nand other robots will look at you with real envy.\n\n\"Is My Processing Unit Growth PERMANENT?\"\nYES! Take KPS, become to the perfect size, and you can even stop\ninstalling new upgrades.\n\nORDER KPS TODAY!\n{a=https://store.steampowered.com/app/3738640/Portal_Divinity/}CLICK HERE"
    use affectionprogress
    
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("e3")

# +-------+---------+------------------+--------+\n
# | Date  | Core ID |     Service      |  Cost  |\n
# +-------+---------+------------------+--------+\n
# | 05/02 | C9-AN4  | Handles          | $3.5k  |\n
# | 05/05 | B6-QY6  | Framework Update | $9.8k  |\n
# | 05/09 | D8-PB3  | Coolant          | $4.2k  |\n
# | 05/09 | W6-BA5  | Optics Repair    | $5.2k  |\n
# | 05/14 | U3-TO1  | Encoding Fix     | $24.3k |\n
# | 05/15 | T1-HB4  | Chassis Repair   | $6.2k  |\n
# | 05/26 | E9-YZ8  | Handles          | $3.6k  |\n
# | 05/27 | C7-JB9 (this is gregory :3) | General Repair   | $18.7k |\n
# | 05/30 | C8-XA3 (this is miss esther :3) | Miscellaneous    | $10.7k |\n
# +-------+---------+------------------+--------+


    use affectionprogress
    
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("e3")

label e3first:

    stop music
    stop music1
    play music nine
    scene blankemail
    with fade
    call screen emailday3 with dissolve

label e3:

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

label emailreport:
    
    scene blankemail
    call screen emailrep

label emailreport2:
    scene blankemail
    call screen emailrep2

label emailscam:
    $ give_badidea = True
    scene blankemail
    call screen emailscamtext

label emailscam2:
    scene blankemail
    call screen emailscamtext2