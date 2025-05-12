screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))

define gui.slot_button_text_selected_hover_color = gui.hover_color
define config.thumbnail_width = 384
define config.thumbnail_height = 216

define gui.file_slot_cols = 1
define gui.file_slot_rows = 2

screen behindoverlay():
    add "gui/options/black.png"

screen file_slots():
    add "gui/loadscreen.png"
    imagebutton idle "gui/back.png" action Hide("file_slots", transition=easeoutbottom)

    vbox spacing 25:

        at transform:
            rotate -14
            rotate_pad False
        
        for i in range(2):
            $ slot = i + 1

            button:
                xysize (585, 330)
                xpos 28
                ypos 390
                background "#59577d"
                action FileAction(slot)

                add FileScreenshot(slot) xalign 0.5

                key "save_delete" action FileDelete(slot) 