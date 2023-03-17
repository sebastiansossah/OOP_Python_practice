from canvas import Canvas
from shapes import Rectangle, Square

canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

colors = {"White": (255, 255, 255), "Black": (0, 0, 0)}
canvas_color = input("Enter canvas color (White or Black)")

canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

while True:
    shape_type = input("what do you like to draw? Enter to quit")

    if shape_type.lower() == 'rectangle':
        rec_x = int(input("Enter x of the rectangle: "))
        rec_y = int(input("Enter y of the rectangle: "))
        rec_width = int(input("Enter the width of the rectangle: "))
        rec_height = int(input("Enter the height of the rectangle: "))
        red = int(input("How much green? "))
        green = int(input("How much blue? "))
        blue = int(input("How much blue? "))

        r1 = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color=(red, green, blue))
        r1.draw(canvas)

    if shape_type.lower() == 'square':
        rec_x = int(input("Enter x of the square: "))
        rec_y = int(input("Enter y of the square: "))
        sqr_side = int(input("Enter the length of the square "))
        red = int(input("How much green? "))
        green = int(input("How much blue? "))
        blue = int(input("How much blue? "))

        s1 = Square(x=rec_x, y=rec_y, side=sqr_side, color=(red, green, blue))
        s1.draw(canvas)

    if shape_type.lower() == 'quit':
        break

canvas.make('canvas.png')
