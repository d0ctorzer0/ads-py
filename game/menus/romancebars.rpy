style cbbar_text:
    font "terminal-grotesque.ttf"
    color "#f0f0f0"
    size 35
    yoffset 3
    xoffset 7
    outlines [ (4, "#000", absolute(0), absolute(0)) ]

screen affectionprogress():
    bar:
        value romance_points["Kris"]
        range 30
        left_bar "bars/kbar.png"
        right_bar "bars/bbar.png"
        xpos 1573
        ypos 371
        xysize (347,51)
    bar:
        value romance_points["Heath"]
        range 31
        left_bar "bars/hbar.png"
        right_bar "bars/bbar.png"
        xpos 1573
        ypos 451
        xysize (347,51)
    bar:
        value romance_points["Aspen"]
        range 30
        left_bar "bars/abar.png"
        right_bar "bars/bbar.png"
        xpos 1573
        ypos 531
        xysize (347,51)
    bar:
        value romance_points["CC"]
        range 33
        left_bar "bars/cbar.png"
        right_bar "bars/bbar.png"
        xpos 1573
        ypos 611
        xysize (347,51)
    bar:
        value romance_points["Rob"]
        range 29
        left_bar "bars/rbar.png"
        right_bar "bars/bbar.png"
        xpos 1573
        ypos 691
        xysize (347,51)
    bar:
        value romance_points["Greg"]
        range 21
        left_bar "bars/gbar.png"
        right_bar "bars/bbar.png"
        xpos 1573
        ypos 771
        xysize (347,51)
    bar:
        value romance_points["???"]
        range 15
        left_bar "bars/ubar.png"
        right_bar "bars/bbar.png"
        xpos 1573
        ypos 851
        xysize (347,51)
    bar:
        value esther_affection
        range 13
        left_bar "bars/ebar.png"
        right_bar "bars/bbar.png"
        xpos 1573
        ypos 931
        xysize (347,51)
    
    if persistent.colorblind == True:
        fixed:
            style_prefix "cbbar"
            text "Kris" xpos 1573 ypos 371
            text "Heath" xpos 1573 ypos 451
            text "Aspen" xpos 1573 ypos 531
            text "CC" xpos 1573 ypos 611
            text "Rob" xpos 1573 ypos 691
            text "Gregory" xpos 1573 ypos 771
            text "???" xpos 1573 ypos 851
            text "Miss Esther" xpos 1573 ypos 931