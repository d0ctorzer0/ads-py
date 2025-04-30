screen emailday5():
    vbox:
        style_prefix "emailbtns"
        textbutton "    from: {color=#725e42}UNKNOWN{/color}\n        Sorry Doc...                                                                                 " action Jump("emailtwelve")
        textbutton "    from: Management\n        End-of-Week Reminder                                                                 " action Jump("emailthirteen")
        textbutton "    from: {color=#db35a9}Miss Esther{/color}\n        Friday Report                                                                             " action Jump("emailfourteen")
    vbox:
        style_prefix "nextday"
        textbutton "NEXT DAY >>" action Jump("day6")
    use affectionprogress

screen email12():
    vbox:
        style_prefix "emltitle"
        text "Sorry Doc..."
    vbox:
        style_prefix "emlfrom"
        text "from: UNKNOWN"
    vbox:
        style_prefix "eml"
        text "Hey, I just wanna apologize for crashin' into that guy's room earlier\ntoday... I had just finished a drink and I was lost, didn't know where I was\nheaded. I'm sure you ain't happy with me, and he prolly ain't, either, so I\nsent him an email too, just in case.\n\nHad to hound around for it... not easy to find such sensitive info, especially\nwhen I've been cut off from the system, yeah? Anyways.\n\nSorry, Doc. Hope you'll forgive an old core like me."
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("e5")

screen email13():
    vbox:
        style_prefix "emltitle"
        text "End-of-Week Reminder"
    vbox:
        style_prefix "emlfrom"
        text "from: Management"
    vbox:
        style_prefix "eml"
        text "Attention on-campus employees.\n\nThis is your obligatory end-of-week email reminding you of our policies\nconcerning remaining on-campus over the weekend. Aperture\nLaboratories is a large facility, and it is the responsibility of all associates\nto ensure that commuting employees come back on Monday to a clean,\norganized, and efficient workspace.\nTo this effect, ensure that:\n\n> All trash is disposed of in designated incineration chambers\n> All research materials are kept under lock when not in use\n> Interaction with off-campus employees is kept to a minimum over the \n   weekend\n"
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "next >>>" action Jump("emailthirteenpt2")

screen email13pt2():
    vbox:
        style_prefix "emltitle"
        text "End-of-Week Reminder"
    vbox:
        style_prefix "emlfrom"
        text "from: Management"
    vbox:
        style_prefix "eml"
        text "Again, it is the responsibility of all on-campus employees to abide by\nthese standards. For more information on these practices and more\nconcerning weekend use of Aperture Labs, please click {a=https://cat-bounce.com/}here.{/a}\n\nThank you,\nManagement"
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("e5")

screen email14():
    vbox:
        style_prefix "emltitle"
        text "Friday Report" #rpo stands for "robot project overhaul"
    vbox:
        style_prefix "emlfrom"
        text "from: Miss Esther"
    vbox:
        style_prefix "eml"
        text "Congratulations on making it halfway, Doctor!\n\nI'm sure you were briefed on the responsibilities of the maintenance\nemployee for Friday before they leave work, but just in case you forgot,\n make sure you submit your paperwork to Dr. McCoy in MM before EOD.\n\nThis includes all checks you've done throughout the week as well as any\nnotes you may have had. (Feel free to mention that gross core we keep\nencountering - maybe they'll do something about it.)\nCheers! See you next week!\n\nRegards,\nMiss Esther"
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("e5")
    
label e5first:
    play music endofday
    scene blankemail
    with fade
    call screen emailday5 with dissolve

label e5:

    scene blankemail
    call screen emailday5

label emailtwelve:
    
    scene blankemail
    call screen email12

label emailthirteen:
    
    scene blankemail
    call screen email13

label emailthirteenpt2:
    
    scene blankemail
    call screen email13pt2

label emailfourteen:
    
    scene blankemail
    call screen email14
