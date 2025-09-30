"""

definition:
    - A clickable widget (button) in CustomTkinter, used to perform actions when pressed.
    - button Supports colors, hover, borders, images, and callbacks




arguments:
    master              → parent widget (root, Frame, CTkFrame)
    width               → button width (px)
    height              → button height (px)
    corner_radius       → corner radius (px)
    border_width        → border thickness
    border_spacing      → space between text/image and border (default=2)
    fg_color            → main color (single, hex, or tuple for light/dark)
    hover_color         → hover color (single/tuple)
    border_color        → border color
    text_color          → text color
    text_color_disabled → text color when disabled
    text                → button label
    font                → (name, size) → size < 0 means pixels
    textvariable        → tkinter.StringVar (dynamic text update)
    image               → PhotoImage (removes text if only image used)
    state               → "normal" | "disabled"
    hover               → True/False (hover effect)
    command             → callback function on click
    compound            → "top" | "left" | "bottom" | "right" (image + text position)
    anchor              → alignment ("n","ne","e","se","s","sw","w","nw","center")

methods:
    button.configure(text="new text")   # update properties
    txt = button.cget("text")           # get current property value
    button.invoke()                     # run command manually
"""

from customtkinter import *

def button_event():
        print("Button Pressed!")

app =CTk()
btn = CTkButton(app, text="Click Me", command=button_event)
btn.pack(padx=20, pady=20)
app.mainloop()