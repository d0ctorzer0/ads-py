init python:
    def reset_data():
        for attr in dir(persistent):
            if not callable(attr) and not attr.startswitch("_"):
                setattr(persistent, attr, None)
        for slot in renpy.list_saved_games(fast=True):
            renpy.unlink_save(slot)
        renpy.quit(relaunch=True)

define cutscenetextbox = False

#SPECIAL DEFAULTS
default plant = False
default ball = False
default picture = False
default spades = True
default emailfromrobday2 = False
default askforu = False
default askforg = False
default giveccpicture = False

#GOODBYES
default krisgoodbye = False
default heathgoodbye = False
default unknownhumor = False
default aspengoodbye = False
default haveaheart = False

#DAY 3 SETUPS
default goodday3 = False

#CUSTCENE T/F - "[blank] cutscene [number]"
default kc1 = False
default hc1 = False
default ac1 = False
default cc1 = False
default rc1 = False

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

#define shorter_easein = MoveTransition(0.3, enter=offscreenright, enter_time_warp=_warper.easein)
#define shorter_easeout = MoveTransition(0.3, exit=offscreenright, enter_time_warp=_warper.easein)

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
default positive = { # 1 = positive, -1 = negative
    "Kris" : 0 ,
    "Heath" : 0 ,
    "???" : 0 ,
    "Aspen" : 0 ,
    "CC" : 0 ,
    "Greg" : 0 ,
    "Rob" : 0 ,
}

default romance_minimum_for_good_ending = 20
default romance_minimum_for_perfect_ending = 30

#ESTHER EVIL SETUP
default esther_affection = 0
default esther_affection_minimum = 15