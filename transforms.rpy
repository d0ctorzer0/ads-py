transform bounce:
    linear 0.05 yoffset -10
    linear 0.05 yoffset 0

transform tilted:
    rotate 25 #change this to rotate more

transform tilted2:
    rotate -17 #change this to rotate more

transform ab_tilt:
    rotate -4.5

transform daydiss:
    on hide:
        linear 0.5 alpha 0.0

transform gallery_size:
    zoom 0.21

define gentleswitch = { "master" : Dissolve(0.2) }

transform emaildiss:
    on show:
        alpha 0.0
        linear 1.0 alpha 1.0