default persistent.hicon = False
default persistent.screenshake = True
default persistent.monochrome = False
default persistent.flash = True
#default vidset = "off"

style fileblu_button_text:
    font "terminal-grotesque.ttf"
    color "#f0f0f0"
    hover_color "#94bbe3"

screen pref_audio:
    style_prefix "fileblu"
    textbutton "<<< back" action Hide("pref_audio", transition=easeoutbottom) ypos 20 xpos 20
    add "gui/options/audio.png"

    vbox:
        style_prefix "slider"
        bar value Preference("music volume") at ab_tilt yanchor -45 xanchor -350

        bar value Preference("voice volume") at ab_tilt yanchor 485 xanchor -365

        bar value Preference("sound volume") at ab_tilt yanchor 1010 xanchor -380

    hbox:
        imagebutton idle "gui/fileempty.png" action Hide("pref_audio"), Show("pref_video") xpos 640 ypos 120
        imagebutton idle "gui/fileempty.png" action Hide("pref_audio"), Show("pref_other") xpos 710 ypos 120

screen pref_video:
    # if hicon or screenshake or monochrome or flashing == False:
    #     $ vidset = "off"
    # if hicon or screenshake or monochrome or flashing == True:
    #     $ vidset = "on"

    style_prefix "fileblu"
    textbutton "<<< back" action Hide("pref_video", transition=easeoutbottom) ypos 20 xpos 20
    add "gui/options/video.png"

    hbox:
        imagebutton idle "gui/fileempty.png" action Hide("pref_video"), Show("pref_audio") xpos 320 ypos 120
        imagebutton idle "gui/fileempty.png" action Hide("pref_video"), Show("pref_other") xpos 710 ypos 120

    # ACCESSIBILITY BUTTONS

    fixed:
        if persistent.hicon == False:
            imagebutton idle "gui/options/off1.png" action SetVariable("persistent.hicon", True) focus_mask True
        if persistent.hicon == True:
            imagebutton idle "gui/options/on1.png" action SetVariable("persistent.hicon", False) focus_mask True

        if persistent.screenshake == False:
            imagebutton idle "gui/options/off2.png" action SetVariable("persistent.screenshake", True) focus_mask True
        if persistent.screenshake == True:
            imagebutton idle "gui/options/on2.png" action SetVariable("persistent.screenshake", False) focus_mask True

        if persistent.monochrome == False:
            imagebutton idle "gui/options/off3.png" action SetVariable("persistent.monochrome", True) focus_mask True
        if persistent.monochrome == True:
            imagebutton idle "gui/options/on3.png" action SetVariable("persistent.monochrome", False) focus_mask True

        if persistent.flash == False:
            imagebutton idle "gui/options/off4.png" action SetVariable("persistent.flash", True) focus_mask True
        if persistent.flash == True:
            imagebutton idle "gui/options/on4.png" action SetVariable("persistent.flash", False) focus_mask True
        
        # i feel like this could be done a lot cleaner... need to get suggestions

screen pref_other:
    style_prefix "fileblu"
    textbutton "<<< back" action Hide("pref_other", transition=easeoutbottom) ypos 20 xpos 20
    add "gui/options/other.png"

    hbox:
        imagebutton idle "gui/fileempty.png" action Hide("pref_other"), Show("pref_video") xpos 640 ypos 120
        imagebutton idle "gui/fileempty.png" action Hide("pref_other"), Show("pref_audio") xpos 130 ypos 120