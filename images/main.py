from ursina import *
import click
import generator
import classes
import time
import threading
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton
import arabic_reshaper
from bidi.algorithm import get_display

app = Ursina()
window.title = "3D Sudoku"
sudoku_parent = Entity(model=None, position=(-3, 0, 0))
window.fullscreen = True
window.cog_button.enabled = False
window.fps_counter.enabled = False
window.exit_button.enabled = False
stop_thread = False
time_show = None
setting_changes = {"texture": "wood_islam", "sound_effect": "on", "language": "en"}
try:
    file = open("settings/settings.txt", 'r+')
    language = (file.readline())[:-1]
    sound_effect = (file.readline())[:-1]
    texture = (file.readline())[:-1]
    file.close()
except:
    language = 'en'
    sound_effect = 'on'
    texture = 'wood_islam'
setting_changes["language"] = language
setting_changes["sound_effect"] = sound_effect
setting_changes["texture"] = texture


def exit_game():
    global stop_thread
    stop_thread = True
    application.quit()


exit_game_button = Button(text="x", position=(0.86, 0.485), scale=(0.06, 0.03), color=color.red)
exit_game_button.on_click = Func(exit_game)


def countdown(t):
    global time_show, stop_thread, timer_on, time_check
    stop_thread = False
    timer_on = True
    time_show = Text(text="00:00")
    while t:
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        destroy(time_show)
        time_show = Text(text=timer, color=rgb(54, 158, 255), position=(-0.1, 0.4), scale=2)
        if stop_thread:
            timer_on = False
            destroy(time_show)
            return True
        time.sleep(1)
        t -= 1
    destroy(time_show)
    timer_on = False
    if time_check:
        after_check("timer")
    time_check = True


def manage_timer(t):
    timer = threading.Thread(target=countdown, args=(t,))
    timer.start()


def close_tip(t_l):
    for item in t_l:
        destroy(item)


def give_tip(tip_button):
    global setting_changes
    tip_list = []
    border = Entity(parent=tip_button, model='wireframe_quad', position=(1.04, -2.08), scale=3.043,
                    color=rgb(54, 158, 255))
    tip_list.append(border)
    t = classes.Image(photo=f"images/Tips - {setting_changes['language']}", scale=(1.05, 1.2), position=(-0.05, 0),
                      parent=border)
    tip_list.append(t)
    out = Button(scale=0.08, parent=border, position=(0.46, 0.46), color=rgb(54, 158, 255), icon="images/close")
    tip_list.append(out)
    out.on_click = Func(close_tip, tip_list)


def difficulty(num, d_l):
    global lang
    for i in range(4):
        d_l[i].enabled = False
        d_l[i].hide()
    if num == -1:
        game(num, False)
    else:
        d_l[4].enabled = True
        d_l[4].show()
        if lang[0] == "arialbd.ttf":
            yes = get_display(arabic_reshaper.reshape(lang[6]))
            no = get_display(arabic_reshaper.reshape(lang[7]))
        else:
            yes = lang[6]
            no = lang[7]
        t_yes = Button(parent=d_l[4], color=rgb(255, 151, 54), position=(0.29, -0.01), text=yes)
        t_yes.text_entity.font = f'fonts/{lang[1]}'
        t_yes.fit_to_text()
        t_yes.on_click = Func(game, num, True)
        t_no = Button(parent=d_l[4], color=rgb(255, 151, 54), position=(0.35, -0.01), text=no)
        t_no.text_entity.font = f'fonts/{lang[1]}'
        t_no.fit_to_text()
        t_no.on_click = Func(game, num, False)


def close_difficulty(main_button, difficulties):
    main_button.disabled = False
    for item in difficulties:
        item.enabled = False
        item.hide()


def difficulty_show(d_l, main_button):
    main_button.disabled = True
    for i in range(6):
        if i != 4:
            d_l[i].enabled = True
            d_l[i].show()


def save_chabges (settings_changes):
    file = open("settings/settings.txt","w")
    file.write(settings_changes["language"]+'\n')
    file.write(settings_changes["sound_effect"]+'\n')
    file.write(settings_changes["texture"]+'\n')
    file.close()

def to_home(a_l):
    for item in a_l:
        destroy(item)
    global setting_changes
    try:
        file = open("settings/settings.txt", 'r+')
        language = (file.readline())[:-1]
        sound_effect = (file.readline())[:-1]
        texture = (file.readline())[:-1]
        file.close()
    except:
        language = 'en'
        sound_effect = 'on'
        texture = 'wood_islam'
    setting_changes["language"] = language
    setting_changes["sound_effect"] = sound_effect
    setting_changes["texture"] = texture
    home()


def settings_menu():
    global home_buttons, setting_changes
    for button in home_buttons[:-1]:
        destroy(button)
    for button in home_buttons[-1]:
        destroy(button)
    home_buttons = []
    settings_list = []
    language_text = Text(text="Language:", position=(-0.3, 0.1))
    settings_list.append(language_text)

    def change_language(lang):
        setting_changes["language"] = lang
    language_dropdown = DropdownMenu('Choose Language', position=(-0.13, 0.1), buttons=(
        DropdownMenuButton('English', on_click=Func(change_language, "en"), highlight_color=rgb(54, 158, 255)),
        DropdownMenuButton("Persian", on_click=Func(change_language, "fa"), highlight_color=rgb(54, 158, 255)),
        DropdownMenuButton('French', on_click=Func(change_language, "fr"), highlight_color=rgb(54, 158, 255)),
        DropdownMenuButton('German', on_click=Func(change_language, "de"), highlight_color=rgb(54, 158, 255)),
        DropdownMenuButton('Arabic', on_click=Func(change_language, "ar"), highlight_color=rgb(54, 158, 255)),
    ))
    language_dropdown.highlight_color = rgb(54, 158, 255)
    settings_list.append(language_dropdown)

    def change_texture(wood_texture):
        setting_changes["texture"] = wood_texture
    texture_text = Text(text="Texture:", position=(-0.3, 0.3))
    settings_list.append(texture_text)
    texture_dropdown = DropdownMenu('Choose Texture', position=(-0.13, 0.3), buttons=(
        DropdownMenuButton('Wood', on_click=Func(change_texture, "wood")),
        DropdownMenuButton('Woodcarving', on_click=Func(change_texture, "wood_islam")),
    ))
    settings_list.append(texture_dropdown)
    sound_effect_text = Text(text="Sound Effect:", position=(-0.3, 0.2))
    settings_list.append(sound_effect_text)
    sound_effect_choose = ButtonGroup(('off', 'on'), position=(-0.08, 0.21), min_selection=1, default='on')
    settings_list.append(sound_effect_choose)

    def on_value_changed_sound():
        setting_changes["sound_effect"] = str(sound_effect_choose.value)

    sound_effect_choose.on_value_changed = on_value_changed_sound

    back = Button(color=rgb(255, 151, 54), text="Back", position=(-0.7, 0.4))
    back.text_entity.font = 'fonts/Soulgood.ttf'
    back.fit_to_text()
    settings_list.append(back)
    back.on_click = Func(to_home, settings_list)

    save = Button(color=rgb(255, 151, 54), text="save", position=(0.7, -0.4))
    save.text_entity.font = 'fonts/Soulgood.ttf'
    save.fit_to_text()
    settings_list.append(save)
    save.on_click = Func(save_chabges, setting_changes)


def about():
    global home_buttons
    for button in home_buttons[:-1]:
        destroy(button)
    for button in home_buttons[-1]:
        destroy(button)
    home_buttons = []
    about_list = []
    photo1 = Button(icon="images/amirmohammad", scale=0.25, position=(-0.3, 0.3))
    about_list.append(photo1)
    t1 = Text(text="Amirmohammad Kavkani", scale=3, position=(-0.15, 0.4), color=rgb(255, 164, 80),
              font='fonts/TheGodfather-v2.ttf')
    about_list.append(t1)
    d1 = Text(text="AI Department", scale=1.75, position=(-0.15, 0.3), color=rgb(255, 151, 54),
              font='fonts/SelfDestructButtonBB_reg.ttf')
    about_list.append(d1)
    photo2 = Button(icon="images/arash", scale=0.25, position=(-0.3, 0))
    about_list.append(photo2)
    t2 = Text(text="Arash Ostadsharif", scale=3, position=(-0.15, 0.1), color=rgb(255, 164, 80),
              font='fonts/TheGodfather-v2.ttf')
    about_list.append(t2)
    d2 = Text(text="Database Department", scale=1.75, position=(-0.15, 0), color=rgb(255, 151, 54),
              font='fonts/SelfDestructButtonBB_reg.ttf')
    about_list.append(d2)
    photo3 = Button(icon="images/bardia", scale=0.25, position=(-0.3, -0.3))
    about_list.append(photo3)
    t3 = Text(text="Bardia Sohrabi", scale=3, position=(-0.15, -0.2), color=rgb(255, 164, 80),
              font='fonts/TheGodfather-v2.ttf')
    about_list.append(t3)
    d3 = Text(text="Graphics Department", scale=1.75, position=(-0.15, -0.3), color=rgb(255, 151, 54),
              font='fonts/SelfDestructButtonBB_reg.ttf')
    about_list.append(d3)
    back = Button(color=rgb(255, 151, 54), text="Back", position=(-0.7, 0.4))
    back.text_entity.font = 'fonts/Soulgood.ttf'
    back.fit_to_text()
    about_list.append(back)
    back.on_click = Func(to_home, about_list)

def solver(solved):
    global stop_thread, timer_on, back_to_home_button
    for i in range(6):
        for j in range(9):
            classes.sudoku_buttons[i * 9 + j].icon = f'images/{str(solved[i][j])}'
            classes.sudoku_buttons[i * 9 + j].disabled = True
    back_to_home_button = classes.sudoku_buttons[54 + len(classes.little_cubes) * 3 + 3]
    if timer_on:
        stop_thread = True
        timer_on = False
    for item in classes.sudoku_buttons[54: 54 + len(classes.little_cubes) * 3 + 8]:
        if item != back_to_home_button:
            classes.sudoku_buttons.pop(classes.sudoku_buttons.index(item))
            destroy(item)
    classes.close_changeable()


def after_check(d, t=None, ok_b=None):
    global time_show, stop_thread, timer_on, time_check, lang
    if d == "timer":
        for button in classes.sudoku_buttons:
            if button != back_to_home_button:
                destroy(button)

        c = Button(icon='images/clock', color=rgb(64, 64, 64), disabled=True, scale=0.6)
        if lang[0] == "arialbd.ttf":
            time_is_up = get_display(arabic_reshaper.reshape(lang[8]))
        else:
            time_is_up = lang[8]

        t = Text(text=f'{time_is_up}', color=rgb(255, 151, 54), scale=3, position=(0, -0.12),
                 font=f'fonts/{lang[1]}')
        t.position = (t.position.x - (t.width/2), t.position.y, t.position.z)
        back_to_home_button.on_click = Func(home, 2, [t, c])
    elif t is None:
        for button in classes.sudoku_buttons:
            if button != back_to_home_button:
                destroy(button)
        xp_timer = 0
        if timer_on:
            stop_thread = True
            timer_on = False
            xp_timer = 32
        time.sleep(0.2)
        time_check = False
        try:
            file = open("data/points.pmd", 'r+')
            xp = eval(file.read())
            xp += d ** 2
            file.close()
        except:
            xp = d ** 2
        file = open('data/points.pmd', 'w')
        file.write(str(xp + xp_timer))
        file.close()
        if lang[0] == "arialbd.ttf":
            Congratulations = get_display(arabic_reshaper.reshape(lang[9]))
        else:
            Congratulations = lang[9]
        t = Text(text=f"{Congratulations} +{d ** 2 + xp_timer} XP", color=rgb(255, 151, 54), scale=2,
                 position=(-0.2, -0.3), font=f'fonts/{lang[1]}')
        c = Button(icon='images/cup', color=rgb(64, 64, 64), disabled=True, scale=0.6)
        back_to_home_button.on_click = Func(home, 2, [t, c])
    else:
        destroy(t)
        destroy(ok_b)


def output(d):
    global lang
    if not classes.output_nums():
        if lang[0] == "arialbd.ttf":
            solve = get_display(arabic_reshaper.reshape(lang[10]))
            ok = get_display(arabic_reshaper.reshape(lang[11]))
        else:
            solve = lang[10]
            ok = lang[11]
        t = Text(text=solve, color=color.red, scale=1.25, position=(-0.5, -0.4),
                 font=f'fonts/{lang[1]}')
        ok_button = Button(text=ok, color=color.red, position=(0.15, -0.42))
        ok_button.text_entity.font = f'fonts/{lang[1]}'
        ok_button.fit_to_text()
        ok_button.on_click = Func(after_check, d, t, ok_button)
        classes.sudoku_buttons.append(t)
        classes.sudoku_buttons.append(ok_button)
    else:
        after_check(d)


def home(scene_code=0, destroy_list = []):
    global home_buttons, stop_thread, setting_changes, lang
    stop_thread = True
    home_buttons = []
    lang = setting_changes['language']
    globals()[setting_changes['language']] = []
    en = ['calibrib.ttf', 'Soulgood.ttf', 'Settings', 'About Us', 'Tips', 'Start a New Game', 'yes', 'no', 'Time is up!'
                                                 , 'Congratulations!', 'You didn`t solve the 3D Sudoku correctly', 'OK',
                                                 'easy', 'medium', 'hard', 'expert', 'time limit?', 'check', "Solve",
                                                                            "Show Changeable Parts", "Back to Home"]

    fr = ['calibrib.ttf ', 'Soulgood.ttf', "Réglages", "À propos de nous", 'Des astuces', 'Commencer une nouvelle '
    'partie', 'oui', 'non', 'le temps est écoulé!', 'Toutes nos félicitations!', 'Vous n`avez pas correctement'
                                         ' résolu le Sudoku 3D', 'D`ACCORD', 'facile', 'moyen', 'difficile', 'expert',
                    'limite de temps?', 'Chèque', "Résoudre", "Afficher les pièces modifiables", "Retour à l'accueil"]

    de = ['calibrib.ttf ', 'Soulgood.ttf', 'Einstellungen', 'Über uns', 'Tipps', 'Starten Sie ein neues Spiel', 'ja',
    'nein', 'die Zeit ist um!', 'Herzliche Glückwünsche!','Sie haben das 3D-Sudoku nicht richtig gelöst', 'OK'
                                                                            , 'einfach', 'mittel', 'schwer', 'Experte',
                             'Zeitlimit?', 'überprüfen', "Lösen", "Änderbare Teile anzeigen", "Zurück zur Startseite"]

    fa = ["arialbd.ttf", "BYekan.ttf", "تنظیمات", "درباره ما", "نکات", "یک بازی جدید را شروع کنید", "آره", "نه",
                                                "وقت تمومه!","تبریک!", "شما سودوکو سه بعدی را درست حل نکردید", "باشه"
                                                                                    ,"آسان", "متوسط", "سخت", "متخصص",
                                            "محدودیت زمانی؟", "بررسی", "حل", "نمایش قطعات قابل تغییر", "بازگشت به خانه"]

    ar = ["arialbd.ttf", "BYekan.ttf", "إعدادات", "معلومات عنا", "نصائح", "ابدأ لعبة جديدة", "نعم", "لا", "انتهى الوقت!"
                                                 , "تهانينا!", "لم تقم بحل لعبة سودوكو ثلاثية الأبعاد بشكل صحيح", "نعم",
                                                                                "سهل" , "متوسط" , "صعب" , "خبير",
                        "المهلة؟", "التحقق من", "حل" , "إظهار الأجزاء القابلة للتغيير" , "الرجوع إلى الصفحة الرئيسية"]
    lang = locals()[lang]
    if scene_code == 1:
        for button in classes.sudoku_buttons:
            destroy(button)
        classes.sudoku_buttons = []
        classes.little_cubes = []
    if scene_code == 2:
        for i in destroy_list:
            destroy(i)
        for button in classes.sudoku_buttons:
            destroy(button)
        classes.sudoku_buttons = []
        classes.little_cubes = []
    # tutorial = Button(icon='video', scale=0.13, position=(-0.7, 0), color=rgb(255, 151, 54))
    # tutorial.on_click = Func(login_run)
    # home_buttons.append(tutorial)
    # tutorial.tooltip = Tooltip("Tutorial")
    if lang[0] == "arialbd.ttf":
        txt = get_display(arabic_reshaper.reshape(lang[2]))
    else:
        txt = lang[2]
    settings = Button(icon="images/settings", scale=0.13, position=(0.7, 0.35), color=rgb(255, 151, 54))
    settings.icon_entity.scale = 0.9
    settings.on_click = Func(settings_menu)
    home_buttons.append(settings)
    settings.tooltip = Tooltip(text=txt, font=lang[0])
    # t = Text(text="New Game", parent=new_game, position=(-0.2, -0.35), scale=5, font='fonts/Soulgood.ttf')
    if lang[0] == "arialbd.ttf":
        txt = get_display(arabic_reshaper.reshape(lang[3]))
    else:
        txt = lang[3]
    about_us = Button(text=txt, position=(0, 0.3), color=rgb(255, 151, 54))
    about_us.text_entity.font = lang[1]
    about_us.fit_to_text()
    about_us.on_click = Func(about)
    # home_buttons.append(t)
    home_buttons.append(about_us)
    if lang[0] == "arialbd.ttf":
        txt = get_display(arabic_reshaper.reshape(lang[4]))
    else:
        txt = lang[4]
    tips = Button(scale=0.13, position=(-0.7, 0.35), color=rgb(255, 151, 54), icon='images/tip')
    tips.on_click = Func(give_tip, tips)
    tips.tooltip = Tooltip(text=txt, font=lang[0])
    home_buttons.append(tips)
    sudoku = Text(text="3D Sudoku", position=(-0.23, 0.45), scale=5, color=rgb(54, 158, 255), font='fonts/Soulgood.ttf')
    home_buttons.append(sudoku)
    masjed_imam = classes.Image("images/masjed", (0.48, -0.26), (0.825, 0.49), camera.ui)
    sheykh_bahayi = Button(icon="images/sheykh", color=rgb(64, 64, 64), disabled=True, position=(-0.71, -0.31),
                           scale=(0.366, 0.375))
    if lang[0] == "arialbd.ttf":
        txt = get_display(arabic_reshaper.reshape(lang[5]))
    else:
        txt = lang[5]
    new_game = Button(icon="images/sudoku2", scale=(0.45, 0.55), color=rgb(255, 151, 54), position=(0, -0.028))
    new_game.tooltip = Tooltip(text=txt, font=lang[0])
    try:
        file = open("data/points.pmd", 'r+')
        xp = eval(file.read())
    except:
        xp = 0
    xp_show = Text(f'{xp} xp', scale=2, color=rgb(54, 158, 255), position=(-0.04, -0.45), font='fonts/Soulgood.ttf')
    home_buttons.append(new_game)
    home_buttons.append(masjed_imam)
    home_buttons.append(sheykh_bahayi)
    home_buttons.append(xp_show)
    home_buttons.append(['0'])
    del home_buttons[-1][0]
    if lang[0] == "arialbd.ttf":
        difficulty_t = get_display(arabic_reshaper.reshape(lang[12]))
    else:
        difficulty_t = lang[12]
    easy = Button(text=difficulty_t, position=(-0.122, -0.33), color=rgb(255, 151, 54), enabled=False)
    Text(text="+16 xp", parent=easy, scale=(17, 18), color=rgb(54, 158, 255), position=(-0.58, -0.7),
         font='fonts/Soulgood.ttf')
    easy.text_entity.font = f'fonts/{lang[1]}'
    easy.fit_to_text()
    easy.hide()
    easy.on_click = Func(difficulty, 4, home_buttons[-1])
    home_buttons[-1].append(easy)
    if lang[0] == "arialbd.ttf":
        difficulty_t = get_display(arabic_reshaper.reshape(lang[13]))
    else:
        difficulty_t = lang[13]
    medium = Button(text=difficulty_t, position=(-0.046, -0.33), color=rgb(255, 151, 54), enabled=False)
    Text(text="+36 xp", parent=medium, scale=(15, 18), color=rgb(54, 158, 255), position=(-0.5, -0.7),
         font='fonts/Soulgood.ttf')
    medium.text_entity.font = f'fonts/{lang[1]}'
    medium.hide()
    medium.fit_to_text()
    medium.on_click = Func(difficulty, 6, home_buttons[-1])
    home_buttons[-1].append(medium)
    if lang[0] == "arialbd.ttf":
        difficulty_t = get_display(arabic_reshaper.reshape(lang[14]))
    else:
        difficulty_t = lang[14]
    hard = Button(text=difficulty_t, position=(0.031, -0.33), color=rgb(255, 151, 54), enabled=False)
    Text(text="+64 xp", parent=hard, scale=18, color=rgb(54, 158, 255), position=(-0.58, -0.7),
         font='fonts/Soulgood.ttf')
    hard.text_entity.font = f'fonts/{lang[1]}'
    home_buttons[-1].append(hard)
    hard.hide()
    hard.fit_to_text()
    hard.on_click = Func(difficulty, 8, home_buttons[-1])
    if lang[0] == "arialbd.ttf":
        difficulty_t = get_display(arabic_reshaper.reshape(lang[15]))
    else:
        difficulty_t = lang[15]
    expert = Button(text=difficulty_t, position=(0.109, -0.33), color=rgb(255, 151, 54), enabled=False)
    Text(text="+512 xp", parent=expert, scale=(14, 18), color=rgb(54, 158, 255), position=(-0.5, -0.7),
         font='fonts/Soulgood.ttf')
    expert.text_entity.font = f'fonts/{lang[1]}'
    home_buttons[-1].append(expert)
    expert.hide()
    expert.fit_to_text()
    expert.on_click = Func(difficulty, -1, home_buttons[-1])
    # expert.position.x = e
    if lang[0] == "arialbd.ttf":
        limit = get_display(arabic_reshaper.reshape(lang[16]))
    else:
        limit = lang[16]
    time_limit = Text(text=f"{limit} (+32 xp)", color=rgb(54, 158, 255), position=(-0.2, -0.33), font=f'fonts/{lang[0]}')
    time_limit.hide()
    home_buttons[-1].append(time_limit)
    close_d = Button(scale=(0.076, 0.067), parent=new_game, position=(0.45, -0.53), color=rgb(255, 151, 54),
                     icon="images/close", enabled=False)
    close_d.hide()
    home_buttons[-1].append(close_d)
    close_d.on_click = Func(close_difficulty, new_game, home_buttons[-1])
    new_game.on_click = Func(difficulty_show, home_buttons[-1], new_game)


def game(d, t=False):
    global home_buttons, back_to_home_button
    if time_show is not None:
        destroy(time_show)
    for button in home_buttons[:-1]:
        destroy(button)
    for button in home_buttons[-1]:
        destroy(button)
    home_buttons = []
    sudoku_parent.rotation = (45, 0, -45)
    global indexes
    numbers, indexes, generated_sudoku, correct_answers = generator.generate_and_remove(d)
    if lang[0] == "arialbd.ttf":
        check = get_display(arabic_reshaper.reshape(lang[17]))
    else:
        check = lang[17]
    check_button = Button(text=check, color=rgb(54, 158, 255), position=(-0.74, -0.45))
    check_button.text_entity.font = f'fonts/{lang[1]}'
    check_button.fit_to_text()
    classes.Cube(sudoku_parent, numbers, generated_sudoku, setting_changes)
    check_button.on_click = Func(output, d)
    classes.sudoku_buttons.append(check_button)
    if lang[0] == "arialbd.ttf":
        solve = get_display(arabic_reshaper.reshape(lang[18]))
    else:
        solve = lang[18]
    solve = Button(text=solve, color=rgb(54, 158, 255), position=(-0.82, -0.45))
    solve.text_entity.font = f'fonts/{lang[1]}'
    solve.fit_to_text()
    solve.on_click = Func(solver, correct_answers)
    classes.sudoku_buttons.append(solve)
    if lang[0] == "arialbd.ttf":
        scp = get_display(arabic_reshaper.reshape(lang[19]))
    else:
        scp = lang[19]
    changeable = Button(text=scp, color=rgb(54, 158, 255), position=(-0.55, -0.45))
    changeable.text_entity.font = f'fonts/{lang[1]}'
    changeable.fit_to_text()
    classes.sudoku_buttons.append(changeable)
    changeable.on_click = Func(classes.show_changeable, generated_sudoku, changeable)
    if lang[0] == "arialbd.ttf":
        bth = get_display(arabic_reshaper.reshape(lang[20]))
    else:
        bth = lang[20]
    back_to_home_button = Button(color=rgb(255, 151, 54), text=bth, position=(-0.7, 0.4))
    back_to_home_button.text_entity.font = f'fonts/{lang[1]}'
    back_to_home_button.fit_to_text()
    classes.sudoku_buttons.append(back_to_home_button)
    back_to_home_button.on_click = Func(home, 1)
    if t:
        manage_timer(1)


def update():
    if mouse.right:
        sudoku_parent.rotation_x += mouse.velocity[1] * 630
        sudoku_parent.rotation_y += mouse.velocity[0] * 630
    if classes.clicked[0] is not None and classes.clicked[1] is not None:
        click.is_clicked(classes.sudoku_buttons, classes.clicked[0], classes.little_cubes, classes.clicked[1], indexes)
        classes.clicked = [None, None]
    if classes.delete != -1:
        c = click.cancel(classes.sudoku_buttons, classes.delete, classes.little_cubes, indexes)
        classes.delete = -1
        classes.clicked = [None, None]
        for i in range(3):
            (classes.sudoku_buttons[c[i]]).little_cube = None


timer_on = False
time_check = True
back_to_home_button = None
home_buttons = []
indexes = []
home()
"""text = "سلام"
reshaped_text = 
Text(text=bidi_text, font="fonts/arialbd.ttf")"""
app.run()
