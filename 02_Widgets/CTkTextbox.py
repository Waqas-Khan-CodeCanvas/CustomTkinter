"""
Widget: CTkTextbox

    definition:
        - A **scrollable multiline text widget** in CustomTkinter.
        - Functions like a standard `tkinter.Text` widget but with **modern styling**, **dark mode**, and **built-in scrollbars**.
        - Supports both **vertical** and **horizontal** scrolling (with wrap='none').
        - Text can be **inserted**, **retrieved**, or **deleted** using standard text indices (e.g. `"0.0"`, `"end"`).
        - Commonly used for **notes**, **logs**, **code editors**, **chat boxes**, or **long text input**.

    arguments:
        master                              → parent widget (CTk, CTkFrame, Frame, or TopLevel)
        width                               → width of textbox in px
        height                              → height of textbox in px
        corner_radius                       → corner radius of textbox
        border_width                        → thickness of outer border (px)
        border_spacing                      → spacing between text and border (default = 3)
        fg_color                            → background color, tuple: (light, dark) or single color
        border_color                        → border color, tuple: (light, dark) or single color
        text_color                          → color of text, tuple: (light, dark) or single color
        scrollbar_button_color              → color of scrollbar thumb, tuple: (light, dark) or single color
        scrollbar_button_hover_color        → hover color for scrollbar thumb
        font                                → text font, tuple: (font_name, size)
        activate_scrollbars                 → True (default) to show scrollbars; False to disable them
        state                               → "normal" (editable) | "disabled" (read-only)
        wrap                                → wrapping mode: 
                                               - 'char' (default): wrap after any character
                                               - 'word': wrap only after spaces
                                               - 'none': disable wrapping; enables horizontal scrolling
        # plus all standard tkinter.Text options:
        autoseparators, cursor, exportselection, insertborderwidth, insertofftime,
        insertontime, insertwidth, maxundo, padx, pady, selectborderwidth,
        spacing1, spacing2, spacing3, tabs, takefocus, undo, xscrollcommand, yscrollcommand

    methods:
        textbox.insert(index, text, tags=None)      → insert text at index (e.g. "0.0", "end", "insert")
        textbox.get(index1, index2)                → get text between two indices
        textbox.delete(index1, index2=None)        → delete text between two indices
        textbox.focus_set()                        → focus the textbox
        textbox.configure(option=value, ...)       → update one or more options dynamically
        textbox.cget(option)                       → get current value of an option
        textbox.bind(sequence, command)            → bind event to function (e.g. "<KeyRelease>")
        textbox.unbind(sequence, funcid=None)      → remove event binding
        # inherits almost all tkinter.Text methods:
        # see https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/text-methods.html

"""

# Example 1: Basic CTkTextbox
from customtkinter import *

app = CTk()
app.title("CTkTextbox Example")

textbox = CTkTextbox(app, width=400, height=200)
textbox.pack(padx=20, pady=20)

textbox.insert("0.0", "Hello, world!\nThis is a CTkTextbox.\nEditable and scrollable!")
print("Text content:", textbox.get("0.0", "end"))

# Make textbox read-only
# textbox.configure(state="disabled")

app.mainloop()


# Example 2: Full-Window Textbox (Resizable)
from customtkinter import *

class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("Full Textbox Example")
        self.geometry("500x400")

        # configure grid to expand
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.textbox = CTkTextbox(
            master=self,
            width=400,
            corner_radius=0,
            wrap="word",
            font=("Consolas", 14)
        )
        self.textbox.grid(row=0, column=0, sticky="nsew")
        self.textbox.insert("0.0", "Some example text!\n" * 50)

app = App()
app.mainloop()


# Example 3: Styled Textbox with No Wrapping
from customtkinter import *

app = CTk()
app.title("Styled Textbox")

styled_box = CTkTextbox(
    app,
    width=500,
    height=250,
    fg_color=("white", "#1E1E1E"),
    border_color=("gray70", "gray30"),
    text_color=("black", "white"),
    scrollbar_button_color=("#3B82F6", "#2563EB"),
    scrollbar_button_hover_color=("#60A5FA", "#1D4ED8"),
    corner_radius=10,
    border_width=2,
    wrap="none"  # disable wrapping for horizontal scrolling
)
styled_box.pack(padx=20, pady=20, fill="both", expand=True)
styled_box.insert("0.0", "This line will not wrap automatically. "*10)

app.mainloop()


# Example 4: Binding Keyboard Events
from customtkinter import *

def on_key(event):
    print("Typed:", textbox.get("0.0", "end-1c"))

app = CTk()
textbox = CTkTextbox(app, width=400, height=150)
textbox.pack(padx=20, pady=20)
textbox.bind("<KeyRelease>", on_key)
app.mainloop()


"""
    usage notes:
        -> Use indices like "0.0" (line 0, char 0) or "end" to insert/get/delete text.
        -> Use    .configure(state="disabled")    to make textbox read-only.
        -> For horizontal scrolling, set    wrap="none".
        -> Retrieve content with    .get("0.0", "end-1c")    to exclude the trailing newline.
        -> Supports most tkinter.Text methods, so it's versatile for text editors.
        -> Customize scrollbar colors for better UI theming.
"""
