"""
Widget: CTkLabel

    definition:
        - A text or image display widget in CustomTkinter.
        - Commonly used for showing static text, dynamic text (via StringVar), or icons/images.
        - Supports custom background colors, text colors, corner radius, fonts, alignment, and compound layout with images.
        - Non-interactive (does not accept user input) but supports event bindings.

arguments:
    master              → parent widget (CTk, CTkFrame, or tkinter.Frame)
    text                → label text (string)
    textvariable        → tkinter.StringVar for dynamic text updates
    width               → width of the label (px)
    height              → height of the label (px)
    corner_radius       → corner radius (px)
    fg_color            → background color (single, tuple, or "transparent")
    text_color          → text color (single or tuple)
    font                → text font (tuple: ("font_name", size, "style"))
    anchor              → text position in the label ("center", "w", "e", "n", "s")
    justify             → alignment of multi-line text ("left", "center", "right")
    padx                → horizontal padding inside the label
    pady                → vertical padding inside the label
    compound            → image position relative to text ("center", "top", "bottom", "left", "right")

    # supports other tkinter.Label arguments as well:
    - bitmap, cursor, image, wraplength, etc.

methods:
    label.configure(attribute=value, ...)     # dynamically update label attributes
    label.cget(attribute_name)                # get current attribute value
    label.bind(sequence, command, add=None)   # bind events (e.g. mouse clicks, hover)

"""


# Example 1: Simple Label
from customtkinter import *
app = CTk()
label = CTkLabel(app,text="Hello, CustomTkinter!",fg_color="transparent")
label.pack(padx=20, pady=20)

# Example 2: Styled Label
styled_label = CTkLabel(app,text="Styled Label",width=200,height=50,corner_radius=8,fg_color=("white", "#2B2B2B"),text_color=("black", "white"),font=("Helvetica", 16, "bold"),anchor="center",justify="center")
styled_label.pack(padx=20, pady=10)
# Example 3: Dynamic Label using StringVar
label_var = StringVar(value="Initial Text")

dynamic_label = CTkLabel(app,textvariable=label_var,fg_color="transparent",font=("Arial", 14))
dynamic_label.pack(padx=20, pady=10)

# Update text dynamically
label_var.set("Updated Text!")


# Example 4: Label with compound image + text
from PIL import Image
# img = customtkinter.CTkImage(Image.open("icon.png"), size=(20, 20))

icon_label = CTkLabel(app,text="Label with Icon",compound="left",fg_color="transparent")
icon_label.pack(padx=20, pady=10)

app.mainloop()

"""
usage notes:
    ->   Use `textvariable` with a `StringVar` to update text dynamically.
    ->   Set `fg_color="transparent" to blend with parent background.
    ->   Use `compound` to display text + image together.
    ->   Use `anchor` for positioning text inside the label.
    ->   Bind events using `.bind()` for hover or click interactivity.

"""