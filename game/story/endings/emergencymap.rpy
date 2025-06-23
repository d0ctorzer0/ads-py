# map dictionary
default emv_kris = False
default emv_heath = False
default emv_cc = False
default emv_greg = False
default emv_rob = False
default emv_aspen = False
default emv_unknown = False

# screens

screen emergencymap():
    imagemap:
        idle "gui/em_map/sectionc8.png"
        hover "gui/em_map/sectionc8 - hover.png"
        
        if emv_rob == False:
            hotspot (978, 608, 281, 159) action Hide("emergencymap", transition=dissolve), Jump("saverob")
        
        if emv_cc == False:
            hotspot (621, 536, 214, 186) action Hide("emergencymap", transition=dissolve), Jump("saveccunknown")

        if emv_unknown == False:
            hotspot (268, 302, 120, 75) action Jump("unknownmissing")
        
        if emv_heath == False:
            hotspot (878, 289, 195, 181) action Hide("emergencymap", transition=dissolve), Jump("saveheath")
        
        if emv_kris == False:
            hotspot (1116, 383, 236, 140) action Hide("emergencymap", transition=dissolve), Jump("savekris")
        
        #arrows
        hotspot (436, 166, 82, 92) action Hide("emergencymap"), Show("emergencymapup", transition=dissolve)
        hotspot (727, 867, 80, 90) action Hide("emergencymap"), Show("emergencymapdown", transition=dissolve)
    image "gui/em_map/sectionc8 - blocked.png"

    if emv_unknown == True:
        image "gui/em_map/closetblocked.png"
    if emv_rob == True:
        image "gui/em_map/gymblocked.png"
    if emv_cc == True:
        image "gui/em_map/roomblocked.png"
    if emv_heath == True:
        image "gui/em_map/breakroomblocked.png"
    if emv_heath == True:
        image "gui/em_map/conferenceblocked.png"

screen emergencymapup():
    imagemap:
        idle "gui/em_map/uppersect.png"
        hover "gui/em_map/uppersect - hover.png"

        if emv_aspen == False:
            hotspot (790, 235, 470, 170) action Hide("emergencymapup", transition=dissolve), Jump("saveaspen")

        hotspot (440, 862, 81, 94) action Hide("emergencymapup"), Show("emergencymap", transition=dissolve)
    image "gui/em_map/upper - blocked.png"
    if emv_aspen == True:
        image "gui/em_map/greenhouseblocked.png"

screen emergencymapdown():
    imagemap:
        idle "gui/em_map/lowersect.png"
        hover "gui/em_map/lowersect - hover.png"

        if emv_greg == False:
            hotspot (320, 191, 395, 173) action Hide("emergencymapdown", transition=dissolve), Jump("savegreg")

        hotspot (734, 167, 71, 88) action Hide("emergencymapdown"), Show("emergencymap", transition=dissolve)
    image "gui/em_map/lower - blocked.png"
    if emv_greg == True:
        image "gui/em_map/loungeblocked.png"

    