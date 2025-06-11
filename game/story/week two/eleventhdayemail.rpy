screen emailday11():
    vbox:
        style_prefix "emailbtns"
        textbutton "    from: Dr. McCoy\n        Transferring Back                                                                        " action Jump("emailone_11")
        textbutton "    from: HR\n        \"RETIREMENT\" ANNOUNCEMENT                                 " action Jump("emailtwo_11")
        if romance_points["Greg"] >= 10:
            textbutton "    from: {color=#c9ae16}Gregory{/color}\n        good to see you again                                                                       " action Jump("emailthree_11")
    vbox:
        style_prefix "nextday"
        textbutton "NEXT DAY >>" action Jump("day12")
    use affectionprogress

screen email1_11():
    vbox:
        style_prefix "emltitle"
        text "Transferring Back"
    vbox:
        style_prefix "emlfrom"
        text "from: Dr. McCoy"
    vbox:
        style_prefix "eml"
        text "Hello,\n\nIt has come to my attention that you will be ending your temporary\nposition in Maintenance this coming Friday. Due to exterior circumstances\nthat do not concern you, this transfer process may be difficult - we did\nnot anticipate this occurence, and we deeply apologize in advance.\n\nFor your safety and the consideration of Aperture Science, we ask that\nyou proceed as normal unless other instruction is given. Please send in\nall your reports and checklists by EOD Friday.\n\nThank you,\nDr. McCoy, Maintenance Lead"
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("e11")

screen email2_11():
    vbox:
        style_prefix "emltitle"
        text "\"RETIREMENT\" ANNOUNCEMENT"
    vbox:
        style_prefix "emlfrom"
        text "from: HR"
    vbox:
        style_prefix "eml"
        text "Attention all Aperture Science employees:\n\nWe are pleased to announce the \"retirement\" of our very own Dr. Pierce\nfrom the Neurology department. Dr. Pierce has been working with us for\nmany years and was a very important innovator in our scrapped brain\nmapping project, but the time has come for him to move on to other\nprojects. \n\nAlthough he has requested no large celebration of his graduation from\nour company, we ask that you send him your best wishes regardless, as\nwe look forward to his future endeavors.\n\n- Human Resources"
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("e11")

label e11first:
    stop music
    stop music1
    play music nine
    scene blankemail
    with fade
    call screen emailday11 with dissolve

label e11:

    scene blankemail
    call screen emailday11

label emailone_11:

    scene blankemail
    call screen email1_11

label emailtwo_11:
    
    scene blankemail
    call screen email2_11

label emailthree_11:
    
    scene blankemail
    call screen email3_11

label emailone_11pt2:
    
    scene blankemail
    call screen email1_11pt2

#oh my god i cant believe i got this to work
#this shit scuffed AS FUCK!!!