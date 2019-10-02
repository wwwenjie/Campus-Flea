4import turtle


# ����һ������,���Ի������
def picture(x1, y1, x, y):
    turtle.up()
    turtle.goto(x1, y1)
    turtle.down()
    # ���������ɫ
    turtle.begin_fill()
    turtle.fillcolor("yellow")
    for i in range(5):
        turtle.forward(x)
        turtle.left(y)
    turtle.end_fill()


# �ٶ�Ϊ3
turtle.speed(3)
# ������ɫ
turtle.bgcolor("red")
# ������ɫ
turtle.color("yellow")
picture(-350, 180, 180, 144)
picture(-170, 330, 60, 144)
picture(-110, 210, 60, 144)
picture(-100, 100, 60, 144)
picture(-180, 35, 60, 144)
turtle.done()
