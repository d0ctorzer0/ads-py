default daynum = "1"
default dayday = "Monday"
default timeofday = "Evening"

style dttitle_text:
    font "terminal-grotesque.ttf"
    color "#fff"
    size 100
style dtsubtitle_text:
    font "terminal-grotesque.ttf"
    color "#616161"
    size 60
style truetitle_text:
    font "alte.ttf"
    color "#fff"
    size 100
style truesubtitle_text:
    font "alte.ttf"
    color "#616161"
    size 60

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

screen timeskip():
    timer 0.5 action Hide("timeskip")
    add "gui/black.png" #at daydiss

screen creditsfadeout():
    add "gui/black.png"

screen truedaytransition():
    timer 2.0 action Hide("truedaytransition")
    add "gui/black.png" #at daydiss
    vbox:
        style_prefix "truetitle"
        text "Day [daynum]"
        xalign 0.5
        yalign 0.5
        #at daydiss
    vbox:
        style_prefix "truesubtitle"
        text "[dayday], [timeofday]"
        xalign 0.5
        yalign 0.6
        #at daydiss  