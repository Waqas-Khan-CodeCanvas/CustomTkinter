"""
Widget: CTkOptionMenu

    definition:
        - A customizable dropdown selection widget in CustomTkinter.
        - Allows users to select one value from a predefined list.
        - Can be used with or without a `tkinter.StringVar` for dynamic value management.
        - Supports custom colors, fonts, states, hover effects, and dropdown styling.

    arguments:
        master                      → parent widget (CTk, CTkFrame, Frame)
        width                       → width of the option menu (px)
        height                      → height of the option menu (px)
        corner_radius               → corner radius (px)
        fg_color                    → main background color (tuple: (light, dark) or single)
        button_color                → color of the right dropdown button (tuple or single)
        button_hover_color          → hover color for the dropdown button (tuple or single)
        dropdown_fg_color           → background color of dropdown list (tuple or single)
        dropdown_hover_color        → hover color for dropdown items (tuple or single)
        dropdown_text_color         → text color for dropdown items (tuple or single)
        text_color                  → text color of the selected option (tuple or single)
        text_color_disabled         → text color when widget is disabled (tuple or single)
        font                        → font of the displayed text (tuple: ("font_name", size))
        dropdown_font               → font for dropdown items (tuple: ("font_name", size))
        hover                       → enable/disable hover effect (True / False)
        state                       → "normal" (clickable) | "disabled" (not clickable)
        command                     → callback function executed when a new value is selected
        variable                    → `tkinter.StringVar` to get/set current value dynamically
        values                      → list of strings shown in the dropdown
        dynamic_resizing            → automatically resize based on text width (True / False)
        anchor                      → alignment of text ("n", "s", "e", "w", "center"), default "w"

    methods:
        optionmenu.configure(attribute=value, ...)   # dynamically update attributes
        optionmenu.cget(attribute_name)              # get current value of any attribute

        optionmenu.set(value)                        # set current selection (string)
        optionmenu.get()                             # get current selected value (string)

"""

# Example 1: Simple CTkOptionMenu (without variable)
from customtkinter import *
def optionmenu_callback(choice):
    print("Dropdown clicked:", choice)
app = CTk()
optionmenu = CTkOptionMenu(app,values=["Option 1", "Option 2", "Option 3"],command=optionmenu_callback)
optionmenu.set("Option 2")   # set default selection
optionmenu.pack(padx=20, pady=20)
# app.mainloop()

# Example 2: CTkOptionMenu with StringVar
def optionmenu_callback(choice):
    print("Current choice:", optionmenu_var.get())

optionmenu_var = StringVar(value="Option 1")
optionmenu2 = CTkOptionMenu(app,values=["Option 1", "Option 2", "Option 3"],variable=optionmenu_var,command=optionmenu_callback,width=180,fg_color=("white", "#2B2B2B"),text_color=("black", "white"),button_color=("#3B8ED0", "#1F6AA5"),font=("Helvetica", 14))
optionmenu2.pack(padx=20, pady=20)

# Example 3: Disabled CTkOptionMenu
disabled_menu = CTkOptionMenu(app,values=["Disabled 1", "Disabled 2"],state="disabled",fg_color=("gray80", "#2E2E2E"))
disabled_menu.pack(padx=20, pady=20)
app.mainloop()



"""
usage notes:
        ->  Use `variable` (tkinter.StringVar) to manage value dynamically.
        ->  `command` is triggered whenever a user selects a new option.
        ->  Use `.set()` to programmatically set selection.
        ->  `.get()` retrieves the currently selected value.
        ->  You can disable the widget using `state="disabled"`.
        ->  Customize colors and fonts for consistent UI theme.
"""