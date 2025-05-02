default persistent.hicon = False
default persistent.screenshake = True
default persistent.colorblind = False
default persistent.flash = True

default persistent.advcap = False
default persistent.narrator = False

default persistent.fullscreen = True

default persistent.skipop1 = False
default persistent.skipop2 = False
default persistent.skipop3 = False

default persistent.bluroption = "2"
#default vidset = "off"

init python:
    def reset_data():
        ## deletes all persistent data use with caution
        [setattr(persistent, attr, None) for attr in dir(persistent) if not attr.startswith("_")]

        ## deletes all save games use with caution!
        for slot in renpy.list_saved_games(fast=True):
            renpy.unlink_save(slot)
        ## a Ren'Py relaunch is nessesary
        renpy.quit(relaunch=True)

style fileblu_button_text:
    font "terminal-grotesque.ttf"
    color "#f0f0f0"
    hover_color "#94bbe3"

screen pref_audio:
    tag pref
    modal True
    style_prefix "fileblu"
    imagebutton idle "gui/back.png" action Hide("pref_audio", transition=easeoutbottom), SetVariable("options_visible", True)
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
    imagebutton idle "gui/back.png" action Hide("pref_video", transition=easeoutbottom), SetVariable("options_visible", True)
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
        imagebutton idle "gui/options/colorblind_[persistent.colorblind].png" action ToggleVariable("persistent.colorblind") focus_mask True
        #elif persistent.colorblind == True:
            #imagebutton idle "gui/options/colorblind_[persistent.colorblind].png" action ToggleVariable("persistent.colorblind") focus_mask True
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
        add "gui/options/blurempty.png" xpos 795 ypos 940
        add "gui/options/blur[persistent.bluroption].png" xpos 795 ypos 940
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
    imagebutton idle "gui/back.png" action Hide("pref_other", transition=easeoutbottom), SetVariable("options_visible", True)
    add "gui/options/other.png"

    hbox:
        imagebutton idle "gui/fileempty.png" action Hide("pref_other"), Show("pref_video") xpos 640 ypos 120
        imagebutton idle "gui/fileempty.png" action Hide("pref_other"), Show("pref_audio") xpos 130 ypos 120
    
    imagebutton idle "gui/options/delete.png" action Play("sound", "sfx/notif.ogg"), Show("deletenotif") xpos 625 ypos 955 focus_mask True
    
    #vbox: Function(reset_data)
        #imagebutton idle "gui/options/delete.png" xpos 500 ypos 500

style notif:
    font "fonts/terminal-grotesque.ttf"
    color "#707070"
    hover_color "#262629"
    size 40

screen deletenotif():
    modal True
    style_prefix "notif"
    add "gui/options/black.png"
    add "gui/overlay/delete_popup.png" yalign .5 xalign .5 zoom 1.2

    hbox:
        textbutton "Yes, I'm sure.":
            text_style "notif" 
            action Function(reset_data)
            xpos 600 ypos 640
        textbutton "No, go back.":
            text_style "notif"
            action Hide("deletenotif")
            xpos 900 ypos 640

# imagebutton for options on mm
screen pref_open():
    imagebutton idle "gui/optionsopen.png" action Show("pref_audio", transition=easeinbottom), SetVariable("options_visible", False) xpos 1010 ypos 980