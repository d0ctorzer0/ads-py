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

default persistent.bgtype = ""
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

screen pref_audio():
    tag pref
    modal True
    style_prefix "fileblu"
    imagebutton idle "gui/back.png" action Hide("pref_audio", transition=easeoutbottom), SetVariable("options_visible", True), Play("sound", "sfx/paperclose.ogg")
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



screen pref_video():
    modal True
    tag pref
    style_prefix "fileblu"
    imagebutton idle "gui/back.png" action Hide("pref_video", transition=easeoutbottom), SetVariable("options_visible", True), Play("sound", "sfx/paperclose.ogg")
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
    
    # image type box
    fixed:
        if persistent.bgtype == "":
            add "images/krisroom.png" at example_size xpos 915 ypos 895
        if persistent.bgtype == "p":
            add "images/pkrisroom.png" at example_size xpos 915 ypos 895
        imagebutton auto "gui/options/painted_%s.png" xpos 785 ypos 915 action SetVariable("persistent.bgtype", "p")
        imagebutton auto "gui/options/source_%s.png" xpos 785 ypos 970 action SetVariable("persistent.bgtype", "")
    

screen pref_other():
    modal True
    tag pref
    style_prefix "fileblu"
    imagebutton idle "gui/back.png" action Hide("pref_other", transition=easeoutbottom), SetVariable("options_visible", True), Play("sound", "sfx/paperclose.ogg")
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

screen mmnotif():
    modal True
    style_prefix "notif"
    add "gui/options/black.png"
    add "gui/overlay/mm_popup.png" yalign .5 xalign .5 zoom 1.2

    hbox:
        textbutton "Yes, I'm sure.":
            text_style "notif" 
            action MainMenu(confirm=False)
            xpos 600 ypos 640
        textbutton "No, go back.":
            text_style "notif"
            action Hide("mmnotif")
            xpos 900 ypos 640

screen quitnotif():
    modal True
    style_prefix "notif"
    add "gui/options/black.png"
    add "gui/overlay/quit_popup.png" yalign .5 xalign .5 zoom 1.2

    hbox:
        textbutton "Yes, I'm sure.":
            text_style "notif" 
            action Quit(confirm=False)
            xpos 600 ypos 640
        textbutton "No, go back.":
            text_style "notif"
            action Hide("quitnotif")
            xpos 900 ypos 640

# imagebutton for options on mm
screen pref_open():
    imagebutton idle "gui/optionsopen.png" action Show("pausemenu", transition=easeinbottom) xpos 1010 ypos 980

screen pausemenu():
    modal True
    dismiss action Hide("pausemenu", transition=easeoutbottom)
    add "gui/pause/pause_idle.png" xpos 55

    imagebutton auto "gui/pause/%s_pause_sl.png" action Show("file_slots", transition=easeinbottom), Play("sound", "sfx/paperopen3.ogg") focus_mask True xpos 55
    imagebutton auto "gui/pause/%s_pause_options.png" action Show("pref_audio", transition=easeinbottom), Play("sound", "sfx/paperopen.ogg2") focus_mask True xpos 55
    imagebutton auto "gui/pause/%s_pause_mm.png" action Play("sound", "sfx/notif.ogg"), Show("mmnotif") focus_mask True xpos 55
    imagebutton auto "gui/pause/%s_pause_quit.png" action Play("sound", "sfx/notif.ogg"), Show("quitnotif") focus_mask True xpos 55

screen aboutmenu():
    modal True
    add "gui/aboutmenu.png"
    imagebutton idle "gui/back.png" action Hide("aboutmenu", transition=easeoutbottom), Play("sound", "sfx/paperclose.ogg")
    imagebutton:
        idle "gui/aboutbutton.png"
        action Show("aboutcredits", transition=dissolve)
        xpos 500
        ypos 600
        at cred_tilt
    imagebutton:
        idle "gui/aboutbutton.png"
        action Show("disclaimers", transition=dissolve)
        xpos 700
        ypos 760
        at disc_tilt

style about_text:
    font "fonts/terminal-grotesque.ttf"
    color "#fff"
    size 40
    xpos 30
    spacing 20
    ypos 170

style about2_text:
    font "fonts/terminal-grotesque.ttf"
    color "#fff"
    size 35
    xpos 30
    spacing 20
    ypos 150
    

screen disclaimers():
    style_prefix "about"
    modal True
    use behindoverlay
    use behindoverlay
    imagebutton idle "gui/back.png" action Hide("disclaimers", transition=dissolve)
    #text "test" xpos 30 ypos 150
    vbox:
        text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
        if gui.about:
            text "[gui.about!t]\n"

        text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")

        text _("\nThis program uses royalty-free sound effects from {a=https://www.freesound.org/}freesound.org{/a} under the Creative Commons License.")

        text _("\nPhotos by Dwight Burdette under {a=https://creativecommons.org/licenses/by/3.0/}CC BY 3.0{/a}")

        text _("\nAperture Dating Simulator was made without the use of artificial intelligence. All writing, art, and music was made entirely by human hands and human code. All voice acting you hear was done by human voices. {color=#ff0000}Fuck AI.\n\n")

        text _("This project is a Portal series fan game. It is not commercially associated in any way with Valve or the Portal\nfranchise, and all material used from Portal falls under the copyright of the Valve Corporation. The base game is,\nand will always be, free to play.")

screen aboutcredits():
    style_prefix "about2"
    modal True
    use behindoverlay
    use behindoverlay
    imagebutton idle "gui/back.png" action Hide("aboutcredits", transition=Dissolve(0.5))

    text "Developer/Artist/Writer:\n{font=Arimo.ttf}{b}———————————{/b}{/font}\nAshleyanna Rivers\n\nBackground Artists:\n{font=Arimo.ttf}{b}—————————{/b}{/font}\nAlyx Shipman\nHazel Thompson\nDustin Oakley\nEvelyn Gallaher\n\nVoice Actors:\n{font=Arimo.ttf}{b}——————{/b}{/font}\nAshleyanna Rivers {size=25}as Miss Esther{/size}\nTyler Banning {size=25}as Kris{/size}\nCassidy Hancock {size=25}as Heath{/size}\nIsaiah Phommavong {size=25}as Aspen{/size}\nTeetad Govitviwat {size=25}as CC{/size}\nBraeden Dugger {size=25}as Rob{/size}\nJohn Wharton {size=25}as Gregory{/size}\nBrian Vecci {size=25}as ???{/size}\nCaz Dugger {size=25}as additional voices{/size}\nIzzy Woody {size=25}as additional voices{/size}"

    text "Music:\n{font=Arimo.ttf}{b}————{/b}{/font}\nTaisiya Pushkar\nDylan Turner\nWilson Hiatt\nDestructo20\n\nPlaytesters:\n{font=Arimo.ttf}{b}——————{/b}{/font}\nRoss Callenry\ncaitgirl02\nthecreatorlynne\nifthenunless\nMorality9\nBembWasHere\nLuke Moretti\n\nSpecial Thanks:\n{font=Arimo.ttf}{b}———————{/b}{/font}\nPortal Mapping and Modding\nSalt Lake City Public Library\nHLMV++ developers" xpos 600

    text "Assets:\n{font=Arimo.ttf}{b}————{/b}{/font}\n" xpos 1100