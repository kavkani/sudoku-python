from ursina import *
app = Ursina()


def change(b, num):
    b.text = str(num)
    b.color = color.black

    destroy(one)
    destroy(two)
    destroy(three)
    destroy(four)
    destroy(five)
    destroy(six)
    destroy(seven)
    destroy(eight)
    destroy(nine)
    buttons()


def click(b):
    for i in range(16):
        b_list[i].color = color.black
    b.color = color.yellow
    global one, two, three, four, five, six, seven, eight, nine
    one = Button(text='1', scale=0.05, position=(0.6, 0.45), color=color.blue)
    one.on_click = Func(change, b, 1)
    two = Button(text='2', scale=0.05, position=(0.6, 0.35), color=color.blue)
    two.on_click = Func(change, b, 2)
    three = Button(text='3', scale=0.05, position=(0.6, 0.25), color=color.blue)
    three.on_click = Func(change, b, 3)
    four = Button(text='4', scale=0.05, position=(0.6, 0.15), color=color.blue)
    four.on_click = Func(change, b, 4)
    five = Button(text='5', scale=0.05, position=(0.6, 0.05), color=color.blue)
    five.on_click = Func(change, b, 5)
    six = Button(text='6', scale=0.05, position=(0.6, -0.05), color=color.blue)
    six.on_click = Func(change, b, 6)
    seven = Button(text='7', scale=0.05, position=(0.6, -0.15), color=color.blue)
    seven.on_click = Func(change, b, 7)
    eight = Button(text='8', scale=0.05, position=(0.6, -0.25), color=color.blue)
    eight.on_click = Func(change, b, 8)
    nine = Button(text='9', scale=0.05, position=(0.6, -0.35), color=color.blue)
    nine.on_click = Func(change, b, 9)


def buttons():
    b1 = Button(scale=0.2, position=(-0.4,  0.35))
    b1.on_click = Func(click, b1)
    b2 = Button(scale=0.2, position=(-0.15,  0.35))
    b2.on_click = Func(click, b2)
    b3 = Button(scale=0.2, position=(0.1, 0.35))
    b3.on_click = Func(click, b3)
    b4 = Button(scale=0.2, position=(0.35, 0.35))
    b4.on_click = Func(click, b4)
    b5 = Button(scale=0.2, position=(-0.4, 0.1))
    b5.on_click = Func(click, b5)
    b6 = Button(scale=0.2, position=(-0.15, 0.1))
    b6.on_click = Func(click, b6)
    b7 = Button(scale=0.2, position=(0.1, 0.1))
    b7.on_click = Func(click, b7)
    b8 = Button(scale=0.2, position=(0.35, 0.1))
    b8.on_click = Func(click, b8)
    b9 = Button(scale=0.2, position=(-0.4, -0.15))
    b9.on_click = Func(click, b9)
    b10 = Button(scale=0.2, position=(-0.15, -0.15))
    b10.on_click = Func(click, b10)
    b11 = Button(scale=0.2, position=(0.1, -0.15))
    b11.on_click = Func(click, b11)
    b12 = Button(scale=0.2, position=(0.35, -0.15))
    b12.on_click = Func(click, b12)
    b13 = Button(scale=0.2, position=(-0.4, -0.4))
    b13.on_click = Func(click, b13)
    b14 = Button(scale=0.2, position=(-0.15, -0.4))
    b14.on_click = Func(click, b14)
    b15 = Button(scale=0.2, position=(0.1, -0.4))
    b15.on_click = Func(click, b15)
    b16 = Button(scale=0.2, position=(0.35, -0.4))
    b16.on_click = Func(click, b16)
    b_list = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16]


one, two, three, four, five, six, seven, eight, nine = 0, 0, 0, 0, 0, 0, 0, 0, 0
bs = Button(scale=0)
b_list = [bs] * 16
buttons()
app.run()
