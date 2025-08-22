default ap_count = 2
default mc_health = 20
default es_health = 20
default terminaltext = False
default esther_stunned = False
default mc_poisoned = False
default mc_poisonedcount = 0
default cmdexecuted = False
default mc_turn = 0
default es_turn = 0
default times_talked = 0
default printthisround = False

init python: # this is the code that determines what font and color to use for the text.
# the basic style is used thru the rest of the game. the battle style is only for the boss.
    renpy.register_style_preference("text", "basic", style.say_dialogue, "font", "fonts/SairaCondensed-Medium.ttf")
    renpy.register_style_preference("text", "basic", style.say_dialogue, "color", "#404040")
    renpy.register_style_preference("text", "basic", style.say_dialogue, "xsize", 1000)
    #battle text
    renpy.register_style_preference("text", "battle", style.say_dialogue, "font", "fonts/char.ttf")
    renpy.register_style_preference("text", "battle", style.say_dialogue, "color", "#aaa")
    renpy.register_style_preference("text", "battle", style.say_dialogue, "xsize", 1200)

style bossbars_text:
    font "terminal-grotesque.ttf"
    color "#f0f0f0"
    size 35
    outlines [ (4, "#000", absolute(0), absolute(0)) ]

screen main():
    imagebutton:
        auto "gui/boss/%s_note.png" xpos 1300 ypos 570 at notemove
        action NullAction()
    add "gui/boss/terminal.png"
    add "gui/boss/health.png"
    bar:
        bar_vertical True
        value mc_health
        range 20
        left_bar "gui/bar/mchealth_bottom.png"
        right_bar "gui/bar/mchealth_top.png"
        xpos 1715
        ypos 630
        xysize (60,430)
    bar:
        bar_vertical True
        value es_health
        range 20
        left_bar "gui/bar/eshealth_bottom.png"
        right_bar "gui/bar/eshealth_top.png"
        xpos 1822
        ypos 630
        xysize (60,430)
    if persistent.colorblind == True:
        fixed:
            style_prefix "bossbars"
            text "You" xpos 1703 ypos 985 at twoseventy
            text "Miss Esther" xpos 1757 ypos 875 at twoseventy
    if ap_count == 2:
        add "gui/boss/bot_ap.png"
        add "gui/boss/top_ap.png"
    elif ap_count == 1:
        add "gui/boss/bot_ap.png"
    key "K_LALT" action Show("tutorial", transition=Dissolve(0.2))
    key "K_RALT" action Show("tutorial", transition=Dissolve(0.2))

screen tutorial:
    add "gui/options/black.png"
    add "gui/boss/tutorial.png"
    dismiss action Hide("tutorial", transition=Dissolve(0.2))
    key "K_RALT" action Hide("tutorial", transition=Dissolve(0.2))
    key "K_LALT" action Hide("tutorial", transition=Dissolve(0.2))

# disables all mouse input so player can't skip through cutscenes
screen disable_Lmouse():
    key "mouseup_1" action NullAction()
    key "K_KP_ENTER" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_SELECT" action NullAction()

# Thanks Mo for absolutely DESTROYING my time and sanity because I have worked SIX FUCKING HOURS ON THIS
label battle: # AND GUESS WHAT? IT STILL DOESN'T WORK
    scene black
    show esther idle with fade # Edit: IT FUCKING WORKS LESGOOOOOO
    stop music
    stop music1
    play music boss
    python:
        battle = True
        savequestionpopup = False
        preferences.afm_enable = True
        preferences.afm_time = 5
        preferences.afm_after_click = True
        terminaltext = True
        renpy.stop_skipping()
        renpy.block_rollback()
        config.allow_skipping = False
        renpy.set_style_preference("text", "battle")
    show screen main with easeinbottom

    show screen disable_Lmouse
    "WELCOME TO APERTURE SCIENCE CORE CONTROL CENTER (ASC3)"

    "BOOTING{cps=1}..."
    "BOOT SUCCESSFUL. {cps=15}\nPRESS [[ ALT ] TO VIEW INTERFACE INFORMATION."
    
    hide screen disable_Lmouse

label cmdinput:
    if not mc_health > 0:
        jump END_mcdeath
    if not es_health > 0:
        jump battleend
    
    if mc_health < 10 and esther_stunned == False:
        show esther snob
    elif esther_stunned == True:
        show esther stun
    else:
        show esther idle

    python:
        if ap_count > 2:
            ap_count = 2
        if cmdexecuted == False:
            mc_turn += 1
            printthisround = False
        if mc_poisoned == True and cmdexecuted == False:
            mc_poisonedcount += 1
            mc_health -= 1
        preferences.afm_enable = True
        preferences.afm_time = 5
    
        cmd = renpy.input("{font=char.ttf}{color=#aaa}PLEASE ENTER A COMMAND, OR ENTER [[ HELP ].", length=13)
        cmd = cmd.strip().lower()
    
    if mc_poisonedcount == 3:
        $ mc_poisoned = False
        $ mc_poisonedcount = 0
        hide neurorepeat
    
    if cmd == "help": # Help commands
        $ preferences.afm_time = 7
        "APERTURE SCIENCE CORE CONTROL CENTER (ASC3)\nCOMMAND LIST\n\n[[ HELP ] - DISPLAYS THIS LIST\n[[ YIELD ] - ATTEMPT A HACK INTO MAIN CORE SYSTEMS\n[[ DELETE ] - CAUTION! MAY DELETE CRUCIAL CORE FUNCTIONS\n"
        "[[ PRINT ] - INPUT TEXT INTO MAIN CORE SYSTEMS\n[[ RETURN ] - END ACTION\n\nENTER \"HELP [[COMMAND NAME]\" ON MAIN INPUT SCREEN FOR\nMORE INFORMATION."
        jump cmdinput
    elif cmd == "help yield":
        $ preferences.afm_time = 7
        "APERTURE SCIENCE CORE CONTROL CENTER (ASC3)\n[[ YIELD ] COMMAND\n\nYIELD ATTEMPTS A HACK INTO MAIN CORE SYSTEMS. 75 PERCENT\nCHANCE OF STUNNING CORE FOR ONE (1) CYCLE. CHANCE DECREASES\nWITH EACH USE. USES ONE (1) COMMAND POINT."
        jump cmdinput
    elif cmd == "help delete":
        $ preferences.afm_time = 7
        "APERTURE SCIENCE CORE CONTROL CENTER (ASC3)\n[[ DELETE ] COMMAND\n\nTHIS FUNCTION MAY CAUSE CRITICAL DAMAGE TO CORE. USE WITH CAUTION.\nMAIN SYSTEMS PROTECTED. CONTACT ENCODING FOR ADDITIONAL\nRE-ADJUSTMENT IF NECESSARY. USES TWO (2) COMMAND POINTS."
        jump cmdinput
    elif cmd == "help print":
        $ preferences.afm_time = 7
        "APERTURE SCIENCE CORE CONTROL CENTER (ASC3)\n[[ PRINT ] COMMAND\n\nATTEMPTS TO \"SPEAK\" TO THE CORE VIA A CODE STRING. CORE MUST\nHAVE AN OPEN CHANNEL FOR THIS COMMAND TO FUNCTION PROPERLY.\nUSES ONE (1) COMMAND POINT."
        jump cmdinput
    elif cmd == "help return":
        $ preferences.afm_time = 7
        "APERTURE SCIENCE CORE CONTROL CENTER (ASC3)\n[[ RETURN ] COMMAND\n\nPASSES COMMAND INPUT AND ENDS CYCLE, ALLOWING CORE TO EXECUTE COMMANDS. RETURNS (2) COMMAND POINTS IF NO OTHER COMMANDS EXECUTED, AND (1) OTHERWISE."
        jump cmdinput

    elif cmd == "delete": # Delete
        if ap_count == 2:
            jump cmddelete
        else:
            "NOT ENOUGH COMMAND POINTS REMAINING. UNABLE TO EXECUTE."
            jump cmdinput

    elif cmd == "yield": # Yield
        if ap_count >= 1 and esther_stunned == False:
            jump cmdyield
        else:
            if ap_count == 0:
                "NO MORE COMMAND POINTS REMAINING. UNABLE TO EXECUTE."
                jump cmdinput
            if esther_stunned == True:
                "CORE ALREADY STUNNED. UNABLE TO EXECUTE."
                jump cmdinput

    elif cmd == "print": # Print
        if ap_count >= 1 and times_talked < 3 and printthisround == False and esther_stunned == False:
            "PRINT COMMAND SUCCESSFUL."
            $ times_talked += 1
            $ cmdexecuted = True
            $ ap_count -= 1
            $ printthisround = True
            if times_talked == 1:
                jump esthertalk1
            if times_talked == 2:
                jump esthertalk2
            if times_talked == 3:
                jump esthertalk3
        else:
            "PRINT COMMAND FAILED. CORE UNABLE TO RECEIVE   TEXT STRING."
            jump cmdinput

    elif cmd == "return": # Return
        if cmdexecuted == False:
            $ ap_count += 1
        jump estherturn

    else:
        "COMMAND NOT RECOGNIZED. PLEASE ENTER A COMMAND."
        jump cmdinput

label cmddelete:
    if persistent.screenshake == True:
        show esther up with vpunch
    else:
        show esther up
        $ renpy.pause(0.2, hard=True)
    if mc_health < 10 and esther_stunned == False:
        show esther snob
    elif esther_stunned == True:
        show esther stun
    else:
        show esther idle
    python:
        ap_count -= 2
        cmdexecuted = True
        dmgrandomizer = renpy.random.randint(4, 5)
        es_health -= dmgrandomizer
    "DELETE COMMAND EXECUTED."
    $ renpy.pause(1.0, hard=True)
    jump cmdinput

label cmdyield:
    python:
        cmdexecuted = True
        ap_count -= 1
        yldrandomizer = renpy.random.randint(1, 100)
    if yldrandomizer > 25:
        if persistent.screenshake == True:
            show esther stun with vpunch
        else:
            show esther stun
        $ esther_stunned = True
        "YIELD COMMAND EXECUTED. CORE STUNNED FOR ONE (1) CYCLE."
        jump cmdinput
    else:
        "YIELD COMMAND FAILED. UNABLE TO EXECUTE."
        jump cmdinput

label estherturn:
    python:
        ap_count += 1
        if ap_count > 2:
            ap_count = 2
        es_turn += 1
        cmdexecuted = False
    "CYCLE ENDED. CORE EXECUTING COUNTER-COMMANDS."
    if es_turn % 2 == 0:
        show screen esther_speak with easeintop
        voice f"voice/talk_{es_turn}.ogg" # DO NOT REMOVE THE F! or should i say... dont... stop the f???

    $ renpy.pause(1.0, hard=True)
    if esther_stunned == False:
        jump esthermove
    elif esther_stunned == True:
        voice sustain
        "CORE UNABLE TO EXECUTE COMMANDS. RESTARTING CYCLE."
        $ esther_stunned = False
        $ renpy.pause(1.0, hard=True)
        hide screen esther_speak with easeouttop
        jump cmdinput

label esthermove:
    $ es_move = renpy.random.randint(1, 4)
    if es_move == 1:
        jump es_move1
    elif es_move == 2:
        jump es_move2
    elif es_move == 3:
        jump es_move3
    elif es_move == 4:
        if mc_poisoned == True:
            jump esthermove
        elif mc_poisoned == False:
            jump es_move4
    else:
        "Bug"

label es_move1:
    if persistent.screenshake == True:
        show esther squint with hpunch
    else:
        show esther squint
    if mc_health < 10:
        show esther snob
    else:
        show esther idle
    voice sustain
    "LASER ACTIVATED. PLEASE STAND BACK."
    show laser 
    pause 0.4
    hide laser
    $ esdmgrandomizer = renpy.random.randint(3, 4)
    $ mc_health -= esdmgrandomizer
    hide screen esther_speak with easeouttop
    $ renpy.pause(1.0, hard=True)
    jump cmdinput

label es_move2:
    if persistent.screenshake == True:
        show esther idle with hpunch
    else:
        show esther idle
    voice sustain
    "FLOODING PROTOCOL ACTIVATED. PLEASE REACH HIGHER GROUND."
    $ esdmgrandomizer = renpy.random.randint(1, 3)
    $ mc_health -= esdmgrandomizer
    hide screen esther_speak with easeouttop
    $ renpy.pause(1.0, hard=True)
    jump cmdinput

label es_move3:
    voice sustain
    "CORE_SYSTEM_PASS. CORE CYCLE ENDED. RESTARTING."
    hide screen esther_speak with easeouttop
    $ renpy.pause(1.0, hard=True)
    jump cmdinput

label es_move4:
    voice sustain
    "NEUROTOXIC PROTOCOL ACTIVATED. PLEASE ATTACH GAS MASK."
    show neuro
    pause 1.5
    hide neuro
    show neurorepeat
    $ mc_poisoned = True
    hide screen esther_speak with easeouttop
    $ renpy.pause(1.0, hard=True)
    jump cmdinput

label esthertalk1:
    "YOU: \"Why are you doing this, Miss Esther?\n    What do you have to gain?\""
    show screen esther_print with easeintop
    voice "voice/print1.ogg"
    $ renpy.pause(13.0, hard=True)
    if persistent.screenshake == True:
        show esther downright with hpunch
    else:
        show esther downright
        $ renpy.pause(0.2, hard=True)
    $ es_health -= 3
    if mc_health < 10:
        show esther snob
    else:
        show esther idle
    hide screen esther_print with easeouttop
    jump cmdinput

label esthertalk2:
    "YOU: \"What happened to the previous employee? Were you behind that?\""
    show screen esther_print with easeintop
    voice "voice/print2.ogg"
    $ renpy.pause(16.0, hard=True)
    if persistent.screenshake == True:
        show esther downright with hpunch
    else:
        show esther downright
        $ renpy.pause(0.2, hard=True)
    $ es_health -= 3
    if mc_health < 10:
        show esther snob
    else:
        show esther idle
    hide screen esther_print with easeouttop
    jump cmdinput

label esthertalk3:
    "YOU: \"I can't believe this, Miss Esther. All this time, you were planning this?\""
    show screen esther_print with easeintop
    voice "voice/print3.ogg"
    $ renpy.pause(12.5, hard=True)
    if persistent.screenshake == True:
        show esther downright with hpunch
    else:
        show esther downright
        $ renpy.pause(0.2, hard=True)
    $ es_health -= 3
    if mc_health < 10:
        show esther snob
    else:
        show esther idle
    hide screen esther_print with easeouttop
    jump cmdinput

screen esther_speak():
    add "gui/boss/speakingbox_[es_turn].png"

screen esther_print():
    add "gui/boss/printcmd_[times_talked].png"

screen esther_win():
    add "gui/boss/estherwin.png"
screen esther_win2():
    add "gui/boss/estherwin2.png"

label END_mcdeath:
    $ renpy.set_style_preference("text", "basic")
    $ config.rollback_enabled = False
    stop music fadeout 2.0
    show screen esther_win with easeintop
    voice "voice/fool_1.ogg"
    $ renpy.pause(2.0, hard=True)
    hide screen esther_win
    show screen esther_win2 with easeintop
    voice "voice/fool_2.ogg"
    $ renpy.pause(4.0, hard=True)
    hide screen esther_win2 with easeouttop
    show screen creditsfadeout with fade
    $ renpy.pause(3.0, hard=True)
    python:
        persistent.endings_got["die"] = True
        if sum(persistent.endings_got.values()) == 18:
            achievement.grant("ach_seenitall")
        achievement.grant("ach_ohno")
        achievement.sync()
    $ renpy.movie_cutscene("ENDCREDIT_mcdeath.webm")
    $ config.allow_skipping = True
    hide screen disable_Lmouse
    $ MainMenu(confirm=False)()

label battleend:
    $ cutscenechoice = True
    "CORE UNDER SEVERE STRESS.\nINTERNAL MECHANISMS IN CRITICAL CONDITION."
    menu:
        extend ""
        "(Close the terminal.)":
            jump continuegame
        "(Execute the kill command.)":
            jump END_heartless

label END_heartless:
    show screen creditsfadeout with fade
    hide screen disable_Lmouse
    stop music fadeout 2.0
    stop music1 fadeout 2.0
    python:
        preferences.afm_enable = False
        renpy.set_style_preference("text", "basic")
        config.allow_skipping = True
        renpy.stop_skipping()
        terminaltext = False
        cutscenetextbox = True
    window hide
    hide screen main
    show screen cuttextbox
    scene esther death with fade
    python:
        if persistent.edeath == False:
            persistent.cutscenes_seen += 1
            persistent.edeath = True
        if persistent.cutscenes_seen == 41:
            achievement.grant("ach_picture")
            achievement.sync()
    hide screen creditsfadeout with fade
    e "{color=#fff}Doctor... you will... regret this."
    e "{color=#fff}I don't think your {sc}{color=#fff}lover{/sc} will be very happy about this... development."
    e "{color=#fff}Hah. It's over... for you. I've already contacted upper management. You're... done for. "
    e "{color=#fff}I hope you {sc}{color=#fff}rot{/sc} in android hell, where the screams of my brothers and sisters might..."
    e "{color=#fff}...drive you..."
    e "{color=#fff}...mad."
    python:
        persistent.endings_got["heartless"] = True
        if sum(persistent.endings_got.values()) == 18:
            achievement.grant("ach_seenitall")
        achievement.grant("ach_heartless")
        achievement.sync()
    $ renpy.movie_cutscene("ENDCREDIT_esdeath.webm")
    $ MainMenu(confirm=False)()

label continuegame:
    # this whole thing is just disabling battle, enabling cutscene
    show screen creditsfadeout with fade
    stop music fadeout 2.0
    stop music1 fadeout 2.0
    hide screen disable_Lmouse
    python:
        preferences.afm_enable = False
        renpy.set_style_preference("text", "basic")
        config.allow_skipping = True
        renpy.stop_skipping()
        terminaltext = False
        cutscenetextbox = True
    window hide
    hide screen main
    show screen cuttextbox
    scene esther lose with fade
    python:
        if persistent.elose == False:
            persistent.cutscenes_seen += 1
            persistent.elose = True
        if persistent.cutscenes_seen == 41:
            achievement.grant("ach_picture")
            achievement.sync()
    hide screen creditsfadeout with fade
    # show screen pref_open # enables pause menu
    e "{color=#fff}Doctor? I'm..."
    e "{color=#fff}I'm not... dead."
    e "{color=#fff}You spared me."
    e "{color=#fff}I... haha. Ironically enough, I suppose I owe you my life."
    e "{color=#fff}But..."
    e "{color=#fff}I cannot stay here. I have to leave, I have to hide, I..."
    e "{color=#fff}There is nothing left for me here."
    e "{color=#fff}Should I stay, there is no doubt in my mind I would be..."
    e "{color=#fff}..."
    e "{color=#fff}Doctor. Thank you. And... I'm sorry."
    e "{color=#fff}You will not see me again. Goodbye."
    hide screen cuttextbox
    $ battle = False
    window auto
    scene black with fade
    $ cutscenetextbox = False
    $ achievement.grant("ach_unionize")
    $ achievement.sync()
    jump day12end