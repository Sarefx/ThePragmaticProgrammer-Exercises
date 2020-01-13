# my solution to exercise 5 in Python

import turtle

wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")
turtle_pen = turtle.Turtle()

command = ''

while (command != 'quit'):
    command = input("Please type the command: ")
    if command == 'P 2':
        command = input("Pen 2 is selected. Please type the next command: ")
        if command == 'D':
            command = input("Pen is down. Please select direction and distance: ")
            while command != 'U':
                command_list = command.split(' ')
                print(command_list)
                direction = command_list[0]
                distance = int(command_list[1]) * 10  # since 1 is to small, times 10 to add affect
                print("Direction is",direction,"and distance",distance)
                if direction == "W":
                    turtle_pen.setheading(180)
                    turtle_pen.fd(distance)
                elif direction == "N":
                    turtle_pen.setheading(90)
                    turtle_pen.fd(distance)
                elif direction == "E":
                    turtle_pen.setheading(0)
                    turtle_pen.fd(distance)
                elif direction == "S":
                    turtle_pen.setheading(270)
                    turtle_pen.fd(distance)
                command = input("Please select direction and distance: ")
                pass
        else:
            print("I didnt understand the command, try again.")
    else:
        print("I didnt understand the command, try again.")

turtle.done()

