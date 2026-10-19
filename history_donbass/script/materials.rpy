
    
init -10 python:
    ROOT_DIR = "mods/history_donbass/"
    IMAGES = ROOT_DIR + "img/"

    image_subdirs = ["img/bg/", "img/cg/", "img/sp/", "img/anim/", "img/ach/", "img/menu_image/", "img/"]

    for i in renpy.list_files():
        if i.startswith(ROOT_DIR + "img/") and i.endswith((".jpg", ".png")):
            for subdir in image_subdirs:
                full_prefix = ROOT_DIR + subdir
                if i.startswith(full_prefix):
                    image_tag = i[len(full_prefix):].rsplit('.', 1)[0]
                    if image_tag:
                        renpy.image(image_tag, i)
                    break 

init -5:
    image img_paramtext = ParameterizedText(xalign=.5, yalign=.5, font=ROOT_DIR + "img/fonts/font_Cygre.ttf")

    #Шрифты
    $ ag_font_cour = ROOT_DIR + "img/fonts/cour.ttf"
    $ ag_font_cygre = ROOT_DIR + "img/fonts/font_Cygre.ttf"
    $ ag_typewriter = ROOT_DIR + "img/fonts/cour.ttf"
    $ ag_Anticva = ROOT_DIR + "img/fonts/Anticva.ttf"
    $ ag_Trender = ROOT_DIR + "img/fonts/Trender.ttf"

    # Скрипт автообьявления звуков в модификации

init -1199 python:
    from os import path
    mod_prefix = False 
    if mod_prefix:
        mod_prefix = '_' + mod_prefix
    else:
        mod_prefix = ''
    modID = 'sound' 

    for file in renpy.list_files(): 
        if modID in file:
            file_name = path.splitext(path.basename(file))[0] + mod_prefix
            if file.endswith((".wav", ".mp2", ".mp3", ".ogg", ".opus")):
                globals()[file_name] = file
                
init:
    
    ##  Персонажи  ## 
    define alena = Character(u"Алена", color="#FFB6C1", what_color="#ffffff")
    define egor = Character(u"Егор", color="#98FB98", what_color="#ffffff")
    define dima = Character(u"Дмитрий", color="#778899", what_color="#ffffff")
    define marina = Character(u"Марина", color="#FFD700", what_color="#ffffff")
    define batushka = Character(u"Батюшка", color="#DCDCDC", what_color="#ffffff")
    define prolog_nar = Character(None, what_color="#ffffff", what_font=ag_font_cour, what_size=44, what_outlines=[(2, "#000", 0, 0)])

    define tvzh = Character(u"Кореспондент", color="#FF7F50", what_color="#ffffff")
    define tvid = Character(u"Телеведущая", color="#FAEBD7", what_color="#ffffff")   

    # NVL-версии для новостных вставок
    define tvid_nvl = Character(u"Телеведущая", color="#FAEBD7", kind=nvl)
    define tvzh_nvl = Character(u"Кореспондент", color="#FF7F50", kind=nvl)
    
init:
    
    ##    Видео    ##

    $ video_list = {
        "menu":ROOT_DIR + "other_materials/video/menu_item.webm",
    }
    
    
    image menu_video_bg = Movie(play=video_list["menu"], loop=True, channel="movie", volume=0.0)

init:


    ##    Звуки    ##

    $ donbass_sfx_list = (ROOT_DIR + "sound/sfx/")
    $ donbass_amb_list = (ROOT_DIR + "sound/amb/")
    $ donbass_mus_list = (ROOT_DIR + "sound/mus/")

    $ renpy.music.register_channel("ambience", "ambience", True)

init python:
    def play_music_from(track, start_time=0.0, fadein=2.0, fadeout=2.0, loop=True, ext=".mp3"):
        file_path = "<from " + str(start_time) + ">" + store.donbass_mus_list + track + ext
        renpy.music.play(file_path, fadein=fadein, fadeout=fadeout, loop=loop)
        
init:
    ##    Anim    ##   
    
    image anger:
        IMAGES + "anim/nenav1.png" with dspr
        pause 0.2
        IMAGES + "anim/nenav2.png" with dspr
        pause 0.2
        IMAGES + "anim/nenav3.png" with dspr
        pause 0.2 
        IMAGES + "anim/nenav4.png" with dspr
        pause 0.2
        IMAGES + "anim/nenav5.png" with dspr
        pause 0.2
        IMAGES + "anim/nenav6.png" with dspr
        pause 0.2
        IMAGES + "anim/nenav7.png" with dspr
        pause 0.2
        IMAGES + "anim/nenav6.png" with dspr
        pause 0.2
        IMAGES + "anim/nenav5.png" with dspr
        pause 0.2
        IMAGES + "anim/nenav4.png" with dspr
        pause 0.2
        IMAGES + "anim/nenav3.png" with dspr
        pause 0.2
        IMAGES + "anim/nenav2.png" with dspr
        pause 0.2
        repeat
#init:

    # Ачивки

    #image ach_quote_unblock = "mods/Afgan/img/ach/ach_quote_unblock.png"

            
init:

    #transfors

    # подпрыгивание персонажа
    transform leap(dt=.25, dyz=.01, dxz=.005):
        subpixel True
        xzoom 1 yzoom 1
        easein dt*.35 yzoom 1+dyz xzoom 1-dxz
        easeout dt*.35 yzoom 1 xzoom 1
        easein dt*.15 yzoom 1-dyz xzoom 1+dxz
        easeout dt*.15 yzoom 1 xzoom 1

    transform button_shake:
        on hover:
            subpixel True
            linear 0.05 xoffset 2
            linear 0.05 xoffset -2
            linear 0.05 xoffset 1
            linear 0.05 xoffset -1
            linear 0.05 xoffset 0
        on idle:
            linear 0.1 xoffset 0


    transform all_ach:
        pos(0.85, 0.85)
        anchor(0.5, 0.5)
        zoom 0.0
        ease 1.5 zoom 1.05
        ease 0.25 zoom 0.95
        ease 0.25 zoom 1.0
        pause 4.0
        ease 0.5 pos(0.8, 0.85)
        ease 0.5 pos(1.0, 0.85) alpha 0.0     

    transform run:
        zoom 1.05 anchor (48,27)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (25,25)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (-25,25)
        repeat

    transform walkpior:
        align (0.5, 0.5)
        zoom 1.01
        ease 0.5 xalign 0.35 yalign 0.65
        ease 0.5 xalign 0.50 yalign 0.50
        ease 0.5 xalign 0.65 yalign 0.65
        ease 0.5 xalign 0.50 yalign 0.50
        repeat

                           

init:
    # трансформация для перемещения фона
    transform moveleft(delay=7.5):
        xalign 1.0
        linear delay xalign 0.0
        repeat


init:
    image et_random_lf:
        choice:
            IMAGES + "anim/et_lf_1.png"
        choice:
            IMAGES + "anim/et_lf_2.png"
        choice:
            IMAGES + "anim/et_lf_3.png"
        choice:
            IMAGES + "anim/et_lf_4.png"
        choice:
            IMAGES + "anim/et_lf_5.png"
        xanchor 0.5 yanchor 0.5 rotate 0
        parallel:
            choice:
                rotate 0
                linear 5 rotate 360
                repeat
            choice:
                rotate 0
                linear 7 rotate -360
                repeat
            choice:
                rotate 0
                linear 9 rotate 360
                repeat
            choice:
                rotate 0
                linear 11 rotate -360
                repeat
            choice:
                rotate 0
                linear 13 rotate 360
                repeat
            choice:
                rotate 0
                linear 15 rotate -360
                repeat
        parallel:
            choice:
                ease 3 xzoom 1.0
            choice:
                ease 3 xzoom 0.5
            choice:
                ease 3 xzoom 0.0
            choice:
                ease 3 xzoom -0.5
            choice:
                ease 3 xzoom -1.0
            repeat
        parallel:
            choice:
                ease 3 yzoom 1.0
            choice:
                ease 3 yzoom 0.5
            choice:
                ease 3 yzoom 0.0
            choice:
                ease 3 yzoom -0.5
            choice:
                ease 3 yzoom -1.0
            repeat

    image et_moving_lf:
        "et_random_lf"
        parallel:
            choice:
                xpos -0.1 ypos 0.2
            choice:
                xpos -0.1 ypos 0.1
            choice:
                xpos -0.1 ypos 0.0
            choice:
                xpos 0.0 ypos -0.1
            choice:
                xpos 0.0 ypos -0.2
            choice:
                xpos 0.1 ypos -0.1
            choice:
                xpos 0.1 ypos -0.2
            choice:
                xpos 0.2 ypos -0.1
            choice:
                xpos 0.2 ypos -0.2
            choice:
                xpos 0.3 ypos -0.1
            choice:
                xpos 0.3 ypos -0.2
        parallel:
            choice:
                easeout 10 xpos 0.5
            choice:
                easeout 10 xpos 0.6
            choice:
                easeout 10 xpos 0.7
            choice:
                easeout 10 xpos 0.8
            choice:
                easeout 10 xpos 0.9
            choice:
                easeout 10 xpos 1.0
            choice:
                easeout 10 xpos 1.1
        parallel:
            choice:
                linear 7 ypos 1.1
            choice:
                linear 8 ypos 1.1
            choice:
                linear 9 ypos 1.1
            choice:
                linear 10 ypos 1.1
            choice:
                linear 10 ypos 1.1
        repeat

    image et_lf:
        contains:
            "et_moving_lf"
        contains:
            pause 0.5
            "et_moving_lf"
        contains:
            pause 1.0
            "et_moving_lf"
        contains:
            pause 1.5
            "et_moving_lf"
        contains:
            pause 2.0
            "et_moving_lf"
        contains:
            pause 2.5
            "et_moving_lf"
        contains:
            pause 3.0
            "et_moving_lf"
        contains:
            pause 3.5
            "et_moving_lf"
        contains:
            pause 4.0
            "et_moving_lf"
        contains:
            pause 4.5
            "et_moving_lf"
        contains:
            pause 5.0
            "et_moving_lf"
        contains:
            pause 5.5
            "et_moving_lf"
        contains:
            pause 6.0
            "et_moving_lf"
        contains:
            pause 6.5
            "et_moving_lf"
        contains:
            pause 7.0
            "et_moving_lf"
        contains:
            pause 7.5
            "et_moving_lf"
        contains:
            pause 8.0
            "et_moving_lf"
        contains:
            pause 8.5
            "et_moving_lf"
        contains:
            pause 9.0
            "et_moving_lf"
        contains:
            pause 9.5
            "et_moving_lf"

    image et_lf2:
        contains:
            "et_lf"
        contains:
            "et_lf"

    image et_lf3:
        contains:
            "et_lf"
        contains:
            "et_lf"
        contains:
            "et_lf"        
    