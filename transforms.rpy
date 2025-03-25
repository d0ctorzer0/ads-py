transform bounce:
    linear 0.05 yoffset -10
    linear 0.05 yoffset 0

transform tilted:
    rotate 25 #change this to rotate more

transform tilted2:
    rotate -17 #change this to rotate more

transform daydiss:
    on hide:
        linear 0.5 alpha 0.0

define gentleswitch = { "master" : Dissolve(0.2) }