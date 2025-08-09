#image e happy = "images/characters/esther/happy.png"
#image e laugh = "images/characters/esther/laugh.png"
#image e shock = "images/characters/esther/shock.png"

default secretchance = "night" 
image mcroom nightchance = "[persistent.bgtype]mcroom [secretchance].png"

image office = "[persistent.bgtype]office.png"
image krisroom = "[persistent.bgtype]krisroom.png"
image krisroom noscreen = "[persistent.bgtype]krisroom noscreen.png"
image heathroom = "[persistent.bgtype]heathroom.png"
image aspenroom = "[persistent.bgtype]aspenroom.png"
image aspenroom night = "[persistent.bgtype]aspenroom night.png"
image ccroom = "[persistent.bgtype]ccroom.png"
image robroom = "[persistent.bgtype]robroom.png"
image lounge = "[persistent.bgtype]lounge.png"
image hall = "[persistent.bgtype]hall.png"
image mcroom day = "[persistent.bgtype]mcroom day.png"
image mcroom night = "[persistent.bgtype]mcroom night.png"
image stairs = "[persistent.bgtype]stairs.png"
image closet = "[persistent.bgtype]closet.png"
image hall hell = "[persistent.bgtype]hall hell.png"
image krisroom hell = "[persistent.bgtype]krisroom hell.png"
image ccroom hell = "[persistent.bgtype]ccroom hell.png"
image heathroom hell = "[persistent.bgtype]heathroom hell.png"
image robroom hell = "[persistent.bgtype]robroom hell.png"

image door1 warm = "[persistent.bgtype]door1 warm.png"
image door1 cool = "[persistent.bgtype]door1 cool.png"
image door1 dark = "[persistent.bgtype]door1 dark.png"

image door2 = "[persistent.bgtype]door2.png"
image door2 cool = "[persistent.bgtype]door2 cool.png"

image door3 warm = "[persistent.bgtype]door3 warm.png"
image door3 no outoforder = "[persistent.bgtype]door3 no outoforder.png"
image door3 cool = "[persistent.bgtype]door3 cool.png"
image door3 dark = "[persistent.bgtype]door3 dark.png"

image neuro:
    "gui/boss/neuro/n_1.png"
    pause .15
    "gui/boss/neuro/n_2.png"
    pause .15
    "gui/boss/neuro/n_3.png"
    pause .15
    "gui/boss/neuro/n_4.png"
    pause .15
    "gui/boss/neuro/n_5.png"
    pause .15
    "gui/boss/neuro/n_6.png"
    pause .15
    "gui/boss/neuro/n_7.png"
    pause .15
    "gui/boss/neuro/n_8.png"
    pause .15
    "gui/boss/neuro/n_9.png"
    pause .15
    "gui/boss/neuro/n_10.png"
    pause .15
    "gui/boss/neuro/n_11.png"
    # total time = 1.5

image neurorepeat:
    "gui/boss/neuro/n_7.png"
    pause .15
    "gui/boss/neuro/n_8.png"
    pause .15
    "gui/boss/neuro/n_9.png"
    pause .15
    "gui/boss/neuro/n_10.png"
    pause .15
    "gui/boss/neuro/n_11.png"
    repeat

image laser:
    "gui/boss/laser/l_1.png"
    pause .05
    "gui/boss/laser/l_2.png"
    pause .05
    "gui/boss/laser/l_3.png"
    pause .05
    "gui/boss/laser/l_4.png"
    pause .05
    "gui/boss/laser/l_5.png"
    pause .05
    "gui/boss/laser/l_6.png"
    pause .05
    "gui/boss/laser/l_7.png"
    pause .05
    "gui/boss/laser/l_8.png"
    pause .05
    #total time = 0.4


# ESTHER BOSS IMAGES #################################

image esther idle:
    "gui/boss/esther/idle_1.png"
    pause .5
    "gui/boss/esther/idle_2.png"
    pause .5
    "gui/boss/esther/idle_3.png"
    pause .5
    "gui/boss/esther/idle_4.png"
    pause .5
    "gui/boss/esther/idle_5.png"
    pause .5
    repeat

image esther snob:
    "gui/boss/esther/snob_1.png"
    pause .5
    "gui/boss/esther/snob_2.png"
    pause .5
    "gui/boss/esther/snob_3.png"
    pause .5
    "gui/boss/esther/snob_4.png"
    pause .5
    "gui/boss/esther/snob_5.png"
    pause .5
    repeat

image esther stun:
    "gui/boss/esther/stun_1.png"
    pause .5
    "gui/boss/esther/stun_2.png"
    pause .5
    "gui/boss/esther/stun_3.png"
    pause .5
    "gui/boss/esther/stun_4.png"
    pause .5
    "gui/boss/esther/stun_3.png"
    pause .5
    "gui/boss/esther/stun_2.png"
    pause .5
    repeat

image esther up:
    "gui/boss/esther/esther up.png"

image esther down:
    "gui/boss/esther/esther down.png"

image esther downleft:
    "gui/boss/esther/esther downleft.png"

image esther squint:
    "gui/boss/esther/esther squint.png"

image flash:
    "#b3000070"
    alpha 0.0
    linear .45 alpha 0.5
    pause 0.55     
    linear .45 alpha 0.0
    repeat