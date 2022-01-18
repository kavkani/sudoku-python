from ursina import *
app = Ursina()


def quit_f():
    app.close_window = True


def change(b, num):
    global b_list
    flag = 0
    b_list[b].text = str(num)
    for i in range(len(b_list)):
        if (b % 4 == i % 4 or b // 4 == i // 4) and i != b:
            if b_list[b].text == b_list[i].text:
                b_list[b].color = color.red
                flag = 1
    if flag == 0:
        b_list[b].color = color.black
    destroy(one)
    destroy(two)
    destroy(three)
    destroy(four)
    destroy(five)
    destroy(six)
    destroy(seven)
    destroy(eight)
    destroy(nine)
    flag2 = 0
    for i in range(len(b_list)):
        if b_list[i].text != "1" and b_list[i].text != "2" and b_list[i].text != "3" and b_list[i].text != "4":
            flag2 = 1
        elif b_list[i].color == color.red:
            flag2 = 1
    if flag2 == 0:
        for j in range(len(b_list)):
            b_list[j].on_click = None
        done = Text(text="You've solved it!", scale=2, position=(-0.15, 0.48))
        quit_b = Button(text="Quit", position=(0, -0.48), scale=1)
        quit_b.fit_to_text()
        quit_b.on_click = Func(quit_f())


def click(b):
    global one, two, three, four, five, six, seven, eight, nine, b_list
    if (b_list[b].text == "1" or b_list[b].text == "2" or b_list[b].text == "3" or b_list[b].text == "4") and b_list[b].color != color.red:
        return 0
    for i in range(len(b_list)):
        if b_list[i].color != color.red and b_list[i].color != color.orange:
            b_list[i].color = color.black
        elif b_list[i].color == color.orange:
            b_list[i].color = color.red
    if b_list[b].color == color.red:
        b_list[b].color = color.orange
    elif b_list[b].color == color.orange:
        b_list[b].color = color.red
        destroy(one)
        destroy(two)
        destroy(three)
        destroy(four)
        destroy(five)
        destroy(six)
        destroy(seven)
        destroy(eight)
        destroy(nine)
        return 0
    elif b_list[b].color == color.yellow:
        b_list[b].color = color.black
        destroy(one)
        destroy(two)
        destroy(three)
        destroy(four)
        destroy(five)
        destroy(six)
        destroy(seven)
        destroy(eight)
        destroy(nine)
        return 0
    else:
        b_list[b].color = color.yellow
    one = Button(text='1', scale=0.07, position=(0.6, 0.3), color=color.blue)
    one.on_click = Func(change, b, 1)
    two = Button(text='2', scale=0.07, position=(0.6, 0.15), color=color.blue)
    two.on_click = Func(change, b, 2)
    three = Button(text='3', scale=0.07, position=(0.6, 0), color=color.blue)
    three.on_click = Func(change, b, 3)
    four = Button(text='4', scale=0.07, position=(0.6, -0.15), color=color.blue)
    four.on_click = Func(change, b, 4)
    return 0
    # five = Button(text='5', scale=0.05, position=(0.6, 0.05), color=color.blue)
    # five.on_click = Func(change, b, 5)
    # six = Button(text='6', scale=0.05, position=(0.6, -0.05), color=color.blue)
    # six.on_click = Func(change, b, 6)
    # seven = Button(text='7', scale=0.05, position=(0.6, -0.15), color=color.blue)
    # seven.on_click = Func(change, b, 7)
    # eight = Button(text='8', scale=0.05, position=(0.6, -0.25), color=color.blue)
    # eight.on_click = Func(change, b, 8)
    # nine = Button(text='9', scale=0.05, position=(0.6, -0.35), color=color.blue)
    # nine.on_click = Func(change, b, 9)


window.fullscreen = True
one, two, three, four, five, six, seven, eight, nine, flag = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
b1 = Button(scale=0.18, position=(-0.3, 0.3), highlight_color=color.lime, color=color.black)
b1.on_click = Func(click, 0)
b2 = Button(scale=0.18, position=(-0.1, 0.3), highlight_color=color.lime, color=color.black, text="3")
b2.on_click = Func(click, 1)
b3 = Button(scale=0.18, position=(0.1, 0.3), highlight_color=color.lime, color=color.black, text="4")
b3.on_click = Func(click, 2)
b4 = Button(scale=0.18, position=(0.3, 0.3), highlight_color=color.lime, color=color.black, text="1")
b4.on_click = Func(click, 3)
b5 = Button(scale=0.18, position=(-0.3, 0.1), highlight_color=color.lime, color=color.black, text="4")
b5.on_click = Func(click, 4)
b6 = Button(scale=0.18, position=(-0.1, 0.1), highlight_color=color.lime, color=color.black, text="1")
b6.on_click = Func(click, 5)
b7 = Button(scale=0.18, position=(0.1, 0.1), highlight_color=color.lime, color=color.black, text="2")
b7.on_click = Func(click, 6)
b8 = Button(scale=0.18, position=(0.3, 0.1), highlight_color=color.lime, color=color.black)
b8.on_click = Func(click, 7)
b9 = Button(scale=0.18, position=(-0.3, -0.1), highlight_color=color.lime, color=color.black, text="3")
b9.on_click = Func(click, 8)
b10 = Button(scale=0.18, position=(-0.1, -0.1), highlight_color=color.lime, color=color.black, text="2")
b10.on_click = Func(click, 9)
b11 = Button(scale=0.18, position=(0.1, -0.1), highlight_color=color.lime, color=color.black, text="1")
b11.on_click = Func(click, 10)
b12 = Button(scale=0.18, position=(0.3, -0.1), highlight_color=color.lime, color=color.black)
b12.on_click = Func(click, 11)
b13 = Button(scale=0.18, position=(-0.3, -0.3), highlight_color=color.lime, color=color.black)
b13.on_click = Func(click, 12)
b14 = Button(scale=0.18, position=(-0.1, -0.3), highlight_color=color.lime, color=color.black, text="4")
b14.on_click = Func(click, 13)
b15 = Button(scale=0.18, position=(0.1, -0.3), highlight_color=color.lime, color=color.black, text="3")
b15.on_click = Func(click, 14)
b16 = Button(scale=0.18, position=(0.3, -0.3), highlight_color=color.lime, color=color.black, text="2")
b16.on_click = Func(click, 15)
b_list = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16]
app.run()
