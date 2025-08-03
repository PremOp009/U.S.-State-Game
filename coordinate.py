import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Click to Get Coordinates")
image = "india_mep.gif"  # <- your image here (if you have one)
screen.addshape(image)
turtle.shape(image)

# Function that gets called when you click
def get_mouse_click_coor(x, y):
    print(f"Clicked at: ({int(x)}, {int(y)})")

# Tell turtle to listen for clicks
screen.onscreenclick(get_mouse_click_coor)

# Keeps the window open
turtle.mainloop()
