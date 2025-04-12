# map dictionary

default v_satoffice = False
default v_satrob = False
default v_satcafe = False

# screens

screen aptmap():
    imagemap:
        idle "gui/map/sectionc8.png"
        hover "gui/map/sectionc8 - hover.png"
        
        if v_satoffice == False:
            hotspot (1450, 567, 221, 323) action Hide("aptmap", transition=dissolve), Jump("satoffice")
        if v_satrob == False:
            hotspot (978, 608, 281, 159) action Jump("satrob")
        if v_satcafe == False:
            hotspot (1017, 864, 381, 103) action Jump("satcafe")
        hotspot (621, 536, 214, 186) action Jump("satcc")
        hotspot (268, 302, 120, 75) action Jump("satunknown")
        hotspot (878, 289, 195, 181) action Jump("satheath")
        hotspot (1116, 383, 236, 140) action Jump("satkris")
        hotspot (436, 166, 82, 92) action Hide("aptmap"), Show("aptmapup", transition=dissolve)
        hotspot (727, 867, 80, 90) action Hide("aptmap"), Show("aptmapdown", transition=dissolve)

screen aptmapup():
    imagemap:
        idle "gui/map/uppersect.png"
        hover "gui/map/uppersect - hover.png"

        hotspot (530, 492, 445, 202) action Jump("biology")
        hotspot (832, 689, 144, 91) action Jump("biology")
        hotspot (790, 235, 470, 170) action Jump("sataspen")

        hotspot (1024, 490, 464, 337) action Jump("management")
        hotspot (1354, 550, 315, 412) action Jump("management")
        hotspot (1515, 366, 153, 196) action Jump("management")

        hotspot (440, 862, 81, 94) action Hide("aptmapup"), Show("aptmap", transition=dissolve)

screen aptmapdown():
    imagemap:
        idle "gui/map/lowersect.png"
        hover "gui/map/lowersect - hover.png"

        hotspot (320, 191, 395, 173) action Jump("satgreg")
        hotspot (1018, 191, 650, 772) action Jump("wheatleycameo")
        hotspot (460, 414, 253, 302) action Jump("recovery")
        hotspot (240, 534, 145, 428) action Jump("manufacture")

        hotspot (734, 167, 71, 88) action Hide("aptmapdown"), Show("aptmap", transition=dissolve)