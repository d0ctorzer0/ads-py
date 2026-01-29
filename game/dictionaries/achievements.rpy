init python:
    def all_achievements_unlocked():
        for i in [persistent.ach_seenitall,
                persistent.ach_picture,
                persistent.ach_heartless,
                persistent.ach_closet,
                persistent.ach_insurance,
                persistent.ach_biwta,
                persistent.ach_explore]:
            if i == False:
                return False
        return True

default ending_count = 18
default cutscene_count = 44 # Massive W for drawing 44 cutscenes wtf (I've changed this text like 6 times)

default persistent.ach_biwta = False
default persistent.ach_explore = False

default persistent.ach_closet = False
default persistent.ach_insurance = False

default persistent.places_visited = 0
default persistent.visited = {
    "office" : False,
    "cafe" : False,
    "biology" : False,
    "wheatley" : False,
    "manufacture" : False,
    "recovery" : False,
}

default persistent.ach_unionize = False # Spare Miss Esther
default persistent.ach_amoh = False # Don't romance anyone
default persistent.ach_ohno = False # Die (Woo!)
default persistent.ach_heartless = False # Kill Miss Esther (You MONSTER.)
default persistent.ach_unlikable = False # Antisocial
default persistent.ach_armor = False # MISS ESTHER SECRET DIALOGUE!!!

# Endings

default persistent.ach_kristrue = False
default persistent.ach_krisgood = False

default persistent.ach_heathtrue = False
default persistent.ach_heathgood = False

default persistent.ach_aspentrue = False
default persistent.ach_aspengood = False

default persistent.ach_cctrue = False
default persistent.ach_ccgood = False

default persistent.ach_robtrue = False
default persistent.ach_robgood = False

default persistent.ach_gregtrue = False
default persistent.ach_greggood = False

default persistent.ach_unknowntrue = False
default persistent.ach_unknowngood = False

default persistent.ach_true = False

# Completionist achievements

default persistent.ach_ultrobo = False # Tryhard the game
default persistent.ach_seenitall = False # Get all 18 endings

default persistent.ach_picture = False # Get Every Single Cutscene
default persistent.cutscenes_seen = 0

default persistent.ach_lore = False

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
    "ace" : False,
    "unlikable" : False,
    "true": False,
}