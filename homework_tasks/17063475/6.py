import turtle as tr

tr.tracer(0)

step = 20

for i in range(8):
    tr.right(45)
    tr.forward(6 * step)

tr.up()

for x in range(-20, 20):
    for y in range(-20, 20):
        tr.goto(x * step, y * step)
        tr.dot()
tr.update()
tr.mainloop()