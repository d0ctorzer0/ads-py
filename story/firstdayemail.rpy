screen emailday1():
    vbox:
        style_prefix "emailbtns"
        textbutton "    from: Miss Esther\n        Welcome to Maintenance                                                                " action Jump("emailone")
        textbutton "    from: Aperture News Now\n        CAVE JOHNSON ALIVE??? Click for pictures >>                               " action Jump("emailtwo")
        textbutton "    from: Management\n        About the Incident.                                                                       " action Jump("emailthree")
    vbox:
        style_prefix "nextday"
        textbutton "NEXT DAY >>" action Jump("day2")
    use affectionprogress

screen email1():
    vbox:
        style_prefix "emltitle"
        text "Welcome to Maintenance"
    vbox:
        style_prefix "emlfrom"
        text "from: Miss Esther"
    vbox:
        style_prefix "eml"
        text "Congratulations on completing your first day in maintenance. I wish to\nextend a formal thank you for your work today.\n\nI know that maintenance is not your first choice and that you'd much\nrather be working your regular position. In light of this, you should\nbe happy to hear that management only needs you here for about two\nweeks before the permanent replacement starts.\n\nYour temporary quarters will be in Section 7, Room 14. The code is 1986.\n\nRest well. I will see you tomorrow.\n\nRegards,\nMiss Esther"
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("fde")

screen email2():
    vbox:
        style_prefix "emltitle"
        text "CAVE JOHNSON ALIVE??? Click for pictures >>"
    vbox:
        style_prefix "emlfrom"
        text "from: Aperture News Now"
    vbox:
        style_prefix "eml"
        text "New evidence has come to light that CAVE JOHNSON, FORMER CEO\nOF APERTURE, IS ALIVE! Many think that the scientific genius has long\nsince passed away, but some Aperture Employees think otherwise.\n\n\"I heard there was a team of scientists who stuffed his brain into a\nmassive metal head,\" reports one. \"They say he now lies at the bottom\nof the facility...\"\n\nThe current CEO has declined to comment, stating, \"These claims are\nbaseless and unscientific. If Mr. Johnson were truly alive, we would do\neverything in our power to bring him back.\"\n\nRead more on this story {a=https://en.wikipedia.org/wiki/Lemon}here.{/a}"
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("fde")

screen email3():
    vbox:
        style_prefix "emltitle"
        text "About the Incident."
    vbox:
        style_prefix "emlfrom"
        text "from: Management"
    vbox:
        style_prefix "eml"
        text "I'm sure many of you have heard about the incident that occurred in our\nfacility shortly after Mr. Johnson's death. I am sending this memo to every\nemployee to assure you that the situation has been resolved and there is\nno need for concern.\n\nMr. Johnson was a great man. Towards the end of his life, we had nearly\nfinished developing our brain mapping technology. After his passing,\nhowever, I made the executive decision as the new head of facility to\nabandon the project and its \"magnum opus\".\n\nThough we retain the data obtained via the brain mapping experiments,\nwe do not plan to put it into use.\n\nI apologize again for any disruptions or inconveniences this situation"
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "next >>>" action Jump("emailthreept2")

screen email3pt2():
    vbox:
        style_prefix "emltitle"
        text "About the Incident."
    vbox:
        style_prefix "emlfrom"
        text "from: Management"
    vbox:
        style_prefix "eml"
        text "may have caused for our company. Looking forward, Aperture's future\nis brighter than ever.\n\nThank you.\n\nCaroline, CEO of Aperture Science"
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("fde")

label fdefirst:

    scene blankemail
    with fade
    call screen emailday1

label fde:

    scene blankemail
    call screen emailday1

label emailone:

    scene blankemail
    call screen email1

label emailtwo:
    
    scene blankemail
    call screen email2

label emailthree:
    
    scene blankemail
    call screen email3

label emailthreept2:
    
    scene blankemail
    call screen email3pt2

#oh my god i cant believe i got this to work
#this shit scuffed AS FUCK!!!