init python:
    achievement.register("ach_explore", stat_max=6)

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