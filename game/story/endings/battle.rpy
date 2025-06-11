default ap_count = 2
default mc_health = 20
default es_health = 20
default terminaltext = False

screen main:
    add "gui/boss/terminal.png"
    add "gui/boss/health.png"
    bar: #cant fucking get this to work, will come back to it
        bar_vertical True
        value mc_health
        range 20
        left_bar "gui/bar/mchealth_bottom.png"
        right_bar "gui/bar/mchealth_top.png"
        xpos 1715
        ypos 630
        xysize (60,430)
    if ap_count == 2:
        add "gui/boss/bot_ap.png"
        add "gui/boss/top_ap.png"
    elif ap_count == 1:
        add "gui/boss/bot_ap.png"
    else:
        pass

screen disable_Lmouse():
    key "mouseup_1" action NullAction()
    key "K_KP_ENTER" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_SELECT" action NullAction()

if terminaltext = True:
    define config.allow_skipping = False
    define gui.text_font = "char.ttf"
    define gui.text_color = '#757575'
    define gui.dialogue_width = 1400

label battle:
    scene white
    show screen disable_Lmouse
    $ preferences.afm_enable = True
    $ preferences.afm_time = 5
    show screen main
    $ terminaltext = True
    "WELCOME TO APERTURE SCIENCE CORE CONTROL CENTER (ASC3)"
    $ renpy.pause(1.0, hard=True)
    "BOOTING{cps=1}..."
    "BOOT SUCCESSFUL"

label cmdinput:
    $ preferences.afm_enable = True
    show screen disable_Lmouse
    $ cmd = renpy.input("PLEASE ENTER A COMMAND, OR ENTER [[ HELP ] FOR MORE INFORMATION.", length=13)
    $ cmd = cmd.strip()
    if cmd == "help":
        $ preferences.afm_enable = False
        hide screen disable_Lmouse
        "APERTURE SCIENCE CORE CONTROL CENTER (ASC3)\nCOMMAND LIST\n\n[[ HELP ] - DISPLAYS THIS LIST\n[[ YIELD ] - ATTEMPT A HACK INTO MAIN CORE SYSTEMS\n[[ DELETE ] - CAUTION! MAY DELETE CRUCIAL CORE FUNCTIONS\n"
        "[[ PRINT ] - INPUT TEXT INTO MAIN CORE SYSTEMS\n[[ RETURN ] - END ACTION\n[[ PASS ] - PASS ACTION\n\nENTER \"HELP [[COMMAND NAME]\" ON MAIN INPUT SCREEN FOR\nMORE INFORMATION."
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
        "APERTURE SCIENCE CORE CONTROL CENTER (ASC3)\n[[ PRINT ] COMMAND\n\nATTEMPTS TO \"SPEAK\" TO THE CORE VIA A CODE STRING. CORE MUST HAVE\nAN OPEN CHANNEL FOR THIS COMMAND TO FUNCTION PROPERLY.\nUSES ONE (1) COMMAND POINT."
        jump cmdinput
    if cmd == "help return":
        $ preferences.afm_enable = False
        hide screen disable_Lmouse
        "APERTURE SCIENCE CORE CONTROL CENTER (ASC3)\n[[ RETURN ] COMMAND\n\nRETURN ENDS USER CYCLE AND ALLOWS CORE TO EXECUTE COMMANDS."
        jump cmdinput
    if cmd == "help pass":
        $ preferences.afm_enable = False
        hide screen disable_Lmouse
        "APERTURE SCIENCE CORE CONTROL CENTER (ASC3)\n[[ PASS ] COMMAND\n\nPASSES COMMAND INPUT AND ENDS CYCLE, ALLOWING CORE TO EXECUTE COMMANDS. RETURNS (1) COMMAND POINT."
        jump cmdinput
    else:
        "COMMAND NOT RECOGNIZED. PLEASE ENTER A COMMAND."
        jump cmdinput