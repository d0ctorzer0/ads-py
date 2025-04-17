# CUTSCENE DESCRIPTIONS:

# KRIS thru ROB
# Day 3, Day 6, Day 10, Day 13, Ending 1/2 (Day 15)
# GREGORY 
# Day 6, Day 7, Day 12, Ending 1/2 (Day 15)
# ???
# Day 6, Day 11, Ending 1/2 (Day 15)

style file_button_text:
    font "terminal-grotesque.ttf"
    color "#f0f0f0"
    hover_color "#f1ce7a"

style tabs_button_text:
    font "chawp.ttf"
    color "#513f1e"
    hover_color "#000000"
    size 35

screen galleryk:
    style_prefix "file"
    textbutton "<<< back" action Hide("galleryk", transition=easeoutbottom) ypos 20 xpos 20

    if persistent.kgunlock == False:
        add "gui/gallery/krislocked.png"
    elif persistent.kgunlock == True:
        add "gui/gallery/krisunlocked.png"

    fixed:
        if persistent.kc1 == True:
            add "characters/kris/kris cutscene 1.png" at gallery_size xpos 300 ypos 216
    
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
    textbutton "<<< back" action Hide("galleryh", transition=easeoutbottom) ypos 20 xpos 20

    if persistent.hgunlock == False:
        add "gui/gallery/heathlocked.png"
    elif persistent.hgunlock == True:
        add "gui/gallery/heathunlocked.png"

    fixed:
        if persistent.hc1 == True:
            add "characters/heath/heath cutscene 1.png" at gallery_size xpos 300 ypos 216
        if persistent.hc2 == True:
            add "characters/heath/heath cutscene 2.png" at gallery_size xpos 760 ypos 216
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
    textbutton "<<< back" action Hide("gallerya", transition=easeoutbottom) ypos 20 xpos 20

    if persistent.agunlock == False:
        add "gui/gallery/aspenlocked.png"
    elif persistent.agunlock == True:
        add "gui/gallery/aspenunlocked.png"
    
    fixed:
        if persistent.ac1 == True:
            add "characters/aspen/aspen cutscene 1.png" at gallery_size xpos 300 ypos 216

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
    textbutton "<<< back" action Hide("galleryc", transition=easeoutbottom) ypos 20 xpos 20

    if persistent.cgunlock == False:
        add "gui/gallery/cclocked.png"
    elif persistent.cgunlock == True:
        add "gui/gallery/ccunlocked.png"

    fixed:
        if persistent.cc1 == True:
            add "characters/cc/cc cutscene 1.png" at gallery_size xpos 300 ypos 216
    
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
    textbutton "<<< back" action Hide("galleryr", transition=easeoutbottom) ypos 20 xpos 20

    if persistent.rgunlock == False:
        add "gui/gallery/roblocked.png"
    elif persistent.rgunlock == True:
        add "gui/gallery/robunlocked.png"
    
    fixed:
        if persistent.rc1 == True:
            add "characters/rob/rob cutscene 1.png" at gallery_size xpos 300 ypos 216

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
    textbutton "<<< back" action Hide("galleryg", transition=easeoutbottom) ypos 20 xpos 20

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
    textbutton "<<< back" action Hide("galleryu", transition=easeoutbottom) ypos 20 xpos 20

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