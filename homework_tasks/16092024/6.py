import turtle as t


length = 70
t.speed(100)

for i in range(12):
    t.right(60)
    t.forward(1 * length)
    t.right(60)
    t.forward(1 * length)
    t.right(270)
t.up()

t.speed(400)

for x in range(-10, 10):
    for y in range(-10, 10):
        t.goto(x*length, y*length)
        t.dot(5)

t.done()