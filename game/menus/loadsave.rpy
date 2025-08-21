screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))

define gui.slot_button_text_selected_hover_color = gui.hover_color
define config.thumbnail_width = 430
define config.thumbnail_height = 240

define gui.file_slot_cols = 2
define gui.file_slot_rows = 3

screen behindoverlay():
    add "gui/options/black.png"

screen file_slots(): # i KNOW this is not efficient OKAY i KNOW this is cobbled together VERY HASTILY okAY I'M AWARE
# do not tell me my code is bad, i know, its FINE! it works and idc about anything else
    modal True
    add "gui/loadscreen.png"

    if savequestionpopup == False:
        dismiss action Hide("file_slots", transition=easeoutbottom), Play("sound", "sfx/paperclose.ogg")
    else:
        dismiss action Hide("file_slots", transition=easeoutbottom), Play("sound", "sfx/paperclose.ogg"), SetVariable("savequestionpopup", "False"), Jump("battle")

    fixed:
        button:
            xysize (430, 242)
            xpos 298
            ypos 218
            background None
            action FileLoad(1)

            add FileScreenshot(1) xsize 430 ysize 242

            key "save_delete" action FileDelete(1)
        
        imagebutton idle "gui/savebutton.png" action SetVariable("preferences.afm_enable", False), FileSave(1) xpos 795 ypos 335
        imagebutton idle "gui/deletebutton.png" action SetVariable("preferences.afm_enable", False), FileDelete(1) xpos 770 ypos 400
    
    fixed:
        button:
            xysize (430, 242)
            xpos 298
            ypos 472
            background None
            action FileLoad(2)

            add FileScreenshot(2) xsize 430 ysize 242

            key "save_delete" action FileDelete(2)
        
        imagebutton idle "gui/savebutton.png" action SetVariable("preferences.afm_enable", False), FileSave(2) xpos 795 ypos 589
        imagebutton idle "gui/deletebutton.png" action SetVariable("preferences.afm_enable", False), FileDelete(2) xpos 770 ypos 654
    
    fixed:
        button:
            xysize (430, 242)
            xpos 298
            ypos 726
            background None
            action FileLoad(3)

            add FileScreenshot(3) xsize 430 ysize 242

            key "save_delete" action FileDelete(3)
        
        imagebutton idle "gui/savebutton.png" action SetVariable("preferences.afm_enable", False), FileSave(3) xpos 795 ypos 843
        imagebutton idle "gui/deletebutton.png" action SetVariable("preferences.afm_enable", False), FileDelete(3) xpos 770 ypos 908
    
    fixed:
        button:
            xysize (430, 242)
            xpos 975
            ypos 218
            background None
            action FileLoad(4)

            add FileScreenshot(4) xsize 430 ysize 242

            key "save_delete" action FileDelete(4)
        
        imagebutton idle "gui/savebutton.png" action SetVariable("preferences.afm_enable", False), FileSave(4) xpos 1472 ypos 335
        imagebutton idle "gui/deletebutton.png" action SetVariable("preferences.afm_enable", False), FileDelete(4) xpos 1447 ypos 400
    
    fixed:
        button:
            xysize (430, 242)
            xpos 975
            ypos 472
            background None
            action FileLoad(5)

            add FileScreenshot(5) xsize 430 ysize 242

            key "save_delete" action FileDelete(5)
        
        imagebutton idle "gui/savebutton.png" action SetVariable("preferences.afm_enable", False), FileSave(5) xpos 1472 ypos 589
        imagebutton idle "gui/deletebutton.png" action SetVariable("preferences.afm_enable", False), FileDelete(5) xpos 1447 ypos 654
    
    fixed:
        button:
            xysize (430, 242)
            xpos 975
            ypos 726
            background None
            action FileLoad(6)

            add FileScreenshot(6) xsize 430 ysize 242

            key "save_delete" action FileDelete(6)
        
        imagebutton idle "gui/savebutton.png" action SetVariable("preferences.afm_enable", False), FileSave(6) xpos 1472 ypos 843
        imagebutton idle "gui/deletebutton.png" action SetVariable("preferences.afm_enable", False), FileDelete(6) xpos 1447 ypos 908
    