import turtle as t

t.speed(100)
k = 10

for i in range(6):
    t.forward(10 * k)
    t.right(60)

t.up()

t.speed(10000)

for x in range(-5, 20):
    for y in range(-20, 10):
        t.goto(x * k, y * k)
        t.dot(5)
t.done()
