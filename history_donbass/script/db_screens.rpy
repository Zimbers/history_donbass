
init 50:

    style db_quick_button is default:
        background None
        xpadding 10
        ypadding 5

    style db_quick_button_text is default:
        font ag_font_cygre
        size 24
        color "#ffffff88"
        hover_color "#ffffff"
        outlines [(2, "#000", 0, 0)]

    style nvl_dialogue:
        font ag_font_cour
        size 44
        outlines [(2, "#000", 0, 0)]
        xalign 0.5
        text_align 0.5

    style nvl_label:
        font ag_font_cour
        size 50
        outlines [(2, "#000", 0, 0)]
        xalign 0.5
        text_align 0.5

init 100:
    screen db_quick_menu():
        zorder 200
        tag db_quick_menu
        default q_alpha = 0.0

        hbox:
            xalign 0.5 
            ypos 0.96
            spacing 40
            at transform:
                linear 0.2 alpha q_alpha

            style_prefix "db_quick"

            textbutton _("Назад") action Rollback()
            #textbutton _("История") action ShowMenu('history')
            #textbutton _("Пропуск") action Skip()
            #textbutton _("Авто") action Preference("auto-forward", "toggle")
            textbutton _("Сохранить") action ShowMenu('save')
            textbutton _("Загрузить") action ShowMenu("load")
            textbutton _("Настройки") action ShowMenu('preferences')

        mousearea:
            area (0, 1250, 2000, 250)
            hovered SetScreenVariable("q_alpha", 1.0)
            unhovered SetScreenVariable("q_alpha", 0.0)

    screen say(who, what, side_image=None, two_window=False):
        zorder 150
        tag say
        window:
            background None
            xalign 0.5
            ypos 1.13
            yanchor 1.0 
            xfill False
            yfill False 
            margin (0, 0, 0, 0) 
            padding (0, 0, 0, 0) 
            yminimum 0 

            frame:
                id "window"
                xfill False
                yminimum 0
                background Frame("mods/history_donbass/img/ui/frame.png", 40, 40) 
                xmaximum 1300 
                yoffset -180
                padding (100, 80, 100, 65) 
 
                vbox:
                    xalign 0.5
                    spacing 10
                    if who:
                        text who:
                            id "who"
                            font ag_font_cour
                            outlines [(4, '#000', 0, 0)]
                            size 50
                            xalign 0.5
                            text_align 0.5
                    text what:
                        id "what"
                        font ag_font_cour
                        size 44
                        outlines [(4, '#000', 0, 0)]
                        text_align 0.5
                        xalign 0.5
                        line_spacing 1
                        slow_cps 40

        if side_image:
            add side_image
        else:
            add SideImage() xalign 0.0 yalign 1.0

    screen nvl(dialogue, items=None):
        zorder 150
        tag nvl
        window:
            style "nvl_window"
            padding (150, 80, 150, 80) 

            has vbox:
                style "nvl_vbox"
                spacing 25

            for who, what, who_id, what_id, window_id in dialogue:
                window:
                    id window_id
                    has vbox:
                        xalign 0.5
                        spacing 5

                    if who is not None:
                        text who id who_id

                    text what id what_id

            if items:
                vbox:
                    id "menu"
                    for caption, action, chosen in items:
                        if action:
                            button:
                                style "nvl_menu_choice_button"
                                action action
                                text caption style "nvl_menu_choice"
                        else:
                            text caption style "nvl_dialogue"
    
