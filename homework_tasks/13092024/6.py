import math

def get_turtle_path():
    angle = 45
    x, y = 0, 0
    vertices = [(x, y)]

    for _ in range(7):
        x += 5 * math.sin(math.radians(angle))
        y += 5 * math.cos(math.radians(angle))
        vertices.append((x, y))

        angle += 45

        x += 10 * math.sin(math.radians(angle))
        y += 10 * math.cos(math.radians(angle))
        vertices.append((x, y))

        angle += 135

    return vertices

def calculate_integer_points(vertices):
    area = 0
    boundary_points = 0

    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % len(vertices)]

        area += x1 * y2 - x2 * y1

        boundary_points += math.gcd(int(abs(x2 - x1)), int(abs(y2 - y1)))

    area = abs(area) / 2
    interior_points = area + 1 - boundary_points / 2
    return int(interior_points)

vertices = get_turtle_path()
result = calculate_integer_points(vertices)
print(result)
