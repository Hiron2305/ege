import turtle as tr

tr.tracer(0)

step = 20

for i in range(9):
    tr.forward(22 * step)
    tr.right(90)
    tr.forward(6 * step)
    tr.right(90)

tr.up()

tr.forward(1 * step)
tr.right(90)
tr.forward(5 * step)
tr.left(90)

tr.down()

for i in range(9):
    tr.forward(53 * step)
    tr.right(90)
    tr.forward(75 * step)
    tr.right(90)

tr.up()

for x in range(-50, 50):
    for y in range(-50, 50):
        tr.goto(x * step, y * step)
        tr.dot()
tr.update()
tr.mainloop()
