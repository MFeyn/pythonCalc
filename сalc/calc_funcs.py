import tkinter
import decimal
import random as rm


def throw_dice(label: tkinter.Label) -> None:
    num = rm.randint(1, 6)
    label['text'] = num
