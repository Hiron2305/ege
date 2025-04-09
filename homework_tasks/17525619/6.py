import turtle as tr

tr.tracer(0)

step = 20

for i in range(4):
    tr.forward(6 * step)
    tr.right(150)
    tr.forward(6 * step)
    tr.right(30)

tr.up()

for x in range(-20, 20):
    for y in range(-20, 20):
        tr.goto(x * step, y * step)
        tr.dot()
tr.update()
tr.mainloop() 
