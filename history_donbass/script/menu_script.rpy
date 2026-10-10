label zastavka:
    stop music fadeout 1.0
    $ play_music_from("Mama_my_vse_bolny", 0.0, fadein=5.0, fadeout=1.0)
    scene black with dissolve
    pause 1
    show naming with dissolve 
    pause 2
    hide naming with dissolve
    pause 1
    show kr at truecenter with dissolve
    pause 2
    hide kr with dissolve 
    jump menu_script 
    hide black with dissolve
label menu_script:
    call screen menu_script with dissolve 
    screen menu_script:
        tag menu
        modal True
        add "menu_image_db"

        vbox:
            xalign 0.52
            yalign 0.5
            spacing 45

            button:
                xalign 0.5
                action [Hide("menu_script", transition=dissolve), Jump("prolog")]
                idle_background None
                hover_background None
                at button_shake
                #hover_sound afgan_sfx_list + "hover.ogg"
                #activate_sound afgan_sfx_list + "click.ogg"
                text _("Начать игру") style "button_text"

            button:
                xalign 0.5
                action ShowMenu("load")
                idle_background None
                hover_background None
                at button_shake
                text _("Загрузить") style "button_text"

            button:
                xalign 0.5
                action ShowMenu("preferences")
                idle_background None
                hover_background None
                at button_shake
                text _("Настройки") style "button_text"

            button:
                xalign 0.5
                action Quit(confirm=not True)
                idle_background None
                hover_background None
                at button_shake
                text _("Выход") style "button_text"


 
style button_text:
    font ag_Anticva
    size 70
    color "#FFFFFF"
    hover_color "#adadad"
    outlines [ (2, "#000", 0, 0) ]
    xalign 0.5
    yalign 0.5
    text_align 0.5
    layout "subtitle"