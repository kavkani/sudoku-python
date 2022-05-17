from ursina import *
import click
import generator
import classes
import time
import threading

app = Ursina()
window.title = "Sudoku 3D"
sudoku_parent = Entity(model=None, position=(-1.6, 0, 0))
window.fullscreen = True
window.cog_button.enabled = False
window.fps_counter.enabled = False
window.exit_button.enabled = False
stop_thread = False
time_show = None


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
    tip_list = []
    border = Entity(parent=tip_button, model='wireframe_quad', position=(1.04, -2.08), scale=3.043,
                    color=rgb(54, 158, 255))
    tip_list.append(border)
    t = Text(parent=border, text="Click on New Game and start\nplaying!\n\nIn the game if you hold right click,\nyou "
                                 "can rotate the cube. To put a\nlittle cube in an empty place, click\non one side of "
                                 "the little cube and\nthen click on where you want it to\nbe positioned. If you want "
                                 "to undo\nany placement, just click on one\nside of the positioned little cube\nand "
                                 "click backspace.\n\nGood Luck!\n:)",
             scale=2.47, position=(-0.49, 0.49))
    tip_list.append(t)
    out = Button(scale=0.08, parent=border, position=(0.46, 0.46), color=rgb(54, 158, 255), icon="images/close")
    tip_list.append(out)
    out.on_click = Func(close_tip, tip_list)


def difficulty(num, d_l):
    for i in range(3):
        d_l[i].disabled = True
        d_l[i].hide()
    d_l[3].disabled = False
    d_l[3].show()
    t_yes = Button(parent=d_l[3], color=rgb(255, 151, 54), position=(0.29, -0.01), text="Yes")
    t_yes.text_entity.font = 'fonts/Soulgood.ttf'
    t_yes.fit_to_text()
    t_yes.on_click = Func(game, num, True)
    t_no = Button(parent=d_l[3], color=rgb(255, 151, 54), position=(0.35, -0.01), text="No")
    t_no.text_entity.font = 'fonts/Soulgood.ttf'
    t_no.fit_to_text()
    t_no.on_click = Func(game, num, False)


def difficulty_show(d_l, main_button):
    main_button.disabled = True
    for i in range(3):
        d_l[i].disabled = False
        d_l[i].show()


def to_home(a_l):
    for item in a_l:
        destroy(item)
    home()


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
    global time_show, stop_thread, timer_on, time_check
    if d == "timer":
        for button in classes.sudoku_buttons:
            if button != back_to_home_button:
                destroy(button)
        c = Button(icon='images/clock', color=rgb(64, 64, 64), disabled=True, scale=0.6)
        t = Text(text='Time is up!', color=rgb(255, 151, 54), scale=3, position=(-0.15, -0.3),
                 font='fonts/Soulgood.ttf')
        back_to_home_button.on_click = Func(home, 2, t, c)
    if t is None:
        for button in classes.sudoku_buttons:
            if button != back_to_home_button:
                destroy(button)
        xp_timer = 0
        if timer_on:
            stop_thread = True
            timer_on = False
            xp_timer = 30
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
        t = Text(text=f"Congratulations! +{d ** 2 + xp_timer} XP", color=rgb(255, 151, 54), scale=2,
                 position=(-0.2, -0.3), font='fonts/Soulgood.ttf')
        c = Button(icon='images/cup', color=rgb(64, 64, 64), disabled=True, scale=0.6)
        back_to_home_button.on_click = Func(home, 2, t, c)
    else:
        destroy(t)
        destroy(ok_b)


def output(d):
    if not classes.output_nums():
        t = Text(text="You didn't solve the 3D Sudoku correctly", color=color.red, scale=1.25, position=(-0.5, -0.4),
                 font='fonts/Soulgood.ttf')
        ok_button = Button(text="OK", color=color.red, position=(0.15, -0.42))
        ok_button.text_entity.font = 'fonts/Soulgood.ttf'
        ok_button.fit_to_text()
        ok_button.on_click = Func(after_check, d, t, ok_button)
        classes.sudoku_buttons.append(t)
        classes.sudoku_buttons.append(ok_button)
    else:
        after_check(d)


def home(scene_code=0, t=None, c=None):
    global home_buttons, stop_thread
    stop_thread = True
    home_buttons = []
    if scene_code == 1:
        for button in classes.sudoku_buttons:
            destroy(button)
        classes.sudoku_buttons = []
        classes.little_cubes = []
    if scene_code == 2:
        destroy(t)
        destroy(c)
        for button in classes.sudoku_buttons:
            destroy(button)
        classes.sudoku_buttons = []
        classes.little_cubes = []
    # tutorial = Button(icon='video', scale=0.13, position=(-0.7, 0), color=rgb(255, 151, 54))
    # tutorial.on_click = Func(login_run)
    # home_buttons.append(tutorial)
    # tutorial.tooltip = Tooltip("Tutorial")
    account = Button(icon="images/account", scale=0.13, position=(0.7, 0.35), color=rgb(255, 151, 54))
    # account.on_click = Func(login_run)
    home_buttons.append(account)
    account.tooltip = Tooltip("Account")
    # t = Text(text="New Game", parent=new_game, position=(-0.2, -0.35), scale=5, font='fonts/Soulgood.ttf')
    about_us = Button(text="ABOUT US", position=(0, 0.3), color=rgb(255, 151, 54))
    about_us.text_entity.font = 'fonts/Soulgood.ttf'
    about_us.fit_to_text()
    about_us.on_click = Func(about)
    # home_buttons.append(t)
    home_buttons.append(about_us)
    tips = Button(scale=0.13, position=(-0.7, 0.35), color=rgb(255, 151, 54), icon='images/tip')
    tips.on_click = Func(give_tip, tips)
    tips.tooltip = Tooltip("Tips")
    home_buttons.append(tips)
    sudoku = Text(text="3D Sudoku", position=(-0.23, 0.45), scale=5, color=rgb(54, 158, 255), font='fonts/Soulgood.ttf')
    home_buttons.append(sudoku)
    masjed_imam = classes.Image("images/masjed")
    """masjed_imam = Button(icon="masjed", color=rgb(64, 64, 64), disabled=True, position=(0.47, -0.25),
                         scale=(0.842, 0.5))"""
    sheykh_bahayi = Button(icon="images/sheykh", color=rgb(64, 64, 64), disabled=True, position=(-0.71, -0.31),
                           scale=(0.366, 0.375))
    new_game = Button(icon="images/sudoku2", scale=(0.45, 0.55), color=rgb(255, 151, 54), position=(0, -0.028))
    new_game.tooltip = Tooltip("Start a new game")
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
    easy = Button(text="Easy", position=(-0.077, -0.33), color=rgb(255, 151, 54), disabled=True)
    Text(text="+16 xp", parent=easy, scale=(17, 18), color=rgb(54, 158, 255), position=(-0.58, -0.7),
         font='fonts/Soulgood.ttf')
    easy.text_entity.font = 'fonts/Soulgood.ttf'
    easy.fit_to_text()
    easy.hide()
    easy.on_click = Func(difficulty, 4, home_buttons[-1])
    home_buttons[-1].append(easy)
    medium = Button(text="Medium", position=(0, -0.33), color=rgb(255, 151, 54), disabled=True)
    Text(text="+36 xp", parent=medium, scale=(15, 18), color=rgb(54, 158, 255), position=(-0.5, -0.7),
         font='fonts/Soulgood.ttf')
    medium.text_entity.font = 'fonts/Soulgood.ttf'
    medium.hide()
    medium.fit_to_text()
    medium.on_click = Func(difficulty, 6, home_buttons[-1])
    home_buttons[-1].append(medium)
    hard = Button(text="Hard", position=(0.076, -0.33), color=rgb(255, 151, 54), disabled=True)
    Text(text="+64 xp", parent=hard, scale=18, color=rgb(54, 158, 255), position=(-0.5, -0.7),
         font='fonts/Soulgood.ttf')
    hard.text_entity.font = 'fonts/Soulgood.ttf'
    home_buttons[-1].append(hard)
    hard.hide()
    hard.fit_to_text()
    hard.on_click = Func(difficulty, 8, home_buttons[-1])
    time_limit = Text(text="Time limit? (+30 xp)", color=rgb(54, 158, 255), position=(-0.2, -0.33))
    time_limit.hide()
    home_buttons[-1].append(time_limit)
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
    check_button = Button(text="Check", color=rgb(54, 158, 255), position=(-0.74, -0.45))
    check_button.text_entity.font = 'fonts/Soulgood.ttf'
    check_button.fit_to_text()
    classes.Cube(sudoku_parent, numbers, generated_sudoku)
    check_button.on_click = Func(output, d)
    classes.sudoku_buttons.append(check_button)
    solve = Button(text="Solve", color=rgb(54, 158, 255), position=(-0.82, -0.45))
    solve.text_entity.font = 'fonts/Soulgood.ttf'
    solve.fit_to_text()
    solve.on_click = Func(solver, correct_answers)
    classes.sudoku_buttons.append(solve)
    changeable = Button(text="Show Changeable Parts", color=rgb(54, 158, 255), position=(-0.55, -0.45))
    changeable.text_entity.font = 'fonts/Soulgood.ttf'
    changeable.fit_to_text()
    classes.sudoku_buttons.append(changeable)
    changeable.on_click = Func(classes.show_changeable, generated_sudoku, changeable)
    back_to_home_button = Button(color=rgb(255, 151, 54), text="Back to Home", position=(-0.7, 0.4))
    back_to_home_button.text_entity.font = 'fonts/Soulgood.ttf'
    back_to_home_button.fit_to_text()
    classes.sudoku_buttons.append(back_to_home_button)
    back_to_home_button.on_click = Func(home, 1)
    if t:
        manage_timer(20 * d)


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
app.run()
