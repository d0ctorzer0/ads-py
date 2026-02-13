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

    if pageselect == 1:
        #xpos 265 ypos 180
        imagebutton auto "gui/rightarrow_%s.png" action SetVariable("pageselect", 2) xpos 1585 ypos 180
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
        
    if pageselect == 2:
        imagebutton auto "gui/leftarrow_%s.png" action SetVariable("pageselect", 1) xpos 265 ypos 180
        imagebutton auto "gui/rightarrow_%s.png" action SetVariable("pageselect", 3) xpos 1585 ypos 180
        fixed:
            button:
                xysize (430, 242)
                xpos 298
                ypos 218
                background None
                action FileLoad(7)

                add FileScreenshot(7) xsize 430 ysize 242

                key "save_delete" action FileDelete(7)
            
            imagebutton idle "gui/savebutton.png" action SetVariable("preferences.afm_enable", False), FileSave(7) xpos 795 ypos 335
            imagebutton idle "gui/deletebutton.png" action SetVariable("preferences.afm_enable", False), FileDelete(7) xpos 770 ypos 400
        
        fixed:
            button:
                xysize (430, 242)
                xpos 298
                ypos 472
                background None
                action FileLoad(8)

                add FileScreenshot(8) xsize 430 ysize 242

                key "save_delete" action FileDelete(8)
            
            imagebutton idle "gui/savebutton.png" action SetVariable("preferences.afm_enable", False), FileSave(8) xpos 795 ypos 589
            imagebutton idle "gui/deletebutton.png" action SetVariable("preferences.afm_enable", False), FileDelete(8) xpos 770 ypos 654
        
        fixed:
            button:
                xysize (430, 242)
                xpos 298
                ypos 726
                background None
                action FileLoad(9)

                add FileScreenshot(9) xsize 430 ysize 242

                key "save_delete" action FileDelete(9)
            
            imagebutton idle "gui/savebutton.png" action SetVariable("preferences.afm_enable", False), FileSave(9) xpos 795 ypos 843
            imagebutton idle "gui/deletebutton.png" action SetVariable("preferences.afm_enable", False), FileDelete(9) xpos 770 ypos 908
        
        fixed:
            button:
                xysize (430, 242)
                xpos 975
                ypos 218
                background None
                action FileLoad(10)

                add FileScreenshot(10) xsize 430 ysize 242

                key "save_delete" action FileDelete(10)
            
            imagebutton idle "gui/savebutton.png" action SetVariable("preferences.afm_enable", False), FileSave(10) xpos 1472 ypos 335
            imagebutton idle "gui/deletebutton.png" action SetVariable("preferences.afm_enable", False), FileDelete(10) xpos 1447 ypos 400
        
        fixed:
            button:
                xysize (430, 242)
                xpos 975
                ypos 472
                background None
                action FileLoad(11)

                add FileScreenshot(11) xsize 430 ysize 242

                key "save_delete" action FileDelete(11)
            
            imagebutton idle "gui/savebutton.png" action SetVariable("preferences.afm_enable", False), FileSave(11) xpos 1472 ypos 589
            imagebutton idle "gui/deletebutton.png" action SetVariable("preferences.afm_enable", False), FileDelete(11) xpos 1447 ypos 654
        
        fixed:
            button:
                xysize (430, 242)
                xpos 975
                ypos 726
                background None
                action FileLoad(12)

                add FileScreenshot(12) xsize 430 ysize 242

                key "save_delete" action FileDelete(12)
            
            imagebutton idle "gui/savebutton.png" action SetVariable("preferences.afm_enable", False), FileSave(12) xpos 1472 ypos 843
            imagebutton idle "gui/deletebutton.png" action SetVariable("preferences.afm_enable", False), FileDelete(12) xpos 1447 ypos 908

    if pageselect == 3:
        imagebutton auto "gui/leftarrow_%s.png" action SetVariable("pageselect", 2) xpos 265 ypos 180
        fixed:
            button:
                xysize (430, 242)
                xpos 298
                ypos 218
                background None
                action FileLoad(13)

                add FileScreenshot(13) xsize 430 ysize 242

                key "save_delete" action FileDelete(13)
            
            imagebutton idle "gui/savebutton.png" action SetVariable("preferences.afm_enable", False), FileSave(13) xpos 795 ypos 335
            imagebutton idle "gui/deletebutton.png" action SetVariable("preferences.afm_enable", False), FileDelete(13) xpos 770 ypos 400
        
        fixed:
            button:
                xysize (430, 242)
                xpos 298
                ypos 472
                background None
                action FileLoad(14)

                add FileScreenshot(14) xsize 430 ysize 242

                key "save_delete" action FileDelete(14)
            
            imagebutton idle "gui/savebutton.png" action SetVariable("preferences.afm_enable", False), FileSave(14) xpos 795 ypos 589
            imagebutton idle "gui/deletebutton.png" action SetVariable("preferences.afm_enable", False), FileDelete(14) xpos 770 ypos 654
        
        fixed:
            button:
                xysize (430, 242)
                xpos 298
                ypos 726
                background None
                action FileLoad(15)

                add FileScreenshot(15) xsize 430 ysize 242

                key "save_delete" action FileDelete(15)
            
            imagebutton idle "gui/savebutton.png" action SetVariable("preferences.afm_enable", False), FileSave(15) xpos 795 ypos 843
            imagebutton idle "gui/deletebutton.png" action SetVariable("preferences.afm_enable", False), FileDelete(15) xpos 770 ypos 908
        
        fixed:
            button:
                xysize (430, 242)
                xpos 975
                ypos 218
                background None
                action FileLoad(16)

                add FileScreenshot(16) xsize 430 ysize 242

                key "save_delete" action FileDelete(16)
            
            imagebutton idle "gui/savebutton.png" action SetVariable("preferences.afm_enable", False), FileSave(16) xpos 1472 ypos 335
            imagebutton idle "gui/deletebutton.png" action SetVariable("preferences.afm_enable", False), FileDelete(16) xpos 1447 ypos 400
        
        fixed:
            button:
                xysize (430, 242)
                xpos 975
                ypos 472
                background None
                action FileLoad(17)

                add FileScreenshot(17) xsize 430 ysize 242

                key "save_delete" action FileDelete(17)
            
            imagebutton idle "gui/savebutton.png" action SetVariable("preferences.afm_enable", False), FileSave(17) xpos 1472 ypos 589
            imagebutton idle "gui/deletebutton.png" action SetVariable("preferences.afm_enable", False), FileDelete(17) xpos 1447 ypos 654
        
        fixed:
            button:
                xysize (430, 242)
                xpos 975
                ypos 726
                background None
                action FileLoad(18)

                add FileScreenshot(18) xsize 430 ysize 242

                key "save_delete" action FileDelete(18)
            
            imagebutton idle "gui/savebutton.png" action SetVariable("preferences.afm_enable", False), FileSave(18) xpos 1472 ypos 843
            imagebutton idle "gui/deletebutton.png" action SetVariable("preferences.afm_enable", False), FileDelete(18) xpos 1447 ypos 908