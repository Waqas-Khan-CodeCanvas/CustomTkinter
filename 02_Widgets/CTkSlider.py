"""
Widget: CTkSlider

    definition:
        - A slider widget in CustomTkinter that allows users to select a numeric value by dragging a handle.
        - Supports both **horizontal** and **vertical** orientations.
        - Can be linked with a variable (   IntVar    or    DoubleVar   ) or controlled via callback.
        - Ideal for adjusting settings like volume, brightness, progress, or any ranged input.

    arguments:
        master                      → parent widget (CTk, CTkFrame, Frame)
        command                     → callback function; called when slider value changes; receives value as argument
        variable                    → tkinter.IntVar or tkinter.DoubleVar; links slider value dynamically
        width                       → total width of the slider (px)
        height                      → height of the slider track (px)
        border_width                → thickness of the border around the slider rail (px)
        from_                       → minimum slider value (lower bound)
        to                          → maximum slider value (upper bound)
        number_of_steps             → number of discrete steps (e.g. 10 for step size = (to - from_)/10)
        fg_color                    → background color (rail color), single or tuple: (light, dark)
        progress_color              → color of the filled (active) part before the handle (single, tuple, or "transparent")
        border_color                → border color around slider (single, tuple, or "transparent")
        button_color                → color of the draggable slider handle (single or tuple)
        button_hover_color          → hover color of the handle (single or tuple)
        orientation                 → "horizontal" (default) | "vertical"
        state                       → "normal" (default, interactive) | "disabled" (non-interactive)
        hover                       → True (default) | False; enable or disable hover effects

    methods:
        slider.configure(attribute=value, ...)   # dynamically configure any attribute
        slider.cget(attribute_name)              # get current value of an attribute
        slider.set(value)                        # set slider position programmatically
        slider.get()                             # get current numeric value of slider

"""

# Example 1: Basic Horizontal Slider
from customtkinter import *

def slider_event(value):
    print("Value:", value)

app = CTk()
slider = CTkSlider(app, from_=0, to=100, command=slider_event)
slider.pack(padx=20, pady=20)
app.mainloop()


# Example 2: Vertical Slider with Variable Binding
from customtkinter import *

def show_value(value):
    print("Slider Var:", slider_var.get())

app = CTk()
slider_var = DoubleVar(value=50)
slider = CTkSlider(app, from_=0, to=100, variable=slider_var, orientation="vertical", command=show_value)
slider.pack(padx=20, pady=20)
app.mainloop()


# Example 3: Styled Slider
from customtkinter import *

def on_change(value):
    print("Brightness:", int(value))

app = CTk()
styled_slider = CTkSlider(
    app,
    from_=0,
    to=100,
    command=on_change,
    fg_color=("gray80", "gray25"),
    progress_color="#00BFFF",
    border_color=("gray60", "gray30"),
    button_color="#1E90FF",
    button_hover_color="#4682B4",
    width=300,
    height=20,
    corner_radius=10
)
styled_slider.pack(padx=20, pady=20)
styled_slider.set(40)
app.mainloop()


# Example 4: Discrete Steps Slider
from customtkinter import *

app = CTk()
def step_event(value):
    print("Step:", int(value))

step_slider = CTkSlider(app, from_=0, to=100, number_of_steps=10, command=step_event)
step_slider.pack(padx=20, pady=20)
app.mainloop()


"""
    usage notes:
        -> Use    .set(value)    to programmatically change the slider position.
        -> Use    .get()    or a linked    variable    to retrieve the current value.
        ->    number_of_steps    converts slider into a step-based selector.
        -> Customize    progress_color    and    button_color    to match your theme.
        -> Use    orientation="vertical"    for vertical sliders.
        -> Disable interaction with    state="disabled".
"""
