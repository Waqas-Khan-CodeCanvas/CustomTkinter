"""
Widget: CTkProgressBar

    definition:
        - A customizable progress bar widget in CustomTkinter.
        - Used to visualize task completion progress or indicate ongoing operations.
        - Can operate in two modes:
            → "determinate": shows exact progress (0.0 to 1.0).
            → "indeterminate": shows ongoing/unknown progress (oscillating).
        - Supports horizontal and vertical orientations, customizable colors, borders, and speeds.

    arguments:
        master                      → parent widget (CTk, CTkFrame, Frame)
        width                       → width of the progress bar (px)
        height                      → height of the progress bar (px)
        border_width                → thickness of border line (px)
        corner_radius               → roundness of corners (px)
        fg_color                    → background color (single or tuple: (light, dark))
        border_color                → border color (single or tuple: (light, dark))
        progress_color              → fill color for progress (single or tuple: (light, dark))
        orientation                 → "horizontal" (default) | "vertical"
        mode                        → "determinate" (default, fixed progress) | "indeterminate" (oscillating progress)
        determinate_speed           → auto progress speed in determinate mode (default=1)
        indeterminate_speed         → oscillation speed in indeterminate mode (default=1)

    methods:
        progressbar.configure(attribute=value, ...)   # dynamically update attributes
        progressbar.cget(attribute_name)              # get current value of any attribute

        progressbar.set(value)                        # set progress (0.0 → 1.0)
        progressbar.get()                             # get current progress value

        progressbar.start()                           # start auto animation (determinate or indeterminate)
        progressbar.stop()                            # stop auto animation
        progressbar.step()                            # manually step forward by speed value

"""

# Example 1: Simple Horizontal ProgressBar (determinate)
from customtkinter import *

app = CTk()
progressbar = CTkProgressBar(app, orientation="horizontal", width=250)
progressbar.pack(padx=20, pady=20)
progressbar.set(0.4)   # set 40% progress
# app.mainloop()


# Example 2: Indeterminate ProgressBar (loading animation)
progressbar2 = CTkProgressBar(app,
                              orientation="horizontal",
                              mode="indeterminate",
                              fg_color=("white", "#2B2B2B"),
                              progress_color=("#3B8ED0", "#1F6AA5"),
                              border_color=("gray70", "gray20"))
progressbar2.pack(padx=20, pady=20)

progressbar2.start()   # start oscillating animation


# Example 3: Vertical ProgressBar with manual stepping
progressbar3 = CTkProgressBar(app,
                              orientation="vertical",
                              width=20,
                              height=150,
                              progress_color="green",
                              mode="determinate")
progressbar3.pack(padx=20, pady=20)
progressbar3.set(0.2)   # 20% filled

# simulate manual updates
def update_progress():
    value = progressbar3.get() + 0.1
    if value <= 1:
        progressbar3.set(value)
        app.after(500, update_progress)

update_progress()
app.mainloop()



"""
    usage notes:
        ->  Use .set(0.0 → 1.0) to represent progress (e.g., 0.5 = 50%).
        ->  In "indeterminate" mode, .start() creates a looping animation.
        ->  Use .stop() to halt automatic animation.
        ->  .step() is useful for manual updates in determinate mode.
        ->  Customize progress_color to match your theme.
        ->  Both orientations ("horizontal" and "vertical") are supported.
"""