"""
Widget: CTkFrame

    definition:
        - A container widget in CustomTkinter used to group and organize other widgets.
        - Supports custom background color, border color, border width, and corner radius.
        - Commonly used for layout management and UI structuring.
        - You can use CTkFrame directly or subclass it to create reusable UI components.

    arguments:
        master              → parent widget (CTk, CTkFrame, Frame, or Toplevel)
        width               → width of the frame (px)
        height              → height of the frame (px)
        corner_radius       → corner radius (px)
        border_width        → thickness of the frame border (px)
        fg_color            → background color (single, tuple, or "transparent")
        border_color        → color of the frame border (single or tuple)

    methods:
        frame.configure(attribute=value, ...)      # configure frame attributes dynamically
        frame.cget(attribute_name)                 # get current value of any attribute
        frame.bind(sequence, command, add=None)    # bind events (hover, clicks, etc.)

"""

# Example 1: Simple CTkFrame
from customtkinter import *

app = CTk()
frame = CTkFrame(master=app,width=200,height=200,fg_color=("white", "#2B2B2B"),border_color=("gray", "white"),border_width=2,corner_radius=10)
frame.pack(padx=20, pady=20)

# Add a label inside the frame
label = CTkLabel(frame, text="Inside CTkFrame")
label.pack(padx=10, pady=10)
app.mainloop()


# Example 2: Frame structured into a class (OOP approach)
import customtkinter
class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Add widgets onto the frame
        self.label = customtkinter.CTkLabel(self, text="This is MyFrame")
        self.label.grid(row=0, column=0, padx=20, pady=20)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")

        # Configure grid system for responsiveness
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Add custom frame
        self.my_frame = MyFrame(master=self, fg_color=("white", "#1E1E1E"))
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

app = App()
app.mainloop()


"""
    usage notes:
    ->  Use CTkFrame as a container to structure UI layout.
    ->  Combine `.pack()`, `.grid()`, or `.place()` for positioning.
    ->  Use `fg_color="transparent"` for a see-through background.
    ->  Use subclassing to build modular and reusable components.
    ->  Bind events using `.bind()` if interaction is needed.
    ->  You can nest multiple CTkFrames for advanced UI layouts.
"""
