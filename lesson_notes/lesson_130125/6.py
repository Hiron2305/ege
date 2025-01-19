import turtle as tr

sc = tr.Screen()
sc.tracer(0)

k = 20

for i in range(2):
    tr.forward(20 * k)
    tr.right(90)
    tr.forward(9 * k)
    tr.right(90)


tr.up()
for x in range(-20, 30):
    for y in range(-20, 20):
        tr.goto(x * k, y * k)
        tr.dot(3)

sc.update()
sc.mainloop()