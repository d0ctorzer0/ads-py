default ach_name = "biwta"
default showpopup = False

screen achievements():
    modal True
    tag achieve
    add "gui/achievements/folder.png"
    imagebutton idle "gui/back.png" action Hide("achievements", transition=easeoutbottom), Play("sound", "sfx/paperclose.ogg")

    vpgrid:

        cols 2
        rows 16
        spacing 55
        xmargin 310
        bottom_margin 130
        ypos 245
        draggable False
        mousewheel True

        scrollbars "vertical"

        if persistent.ach_krisgood == False:
            add "gui/achievements/krisgood_locked.png"
        elif persistent.ach_krisgood == True:
            add "gui/achievements/krisgood_unlocked.png"
        if persistent.ach_kristrue == False:
            add "gui/achievements/kristrue_locked.png"
        else:
            add "gui/achievements/kristrue_unlocked.png"

        if persistent.ach_heathgood == False:
            add "gui/achievements/heathgood_locked.png"
        else:
            add "gui/achievements/heathgood_unlocked.png"
        if persistent.ach_heathtrue == False:
            add "gui/achievements/heathtrue_locked.png"
        else:
            add "gui/achievements/heathtrue_unlocked.png"

        if persistent.ach_aspengood == False:
            add "gui/achievements/aspengood_locked.png"
        else:
            add "gui/achievements/aspengood_unlocked.png"
        if persistent.ach_aspentrue == False:
            add "gui/achievements/aspentrue_locked.png"
        else:
            add "gui/achievements/aspentrue_unlocked.png"

        if persistent.ach_ccgood == False:
            add "gui/achievements/ccgood_locked.png"
        else:
            add "gui/achievements/ccgood_unlocked.png"
        if persistent.ach_cctrue == False:
            add "gui/achievements/cctrue_locked.png"
        else:
            add "gui/achievements/cctrue_unlocked.png"

        if persistent.ach_robgood == False:
            add "gui/achievements/robgood_locked.png"
        else:
            add "gui/achievements/robgood_unlocked.png"
        if persistent.ach_robtrue == False:
            add "gui/achievements/robtrue_locked.png"
        else:
            add "gui/achievements/robtrue_unlocked.png"

        if persistent.ach_greggood == False:
            add "gui/achievements/greggood_locked.png"
        else:
            add "gui/achievements/greggood_unlocked.png"
        if persistent.ach_gregtrue == False:
            add "gui/achievements/gregtrue_locked.png"
        else:
            add "gui/achievements/gregtrue_unlocked.png"

        if persistent.ach_unknowngood == False:
            add "gui/achievements/unknowngood_locked.png"
        else:
            add "gui/achievements/unknowngood_unlocked.png"
        if persistent.ach_unknowntrue == False:
            add "gui/achievements/unknowntrue_locked.png"
        else:
            add "gui/achievements/unknowntrue_unlocked.png"

        if persistent.ach_ultrobo == False:
            add "gui/achievements/ultrobo_locked.png"
        else:
            add "gui/achievements/ultrobo_unlocked.png"
        if persistent.ach_true == False:
            add "gui/achievements/true_locked.png"
        else:
            add "gui/achievements/true_unlocked.png"

        if persistent.ach_unlikable == False:
            add "gui/achievements/unlikable_locked.png"
        else:
            add "gui/achievements/unlikable_unlocked.png"
        if persistent.ach_amoh == False:
            add "gui/achievements/amoh_locked.png"
        else:
            add "gui/achievements/amoh_unlocked.png"

        if persistent.ach_unionize == False:
            add "gui/achievements/unionize_locked.png"
        else:
            add "gui/achievements/unionize_unlocked.png"
        if persistent.ach_heartless == False:
            add "gui/achievements/heartless_locked.png"
        else:
            add "gui/achievements/heartless_unlocked.png"

        if persistent.ach_ohno == False:
            add "gui/achievements/ohno_locked.png"
        else:
            add "gui/achievements/ohno_unlocked.png"
        if persistent.ach_armor == False:
            add "gui/achievements/armor_locked.png"
        else:
            add "gui/achievements/armor_unlocked.png"

        if persistent.ach_seenitall == False:
            add "gui/achievements/seenitall_locked.png"
        else:
            add "gui/achievements/seenitall_unlocked.png"
        if persistent.ach_picture == False:
            add "gui/achievements/picture_locked.png"
        else:
            add "gui/achievements/picture_unlocked.png"
        
        if persistent.ach_closet == False:
            add "gui/achievements/closet_locked.png"
        else:
            add "gui/achievements/closet_unlocked.png"
        if persistent.ach_insurance == False:
            add "gui/achievements/insurance_locked.png"
        else:
            add "gui/achievements/insurance_unlocked.png"
        
        if persistent.ach_explore == False:
            add "gui/achievements/explore_locked.png"
        else:
            add "gui/achievements/explore_unlocked.png"
        if persistent.ach_biwta == False:
            add "gui/achievements/biwta_locked.png"
        else:
            add "gui/achievements/biwta_unlocked.png"
        
        if persistent.ach_badidea == False:
            add "gui/achievements/badidea_locked.png"
        else:
            add "gui/achievements/badidea_unlocked.png"
        if persistent.ach_lore == False: # this will be the lore achievement
            add "gui/achievements/lore_locked.png"
        else:
            add "gui/achievements/lore_unlocked.png"
        
    
    add "gui/achievements/folder_overlay.png"

    bar:
        value persistent.achievementcount
        range 30
        left_bar "gui/bar/achbar_left.png"
        right_bar "gui/bar/achbar_right.png"
        ypos 190
        xpos 290
        xmaximum 1335

screen ach_popup:
    zorder 2000
    timer 4.0 action Hide("ach_popup", transition=easeoutbottom)
    add "gui/achievements/ach_underlay.png" xalign 1.0 yalign 1.0:
        at transform:
            zoom 0.75
    add "gui/achievements/[ach_name]_unlocked.png" xalign 1.0 yalign 1.0:
        at transform:
            zoom 0.75