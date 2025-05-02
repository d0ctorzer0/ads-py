# CUTSCENE DESCRIPTIONS:

# KRIS thru ROB
# Day 3, Day 6, Day 10, Day 13, Ending 1/2 (Day 15)
# GREGORY 
# Day 6, Day 7, Day 12, Ending 1/2 (Day 15)
# ???
# Day 6, Day 11, Ending 1/2 (Day 15)

default selected_char = "kris"

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
    imagebutton idle "gui/back.png" action Hide("galleryk", transition=easeoutbottom)

    if persistent.kgunlock == False:
        add "gui/gallery/krislocked.png"
    elif persistent.kgunlock == True:
        add "gui/gallery/krisunlocked.png"

    fixed:
        if persistent.kc1 == True:
            imagebutton idle "characters/kris/kris cutscene 1.png" action Show("fullcutscene1", transition=gallswitch) at gallery_size xpos 300 ypos 216
        if persistent.kc2 == True:
            imagebutton idle "characters/kris/kris cutscene 2.png" action Show("fullcutscene2", transition=gallswitch) at gallery_size xpos 760 ypos 216
    
    vbox:
        style_prefix "tabs"
        textbutton "KRIS" xpos 364 ypos 130 action NullAction()
        textbutton "HEATH" xpos 535 ypos 84 action Hide("galleryk"), Show("galleryh"), SetVariable("selected_char", "heath")
        textbutton "ASPEN" xpos 717 ypos 34 action Hide("galleryk"), Show("gallerya"), SetVariable("selected_char", "aspen")
        textbutton "CC" xpos 924 ypos -14 action Hide("galleryk"), Show("galleryc"), SetVariable("selected_char", "cc")
        textbutton "ROB" xpos 1100 ypos -63 action Hide("galleryk"), Show("galleryr"), SetVariable("selected_char", "rob")
        textbutton "GREG" xpos 1265 ypos -112 action Hide("galleryk"), Show("galleryg"), SetVariable("selected_char", "gregory")
        textbutton "xxx" xpos 1460 ypos -160 action Hide("galleryk"), Show("galleryu"), SetVariable("selected_char", "unknown")

screen galleryh:
    style_prefix "file"
    imagebutton idle "gui/back.png" action Hide("galleryh", transition=easeoutbottom)

    if persistent.hgunlock == False:
        add "gui/gallery/heathlocked.png"
    elif persistent.hgunlock == True:
        add "gui/gallery/heathunlocked.png"

    fixed:
        if persistent.hc1 == True:
            imagebutton idle "characters/heath/heath cutscene 1.png" action Show("fullcutscene1", transition=gallswitch) at gallery_size xpos 300 ypos 216
        if persistent.hc2 == True:
            imagebutton idle "characters/heath/heath cutscene 2.png" action Show("fullcutscene2", transition=gallswitch) at gallery_size xpos 760 ypos 216
    vbox:
        style_prefix "tabs"
        textbutton "KRIS" xpos 364 ypos 130 action Hide("galleryh"), Show("galleryk"), SetVariable("selected_char", "kris")
        textbutton "HEATH" xpos 535 ypos 84 action NullAction()
        textbutton "ASPEN" xpos 717 ypos 34 action Hide("galleryh"), Show("gallerya"), SetVariable("selected_char", "aspen")
        textbutton "CC" xpos 924 ypos -14 action Hide("galleryh"), Show("galleryc"), SetVariable("selected_char", "cc")
        textbutton "ROB" xpos 1100 ypos -63 action Hide("galleryh"), Show("galleryr"), SetVariable("selected_char", "rob")
        textbutton "GREG" xpos 1265 ypos -112 action Hide("galleryh"), Show("galleryg"), SetVariable("selected_char", "gregory")
        textbutton "xxx" xpos 1460 ypos -160 action Hide("galleryh"), Show("galleryu"), SetVariable("selected_char", "unknown")

screen gallerya:
    style_prefix "file"
    imagebutton idle "gui/back.png" action Hide("gallerya", transition=easeoutbottom)

    if persistent.agunlock == False:
        add "gui/gallery/aspenlocked.png"
    elif persistent.agunlock == True:
        add "gui/gallery/aspenunlocked.png"
    
    fixed:
        if persistent.ac1 == True:
            imagebutton idle "characters/aspen/aspen cutscene 1.png" action Show("fullcutscene1", transition=gallswitch) at gallery_size xpos 300 ypos 216
        if persistent.hc2 == True:
            imagebutton idle "characters/aspen/aspen cutscene 2.png" action Show("fullcutscene2", transition=gallswitch) at gallery_size xpos 760 ypos 216

    vbox:
        style_prefix "tabs"
        textbutton "KRIS" xpos 364 ypos 130 action Hide("gallerya"), Show("galleryk"), SetVariable("selected_char", "kris")
        textbutton "HEATH" xpos 535 ypos 84 action Hide("gallerya"), Show("galleryh"), SetVariable("selected_char", "heath")
        textbutton "ASPEN" xpos 717 ypos 34 action NullAction()
        textbutton "CC" xpos 924 ypos -14 action Hide("gallerya"), Show("galleryc"), SetVariable("selected_char", "cc")
        textbutton "ROB" xpos 1100 ypos -63 action Hide("gallerya"), Show("galleryr"), SetVariable("selected_char", "rob")
        textbutton "GREG" xpos 1265 ypos -112 action Hide("gallerya"), Show("galleryg"), SetVariable("selected_char", "gregory")
        textbutton "xxx" xpos 1460 ypos -160 action Hide("gallerya"), Show("galleryu"), SetVariable("selected_char", "unknown")

screen galleryc:
    style_prefix "file"
    imagebutton idle "gui/back.png" action Hide("galleryc", transition=easeoutbottom)

    if persistent.cgunlock == False:
        add "gui/gallery/cclocked.png"
    elif persistent.cgunlock == True:
        add "gui/gallery/ccunlocked.png"

    fixed:
        if persistent.cc1 == True:
            imagebutton idle "characters/cc/cc cutscene 1.png" at gallery_size xpos 300 ypos 216
    
    vbox:
        style_prefix "tabs"
        textbutton "KRIS" xpos 364 ypos 130 action Hide("galleryc"), Show("galleryk"), SetVariable("selected_char", "kris")
        textbutton "HEATH" xpos 535 ypos 84 action Hide("galleryc"), Show("galleryh"), SetVariable("selected_char", "heath")
        textbutton "ASPEN" xpos 717 ypos 34 action Hide("galleryc"), Show("gallerya"), SetVariable("selected_char", "aspen")
        textbutton "CC" xpos 924 ypos -14 action NullAction()
        textbutton "ROB" xpos 1100 ypos -63 action Hide("galleryc"), Show("galleryr"), SetVariable("selected_char", "rob")
        textbutton "GREG" xpos 1265 ypos -112 action Hide("galleryc"), Show("galleryg"), SetVariable("selected_char", "gregory")
        textbutton "xxx" xpos 1460 ypos -160 action Hide("galleryc"), Show("galleryu"), SetVariable("selected_char", "unknown")

screen galleryr:
    style_prefix "file"
    imagebutton idle "gui/back.png" action Hide("galleryr", transition=easeoutbottom)

    if persistent.rgunlock == False:
        add "gui/gallery/roblocked.png"
    elif persistent.rgunlock == True:
        add "gui/gallery/robunlocked.png"
    
    fixed:
        if persistent.rc1 == True:
            imagebutton idle "characters/rob/rob cutscene 1.png" action Show("fullcutscene1", transition=gallswitch) at gallery_size xpos 300 ypos 216
        if persistent.hc2 == True:
            imagebutton idle "characters/rob/rob cutscene 2.png" action Show("fullcutscene2", transition=gallswitch) at gallery_size xpos 760 ypos 216

    vbox:
        style_prefix "tabs"
        textbutton "KRIS" xpos 364 ypos 130 action Hide("galleryr"), Show("galleryk"), SetVariable("selected_char", "kris")
        textbutton "HEATH" xpos 535 ypos 84 action Hide("galleryr"), Show("galleryh"), SetVariable("selected_char", "heath")
        textbutton "ASPEN" xpos 717 ypos 34 action Hide("galleryr"), Show("gallerya"), SetVariable("selected_char", "aspen")
        textbutton "CC" xpos 924 ypos -14 action Hide("galleryr"), Show("galleryc"), SetVariable("selected_char", "cc")
        textbutton "ROB" xpos 1100 ypos -63 action NullAction()
        textbutton "GREG" xpos 1265 ypos -112 action Hide("galleryr"), Show("galleryg"), SetVariable("selected_char", "gregory")
        textbutton "xxx" xpos 1460 ypos -160 action Hide("galleryr"), Show("galleryu"), SetVariable("selected_char", "unknown")

screen galleryg:
    style_prefix "file"
    imagebutton idle "gui/back.png" action Hide("galleryg", transition=easeoutbottom)

    if persistent.ggunlock == False:
        add "gui/gallery/gregorylocked.png"
    elif persistent.ggunlock == True:
        add "gui/gallery/gregoryunlocked.png"

    fixed:
        if persistent.gc1 == True:
            imagebutton idle "characters/gregory/gregory cutscene 1.png" action Show("fullcutscene1", transition=gallswitch) at gallery_size xpos 300 ypos 216

    vbox:
        style_prefix "tabs"
        textbutton "KRIS" xpos 364 ypos 130 action Hide("galleryg"), Show("galleryk"), SetVariable("selected_char", "kris")
        textbutton "HEATH" xpos 535 ypos 84 action Hide("galleryg"), Show("galleryh"), SetVariable("selected_char", "heath")
        textbutton "ASPEN" xpos 717 ypos 34 action Hide("galleryg"), Show("gallerya"), SetVariable("selected_char", "aspen")
        textbutton "CC" xpos 924 ypos -14 action Hide("galleryg"), Show("galleryc"), SetVariable("selected_char", "cc")
        textbutton "ROB" xpos 1100 ypos -63 action Hide("galleryg"), Show("galleryr"), SetVariable("selected_char", "rob")
        textbutton "GREG" xpos 1265 ypos -112 action NullAction()
        textbutton "xxx" xpos 1460 ypos -160 action Hide("galleryg"), Show("galleryu"), SetVariable("selected_char", "unknown")

screen galleryu:
    style_prefix "file"
    imagebutton idle "gui/back.png" action Hide("galleryu", transition=easeoutbottom)

    if persistent.ugunlock == False:
        add "gui/gallery/unknownlocked.png"
    elif persistent.ugunlock == True:
        add "gui/gallery/unknownunlocked.png"

    fixed:
        if persistent.uc1 == True:
            imagebutton idle "characters/unknown/unknown cutscene 1.png" action Show("fullcutscene1", transition=gallswitch) at gallery_size xpos 300 ypos 216

    vbox:
        style_prefix "tabs"
        textbutton "KRIS" xpos 364 ypos 130 action Hide("galleryu"), Show("galleryk"), SetVariable("selected_char", "kris")
        textbutton "HEATH" xpos 535 ypos 84 action Hide("galleryu"), Show("galleryh"), SetVariable("selected_char", "heath")
        textbutton "ASPEN" xpos 717 ypos 34 action Hide("galleryu"), Show("gallerya"), SetVariable("selected_char", "aspen")
        textbutton "CC" xpos 924 ypos -14 action Hide("galleryu"), Show("galleryc"), SetVariable("selected_char", "cc")
        textbutton "ROB" xpos 1100 ypos -63 action Hide("galleryu"), Show("galleryr"), SetVariable("selected_char", "rob")
        textbutton "GREG" xpos 1265 ypos -112 action Hide("galleryu"), Show("galleryg"), SetVariable("selected_char", "gregory")
        textbutton "xxx" xpos 1460 ypos -160 action NullAction()



screen fullcutscene1:
    add "characters/[selected_char]/[selected_char] cutscene 1.png"
    imagebutton idle "gui/back.png" action Hide("fullcutscene1", transition=gallswitch)

screen fullcutscene2:
    add "characters/[selected_char]/[selected_char] cutscene 2.png"
    imagebutton idle "gui/back.png" action Hide("fullcutscene2", transition=gallswitch)