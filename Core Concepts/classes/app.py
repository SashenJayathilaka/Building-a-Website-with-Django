class Point:
    def move(self):
        print('Move')

    def draw(self):
        print('Draw')

point_1 = Point()
point_1.x = 10
point_1.y = 20

print(point_1.x)
point_1.draw()
point_1.move()

point2 = Point()
point2.x = 50
print(point2.x)