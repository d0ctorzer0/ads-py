default daynum = "1"
default dayday = "Monday"

screen daytransition():
    timer 2.0 action Hide("daytransition")
    add "gui/black.png" #at daydiss
    vbox:
        style_prefix "dttitle"
        text "DAY [daynum]"
        xalign 0.5
        yalign 0.5
        #at daydiss
    vbox:
        style_prefix "dtsubtitle"
        text "[dayday]"
        xalign 0.5
        yalign 0.6
        #at daydiss