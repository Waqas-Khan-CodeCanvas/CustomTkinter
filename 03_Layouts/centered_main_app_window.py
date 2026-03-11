from customtkinter import *

win = CTk()
win.resizable(False, False)
win

app_screen_with = win.winfo_screenwidth() +10
app_screen_height = win.winfo_screenheight()

x_center = int(win.winfo_screenwidth() /2 - app_screen_with / 2) - 10
y_center = int(win.winfo_screenheight() /2 -app_screen_height / 2)
win.geometry(f"{app_screen_with}x{app_screen_height}+{x_center}+{y_center}")

win.mainloop()
