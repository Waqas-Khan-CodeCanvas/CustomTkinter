"""
Widget: CTkCheckBox

    Definition:
    - A clickable toggle widget used to represent a binary choice (checked / unchecked).
    - Supports custom colors, hover effects, borders, dynamic variables, and callback functions.

    Example:
        A window with a checkbox labeled "CTkCheckBox".
        Clicking it toggles between on/off and prints the current value in the console.



    Arguments / Properties:
        master              → parent widget (root, Frame, CTkFrame)
        width               → total width of the widget (px)
        height              → total height of the widget (px)
        checkbox_width      → width of the checkbox box (px)
        checkbox_height     → height of the checkbox box (px)
        corner_radius       → corner radius (px)
        border_width        → border thickness (px)
        fg_color            → inside (foreground) color; tuple or single
        border_color        → border color; tuple or single
        hover_color         → hover color; tuple or single
        text_color          → text color; tuple or single
        text_color_disabled → text color when disabled
        text                → checkbox label text
        textvariable        → tkinter.StringVar() for dynamic text
        font                → text font (tuple: ("Arial", 14))
        hover               → enable/disable hover effect (True/False)
        state               → tkinter.NORMAL or tkinter.DISABLED
        command             → function called when checkbox clicked
        variable            → tkinter variable to read/write state
        onvalue             → value stored when checked
        offvalue            → value stored when unchecked


    Methods:
        checkbox.configure(option=value)     # change properties dynamically
        checkbox.cget("text")                # get current attribute value
        checkbox.get()                       # get current state (on/off)
        checkbox.select()                    # set checked (does not trigger command)
        checkbox.deselect()                  # set unchecked (does not trigger command)
        checkbox.toggle()                    # flip current state (triggers command)

    Examples:
        checkbox.configure(state="disabled")
        text = checkbox.cget("text")
        value = checkbox.get()
        checkbox.select()
        checkbox.deselect()
        checkbox.toggle()

    Notes:
        - Use StringVar or IntVar to track state easily.
        - onvalue/offvalue can be custom strings or integers.
        - When state="disabled", checkbox becomes unclickable and darker.
"""




import customtkinter

def checkbox_event():
    print("checkbox toggled, current value:", check_var.get())

app = customtkinter.CTk()

check_var = customtkinter.StringVar(value="on")
checkbox = customtkinter.CTkCheckBox(
    master=app,
    text="CTkCheckBox",
    command=checkbox_event,
    variable=check_var,
    onvalue="on",
    offvalue="off"
)
checkbox.pack(padx=20, pady=20)

app.mainloop()