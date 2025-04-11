default persistent.hicon = False
default persistent.screenshake = True
default persistent.monochrome = False
default persistent.mset = ""
default persistent.flash = True

default persistent.advcap = False
default persistent.narrator = False

default persistent.fullscreen = True

default persistent.skipop1 = False
default persistent.skipop2 = False
default persistent.skipop3 = False

default persistent.bluroption = "0"
#default vidset = "off"

style fileblu_button_text:
    font "terminal-grotesque.ttf"
    color "#f0f0f0"
    hover_color "#94bbe3"

screen pref_audio:
    tag pref
    modal True
    style_prefix "fileblu"
    textbutton "<<< back" action Hide("pref_audio", transition=easeoutbottom), SetVariable("options_visible", True) ypos 20 xpos 20
    add "gui/options/audio.png"

    vbox:
        style_prefix "slider"
        bar value Preference("music volume") at ab_tilt yanchor -45 xanchor -350

        bar value Preference("voice volume") at ab_tilt yanchor 485 xanchor -365

        bar value Preference("sound volume") at ab_tilt yanchor 1010 xanchor -380

    hbox:
        imagebutton idle "gui/fileempty.png" action Hide("pref_audio"), Show("pref_video") xpos 640 ypos 120
        imagebutton idle "gui/fileempty.png" action Hide("pref_audio"), Show("pref_other") xpos 710 ypos 120
    
    # checkboxes
    hbox:
        imagebutton idle "gui/options/check_[persistent.advcap].png" xpos 388 ypos 685 action ToggleVariable("persistent.advcap") at ab_tilt
        imagebutton idle "gui/options/check_[persistent.narrator].png" xpos 290 ypos 838 action ToggleVariable("persistent.narrator"), Preference("self voicing", "toggle") at ab_tilt



screen pref_video:
    modal True
    tag pref
    style_prefix "fileblu"
    textbutton "<<< back" action Hide("pref_video", transition=easeoutbottom), SetVariable("options_visible", True) ypos 20 xpos 20
    add "gui/options/video.png"

    hbox:
        imagebutton idle "gui/fileempty.png" action Hide("pref_video"), Show("pref_audio") xpos 320 ypos 120
        imagebutton idle "gui/fileempty.png" action Hide("pref_video"), Show("pref_other") xpos 710 ypos 120

    # FULLSCREEN BUTTONS

    fixed:
        if persistent.fullscreen == True:
            imagebutton idle "gui/options/off.png" xpos 1290 ypos 505 action ToggleVariable("persistent.fullscreen"), Preference("display", "fullscreen")
            add "gui/options/on.png" xpos 1290 ypos 675
        if persistent.fullscreen == False:
            imagebutton idle "gui/options/off.png" xpos 1290 ypos 675 action ToggleVariable("persistent.fullscreen"), Preference("display", "window")
            add "gui/options/on.png" xpos 1290 ypos 505
    
    # ACCESSIBILITY BUTTONS

    fixed:
        if persistent.hicon == False:
            imagebutton idle "gui/options/hicon_[persistent.hicon].png" action ToggleVariable("persistent.hicon"), Preference("high contrast text", "enable") focus_mask True
        elif persistent.hicon == True:
            imagebutton idle "gui/options/hicon_[persistent.hicon].png" action ToggleVariable("persistent.hicon"), Preference("high contrast text", "disable") focus_mask True
        imagebutton idle "gui/options/screenshake_[persistent.screenshake].png" action ToggleVariable("persistent.screenshake") focus_mask True
        if persistent.monochrome == False:
            imagebutton idle "gui/options/monochrome_[persistent.monochrome].png" action ToggleVariable("persistent.monochrome"), SetVariable("persistent.mset", "monochrome/m_") focus_mask True
        elif persistent.monochrome == True:
            imagebutton idle "gui/options/monochrome_[persistent.monochrome].png" action ToggleVariable("persistent.monochrome"), SetVariable("persistent.mset", "") focus_mask True
        imagebutton idle "gui/options/flash_[persistent.flash].png" action ToggleVariable("persistent.flash") focus_mask True
    
    # SKIP BUTTONS
    vbox:
        imagebutton idle "gui/options/check_[persistent.skipop1].png" xpos 837 ypos 564 action ToggleVariable("persistent.skipop1"), Preference("skip", "toggle")
        imagebutton idle "gui/options/check_[persistent.skipop2].png" xpos 835 ypos 570 action ToggleVariable("persistent.skipop2"), Preference("after choices", "toggle")
        imagebutton idle "gui/options/check_[persistent.skipop3].png" xpos 835 ypos 565 action ToggleVariable("persistent.skipop3"), InvertSelected(Preference("transitions", "toggle"))

    # sliders
    vbox:
        style_prefix "slider"
        bar value Preference("text speed") xpos 850 ypos 315

        bar value Preference("auto-forward time") xpos 850 ypos 365
    
    # blur box
    fixed:
        add "gui/options/[persistent.mset]blurempty.png" xpos 795 ypos 940
        add "gui/options/[persistent.mset]blur[persistent.bluroption].png" xpos 795 ypos 940
        imagebutton idle "gui/options/emptyblurbutton.png" xpos 805 ypos 955 action SetVariable("persistent.bluroption", "0")
        imagebutton idle "gui/options/emptyblurbutton.png" xpos 880 ypos 955 action SetVariable("persistent.bluroption", "1")
        imagebutton idle "gui/options/emptyblurbutton.png" xpos 955 ypos 955 action SetVariable("persistent.bluroption", "2")
        imagebutton idle "gui/options/emptyblurbutton.png" xpos 1030 ypos 955 action SetVariable("persistent.bluroption", "3")
        imagebutton idle "gui/options/emptyblurbutton.png" xpos 1105 ypos 955 action SetVariable("persistent.bluroption", "4")
        imagebutton idle "gui/options/emptyblurbutton.png" xpos 1180 ypos 955 action SetVariable("persistent.bluroption", "5")
    

screen pref_other:
    modal True
    tag pref
    style_prefix "fileblu"
    textbutton "<<< back" action Hide("pref_other", transition=easeoutbottom), SetVariable("options_visible", True) ypos 20 xpos 20
    add "gui/options/other.png"

    hbox:
        imagebutton idle "gui/fileempty.png" action Hide("pref_other"), Show("pref_video") xpos 640 ypos 120
        imagebutton idle "gui/fileempty.png" action Hide("pref_other"), Show("pref_audio") xpos 130 ypos 120
    
    #vbox:
        #imagebutton idle "gui/options/delete.png" xpos 500 ypos 500


# imagebutton for options on mm
screen pref_open():
    imagebutton idle "gui/optionsopen.png" action Show("pref_audio", transition=easeinbottom), SetVariable("options_visible", False) xpos 1010 ypos 980