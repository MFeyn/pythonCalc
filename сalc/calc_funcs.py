import tkinter
import decimal


def clear_all_entries(ent_fields: list) -> None:
    for field in ent_fields:
        field.delete(0, tkinter.END)


def send_all_entries(lbl_fields: list, ent_fields: list) -> None:
    for ent_field, lbl_field in zip(ent_fields, lbl_fields):
        print(f'{lbl_field.cget("text")} {ent_field.get()}')
