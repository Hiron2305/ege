import turtle as tr

tr.tracer(0)

step = 20

for i in range(2):
    tr.forward(15 * step)
    tr.right(90)
    tr.forward(8 * step)
    tr.right(90)

tr.up()

for x in range(-20, 20):
    for y in range(-20, 20):
        tr.goto(x * step, y * step)
        tr.dot()
tr.update()
tr.mainloop()
