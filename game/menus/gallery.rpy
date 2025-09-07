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

style tabs_text:
    font "chawp.ttf"
    color "#130909"
    size 35

screen gallerye():
    modal True
    tag gallery
    imagebutton idle "gui/back.png" action Hide("gallerye", transition=easeoutbottom), Play("sound", "sfx/paperclose.ogg")

    imagebutton idle "gui/gallery/gallery.png" focus_mask True action Show("galleryk")
    add "gui/gallery/redfile.png"

    if persistent.ec1 == False:
        add "gui/gallery/area1.png"
    else:
        imagebutton idle "characters/esther/esther lose.png" at egal_size1 xpos 320 ypos 100 action Show("fullelose", transition=gallswitch)
        add "gui/gallery/tape1.png"

    if persistent.ec2 == False:
        add "gui/gallery/area2.png"
    else:
        imagebutton idle "characters/esther/esther death.png" at egal_size2 xpos 820 ypos 350 action Show("fulledeath", transition=gallswitch)
        add "gui/gallery/tape2.png"
    
    fixed:
        style_prefix "tabs"
        text "M. ESTHER" xpos 362 ypos 142

screen galleryefull():
    modal True
    tag gallery
    imagebutton idle "gui/back.png" action Hide("galleryefull", transition=easeoutbottom), Play("sound", "sfx/paperclose.ogg")

    imagebutton idle "gui/gallery/gallery.png" focus_mask True action Show("galleryk")
    add "gui/gallery/pinkfile.png"

    fixed:
        if persistent.ec1 == True:
            imagebutton idle "characters/esther/esther lose.png" action Show("fullelose", transition=gallswitch) at gallery_size xpos 300 ypos 216
        if persistent.ec2 == True:
            imagebutton idle "characters/esther/esther death.png" action Show("fulledeath", transition=gallswitch) at gallery_size xpos 750 ypos 216
        if persistent.ec3 == True:
            imagebutton idle "characters/esther/esther cutscene 3.png" action Show("fulle3", transition=gallswitch) at gallery_size xpos 300 ypos 480
        if persistent.ec4 == True:
            imagebutton idle "characters/esther/esther cutscene 4.png" action Show("fulle4", transition=gallswitch) at gallery_size xpos 750 ypos 480
        if persistent.ec5 == True:
            imagebutton idle "characters/esther/esther cutscene 5.png" action Show("fulle5", transition=gallswitch) at gallery_size xpos 300 ypos 744
    
    fixed:
        style_prefix "tabs"
        text "M. ESTHER" xpos 362 ypos 142

screen fulledeath():
    modal True
    add "characters/esther/esther death.png"
    imagebutton idle "gui/back.png" action Hide("fulledeath", transition=gallswitch)

screen fullelose():
    modal True
    add "characters/esther/esther lose.png"
    imagebutton idle "gui/back.png" action Hide("fullelose", transition=gallswitch)

#yes i know i could just add a selectedchar variable for miss esther but im lazy <3
screen fulle3():
    modal True
    add "characters/esther/esther cutscene 3.png"
    imagebutton idle "gui/back.png" action Hide("fulle3", transition=gallswitch)

screen fulle4():
    modal True
    add "characters/esther/esther cutscene 4.png"
    imagebutton idle "gui/back.png" action Hide("fulle4", transition=gallswitch)

screen fulle5():
    modal True
    add "characters/esther/esther cutscene 5.png"
    imagebutton idle "gui/back.png" action Hide("fulle5", transition=gallswitch)

####################################################
# MAIN GALLERY
####################################################

screen galleryk():
    modal True
    tag gallery
    style_prefix "file"
    imagebutton idle "gui/back.png" action Hide("galleryk", transition=easeoutbottom), Play("sound", "sfx/paperclose.ogg")

    if persistent.ec3 == True:
        imagebutton idle "gui/gallery/classifiedpink.png" focus_mask True action Show("galleryefull")
    elif persistent.ec1 == True or persistent.ec2 == True and persistent.ec3 == False:
        imagebutton idle "gui/gallery/classified.png" focus_mask True action Show("gallerye")
 
    if persistent.kgunlock == False:
        add "gui/gallery/krislocked.png"
    else:
        add "gui/gallery/krisunlocked.png"

    fixed:
        if persistent.kc1 == True:
            imagebutton idle "characters/kris/kris cutscene 1.png" action Show("fullcutscene1", transition=gallswitch) at gallery_size xpos 300 ypos 216
        if persistent.kc2 == True:
            imagebutton idle "characters/kris/kris cutscene 2.png" action Show("fullcutscene2", transition=gallswitch) at gallery_size xpos 750 ypos 216
        if persistent.kc3 == True:
            imagebutton idle "characters/kris/kris cutscene 3.png" action Show("fullcutscene3", transition=gallswitch) at gallery_size xpos 300 ypos 480
        if persistent.kc4 == True:
            imagebutton idle "characters/kris/kris cutscene 4.png" action Show("fullcutscene4", transition=gallswitch) at gallery_size xpos 750 ypos 480
        if persistent.kc5 == True:
            imagebutton idle "characters/kris/kris cutscene 5.png" action Show("fullcutscene5", transition=gallswitch) at gallery_size xpos 300 ypos 744
        if persistent.kc6 == True:
            imagebutton idle "characters/kris/kris cutscene 6.png" action Show("fullcutscene6", transition=gallswitch) at gallery_size xpos 750 ypos 744
    vbox:
        style_prefix "tabs"
        textbutton "KRIS" xpos 364 ypos 130 action NullAction()
        textbutton "HEATH" xpos 535 ypos 84 action Show("galleryh"), SetVariable("selected_char", "heath")
        textbutton "ASPEN" xpos 717 ypos 34 action Show("gallerya"), SetVariable("selected_char", "aspen")
        textbutton "CC" xpos 924 ypos -14 action Show("galleryc"), SetVariable("selected_char", "cc")
        textbutton "ROB" xpos 1100 ypos -63 action Show("galleryr"), SetVariable("selected_char", "rob")
        textbutton "GREG" xpos 1265 ypos -112 action Show("galleryg"), SetVariable("selected_char", "gregory")
        textbutton "          " xpos 1460 ypos -160 action Show("galleryu"), SetVariable("selected_char", "unknown")

screen galleryh():
    tag gallery
    modal True
    style_prefix "file"
    imagebutton idle "gui/back.png" action Hide("galleryh", transition=easeoutbottom), Play("sound", "sfx/paperclose.ogg")

    if persistent.ec3 == True:
        imagebutton idle "gui/gallery/classifiedpink.png" focus_mask True action Show("galleryefull")
    elif persistent.ec1 == True or persistent.ec2 == True:
        imagebutton idle "gui/gallery/classified.png" focus_mask True action Show("gallerye")

    if persistent.hgunlock == False:
        add "gui/gallery/heathlocked.png"
    else:
        add "gui/gallery/heathunlocked.png"

    fixed:
        if persistent.hc1 == True:
            imagebutton idle "characters/heath/heath cutscene 1.png" action Show("fullcutscene1", transition=gallswitch) at gallery_size xpos 300 ypos 216
        if persistent.hc2 == True:
            imagebutton idle "characters/heath/heath cutscene 2.png" action Show("fullcutscene2", transition=gallswitch) at gallery_size xpos 750 ypos 216
        if persistent.hc3 == True:
            imagebutton idle "characters/heath/heath cutscene 3.png" action Show("fullcutscene3", transition=gallswitch) at gallery_size xpos 300 ypos 480
        if persistent.hc4 == True:
            imagebutton idle "characters/heath/heath cutscene 4.png" action Show("fullcutscene4", transition=gallswitch) at gallery_size xpos 750 ypos 480
        if persistent.hc5 == True:
            imagebutton idle "characters/heath/heath cutscene 5.png" action Show("fullcutscene5", transition=gallswitch) at gallery_size xpos 300 ypos 744
        if persistent.hc6 == True:
            imagebutton idle "characters/heath/heath cutscene 6.png" action Show("fullcutscene6", transition=gallswitch) at gallery_size xpos 750 ypos 744
    vbox:
        style_prefix "tabs"
        textbutton "KRIS" xpos 364 ypos 130 action Show("galleryk"), SetVariable("selected_char", "kris")
        textbutton "HEATH" xpos 535 ypos 84 action NullAction()
        textbutton "ASPEN" xpos 717 ypos 34 action Show("gallerya"), SetVariable("selected_char", "aspen")
        textbutton "CC" xpos 924 ypos -14 action Show("galleryc"), SetVariable("selected_char", "cc")
        textbutton "ROB" xpos 1100 ypos -63 action Show("galleryr"), SetVariable("selected_char", "rob")
        textbutton "GREG" xpos 1265 ypos -112 action Show("galleryg"), SetVariable("selected_char", "gregory")
        textbutton "          " xpos 1460 ypos -160 action Show("galleryu"), SetVariable("selected_char", "unknown")

screen gallerya():
    tag gallery
    modal True
    style_prefix "file"
    imagebutton idle "gui/back.png" action Hide("gallerya", transition=easeoutbottom), Play("sound", "sfx/paperclose.ogg")

    if persistent.ec3 == True:
        imagebutton idle "gui/gallery/classifiedpink.png" focus_mask True action Show("galleryefull")
    elif persistent.ec1 == True or persistent.ec2 == True:
        imagebutton idle "gui/gallery/classified.png" focus_mask True action Show("gallerye")

    if persistent.agunlock == False:
        add "gui/gallery/aspenlocked.png"
    else:
        add "gui/gallery/aspenunlocked.png"
    
    fixed:
        if persistent.ac1 == True:
            imagebutton idle "characters/aspen/aspen cutscene 1.png" action Show("fullcutscene1", transition=gallswitch) at gallery_size xpos 300 ypos 216
        if persistent.ac2 == True:
            imagebutton idle "characters/aspen/aspen cutscene 2.png" action Show("fullcutscene2", transition=gallswitch) at gallery_size xpos 750 ypos 216
        if persistent.ac3 == True:
            imagebutton idle "characters/aspen/aspen cutscene 3.png" action Show("fullcutscene3", transition=gallswitch) at gallery_size xpos 300 ypos 480
        if persistent.ac4 == True:
            imagebutton idle "characters/aspen/aspen cutscene 4.png" action Show("fullcutscene4", transition=gallswitch) at gallery_size xpos 750 ypos 480
        if persistent.ac5 == True:
            imagebutton idle "characters/aspen/aspen cutscene 5.png" action Show("fullcutscene5", transition=gallswitch) at gallery_size xpos 300 ypos 744
        if persistent.ac6 == True:
            imagebutton idle "characters/aspen/aspen cutscene 6.png" action Show("fullcutscene6", transition=gallswitch) at gallery_size xpos 750 ypos 744
    
    vbox:
        style_prefix "tabs"
        textbutton "KRIS" xpos 364 ypos 130 action Show("galleryk"), SetVariable("selected_char", "kris")
        textbutton "HEATH" xpos 535 ypos 84 action Show("galleryh"), SetVariable("selected_char", "heath")
        textbutton "ASPEN" xpos 717 ypos 34 action NullAction()
        textbutton "CC" xpos 924 ypos -14 action Show("galleryc"), SetVariable("selected_char", "cc")
        textbutton "ROB" xpos 1100 ypos -63 action Show("galleryr"), SetVariable("selected_char", "rob")
        textbutton "GREG" xpos 1265 ypos -112 action Show("galleryg"), SetVariable("selected_char", "gregory")
        textbutton "          " xpos 1460 ypos -160 action Show("galleryu"), SetVariable("selected_char", "unknown")

screen galleryc():
    tag gallery
    modal True
    style_prefix "file"
    imagebutton idle "gui/back.png" action Hide("galleryc", transition=easeoutbottom), Play("sound", "sfx/paperclose.ogg")

    if persistent.ec3 == True:
        imagebutton idle "gui/gallery/classifiedpink.png" focus_mask True action Show("galleryefull")
    elif persistent.ec3 == True:
        imagebutton idle "gui/gallery/classifiedpink.png" focus_mask True action Show("galleryefull")
    elif persistent.ec1 == True or persistent.ec2 == True:
        imagebutton idle "gui/gallery/classified.png" focus_mask True action Show("gallerye")

    if persistent.cgunlock == False:
        add "gui/gallery/cclocked.png"
    else:
        add "gui/gallery/ccunlocked.png"

    fixed:
        if persistent.cc1 == True:
            imagebutton idle "characters/cc/cc cutscene 1.png" action Show("fullcutscene1", transition=gallswitch) at gallery_size xpos 300 ypos 216
        if persistent.cc2 == True:
            imagebutton idle "characters/cc/cc cutscene 2.png" action Show("fullcutscene2", transition=gallswitch) at gallery_size xpos 750 ypos 216
        if persistent.cc3 == True:
            imagebutton idle "characters/cc/cc cutscene 3.png" action Show("fullcutscene3", transition=gallswitch) at gallery_size xpos 300 ypos 480
        if persistent.cc4 == True:
            imagebutton idle "characters/cc/cc cutscene 4.png" action Show("fullcutscene4", transition=gallswitch) at gallery_size xpos 750 ypos 480
        if persistent.cc5 == True:
            imagebutton idle "characters/cc/cc cutscene 5.png" action Show("fullcutscene5", transition=gallswitch) at gallery_size xpos 300 ypos 744
        if persistent.cc6 == True:
            imagebutton idle "characters/cc/cc cutscene 6.png" action Show("fullcutscene6", transition=gallswitch) at gallery_size xpos 750 ypos 744
    
    vbox:
        style_prefix "tabs"
        textbutton "KRIS" xpos 364 ypos 130 action Show("galleryk"), SetVariable("selected_char", "kris")
        textbutton "HEATH" xpos 535 ypos 84 action Show("galleryh"), SetVariable("selected_char", "heath")
        textbutton "ASPEN" xpos 717 ypos 34 action Show("gallerya"), SetVariable("selected_char", "aspen")
        textbutton "CC" xpos 924 ypos -14 action NullAction()
        textbutton "ROB" xpos 1100 ypos -63 action Show("galleryr"), SetVariable("selected_char", "rob")
        textbutton "GREG" xpos 1265 ypos -112 action Show("galleryg"), SetVariable("selected_char", "gregory")
        textbutton "          " xpos 1460 ypos -160 action Show("galleryu"), SetVariable("selected_char", "unknown")

screen galleryr():
    tag gallery
    modal True
    style_prefix "file"
    imagebutton idle "gui/back.png" action Hide("galleryr", transition=easeoutbottom), Play("sound", "sfx/paperclose.ogg")

    if persistent.ec3 == True:
        imagebutton idle "gui/gallery/classifiedpink.png" focus_mask True action Show("galleryefull")
    elif persistent.ec1 == True or persistent.ec2 == True:
        imagebutton idle "gui/gallery/classified.png" focus_mask True action Show("gallerye")

    if persistent.rgunlock == False:
        add "gui/gallery/roblocked.png"
    else:
        add "gui/gallery/robunlocked.png"
    
    fixed:
        if persistent.rc1 == True:
            imagebutton idle "characters/rob/rob cutscene 1.png" action Show("fullcutscene1", transition=gallswitch) at gallery_size xpos 300 ypos 216
        if persistent.rc2 == True:
            imagebutton idle "characters/rob/rob cutscene 2.png" action Show("fullcutscene2", transition=gallswitch) at gallery_size xpos 750 ypos 216
        if persistent.rc3 == True:
            imagebutton idle "characters/rob/rob cutscene 3.png" action Show("fullcutscene3", transition=gallswitch) at gallery_size xpos 300 ypos 480
        if persistent.rc4 == True:
            imagebutton idle "characters/rob/rob cutscene 4.png" action Show("fullcutscene4", transition=gallswitch) at gallery_size xpos 750 ypos 480
        if persistent.rc5 == True:
            imagebutton idle "characters/rob/rob cutscene 5.png" action Show("fullcutscene5", transition=gallswitch) at gallery_size xpos 300 ypos 744
        if persistent.rc6 == True:
            imagebutton idle "characters/rob/rob cutscene 6.png" action Show("fullcutscene6", transition=gallswitch) at gallery_size xpos 750 ypos 744
        
    vbox:
        style_prefix "tabs"
        textbutton "KRIS" xpos 364 ypos 130 action Show("galleryk"), SetVariable("selected_char", "kris")
        textbutton "HEATH" xpos 535 ypos 84 action Show("galleryh"), SetVariable("selected_char", "heath")
        textbutton "ASPEN" xpos 717 ypos 34 action Show("gallerya"), SetVariable("selected_char", "aspen")
        textbutton "CC" xpos 924 ypos -14 action Show("galleryc"), SetVariable("selected_char", "cc")
        textbutton "ROB" xpos 1100 ypos -63 action NullAction()
        textbutton "GREG" xpos 1265 ypos -112 action Show("galleryg"), SetVariable("selected_char", "gregory")
        textbutton "          " xpos 1460 ypos -160 action Show("galleryu"), SetVariable("selected_char", "unknown")

screen galleryg():
    tag gallery
    modal True
    style_prefix "file"
    imagebutton idle "gui/back.png" action Hide("galleryg", transition=easeoutbottom), Play("sound", "sfx/paperclose.ogg")

    if persistent.ec3 == True:
        imagebutton idle "gui/gallery/classifiedpink.png" focus_mask True action Show("galleryefull")
    elif persistent.ec1 == True or persistent.ec2 == True:
        imagebutton idle "gui/gallery/classified.png" focus_mask True action Show("gallerye")

    if persistent.ggunlock == False:
        add "gui/gallery/gregorylocked.png"
    else:
        add "gui/gallery/gregoryunlocked.png"

    fixed:
        if persistent.gc1 == True:
            imagebutton idle "characters/gregory/gregory cutscene 1.png" action Show("fullcutscene1", transition=gallswitch) at gallery_size xpos 300 ypos 216
        if persistent.gc2 == True:
            imagebutton idle "characters/gregory/gregory cutscene 2.png" action Show("fullcutscene2", transition=gallswitch) at gallery_size xpos 750 ypos 216
        if persistent.gc3 == True:
            imagebutton idle "characters/gregory/gregory cutscene 3.png" action Show("fullcutscene3", transition=gallswitch) at gallery_size xpos 300 ypos 480
        if persistent.gc4 == True:
            imagebutton idle "characters/gregory/gregory cutscene 4.png" action Show("fullcutscene4", transition=gallswitch) at gallery_size xpos 750 ypos 480
        if persistent.gc5 == True:
            imagebutton idle "characters/gregory/gregory cutscene 5.png" action Show("fullcutscene5", transition=gallswitch) at gallery_size xpos 300 ypos 744

    vbox:
        style_prefix "tabs"
        textbutton "KRIS" xpos 364 ypos 130 action Show("galleryk"), SetVariable("selected_char", "kris")
        textbutton "HEATH" xpos 535 ypos 84 action Show("galleryh"), SetVariable("selected_char", "heath")
        textbutton "ASPEN" xpos 717 ypos 34 action Show("gallerya"), SetVariable("selected_char", "aspen")
        textbutton "CC" xpos 924 ypos -14 action Show("galleryc"), SetVariable("selected_char", "cc")
        textbutton "ROB" xpos 1100 ypos -63 action Show("galleryr"), SetVariable("selected_char", "rob")
        textbutton "GREG" xpos 1265 ypos -112 action NullAction()
        textbutton "          " xpos 1460 ypos -160 action Show("galleryu"), SetVariable("selected_char", "unknown")

screen galleryu():
    tag gallery
    modal True
    style_prefix "file"
    imagebutton idle "gui/back.png" action Hide("galleryu", transition=easeoutbottom), Play("sound", "sfx/paperclose.ogg")

    if persistent.ec3 == True:
        imagebutton idle "gui/gallery/classifiedpink.png" focus_mask True action Show("galleryefull")
    elif persistent.ec1 == True or persistent.ec2 == True:
        imagebutton idle "gui/gallery/classified.png" focus_mask True action Show("gallerye")
        
    if persistent.ugunlock == False:
        add "gui/gallery/unknownlocked.png"
    else:
        add "gui/gallery/unknownunlocked.png"

    fixed:
        if persistent.uc1 == True:
            imagebutton idle "characters/unknown/unknown cutscene 1.png" action Show("fullcutscene1", transition=gallswitch) at gallery_size xpos 300 ypos 216
        if persistent.uc2 == True:
            imagebutton idle "characters/unknown/unknown cutscene 2.png" action Show("fullcutscene2", transition=gallswitch) at gallery_size xpos 750 ypos 216
        if persistent.uc3 == True:
            imagebutton idle "characters/unknown/unknown cutscene 3.png" action Show("fullcutscene3", transition=gallswitch) at gallery_size xpos 300 ypos 480
        if persistent.uc4 == True:
            imagebutton idle "characters/unknown/unknown cutscene 4.png" action Show("fullcutscene4", transition=gallswitch) at gallery_size xpos 750 ypos 480
        if persistent.uc5 == True:
            imagebutton idle "characters/unknown/unknown cutscene 5.png" action Show("fullcutscene5", transition=gallswitch) at gallery_size xpos 300 ypos 744

    vbox:
        style_prefix "tabs"
        textbutton "KRIS" xpos 364 ypos 130 action Show("galleryk"), SetVariable("selected_char", "kris")
        textbutton "HEATH" xpos 535 ypos 84 action Show("galleryh"), SetVariable("selected_char", "heath")
        textbutton "ASPEN" xpos 717 ypos 34 action Show("gallerya"), SetVariable("selected_char", "aspen")
        textbutton "CC" xpos 924 ypos -14 action Show("galleryc"), SetVariable("selected_char", "cc")
        textbutton "ROB" xpos 1100 ypos -63 action Show("galleryr"), SetVariable("selected_char", "rob")
        textbutton "GREG" xpos 1265 ypos -112 action Show("galleryg"), SetVariable("selected_char", "gregory")
        textbutton "          " xpos 1460 ypos -160 action NullAction()



screen fullcutscene1():
    modal True
    add "characters/[selected_char]/[selected_char] cutscene 1.png"
    imagebutton idle "gui/back.png" action Hide("fullcutscene1", transition=gallswitch)

screen fullcutscene2():
    modal True
    add "characters/[selected_char]/[selected_char] cutscene 2.png"
    imagebutton idle "gui/back.png" action Hide("fullcutscene2", transition=gallswitch)

screen fullcutscene3():
    modal True
    add "characters/[selected_char]/[selected_char] cutscene 3.png"
    imagebutton idle "gui/back.png" action Hide("fullcutscene3", transition=gallswitch)

screen fullcutscene4():
    modal True
    add "characters/[selected_char]/[selected_char] cutscene 4.png"
    imagebutton idle "gui/back.png" action Hide("fullcutscene4", transition=gallswitch)

screen fullcutscene5():
    modal True
    add "characters/[selected_char]/[selected_char] cutscene 5.png"
    imagebutton idle "gui/back.png" action Hide("fullcutscene5", transition=gallswitch)

screen fullcutscene6():
    modal True
    add "characters/[selected_char]/[selected_char] cutscene 6.png"
    imagebutton idle "gui/back.png" action Hide("fullcutscene6", transition=gallswitch)