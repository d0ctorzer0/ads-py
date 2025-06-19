transform bounce:
    linear 0.05 yoffset -10
    linear 0.05 yoffset 0

transform tilted:
    rotate 25 #change this to rotate more

transform tilted2:
    rotate -17 #change this to rotate more

transform ab_tilt:
    rotate -4.5

transform save_tilt:
    matrixtransform RotateMatrix(0.0, 0.0, -14)

transform cred_tilt:
    rotate -8

transform disc_tilt:
    rotate 5

transform delete_tilt:
    matrixtransform RotateMatrix(0.0, 0.0, -90)

transform daydiss:
    on hide:
        linear 0.5 alpha 0.0

transform gallery_size:
    zoom 0.21

define gentleswitch = { "master" : Dissolve(0.2) }
define vigswitch = Dissolve(0.1)
define gallswitch = Dissolve(0.3)

transform emaildiss:
    on show:
        alpha 0.0
        linear 1.0 alpha 1.0

screen vignette():
    add "vignette.png"

transform splashfadeout:
    alpha 1.00
    easeout 1.0 alpha 0.00