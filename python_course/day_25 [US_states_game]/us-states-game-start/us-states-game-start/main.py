import turtle
import pandas

score = 0
my_turtle = turtle.Turtle()
data = pandas.read_csv('50_states.csv')
screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
answer = screen.textinput(title='Guess the State', prompt='Type in the states name!')
state_names = data['state'].to_list()  # list of state names
guessed_states = []
while score < 50:
    answer = answer.title()
    if answer == 'Exit':
        not_guessed = [x for x in state_names if x not in guessed_states]
        df = pandas.DataFrame(not_guessed)
        df.to_csv('states_to_learn.csv')
        break
    print(answer)
    if answer in state_names:
        if answer not in guessed_states:
            guessed_states.append(answer)
            score += 1
            screen.title(f"{score}/50 states correct")
            state_data = data[data['state'] == answer].values.flatten().tolist() # flatten used to remove nesting
            # print(state_data)   # [state, xcor, ycor]
            xcor = state_data[1]   # use int(state_data.x)
            ycor = state_data[2]   # int(state_data.y)  this way everything after .values including .values is not required
            my_turtle.penup()
            my_turtle.goto(xcor, ycor)
            my_turtle.write(answer)    # can also use state_data.state.item() instead of answer
            my_turtle.ht()
    answer = screen.textinput(title=f'{score}/50 states correct.',prompt='Guess the state')


# To get coordinates of the states
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# To remove the guessed answer from all states so that it can be used for learning purposes

screen.exitonclick()