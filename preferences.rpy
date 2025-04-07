style fileblu_button_text:
    font "terminal-grotesque.ttf"
    color "#f0f0f0"
    hover_color "#94bbe3"

style audiosld:
    ysize 10
    left_bar "bars/hbar.png"
    right_bar "bars/bbar.png"

screen pref_audio:
    style_prefix "fileblu"
    textbutton "<<< back" action Hide("pref_audio", transition=easeoutbottom) ypos 30 xpos 20
    add "gui/options/audio.png"

    vbox:
        style_prefix "audiosld"
        bar value Preference("music volume") at ab_tilt
        
        bar value Preference("voice volume")

        bar value Preference("sound volume")


screen pref_video:
    
    add "gui/options/video.png"

screen pref_other:
    
    add "gui/options/other.png"