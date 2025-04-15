label satend:
    scene black with fade
    n "It's getting late. What's your plans for tonight?"
    menu:
        "Dinner with Kris at the lounge." if inv_kris == True:
            jump satend_kris
        "Watching Heath's performance." if inv_heath == True:
            jump satend_heath
        "Visit CC to see what he's prepared." if inv_cc == True:
            jump satend_cc
        "{i}Mycena chlorophos{/i} with Aspen." if inv_aspen == True:
            jump satend_aspen
        "Watching the SuperBowl with Rob." if inv_rob == True:
            jump satend_rob

        "I think I'll just go to bed early.":
            jump satend_mc