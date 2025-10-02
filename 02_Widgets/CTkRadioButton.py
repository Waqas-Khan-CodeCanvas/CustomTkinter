"""
Widget: CTkRadioButton

    definition:
        - A customizable radio button widget in CustomTkinter.
        - Used to select one option from a group of mutually exclusive choices.
        - Works with a shared tkinter variable (IntVar or StringVar), where each button has a unique `value`.
        - When one radio button is selected, all others linked to the same variable are automatically deselected.
        - Supports hover effects, custom colors, fonts, states, and dynamic text.

    arguments:
        master                      → parent widget (CTk, CTkFrame, Frame)
        width                       → total width of the widget (px)
        height                      → total height of the widget (px)
        radiobutton_width           → diameter/width of the circular button (px)
        radiobutton_height          → height of the circular button (px)
        corner_radius               → corner radius of the button (px)
        border_width_unchecked      → border width when unchecked (px)
        border_width_checked        → border width when checked (px)
        fg_color                    → fill color when selected (tuple or single)
        border_color                → border color (tuple or single)
        hover_color                 → hover color when cursor is over the button
        text_color                  → color of the text label (tuple or single)
        text_color_disabled         → text color when disabled
        text                        → label text
        textvariable                → tkinter.StringVar to dynamically control text
        font                        → text font (tuple: ("font_name", size))
        hover                       → enable/disable hover effect (True / False)
        state                       → "normal" (clickable) | "disabled" (not clickable)
        command                     → function executed when radio button is clicked
        variable                    → tkinter.IntVar or StringVar (shared among a group)
        value                       → unique int/string assigned to this radio button when selected

    methods:
        radiobutton.configure(attribute=value, ...)   # dynamically update attributes
        radiobutton.cget(attribute_name)              # get current value of an attribute

        radiobutton.select()                          # programmatically select (sets variable)
        radiobutton.deselect()                        # programmatically deselect
        radiobutton.invoke()                          # simulate a user click (triggers command)

"""

# Example 1: Simple CTkRadioButton group (IntVar)
from customtkinter import *
import tkinter

def radiobutton_event():
    print("Radiobutton toggled, current value:", radio_var.get())

app = CTk()
radio_var = tkinter.IntVar(value=0)

radiobutton_1 = CTkRadioButton(app,
                               text="Option 1",
                               command=radiobutton_event,
                               variable=radio_var,
                               value=1)
radiobutton_1.pack(padx=20, pady=10)

radiobutton_2 = CTkRadioButton(app,
                               text="Option 2",
                               command=radiobutton_event,
                               variable=radio_var,
                               value=2)
radiobutton_2.pack(padx=20, pady=10)
# app.mainloop()


# Example 2: StringVar-based CTkRadioButton with custom style
def mode_selected():
    print("Selected mode:", mode_var.get())

mode_var = tkinter.StringVar(value="Light")
radio_light = CTkRadioButton(app,
                             text="Light Mode",
                             variable=mode_var,
                             value="Light",
                             command=mode_selected,
                             fg_color="#3B8ED0",
                             text_color=("black", "white"),
                             font=("Helvetica", 14))
radio_light.pack(padx=20, pady=10)

radio_dark = CTkRadioButton(app,
                            text="Dark Mode",
                            variable=mode_var,
                            value="Dark",
                            command=mode_selected,
                            fg_color="#1F6AA5",
                            text_color=("black", "white"),
                            font=("Helvetica", 14))
radio_dark.pack(padx=20, pady=10)


# Example 3: Disabled CTkRadioButton
disabled_radio = CTkRadioButton(app,
                                text="Disabled Option",
                                state="disabled",
                                variable=radio_var,
                                value=3)
disabled_radio.pack(padx=20, pady=10)

app.mainloop()



"""
    usage notes:
        ->  Use the same variable across multiple radio buttons to create a group.
        ->  Assign a unique value to each radio button for identification.
        ->  .get() should be called on the variable to read the current selection.
        ->  .select() changes the selection without triggering command.
        ->  .invoke() simulates a click and triggers the command.
        ->  Set state="disabled" to make a button non-interactive.
"""