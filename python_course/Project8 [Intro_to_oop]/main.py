# import turtle
#
#
# timmy = turtle.Turtle()
# timmy.shape('turtle')
# timmy.color("coral")
# timmy.forward(100)
#
#
# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokemon Name', ['pikachu', 'squirtle', 'charmander'])
table.add_column('type', ['electric', 'water', 'fire'])
table.border = False
print(table)




