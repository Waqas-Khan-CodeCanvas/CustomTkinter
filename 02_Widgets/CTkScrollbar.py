""" 
Widget: CTkScrollbar

    definition:
        - A customizable scrollbar widget in CustomTkinter.
        - Used to add vertical or horizontal scrolling capability to other scrollable widgets (e.g., CTkTextbox, Canvas, Listbox).
        - Designed with modern aesthetics, supports light/dark themes, custom colors, rounded corners, and hover effects.
        - Works by connecting to another widget’s `yview` or `xview` method.

    arguments:
        master → parent widget (CTk, CTkFrame, Frame)
        command → function to call when scrollbar moves (typically widget.yview or widget.xview)
        width → width of the scrollbar (px)
        height → height of the scrollbar (px)
        corner_radius → corner radius of the scrollbar (px)
        border_spacing → space around the scrollbar (px)
        fg_color → background color (single color, tuple(light, dark), or "transparent")
        button_color → scrollbar slider color (single color or tuple)
        button_hover_color → slider hover color (single color or tuple)
        minimum_pixel_length → minimum visible size of the scrollbar slider (px)
        orientation → "vertical" (default) or "horizontal"
        hover → True / False, enable or disable hover effect

    methods:
        scrollbar.configure(attribute=value, ...)   # dynamically configure properties
        scrollbar.cget(attribute_name)              # get current value of an attribute
        scrollbar.get()                             # get current (start, end) view values
        scrollbar.set(start, end)                   # set start and end position of scrollbar manually

usage notes:
-> Always connect the scrollbar to a scrollable widget’s view function:
      scrollbar = CTkScrollbar(app, command=widget.yview)
      widget.configure(yscrollcommand=scrollbar.set)
-> Use orientation="horizontal" for horizontal scrolling.
-> Best used with CTkTextbox, CTkCanvas, CTkScrollableFrame, or any widget supporting yview/xview.
-> You can disable hover effects for static UI by setting hover=False.
-> Customize colors and radius for better theme consistency.

"""

# Example 1: Basic vertical scrollbar with CTkTextbox
from customtkinter import *

app = CTk()
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

# Create a textbox without internal scrollbars
textbox = CTkTextbox(app, activate_scrollbars=False)
textbox.grid(row=0, column=0, sticky="nsew")

# Create and connect CTkScrollbar
scrollbar = CTkScrollbar(app, command=textbox.yview)
scrollbar.grid(row=0, column=1, sticky="ns")

# Link textbox scroll to scrollbar
textbox.configure(yscrollcommand=scrollbar.set)

app.mainloop()


# Example 2: Horizontal scrollbar with Canvas
from customtkinter import *

app = CTk()
app.geometry("400x200")

canvas = CTkCanvas(app, scrollregion=(0, 0, 1000, 1000), background="#2b2b2b", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Create horizontal scrollbar
scroll_x = CTkScrollbar(app, orientation="horizontal", command=canvas.xview)
scroll_x.pack(fill="x")

# Connect scrollbar to canvas
canvas.configure(xscrollcommand=scroll_x.set)

# Draw example items
for i in range(20):
    canvas.create_text(50 + i * 50, 50, text=f"Item {i}", fill="white")

app.mainloop()


# Example 3: Customized scrollbar
from customtkinter import *

app = CTk()
text_widget = CTkTextbox(app, width=250, height=150, activate_scrollbars=False)
text_widget.pack(side="left", padx=10, pady=10)

custom_scrollbar = CTkScrollbar(app,
                                command=text_widget.yview,
                                fg_color="transparent",
                                button_color="#00BFFF",
                                button_hover_color="#1E90FF",
                                corner_radius=8,
                                width=12)
custom_scrollbar.pack(side="right", fill="y", pady=10)

text_widget.configure(yscrollcommand=custom_scrollbar.set)

for i in range(50):
    text_widget.insert("end", f"Line {i+1}\n")

app.mainloop()
