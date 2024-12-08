import turtle as tr


wn = tr .Screen()

wn.tracer(0)
step = 20

tr.speed(100)

for i in range(4):
    tr.forward(14 * step)
    tr.right(90)
for i in range(5):
    tr.forward(5 * step)
    tr.right(45)

tr.up()

for x in range(0, 20):
    for y in range(-20, 10):
        tr.goto(x * step, y * step)
        tr.dot()
wn.update()
wn.mainloop()