init python:
    def reset_data():
        for attr in dir(persistent):
            if not callable(attr) and not attr.startswitch("_"):
                setattr(persistent, attr, None)
        for slot in renpy.list_saved_games(fast=True):
            renpy.unlink_save(slot)
        renpy.quit(relaunch=True)

init:
    $ config.keymap['help'].remove('K_F1')
    # key "K_LEFT" action NullAction()
    # key "KP_LEFT" action NullAction()
    # $ config.key "K_RIGHT" action NullAction()
    # $ config.key "KP_RIGHT" action NullAction()
    # $ config.key "K_UP" action NullAction()
    # $ config.key "KP_UP" action NullAction()
    # $ config.key "K_DOWN" action NullAction()
    # $ config.key "KP_DOWN" action NullAction()

screen disable_arrows(): #disable arrow keys
    key "K_RIGHT" action NullAction()
    key "KP_RIGHT" action NullAction()
    key "K_LEFT" action NullAction()
    key "KP_LEFT" action NullAction()
    key "K_UP" action NullAction()
    key "KP_UP" action NullAction()
    key "K_DOWN" action NullAction()
    key "KP_DOWN" action NullAction()

label splashscreen:
    $ renpy.movie_cutscene("arlogo_intro.webm")
    $ config.allow_skipping = True
    $ renpy.register_style_preference("text", "basic", style.say_dialogue, "font", "fonts/SairaCondensed-Medium.ttf")
    $ renpy.register_style_preference("text", "basic", style.say_dialogue, "color", "#404040")
    $ renpy.register_style_preference("text", "basic", style.say_dialogue, "xsize", 1000)
    $ renpy.set_style_preference("text", "basic")
    scene mm with dissolve
    return

# define config.mouse = { }
# define config.mouse['default'] = [ ( "gui/cursor.png", 0, 0) ]

define cutscenetextbox = False
define _game_menu_screen = None

#SPECIAL DEFAULTS
default plant = False
default ball = False
default picture = False
default spades = True
default emailfromunknownday2 = False
default askforu = False
default askforg = False
default giveccpicture = False
default cctv = False
default knowabtwaterfall = False
default cactusname = ""
default battle = False
default aspenknowabtbertha = False

#GOODBYES
default krisgoodbye = False
default heathgoodbye = False
default unknownhumor = False
default aspengoodbye = False
default haveaheart = False

#DAY SETUPS
default goodday3 = False
default day6stay = False
default satchoose_kris = False
default satchoose_heath = False
default satchoose_aspen = False
default satchoose_cc = False
default satchoose_rob = False

#CUSTCENE T/F - "[blank] cutscene [number]"
default persistent.kc1 = False
default persistent.kc2 = False
default persistent.kc3 = False
default persistent.kc4 = False
default persistent.kc5 = False
default persistent.kc6 = False

default persistent.hc1 = False
default persistent.hc2 = False
default persistent.hc3 = False
default persistent.hc4 = False
default persistent.hc5 = False
default persistent.hc6 = False

default persistent.ac1 = False
default persistent.ac2 = False
default persistent.ac3 = False
default persistent.ac4 = False

default persistent.cc1 = False
default persistent.cc2 = False
default persistent.cc3 = False
default persistent.cc4 = False
default persistent.cc5 = False

default persistent.rc1 = False
default persistent.rc2 = False
default persistent.rc3 = False
default persistent.rc4 = False

default persistent.gc1 = False
default persistent.gc2 = False
default persistent.gc3 = False

default persistent.uc1 = False
default persistent.uc2 = False
default persistent.uc3 = persistent.cc4
default persistent.uc4 = False

#DAY 3 - "with [blank] day 3"
default wkd3 = False
default whd3 = False
default wad3 = False
default wcd3 = False
default wrd3 = False

#FRIDAY SETUP
default tshirt = False
default formal = False
default uniform = False
default vaca = False
default askestherday2 = False
#GALLERY SETUP
default persistent.kgunlock = False
default persistent.hgunlock = False
default persistent.agunlock = False
default persistent.cgunlock = False
default persistent.rgunlock = False
default persistent.ggunlock = False
default persistent.ugunlock = False

default emailfromgregday9 = False
default emailfromunknownday9 = False
#define shorter_easein = MoveTransition(0.3, enter=offscreenright, enter_time_warp=_warper.easein)
#define shorter_easeout = MoveTransition(0.3, exit=offscreenright, enter_time_warp=_warper.easein)

#ENDING SETUP
default lock_kris = False
default lock_heath = False
default lock_aspen = False
default lock_cc = False
default lock_rob = False
default lock_gregory = False
default lock_unknown = False

#ROMANCE SETUP
default romance_points = {
    "Kris" : 0 ,
    "Heath" : 0 ,
    "???" : 0 ,
    "Aspen" : 0 ,
    "CC" : 0 ,
    "Greg" : 0 ,
    "Rob" : 0 ,
}
default positive = { # 0 = positive, -1 = negative
    "Kris" : 0 ,
    "Heath" : 0 ,
    "???" : 0 ,
    "Aspen" : 0 ,
    "CC" : 0 ,
    "Greg" : 0 ,
    "Rob" : 0 ,
}
default priority = {
    "Kris" : 0 ,
    "Heath" : 0 ,
    "???" : 0 ,
    "Aspen" : 0 ,
    "CC" : 0 ,
    "Greg" : 0 ,
    "Rob" : 0 ,
}
$ highest_priority = max(priority, key=priority.get)

default romance_minimum_for_good_ending = 20
default romance_minimum_for_true_ending = 30

default esther_affection = 0