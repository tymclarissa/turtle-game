import turtle
import random

TRACK_X, TRACK_Y, TRACK_LEN, TRACK_WIDTH, LANE_WIDTH = -350, 200, 700, 400, 100
LANE_NUMBER_X, LANE_NUMBER_Y = -380, 130
FINISH_X = 250
TURTLE_X, TURTLE_Y = -300, 150


def setup_screen():
    global turt, screen

    screen = turtle.getscreen()
    screen.setup(800, 500)
    screen.title("Racing Turtles")
    screen.bgcolor("#9f4123")

    turt = turtle.getturtle()
    turt.speed(0)
    turt.penup()
    turt.goto(-100, 205)
    turt.color("white")
    turt.write("Racing turtles", font=("Arial", 20, "bold"))
    draw_track()
    draw_finishline()


def draw_track():
    turt.goto(TRACK_X, TRACK_Y)
    turt.pendown()
    turt.color("chocolate")
    turt.begin_fill()
    for i in range(2):
        turt.forward(TRACK_LEN)
        turt.right(90)
        turt.forward(TRACK_WIDTH)
        turt.right(90)

    turt.end_fill()

    turt.color("white")
    for index in range(5):
        turt.penup()
        turt.goto(TRACK_X, TRACK_Y - LANE_WIDTH * index)
        turt.pendown()
        turt.forward(TRACK_LEN)

    turt.penup()
    for index in range(4):
        turt.goto(LANE_NUMBER_X, LANE_NUMBER_Y - LANE_WIDTH * index)
        turt.write(index + 1, font=("Arial", 20, "bold"))


def draw_finishline():
    turt.penup()
    turt.goto(FINISH_X, TRACK_Y)
    turt.right(90)
    turt.pendown()
    turt.width(10)
    turt.forward(TRACK_WIDTH)


def setup_turtle():
    global turtle1, turtle2, turtle3, turtle4
    turtle1 = turtle.Turtle()
    turtle2 = turtle.Turtle()
    turtle3 = turtle.Turtle()
    turtle4 = turtle.Turtle()

    turtle1.penup()
    turtle1.color("lightblue")
    turtle1.shape("turtle")
    turtle1.turtlesize(2)
    turtle1.goto(TURTLE_X, TURTLE_Y)
    turtle1.pendown()

    turtle2.penup()
    turtle2.color("pink")
    turtle2.shape("turtle")
    turtle2.turtlesize(2)
    turtle2.goto(TURTLE_X, TURTLE_Y - 100)
    turtle2.pendown()

    turtle3.penup()
    turtle3.color("lightgreen")
    turtle3.shape("turtle")
    turtle3.turtlesize(2)
    turtle3.goto(TURTLE_X, TURTLE_Y - 200)
    turtle3.pendown()

    turtle4.penup()
    turtle4.color("white")
    turtle4.shape("turtle")
    turtle4.turtlesize(2)
    turtle4.goto(TURTLE_X, TURTLE_Y - 300)
    turtle4.pendown()


def get_userguess():
    return screen.numinput("Guess!",
                           "Which turtle will win? (1,2,3,4)",
                           minval=1,
                           maxval=4)


def race(user_guess: int):
    while (turtle1.xcor() <= FINISH_X and turtle2.xcor() <= FINISH_X
           and turtle3.xcor() <= FINISH_X and turtle4.xcor() <= FINISH_X):
        turtle1.forward(random.randint(1, 20))
        turtle2.forward(random.randint(1, 20))
        turtle3.forward(random.randint(1, 20))
        turtle4.forward(random.randint(1, 20))

        if turtle1.xcor() > FINISH_X:
            winner = 1
        elif turtle2.xcor() > FINISH_X:
            winner = 2
        elif turtle3.xcor() > FINISH_X:
            winner = 3
        elif turtle4.xcor() > FINISH_X:
            winner = 4

    if (user_guess == winner):
        screen.textinput("Game over!",
                         "you win! Turtle " + str(winner) + "won the game")
    else:
        screen.textinput("Game over!",
                         "you lose! Turtle " + str(winner) + "won the game")


def main():
    setup_screen()
    setup_turtle()
    user_guess = get_userguess()
    race(user_guess)


if __name__ == "__main__":
    main()
