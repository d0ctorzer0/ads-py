style file_button_text:
    font "terminal-grotesque.ttf"
    color "#f0f0f0"
    hover_color "#f1ce7a"
    xpos 30
    ypos 50

style tabs_button_text:
    font "chawp.ttf"
    color "#513f1e"
    hover_color "#000000"
    size 35

screen galleryk:
    style_prefix "file"
    textbutton "<<< back" action Hide("galleryk", transition=easeoutbottom)

    if persistent.kgunlock == False:
        add "gui/gallery/krislocked.png"
    elif persistent.kgunlock == True:
        add "gui/gallery/krisunlocked.png"

    vbox:
        style_prefix "tabs"
        textbutton "KRIS" xpos 364 ypos 130 action NullAction()
        textbutton "HEATH" xpos 535 ypos 84 action Hide("galleryk"), Show("galleryh")
        textbutton "ASPEN" xpos 717 ypos 34 action Hide("galleryk"), Show("gallerya")
        textbutton "CC" xpos 924 ypos -14 action Hide("galleryk"), Show("galleryc")
        textbutton "ROB" xpos 1100 ypos -63 action Hide("galleryk"), Show("galleryr")
        textbutton "GREG" xpos 1265 ypos -112 action Hide("galleryk"), Show("galleryg")
        textbutton "xxx" xpos 1460 ypos -160 action Hide("galleryk"), Show("galleryu")

screen galleryh:
    style_prefix "file"
    textbutton "<<< back" action Hide("galleryh", transition=easeoutbottom)

    if persistent.hgunlock == False:
        add "gui/gallery/heathlocked.png"
    elif persistent.hgunlock == True:
        add "gui/gallery/heathunlocked.png"

    vbox:
        style_prefix "tabs"
        textbutton "KRIS" xpos 364 ypos 130 action Hide("galleryh"), Show("galleryk")
        textbutton "HEATH" xpos 535 ypos 84 action NullAction()
        textbutton "ASPEN" xpos 717 ypos 34 action Hide("galleryh"), Show("gallerya")
        textbutton "CC" xpos 924 ypos -14 action Hide("galleryh"), Show("galleryc")
        textbutton "ROB" xpos 1100 ypos -63 action Hide("galleryh"), Show("galleryr")
        textbutton "GREG" xpos 1265 ypos -112 action Hide("galleryh"), Show("galleryg")
        textbutton "xxx" xpos 1460 ypos -160 action Hide("galleryh"), Show("galleryu")

screen gallerya:
    style_prefix "file"
    textbutton "<<< back" action Hide("gallerya", transition=easeoutbottom)

    if persistent.agunlock == False:
        add "gui/gallery/aspenlocked.png"
    elif persistent.agunlock == True:
        add "gui/gallery/aspenunlocked.png"

    vbox:
        style_prefix "tabs"
        textbutton "KRIS" xpos 364 ypos 130 action Hide("gallerya"), Show("galleryk")
        textbutton "HEATH" xpos 535 ypos 84 action Hide("gallerya"), Show("galleryh")
        textbutton "ASPEN" xpos 717 ypos 34 action NullAction()
        textbutton "CC" xpos 924 ypos -14 action Hide("gallerya"), Show("galleryc")
        textbutton "ROB" xpos 1100 ypos -63 action Hide("gallerya"), Show("galleryr")
        textbutton "GREG" xpos 1265 ypos -112 action Hide("gallerya"), Show("galleryg")
        textbutton "xxx" xpos 1460 ypos -160 action Hide("gallerya"), Show("galleryu")

screen galleryc:
    style_prefix "file"
    textbutton "<<< back" action Hide("galleryc", transition=easeoutbottom)

    if persistent.cgunlock == False:
        add "gui/gallery/cclocked.png"
    elif persistent.cgunlock == True:
        add "gui/gallery/ccunlocked.png"

    vbox:
        style_prefix "tabs"
        textbutton "KRIS" xpos 364 ypos 130 action Hide("galleryc"), Show("galleryk")
        textbutton "HEATH" xpos 535 ypos 84 action Hide("galleryc"), Show("galleryh")
        textbutton "ASPEN" xpos 717 ypos 34 action Hide("galleryc"), Show("gallerya")
        textbutton "CC" xpos 924 ypos -14 action NullAction()
        textbutton "ROB" xpos 1100 ypos -63 action Hide("galleryc"), Show("galleryr")
        textbutton "GREG" xpos 1265 ypos -112 action Hide("galleryc"), Show("galleryg")
        textbutton "xxx" xpos 1460 ypos -160 action Hide("galleryc"), Show("galleryu")

screen galleryr:
    style_prefix "file"
    textbutton "<<< back" action Hide("galleryr", transition=easeoutbottom)

    if persistent.rgunlock == False:
        add "gui/gallery/roblocked.png"
    elif persistent.rgunlock == True:
        add "gui/gallery/robunlocked.png"

    vbox:
        style_prefix "tabs"
        textbutton "KRIS" xpos 364 ypos 130 action Hide("galleryr"), Show("galleryk")
        textbutton "HEATH" xpos 535 ypos 84 action Hide("galleryr"), Show("galleryh")
        textbutton "ASPEN" xpos 717 ypos 34 action Hide("galleryr"), Show("gallerya")
        textbutton "CC" xpos 924 ypos -14 action Hide("galleryr"), Show("galleryc")
        textbutton "ROB" xpos 1100 ypos -63 action NullAction()
        textbutton "GREG" xpos 1265 ypos -112 action Hide("galleryr"), Show("galleryg")
        textbutton "xxx" xpos 1460 ypos -160 action Hide("galleryr"), Show("galleryu")

screen galleryg:
    style_prefix "file"
    textbutton "<<< back" action Hide("galleryg", transition=easeoutbottom)

    if persistent.ggunlock == False:
        add "gui/gallery/gregorylocked.png"
    elif persistent.ggunlock == True:
        add "gui/gallery/gregoryunlocked.png"

    vbox:
        style_prefix "tabs"
        textbutton "KRIS" xpos 364 ypos 130 action Hide("galleryg"), Show("galleryk")
        textbutton "HEATH" xpos 535 ypos 84 action Hide("galleryg"), Show("galleryh")
        textbutton "ASPEN" xpos 717 ypos 34 action Hide("galleryg"), Show("gallerya")
        textbutton "CC" xpos 924 ypos -14 action Hide("galleryg"), Show("galleryc")
        textbutton "ROB" xpos 1100 ypos -63 action Hide("galleryg"), Show("galleryr")
        textbutton "GREG" xpos 1265 ypos -112 action NullAction()
        textbutton "xxx" xpos 1460 ypos -160 action Hide("galleryg"), Show("galleryu")

screen galleryu:
    style_prefix "file"
    textbutton "<<< back" action Hide("galleryu", transition=easeoutbottom)

    if persistent.ugunlock == False:
        add "gui/gallery/unknownlocked.png"
    elif persistent.ugunlock == True:
        add "gui/gallery/unknownunlocked.png"

    vbox:
        style_prefix "tabs"
        textbutton "KRIS" xpos 364 ypos 130 action Hide("galleryu"), Show("galleryk")
        textbutton "HEATH" xpos 535 ypos 84 action Hide("galleryu"), Show("galleryh")
        textbutton "ASPEN" xpos 717 ypos 34 action Hide("galleryu"), Show("gallerya")
        textbutton "CC" xpos 924 ypos -14 action Hide("galleryu"), Show("galleryc")
        textbutton "ROB" xpos 1100 ypos -63 action Hide("galleryu"), Show("galleryr")
        textbutton "GREG" xpos 1265 ypos -112 action Hide("galleryu"), Show("galleryg")
        textbutton "xxx" xpos 1460 ypos -160 action NullAction()