style file_text:
    font "terminal-grotesque.ttf"
    color "#f0f0f0"
    hover_color "#fff"
    xpos 30
    ypos 30

screen gallery:
    style_prefix "file"
    text "<<< back"
    if kgunlock == False:
        add "gui/gallery/krislocked.png"