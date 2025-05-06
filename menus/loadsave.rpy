screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))

screen behindoverlay():
    add "gui/options/black.png"

screen file_slots():
    add "gui/loadscreen.png"
    imagebutton idle "gui/back.png" action Hide("file_slots", transition=easeoutbottom)

    grid gui.file_slot_cols gui.file_slot_rows at save_tilt:
        style_prefix "slot"

        spacing 0

        for i in range(gui.file_slot_cols * gui.file_slot_rows):

            $ slot = i + 1

            vbox:
                button:
                    action FileAction(slot)

                    has vbox

                    add FileScreenshot(slot) xalign 0.5

                    key "save_delete" action FileDelete(slot) 