screen emailday2():
    vbox:
        style_prefix "emailbtns"
        textbutton "    from: {color=#725e42}UNKNOWN{/color}\n        A little message...                                                                        " action Jump("emailfour")
        textbutton "    from: {color=#c9ae16}Gregory{/color}\n        sorry about yesterday!                                                                 " action Jump("emailfive")
        textbutton "    from: HR\n        MEMO TO ALL EMPLOYEES                                                           " action Jump("emailsix")
    vbox:
        style_prefix "nextday"
        textbutton "NEXT DAY >>" action Jump("day3")
    use affectionprogress

screen email4():
    vbox:
        style_prefix "emltitle"
        text "A little message..."
    vbox:
        style_prefix "emlfrom"
        text "from: UNKNOWN"
    vbox:
        style_prefix "eml"
        if emailfromrobday2 == True:
            text "I told you I'd send ya a little message. Listen, I keep seein' ya 'round these\nparts, and I'm gonna take a chance while I have it, yeah? Not a lot of\nopportunities for a core such as myself. Y'know...\n\nSo hey, maybe over the weekend, you wanna stop by my place? It's\npretty humble, just a closet with a charging port. Big closet though. Lots\nof room for a human. Whaddaya say?\n\nY'know what, don't respond - I already know the answer is yes. So I'll\nsee ya soon."
        if emailfromrobday2 == False:
            text "Heyyy there. You keep blowin' me off now and it's not very kind of ya!\nI'm just tryna make a move on a pretty human, here. Can't fault a core\nfor that. So hey, next time I catch ya 'round, be little nicer, yeah?\n\nAnyway. You should slide on over to my place this weekend. I've got\nenough drinks for the two of us. I might even have some \"human alcohol\"\nin here somewhere."
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("e2")

screen email5():
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
        textbutton "<<< back" action Jump("e2")

screen email6():
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
        textbutton "next >>>" action Jump("emailsixpt2")

screen email6pt2():
    vbox:
        style_prefix "emltitle"
        text "MEMO TO ALL EMPLOYEES"
    vbox:
        style_prefix "emlfrom"
        text "from: HR"
    vbox:
        style_prefix "eml"
        text "Employees whose referral is selected will be eligible to recieve up\nto $200. We will NOT, under ANY CIRCUMSTANCES, accept any former\nBlack Mesa employees.\n\nPlease send an email to PEB regarding any questions or referral\nsubmissions.\n\nThank you,\nHR"
# hi if ur reading my code heres a bit of lore... PEB here is supposed to be the party escort bot, the core that dragged chell back in the portal\portal 2 universe
    use affectionprogress
    vbox:
        style_prefix "emlback"
        textbutton "<<< back" action Jump("e2")
    
label e2first:

    scene blankemail
    with fade
    call screen emailday2 with dissolve

label e2:

    scene blankemail
    call screen emailday2

label emailfour:

    scene blankemail
    call screen email4

label emailfive:
    
    scene blankemail
    call screen email5

label emailsix:
    
    scene blankemail
    call screen email6

label emailsixpt2:

    scene blankemail
    call screen email6pt2