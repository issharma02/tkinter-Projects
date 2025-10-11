from tkinter import *
from tkinter.messagebox import askokcancel


win = Tk()

WIDTH = 700
HEIGHT = 500

# canvas create
canvas = Canvas(win, width = WIDTH, height = HEIGHT, bg = "lightblue")
canvas.pack()


count = 0

score_text = canvas.create_text(WIDTH - 100, 30, text = f"Score: {count}")


paddle_width = 80
paddle_height = 20


# creation of paddle
paddle = canvas.create_rectangle(
    (WIDTH - paddle_width) / 2, HEIGHT - 20,
    (WIDTH + paddle_width) / 2, HEIGHT - 20 + 10,
    fill = "black"
)


dx = 5
dy = 5


# ball creation
ball = canvas.create_oval(10, 55, 50, 100, fill = "brown")


# when hits the wall -  paddle
def ball_hits_paddle():
    bx1, by1, bx2, by2 = canvas.coords(ball)
    px1, py1, px2, py2 = canvas.coords(paddle)

    vertical = by2 >= py1 and by1 < py1
    horizontal = bx2 >= px1 and bx1 <= px2
    downward   = dy > 0 

    return vertical and horizontal and downward




# when hits the wall -  ball
def ball_movement():
    global dx, dy
    x1, y1, x2, y2 = canvas.coords(ball)
    if x2 >= WIDTH or x1 < 0:
        dx = -dx
    elif y1 <= 0:
        dy = -dy



# score function
def score():
    global count, score_text
    count += 1

    canvas.itemconfig(score_text, text = f"Score: {count}")



# increase speed of the ball 
def speed():
    global dx, dy
    if count % 3 == 0:
        dx = dx * 1.1
        dy = dy * 1.1




# movement of the ball
def move_ball():
    global dx, dy
    x1, y1, x2, y2 = canvas.coords(ball)
    canvas.move(ball, dx, dy)

    if ball_hits_paddle():
        dy = -dy
        score()
        speed()

    if y2 >= HEIGHT:
        return game_over_message()
    

    ball_movement()

    canvas.after(30, move_ball)


move_ball()


# restart the game
def reset_game():
    global dx, dy
    dx = 5
    dy = 5

    count = 0
    canvas.itemconfig(score_text, text = f"Score: {count}")

    x1, y1, x2, y2 = canvas.coords(ball)
    canvas.coords(ball, 200, 100, 240, 140)
    canvas.coords(paddle,
    (WIDTH - paddle_width) / 2, HEIGHT - 20,
    (WIDTH + paddle_width) / 2, HEIGHT - 20 + 10)

    move_ball()


# gameover message function
def game_over_message():
    ans = askokcancel(title = "Game Over", 
                      message = "Play Again?")
    if ans:
        reset_game()
    else:
        win.destroy()





# paddle moving left right
def move_left(event):
    x1, y1, x2, y2 = canvas.coords(paddle)
    if x1 > 0:
        canvas.move(paddle, -20, 0)
    

def move_right(event):
    x1, y1, x2, y2 = canvas.coords(paddle)
    if x2 < WIDTH:
        canvas.move(paddle, 20, 0)


win.bind("<Left>", move_left)
win.bind("<Right>", move_right)

win.mainloop()

