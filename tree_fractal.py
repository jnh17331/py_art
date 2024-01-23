import turtle

minimum_branch_length = 3

def build_tree(t, branch_length, shorten_by, angle):
    if branch_length > minimum_branch_length:
        t.forward(branch_length)
        new_length = branch_length - shorten_by

        t.left(angle)
        build_tree(t, new_length, shorten_by, angle)

        t.right(angle * 2)
        build_tree(t, new_length, shorten_by, angle)

        t.left(angle)
        t.backward(branch_length)

tree = turtle.Turtle()
tree.pensize(2.5)
tree.hideturtle()
tree.setheading(90)
tree.color('#6495ed')

build_tree(tree, 80, 10, 25)
turtle.mainloop()