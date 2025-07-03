init python:
    achievement.register("ach_explore", stat_max=6)
    achievement.register("ach_ultrobo", stat_max=7)
    achievement.register("ach_seenitall", stat_max=18)
    achievement.register("ach_picture", stat_max=43) # Massive W for drawing 43 cutscenes wtf

default persistent.ach_biwta = True
default persistent.ach_explore = True

default persistent.places_visited = 0
default persistent.visited = {
    "office" : False,
    "cafe" : False,
    "biology" : False,
    "wheatley" : False,
    "manufacture" : False,
    "recovery" : False,
}

default persistent.ach_unionize = True # Spare Miss Esther
default persistent.ach_amoh = True # Don't romance anyone
default persistent.ach_ohno = True # Die (Woo!)
default persistent.ach_heartless = True # Kill Miss Esther (You MONSTER.)
default persistent.ach_unlikeable = True # Antisocial

# Endings

default persistent.ach_kristrue = True
default persistent.ach_krisgood = True

default persistent.ach_heathtrue = True
default persistent.ach_heathgood = True

default persistent.ach_aspentrue = True
default persistent.ach_aspengood = True

default persistent.ach_cctrue = True
default persistent.ach_ccgood = True

default persistent.ach_robtrue = True
default persistent.ach_robgood = True

default persistent.ach_gregtrue = True
default persistent.ach_greggood = True

default persistent.ach_unknowntrue = True
default persistent.ach_unknowngood = True

# Completionist achievements

default persistent.ach_ultrobo = True # Tryhard the game
default persistent.ach_seenitall = True # Get all 18 endings

default persistent.ach_picture = True # Get Every Single Cutscene
default persistent.cutscenes_seen = 0

default persistent.endings_count = 0
default persistent.endings_got = {
    "kristrue" : False,
    "krisgood" : False,
    "heathtrue" : False,
    "heathgood" : False,
    "aspentrue" : False,
    "aspengood" : False,
    "cctrue" : False,
    "ccgood" : False,
    "robtrue" : False,
    "robgood" : False,
    "gregtrue" : False,
    "greggood" : False,
    "unknowntrue" : False,
    "unknowngood" : False,
    "die" : False,
    "heartless" : False,
    "ace" : False,
    "unlikeable" : False,
}

# Implemented:
# Good: Kris, Heath, Aspen, CC, ???
# True: Kris
# BIWTA, explore, heartless, unionize, ohno