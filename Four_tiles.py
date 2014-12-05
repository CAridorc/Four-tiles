import pygame as pg
import sys
import random
import time
from pygame.locals import *

if sys.version_info.major == 3:
    impotr tkinter.messagebox as tkMessageBox
    import tkinter as tk
else:
    import Tkinter as tk
    import tkMessageBox




def game(waiting_time):
    pg.init()
    pg.display.set_caption("Four tiles game")

    WIDTH = 600
    HEIGHT = 400
    DISPLAY = pg.display.set_mode((WIDTH, HEIGHT), 0, 32)

    NUMBER_OF_BUTTONS = 4
    
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    PINK = (255,150,180)
    BROWN = (180,80,0)
    ORANGE = (255,180,0)
    CYAN = (0, 183, 235)
    VIOLET = (127, 0, 255)

    ALL_COLORS = [WHITE, RED, GREEN, BLUE, YELLOW, PINK
    BROWN, ORANGE, CYAN, VOILET]

    COLORS = [random.choice(COLORS) for _ in range(NUMBER_OF_BUTTONS)]

    def generate_correct_sequence(length):
        """
        Creates a sequence of a given length
        where no digit appears two times in a row.
        """
        sequence = [random.randint(1,4)]
        while (len(sequence) + 1) < length:
                r = random.randint(1,4)
                if r != sequence[-1]:
                        sequence.append(r)
        return sequence

    def draw_button(n, color):
        if n == 1:
            pg.draw.rect(DISPLAY, color, (0, 0, WIDTH / 2, HEIGHT / 2))
        elif n == 2:
            pg.draw.rect(DISPLAY,color,
            (WIDTH / 2, 0, WIDTH / 2, HEIGHT / 2))
        elif n == 3:
            pg.draw.rect(DISPLAY,color,
            (0, HEIGHT / 2, WIDTH / 2, HEIGHT / 2))
        elif n == 4:
            pg.draw.rect(DISPLAY,color,
            (WIDTH / 2, HEIGHT / 2, WIDTH / 2, HEIGHT / 2))


    def draw_buttons():
        for i in range(1, 5):
            draw_button(i, COLORS[i - 1])

    def what_button_is_clicked(mouse_pos):
        """
        The buttons are numbered in the following way
            1 | 2
            _____

            3 | 4
        """
        x,y = mouse_pos[0],mouse_pos[1]
        if x < WIDTH / 2 and y < HEIGHT / 2:
            return 1

        elif x > WIDTH / 2 and y < HEIGHT / 2:
            return 2

        elif x < WIDTH / 2 and y > HEIGHT / 2:
            return 3

        elif x > WIDTH / 2 and y > HEIGHT / 2:
            return 4


    def flash(button_number, waiting_time):
        draw_button(button_number, WHITE)
        pg.display.update()
        pg.time.wait(waiting_time)
        draw_button(button_number, COLORS[button_number - 1])
        pg.display.update()

    def inform_user(correct_sequence, delay):
        for button in correct_sequence:
            flash(button, delay)

    lenght = 1
    is_over = False

    while not is_over:
            draw_buttons()
            correct_sequence = generate_correct_sequence(lenght)
            inform_user(correct_sequence, waiting_time)

            while True:
                for event in pg.event.get():
                    if event.type == QUIT:
                        pg.quit()
                    if event.type == pg.MOUSEBUTTONUP:
                        mouse_pos = pg.mouse.get_pos()
                        if what_button_is_clicked(mouse_pos) == correct_sequence[0]:
                            correct_sequence.pop(0)
                        else:
                            tkMessageBox.showinfo("GAME OVER", "Your score is {}".format(lenght))
                            pg.quit()


                if correct_sequence == []:
                        break

            lenght += 1

if __name__ == "__main__":
    root = tk.Tk()
    root.wm_title("Four tiles game")

    def play():
        game(w.get()*200)

    INTRODUCTION = tk.StringVar()
    INTRODUCTION.set("""Welcome to the four tiles game.
You will see some tiles light up one after the other.
Afterwards, you must click them in the same order they lit up before.""")
    tk.Message(root, textvariable=INTRODUCTION, width=500, font=30).pack()

    tk.Label(root, text="Select the flashing time down here", font=30).pack()
    w = tk.Scale(root, from_=1, to=5, orient=tk.HORIZONTAL, length=400)
    w.pack()

    tk.Button(root, text="Play", command=play).pack()

    tk.mainloop()
