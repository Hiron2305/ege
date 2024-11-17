import turtle as t

t.speed(100)
k = 10

for i in range(3):
    t.forward(7 * k)
    t.right(90)

t.forward(8 * k)

for i in range(3):
    t.left(90)
    t.forward(5 * k)

t.up()

for x in range(-10, 10):
    for y in range(-10, 10):
        t.goto(x * k, y * k)
        t.dot(3)
t.done()