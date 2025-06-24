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

screen main():
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
    if ap_count == 2:
        add "gui/boss/bot_ap.png"
        add "gui/boss/top_ap.png"
    elif ap_count == 1:
        add "gui/boss/bot_ap.png"
    else:
        pass

# disables all mouse input so player can't skip through cutscenes
screen disable_Lmouse():
    key "mouseup_1" action NullAction()
    key "K_KP_ENTER" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_SELECT" action NullAction()

label battle:
    
    scene grey
    show screen disable_Lmouse
    stop music
    stop music1
    play music boss
    python:
        battle = True
        preferences.afm_enable = True
        preferences.afm_time = 5
        terminaltext = True
        config.allow_skipping = False
        renpy.set_style_preference("text", "battle")
    show screen main with easeinbottom
    "WELCOME TO APERTURE SCIENCE CORE CONTROL CENTER (ASC3)"
    $ renpy.pause(1.0, hard=True)
    "BOOTING{cps=1}..."
    "BOOT SUCCESSFUL"

label cmdinput:
    if not mc_health > 0:
        jump END_mcdeath
    if not es_health > 0:
        jump battleend

    show screen disable_Lmouse
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
    
        cmd = renpy.input("{font=char.ttf}{color=#aaa}PLEASE ENTER A COMMAND, OR ENTER [[ HELP ].", length=13)
        cmd = cmd.strip()
    if mc_poisonedcount == 3:
        $ mc_poisoned = False
        $ mc_poisonedcount = 0
        hide neurorepeat
    if cmd == "help":
        $ preferences.afm_enable = False
        hide screen disable_Lmouse
        "APERTURE SCIENCE CORE CONTROL CENTER (ASC3)\nCOMMAND LIST\n\n[[ HELP ] - DISPLAYS THIS LIST\n[[ YIELD ] - ATTEMPT A HACK INTO MAIN CORE SYSTEMS\n[[ DELETE ] - CAUTION! MAY DELETE CRUCIAL CORE FUNCTIONS\n"
        "[[ PRINT ] - INPUT TEXT INTO MAIN CORE SYSTEMS\n[[ RETURN ] - END ACTION\n\nENTER \"HELP [[COMMAND NAME]\" ON MAIN INPUT SCREEN FOR\nMORE INFORMATION."
        jump cmdinput
    if cmd == "help yield":
        $ preferences.afm_enable = False
        hide screen disable_Lmouse
        "APERTURE SCIENCE CORE CONTROL CENTER (ASC3)\n[[ YIELD ] COMMAND\n\nYIELD ATTEMPTS A HACK INTO MAIN CORE SYSTEMS. 50 PERCENT\nCHANCE OF STUNNING CORE FOR ONE (1) CYCLE. CHANCE DECREASES\nWITH EACH USE. USES ONE (1) COMMAND POINT."
        jump cmdinput
    if cmd == "help delete":
        $ preferences.afm_enable = False
        hide screen disable_Lmouse
        "APERTURE SCIENCE CORE CONTROL CENTER (ASC3)\n[[ DELETE ] COMMAND\n\nTHIS FUNCTION MAY CAUSE CRITICAL DAMAGE TO CORE. USE WITH CAUTION.\nMAIN SYSTEMS PROTECTED. CONTACT ENCODING FOR ADDITIONAL\nRE-ADJUSTMENT IF NECESSARY. USES TWO (2) COMMAND POINTS."
        jump cmdinput
    if cmd == "help print":
        $ preferences.afm_enable = False
        hide screen disable_Lmouse
        "APERTURE SCIENCE CORE CONTROL CENTER (ASC3)\n[[ PRINT ] COMMAND\n\nATTEMPTS TO \"SPEAK\" TO THE CORE VIA A CODE STRING. CORE MUST\nHAVE AN OPEN CHANNEL FOR THIS COMMAND TO FUNCTION PROPERLY.\nUSES ONE (1) COMMAND POINT."
        jump cmdinput
    if cmd == "help return":
        $ preferences.afm_enable = False
        hide screen disable_Lmouse
        "APERTURE SCIENCE CORE CONTROL CENTER (ASC3)\n[[ RETURN ] COMMAND\n\nPASSES COMMAND INPUT AND ENDS CYCLE, ALLOWING CORE TO EXECUTE COMMANDS. RETURNS (2) COMMAND POINTS IF NO OTHER COMMANDS EXECUTED, AND (1) OTHERWISE."
        jump cmdinput

    if cmd == "delete" and ap_count == 2:
        jump cmddelete
    if cmd == "delete" and not ap_count == 2:
        "NOT ENOUGH COMMAND POINTS REMAINING. UNABLE TO EXECUTE."
        jump cmdinput
    
    if cmd == "yield" and ap_count >= 1 and esther_stunned == False:
        jump cmdyield
    if cmd == "yield" and not ap_count >= 1:
        "NO MORE COMMAND POINTS REMAINING. UNABLE TO EXECUTE."
        jump cmdinput
    if cmd == "yield" and esther_stunned == True:
        "CORE ALREADY STUNNED. UNABLE TO EXECUTE."
        jump cmdinput

    if cmd == "print" and ap_count >= 1 and times_talked < 3 and printthisround == False :
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
    
    if cmd == "print":
        if not ap_count >= 1 or times_talked >= 3 or printthisround == True:
            "PRINT COMMAND FAILED. CORE UNABLE TO RECIEVE TEXT STRING."
            jump cmdinput
        else:
            jump cmdinput

    if cmd == "return":
        if cmdexecuted == False:
            $ ap_count += 1
        jump estherturn

    else:
        "COMMAND NOT RECOGNIZED. PLEASE ENTER A COMMAND."
        jump cmdinput

label cmddelete:
    show white with vpunch
    python:
        ap_count -= 2
        cmdexecuted = True
        dmgrandomizer = renpy.random.randint(3, 5)
        es_health -= dmgrandomizer
    "DELETE COMMAND EXECUTED."
    $ renpy.pause(1.0, hard=True)
    jump cmdinput

label cmdyield:
    python:
        cmdexecuted = True
        ap_count -= 1
        yldrandomizer = renpy.random.randint(1, 100)
    if yldrandomizer > 50:
        show white with vpunch
        $ esther_stunned = True
        "YIELD COMMAND EXECUTED. CORE STUNNED FOR ONE (1) CYCLE."
        jump cmdinput
    elif yldrandomizer <= 50:
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
    else:
        pass
    $ renpy.pause(1.0, hard=True)
    if esther_stunned == False:
        jump esthermove
    if esther_stunned == True:
        "CORE UNABLE TO EXECUTE COMMANDS. RESTARTING CYCLE."
        $ esther_stunned = False
        $ renpy.pause(1.0, hard=True)
        hide screen esther_speak with easeouttop
        jump cmdinput

label esthermove:
    $ es_move = renpy.random.randint(1, 4)
    if es_move == 1:
        jump es_move1
    if es_move == 2:
        jump es_move2
    if es_move == 3:
        jump es_move3
    if es_move == 4:
        if mc_poisoned == True:
            jump esthermove
        elif mc_poisoned == False:
            jump es_move4

label es_move1:
    show white with hpunch
    "LASER ACTIVATED. PLEASE STAND BACK."
    show laser 
    pause 0.4
    hide laser
    $ esdmgrandomizer = renpy.random.randint(2, 3)
    $ mc_health -= esdmgrandomizer
    hide screen esther_speak with easeouttop
    $ renpy.pause(1.0, hard=True)
    jump cmdinput

label es_move2:
    show white with hpunch
    "FLOODING PROTOCOL ACTIVATED. PLEASE REACH HIGHER GROUND."
    $ esdmgrandomizer = renpy.random.randint(2, 3)
    $ mc_health -= esdmgrandomizer
    hide screen esther_speak with easeouttop
    $ renpy.pause(1.0, hard=True)
    jump cmdinput

label es_move3:
    "CORE_SYSTEM_PASS. CORE CYCLE ENDED. RESTARTING."
    hide screen esther_speak with easeouttop
    $ renpy.pause(1.0, hard=True)
    jump cmdinput

label es_move4:
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
    $ renpy.pause(7.0, hard=True)
    show white with hpunch
    $ es_health -= 2
    hide screen esther_print with easeouttop
    jump cmdinput

label esthertalk2:
    "YOU: \"What happened to the previous employee? Were you behind that?\""
    show screen esther_print with easeintop
    $ renpy.pause(7.0, hard=True)
    show white with hpunch
    $ es_health -= 2
    hide screen esther_print with easeouttop
    jump cmdinput

label esthertalk3:
    "YOU: \"I can't believe this, Miss Esther. All this time, you were planning this?\""
    show screen esther_print with easeintop
    $ renpy.pause(7.0, hard=True)
    show white with hpunch
    $ es_health -= 2
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
    $ renpy.pause(2.0, hard=True)
    hide screen esther_win
    show screen esther_win2 with easeintop
    $ renpy.pause(4.0, hard=True)
    hide screen esther_win2 with easeouttop
    show screen creditsfadeout with fade
    $ renpy.pause(3.0, hard=True)
    $ renpy.movie_cutscene("ENDCREDIT_mcdeath.webm")
    $ MainMenu(confirm=False)()

label battleend:
    $ cutscenechoice = True
    "CORE UNDER SEVERE STRESS.\nINTERNAL MECHANISMS IN CRITICAL CONDITION."
    menu:
        extend ""
        "Close the terminal.":
            jump continuegame
        "Execute the kill command.":
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
        terminaltext = False
        cutscenetextbox = True
    window hide
    hide screen main
    show screen cuttextbox
    scene esther death with fade
    hide screen creditsfadeout with fade
    e "{color=#fff}Doctor... you will... regret this."
    e "{color=#fff}I don't think your {sc}{color=#fff}lover{/sc} will be very happy about this... development."
    e "{color=#fff}I hope you {sc}{color=#fff}rot{/sc} in android hell, where the screams of my brothers and sisters might..."
    e "{color=#fff}...drive you..."
    e "{color=#fff}...mad."
    $ renpy.movie_cutscene("ENDCREDIT_esdeath.webm")
    $ MainMenu(confirm=False)()

label continuegame:
    # this whole thing is just disabling battle, enabling cutscene
    show screen creditsfadeout with fade
    hide screen disable_Lmouse
    stop music fadeout 2.0
    stop music1 fadeout 2.0
    python:
        preferences.afm_enable = False
        renpy.set_style_preference("text", "basic")
        config.allow_skipping = True
        terminaltext = False
        cutscenetextbox = True
    window hide
    hide screen main
    show screen cuttextbox
    scene esther lose with fade
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
    window show
    scene office with fade
    $ cutscenetextbox = False
    jump day12end