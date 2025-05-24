# map dictionary

default cores_visited = 0

default v_satoffice = False
default v_recovery = False
default v_satcafe = False
default v_kris = False
default inv_kris = False
default v_heath = False
default inv_heath = False
default v_cc = False
default inv_cc = False
default informed_about_canister = False
default v_greg = False
default v_rob = False
default inv_rob = False
default v_aspen = False
default inv_aspen = False
default v_unknown = False

default v_biology = False

default v_manufacture = False
default v_wheatley = False

# screens

screen aptmap():
    imagemap:
        idle "gui/map/sectionc8.png"
        hover "gui/map/sectionc8 - hover.png"
        
        if v_satoffice == False:
            hotspot (1450, 567, 221, 323) action Hide("aptmap", transition=dissolve), Jump("satoffice")
        if v_rob == False:
            hotspot (978, 608, 281, 159) action Hide("aptmap", transition=dissolve), Jump("satrob")
        if v_satcafe == False:
            hotspot (1017, 864, 381, 103) action Hide("aptmap", transition=dissolve), Jump("satcafe")
        if v_cc == False:
            hotspot (621, 536, 214, 186) action Hide("aptmap", transition=dissolve), Jump("satcc")
        if v_unknown == False:
            hotspot (268, 302, 120, 75) action Jump("satunknown")
        if v_heath == False:
            hotspot (878, 289, 195, 181) action Hide("aptmap", transition=dissolve), Jump("satheath")
        if v_kris == False:
            hotspot (1116, 383, 236, 140) action Hide("aptmap", transition=dissolve), Jump("satkris")
        
        #arrows
        hotspot (436, 166, 82, 92) action Hide("aptmap"), Show("aptmapup", transition=dissolve)
        hotspot (727, 867, 80, 90) action Hide("aptmap"), Show("aptmapdown", transition=dissolve)

screen aptmapup():
    imagemap:
        idle "gui/map/uppersect.png"
        hover "gui/map/uppersect - hover.png"

        if v_biology == False:
            hotspot (530, 492, 445, 202) action Hide("aptmapup", transition=dissolve), Jump("biology")
            hotspot (832, 689, 144, 91) action Hide("aptmapup", transition=dissolve), Jump("biology")
        if v_aspen == False:
            hotspot (790, 235, 470, 170) action Hide("aptmapup", transition=dissolve), Jump("sataspen")

        hotspot (1024, 490, 464, 337) action Jump("management")

        hotspot (440, 862, 81, 94) action Hide("aptmapup"), Show("aptmap", transition=dissolve)

screen aptmapdown():
    imagemap:
        idle "gui/map/lowersect.png"
        hover "gui/map/lowersect - hover.png"

        if v_greg == False:
            hotspot (320, 191, 395, 173) action Hide("aptmapdown", transition=dissolve), Jump("satgreg")
        if v_wheatley == False:
            hotspot (1018, 191, 650, 772) action Hide("aptmapdown", transition=dissolve), Jump("wheatleycameo")
        if v_recovery == False:
            hotspot (460, 414, 253, 302) action Hide("aptmapdown", transition=dissolve), Jump("recovery")
        if v_manufacture == False:
            hotspot (240, 534, 145, 428) action Hide("aptmapdown", transition=dissolve), Jump("manufacture")

        hotspot (734, 167, 71, 88) action Hide("aptmapdown"), Show("aptmap", transition=dissolve)