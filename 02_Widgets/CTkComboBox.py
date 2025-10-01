"""
Widget: CTkComboBox

    definition:
        - A drop-down widget in CustomTkinter that allows the user to select one value from a list.
        - Supports custom colors, hover effects, borders, fonts, and variables for dynamic state management.
        - You can either use it with or without a tkinter.StringVar variable.


arguments:
    master                  → parent widget (root, Frame, CTkFrame)
    width                   → width of the combobox (px)
    height                  → height of the combobox (px)
    corner_radius           → corner radius (px)
    border_width            → border thickness (px)
    fg_color                → foreground (inside) color (single or tuple)
    border_color            → border color (single or tuple)
    button_color            → color of dropdown button (single or tuple)
    button_hover_color      → hover color of dropdown button
    dropdown_fg_color       → background color of dropdown menu
    dropdown_hover_color    → hover color of dropdown menu items
    dropdown_text_color     → text color inside dropdown items
    text_color              → text color inside entry box
    text_color_disabled     → text color when disabled
    font                    → main font for entry text
    dropdown_font           → font used for dropdown items
    values                  → list of string values shown in dropdown
    hover                   → enable/disable hover effect (True/False)
    state                   → "normal" | "disabled" | "readonly"
    command                 → callback function when user selects a value
    variable                → tkinter.StringVar to get/set value dynamically
    justify                 → "left" | "center" | "right" (text alignment)



methods:
    combobox.configure(values=["new1", "new2"])  # update dropdown list
    state = combobox.cget("state")               # get current state
    combobox.set("new value")                    # set current value (even if not in list)
    current = combobox.get()                     # get current selected value
"""

import customtkinter

def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)

app = customtkinter.CTk()
combobox = customtkinter.CTkComboBox(
    app,
    values=["option 1", "option 2", "option 3"],
    command=combobox_callback
)
combobox.set("option 2")
combobox.pack(padx=20, pady=20)

# Example 2: With variable
combobox_var = customtkinter.StringVar(value="option 1")
combobox2 = customtkinter.CTkComboBox(
    app,
    values=["option 1", "option 2", "option 3"],
    command=combobox_callback,
    variable=combobox_var
)
combobox2.pack(padx=20, pady=20)

app.mainloop()
