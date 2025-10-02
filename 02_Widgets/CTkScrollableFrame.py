"""
Widget: CTkScrollableFrame

    definition:
        - A scrollable container widget in CustomTkinter.
        - Used to hold and organize multiple widgets within a scrollable area.
        - Supports both vertical and horizontal scrolling.
        - Ideal for displaying long lists, forms, or dynamically generated content.
        - Can be subclassed for clean and structured layout design.

    arguments:
        master                          → parent widget (CTk, CTkFrame, Frame)
        width                           → width of the inner scrollable area (px)
        height                          → height of the inner scrollable area (px)
        corner_radius                   → corner radius of frame (px)
        border_width                    → border width (px)
        fg_color                        → background color (single, tuple, or "transparent")
        border_color                    → border color (single or tuple)
        scrollbar_fg_color              → scrollbar track color
        scrollbar_button_color          → scrollbar handle color
        scrollbar_button_hover_color    → scrollbar handle hover color
        label_fg_color                  → label (title) background color
        label_text_color                → label text color
        label_text                      → label text/title displayed at top
        label_font                      → label font (tuple: ("font_name", size))
        label_anchor                    → label text alignment ("n", "ne", "e", "se", "s", "sw", "w", "nw", "center")
        orientation                     → "vertical" (default) | "horizontal"

    methods:
        scrollable_frame.configure(attribute=value, ...)   # dynamically update attributes
        scrollable_frame.cget(attribute_name)              # get current attribute value

"""

# Example 1: Basic Vertical Scrollable Frame
from customtkinter import *

app = CTk()

scrollable_frame = CTkScrollableFrame(app, width=300, height=200, label_text="Scrollable Area")
scrollable_frame.pack(padx=20, pady=20)

# Add content inside the frame
for i in range(20):
    label = CTkLabel(scrollable_frame, text=f"Item {i+1}")
    label.pack(pady=5, padx=10)

app.mainloop()


# Example 2: Using a subclass for cleaner structure
class MyFrame(CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.label = CTkLabel(self, text="Inside Scrollable Frame")
        self.label.grid(row=0, column=0, padx=20, pady=10)

        # Add multiple widgets dynamically
        for i in range(10):
            btn = CTkButton(self, text=f"Button {i+1}")
            btn.grid(row=i+1, column=0, padx=20, pady=5)

class App(CTk):
    def __init__(self):
        super().__init__()
        self.my_frame = MyFrame(master=self, width=300, height=250, label_text="Custom Frame")
        self.my_frame.pack(padx=20, pady=20)

app = App()
app.mainloop()


# Example 3: Full Window Scrollable Frame
class FullApp(CTk):
    def __init__(self):
        super().__init__()
        self.title("Full Window Scroll Frame")

        # allow frame to expand
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.scroll_frame = CTkScrollableFrame(master=self,
                                               corner_radius=0,
                                               fg_color="transparent",
                                               label_text="Full Frame")
        self.scroll_frame.grid(row=0, column=0, sticky="nsew")

        # Add content
        for i in range(30):
            CTkLabel(self.scroll_frame, text=f"Row {i+1}").grid(row=i, column=0, padx=20, pady=5)

FullApp().mainloop()



"""
    usage notes:
        ->  Add widgets directly inside the scrollable frame using  .pack()  or  .grid() .
        ->  Use  orientation="horizontal"  for horizontal scrolling.
        ->  You can subclass  CTkScrollableFrame  to create reusable layouts.
        ->  Use  corner_radius=0, fg_color="transparent"  to blend with parent background.
        ->  Combine with  .grid(sticky="nsew")  and parent’s  grid_rowconfigure  for full-window filling.
"""
