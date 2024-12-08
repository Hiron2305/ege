import turtle as t

t.speed(50)
k = 10

t.color("red")


for i in range(4):
    t.forward(8 * k)
    t.right(90)

t.color("blue")

for j in range(3):
    t.forward(12 * k)
    t.right(120)



t.up()

t.color("black")
for x in range(-2, 15):
    for y in range(-11, 6):
        t.goto(x * k, y * k)
        t.dot(3)

t.done()