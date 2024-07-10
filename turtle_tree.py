import turtle

# Set up the turtle
t = turtle.Turtle()
t.screen.bgcolor('black')
t.pensize(2)
t.color('green')
t.left(90)
t.backward(100)
t.speed(200)
t.shape('turtle')

def tree(size):
    """
    Recursive function to draw a tree using turtle graphics.

    :param size: the initial size of the tree
    """
    if size < 10:
        return
    else:
        t.forward(size)
        t.color('orange')
        t.circle(2)
        t.color('brown')
        t.left(30)
        tree(3 * size / 4)
        t.right(60)
        tree(3 * size / 4)
        t.left(30)
        t.backward(size)

# Draw a tree with an initial size of 100
tree(100)

# Keep the turtle graphics window open
turtle.done()
