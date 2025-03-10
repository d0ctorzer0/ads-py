screen emailday2():
    vbox:
        style_prefix "emailbtns"
        textbutton "    {color=#725e42}from: UNKNOWN{/color}\n        A little message...                                                                        " action Jump("emailfour")
        textbutton "    {color=#c9ae16}from: Gregory{/color}\n        sorry about yesterday!                                                                 " action Jump("emailfive")
        textbutton "    from: HR\n        MEMO TO ALL EMPLOYEES                                                           " action Jump("emailsix")
    vbox:
        style_prefix "nextday"
        #textbutton "NEXT DAY >>" action Jump("day2")
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
        textbutton "<<< back" action Jump("sde")

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
        textbutton "<<< back" action Jump("sde")

screen email6():
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
        textbutton "<<< back" action Jump("sde")
    
label sdefirst:

    scene blankemail
    with fade
    call screen emailday2

label sde:

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