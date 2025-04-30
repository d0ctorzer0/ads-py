screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))

screen behindoverlay():
    add "gui/options/black.png"

screen file_slots():
    use behindoverlay
    add "gui/loadscreen.png"
    textbutton _("Return"):
        style "return_button"

        action Hide("file_slots", transition=easeoutbottom)
    textbutton _("Main Menu"):
        style "return_button"

        action MainMenu()