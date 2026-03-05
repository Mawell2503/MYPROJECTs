import tkinter as tk

def CursorIndex(cursor_index, text):
    cursor_index.index(tk.INSERT)
    previous_char = cursor_index.get(f"")
    next_char = cursor_index.get()

    #  check if cursor is in between spaces
    if previous_char == " " and next_char == " ":
        cursor_index -= 1
        while text[cursor_index] != " ":
            cursor_index -= 1
    #  move backwards
    else:
        while text[cursor_index] != " ":
            cursor_index -= 1

    cursor_index += 1
    