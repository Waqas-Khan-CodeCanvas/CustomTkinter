"""
Widget: CTkSwitch

    definition:
        - A toggle-style switch widget in CustomTkinter that allows users to **switch between two states** (ON/OFF).
        - Similar to a checkbox but with a more modern visual design (like mobile toggles).
        - Can be linked to a     tkinter.StringVar     or     IntVar     to track state.
        - Ideal for enabling/disabling features, toggling settings, or binary options.

    arguments:
        master                      → parent widget (CTk, CTkFrame, Frame)
        width                       → total width of the entire switch widget (px)
        height                      → height of the switch widget (px)
        switch_width                → width of the actual switch toggle (px)
        switch_height               → height of the actual switch toggle (px)
        corner_radius               → corner radius of the switch background (px)
        border_width                → border width of the switch box (px)
        fg_color                    → background color of the switch track (single or tuple: (light, dark))
        border_color                → border color (single, tuple, or "transparent")
        progress_color              → color when the switch is ON (single, tuple, or "transparent")
        button_color                → color of the toggle button (single or tuple)
        button_hover_color          → hover color of the button (single or tuple)
        hover_color                 → hover color of the switch background (single or tuple)
        text                        → label text displayed next to the switch
        textvariable                →     tkinter.StringVar     to dynamically control label text
        text_color                  → text color (single or tuple)
        font                        → font style for text (tuple: ("FontName", size))
        command                     → function called when the switch is toggled; triggered on manual click or     .toggle()    
        variable                    →     tkinter.StringVar     or     IntVar     to bind switch state
        onvalue                     → value assigned to variable when switch is ON
        offvalue                    → value assigned to variable when switch is OFF
        state                       → "normal" (default, clickable) | "disabled" (non-clickable)

    methods:
        switch.configure(attribute=value, ...)   # dynamically configure attributes
        switch.cget(attribute_name)              # get current attribute value
        switch.get()                             # get current switch value (onvalue/offvalue)
        switch.select()                          # turn ON programmatically (no command triggered)
        switch.deselect()                        # turn OFF programmatically (no command triggered)
        switch.toggle()                          # flip state programmatically (command is triggered)

"""

# Example 1: Basic CTkSwitch with command
from customtkinter import *

def switch_event():
    print("Switch toggled, current value:", switch_var.get())

app = CTk()
switch_var = StringVar(value="on")
switch = CTkSwitch(
    app,
    text="Wi-Fi",
    command=switch_event,
    variable=switch_var,
    onvalue="on",
    offvalue="off"
)
switch.pack(padx=20, pady=20)
app.mainloop()


# Example 2: Integer Variable Switch
from customtkinter import *

def on_toggle():
    print("Current:", int_switch.get())

app = CTk()
int_switch = IntVar(value=1)
switch = CTkSwitch(
    app,
    text="Power",
    variable=int_switch,
    onvalue=1,
    offvalue=0,
    command=on_toggle
)
switch.pack(padx=20, pady=20)
app.mainloop()


# Example 3: Styled Switch
from customtkinter import *

def toggle_action():
    print("Dark Mode:", theme_switch.get())

app = CTk()
theme_switch = StringVar(value="off")
styled_switch = CTkSwitch(
    app,
    text="Dark Mode",
    variable=theme_switch,
    onvalue="on",
    offvalue="off",
    command=toggle_action,
    fg_color=("gray80", "gray25"),
    progress_color="#00BFFF",
    button_color="#1E90FF",
    button_hover_color="#4682B4",
    text_color=("black", "white"),
    font=("Helvetica", 13, "bold"),
    width=100,
    height=28,
    corner_radius=10
)
styled_switch.pack(padx=20, pady=20)
app.mainloop()


# Example 4: Programmatic Control
from customtkinter import *

app = CTk()
sw = CTkSwitch(app, text="Auto Mode")
sw.pack(padx=20, pady=20)
sw.select()       # turn ON
print("Initial:", sw.get())
sw.deselect()     # turn OFF
sw.toggle()       # flip state
app.mainloop()


"""
    usage notes:
        -> Use     .get()     to read the current state (onvalue/offvalue).
        -> Use     .set()     indirectly by     .select()     or     .deselect()     to change state silently.
        ->     .toggle()     changes state and triggers the command callback.
        -> You can bind     StringVar     or     IntVar     for reactive state handling.
        -> Customize     progress_color     for ON state and     fg_color     for OFF state.
        -> Disable switch interaction using     state="disabled"    .
"""
