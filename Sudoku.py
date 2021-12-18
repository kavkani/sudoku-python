from ursina import *
import numpy as np
import random
app = Ursina()


def enable(b, t):
    if b_list[b].color == color.orange:
        b_list[b].color = color.red
    else:
        b_list[b].color = color.black
    for button in b_list:
        button.disabled = False
    if t != "X":
        b_list[b].text = t
    for num in nums:
        num.disabled = True
    deselect.disabled = True


def quit_f():
    app.close_window = True


def click(b):
    global nums, b_list, deselect
    for button in b_list:
        if button != b_list[b]:
            button.disabled = True
    if b_list[b].color == color.red:
        b_list[b].color = color.orange
    else:
        b_list[b].color = color.yellow
    for num in nums:
        num.disabled = False
        num.on_click = Func(enable, b, num.text)
    deselect.disabled = False
    deselect.on_click = Func(enable, b, deselect.text)
    return 0


b_list = []
deselect = Button(text='X', scale=0.07, position=(0.6, -0.3), color=color.blue, disabled=True)
y = 0.3
nums = []
for i in range(4):
    number = Button(text=str(i + 1), scale=0.07, position=(0.6, y), color=color.blue, disabled=True)
    nums.append(number)
    y -= 0.15
y = 0.3
for i in range(4):
    x = -0.3
    for j in range(4):
        b = Button(scale=0.18, position=(x, y), highlight_color=color.lime, color=color.black)
        b_list.append(b)
        b.on_click = Func(click, i * 4 + j)
        x += 0.2
    y -= 0.2

window.fullscreen = True
app.run()
