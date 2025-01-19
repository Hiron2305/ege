import turtle as tr

screen = tr.Screen()

screen.tracer(0)

k = 10

for i in range(8):
    tr.forward(16 * k)
    tr.right(90)
    tr.forward(22 * k)
    tr.right(90)

tr.up()

tr.forward(5 * k)
tr.right(90)
tr.forward(5 * k)
tr.left(90)

tr.down()

for i in range(8):
    tr.forward(52 * k)
    tr.right(90)
    tr.forward(77 * k)
    tr.right(90)

tr.up()

for x in range(-50, 50):
    for y in range(-50, 50):
        tr.goto(x * k, y * k)
        tr.dot(3)
screen.update()
tr.mainloop()