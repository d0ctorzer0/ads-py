screen emailday10():
    vbox:
        style_prefix "emltitle"
        text "NO NEW MESSAGES"
    vbox:
        style_prefix "nextday"
        textbutton "NEXT DAY >>" action Jump("day11")
    use affectionprogress

label e10first:
    stop music
    stop music1
    play music nine
    scene blankemail
    with fade
    call screen emailday10 with dissolve