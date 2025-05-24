screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))

define gui.slot_button_text_selected_hover_color = gui.hover_color
define config.thumbnail_width = 585
define config.thumbnail_height = 330

define gui.file_slot_cols = 1
define gui.file_slot_rows = 2

screen behindoverlay():
    add "gui/options/black.png"

screen file_slots():
    modal True
    add "gui/loadscreen.png"

    dismiss action Hide("file_slots", transition=easeoutbottom), Play("sound", "sfx/paperclose.ogg")

    vbox spacing -30:

        at transform:
            rotate -14
            rotate_pad False
        
        for i in range(2):
            $ slot = i + 1

            button:
                xysize (585, 330)
                xpos 28
                ypos 390
                background None
                action FileAction(slot)

                add FileScreenshot(slot) xalign 0.5

                key "save_delete" action FileDelete(slot)
            
            vbox spacing 5:
                imagebutton idle "gui/loadbutton2.png" action FileLoad(slot) xpos 580 ypos 80
            
            vbox spacing 5:
                imagebutton idle "gui/savedelete.png" action FileDelete(slot) at delete_tilt xpos -125 ypos 165
    