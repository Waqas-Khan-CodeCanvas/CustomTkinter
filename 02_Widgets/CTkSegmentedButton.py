"""
Widget: CTkSegmentedButton

    definition:
        - A segmented button widget in CustomTkinter that allows users to select **one option from multiple segments**.
        - Visually displays a row of connected buttons, with one active (selected) segment at a time.
        - Ideal for toggling between modes, filters, or categories.
        - Can be controlled with or without a `tkinter.StringVar` for dynamic value tracking.

    arguments:
        master                      → parent widget (CTk, CTkFrame, Frame)
        width                       → total width of the segmented button (px)
        height                      → height of each button (px)
        corner_radius               → corner radius of the entire segmented group (px)
        border_width                → spacing between the outer border and buttons (px)
        fg_color                    → background color around the buttons (single color or tuple: (light, dark))
        selected_color              → color of the active (selected) button (single or tuple: (light, dark))
        selected_hover_color        → hover color of the selected button (single or tuple: (light, dark))
        unselected_color            → color of inactive (unselected) buttons (single, tuple, or "transparent")
        unselected_hover_color      → hover color for inactive buttons (single or tuple: (light, dark))
        text_color                  → text color for all buttons (single or tuple: (light, dark))
        text_color_disabled         → text color when the button is disabled (single or tuple: (light, dark))
        font                        → font style for button text (tuple: ("FontName", size))
        values                      → list of string values (each becomes a button segment)
        variable                    → tkinter.StringVar to track the current selected value
        state                       → "normal" (default, clickable) | "disabled" (not clickable)
        command                     → function called when a button is clicked; receives selected value as parameter
        dynamic_resizing            → True (default) | False; whether to auto-resize for large text

    methods:
        segmented_button.configure(attribute=value, ...)   # dynamically configure attributes
        segmented_button.cget(attribute_name)              # get current value of an attribute
        segmented_button.set(value)                        # set selected segment by value
        segmented_button.get()                             # return current selected value
        segmented_button.insert(index, value)              # insert new button at position
        segmented_button.move(new_index, value)            # move existing button to new index
        segmented_button.delete(value)                     # remove a button from the segmented control

"""

# Example 1: Basic CTkSegmentedButton without variable
from customtkinter import *

def segmented_callback(value):
    print("Selected:", value)

app = CTk()
segmented_button = CTkSegmentedButton(
    app,
    values=["Option 1", "Option 2", "Option 3"],
    command=segmented_callback
)
segmented_button.pack(padx=20, pady=20)
# Set default selected value
segmented_button.set("Option 1")
app.mainloop()


# Example 2: With StringVar (dynamic tracking)
from customtkinter import *

def segmented_callback(value):
    print("Selected (via var):", segmented_var.get())

app = CTk()
segmented_var = StringVar(value="Value 2")
segmented_button = CTkSegmentedButton(
    app,
    values=["Value 1", "Value 2", "Value 3"],
    variable=segmented_var,
    command=segmented_callback
)
segmented_button.pack(padx=20, pady=20)
app.mainloop()


# Example 3: Styled Segmented Button
from customtkinter import *
app = CTk()
def on_select(value):
    print("Current mode:", value)
styled_segment = CTkSegmentedButton(
    app,
    values=["Day", "Week", "Month"],
    command=on_select,
    fg_color=("gray90", "gray20") ,
    selected_color="#00BFFF",
    selected_hover_color="#1E90FF",
    unselected_color=("#F0F0F0", "#2B2B2B"),
    unselected_hover_color=("#E0E0E0", "#3A3A3A"),
    text_color=("black", "white"),
    font=("Helvetica", 13, "bold"),
    corner_radius=10,
    width=300,
    height=35
)
styled_segment.pack(padx=20, pady=20)
styled_segment.set("Day")
app.mainloop()


# Example 4: Add / Move / Delete buttons dynamically
from customtkinter import *
app = CTk()
seg = CTkSegmentedButton(app, values=["A", "B", "C"])
seg.pack(padx=20, pady=20)
# Insert new button
seg.insert(1, "X")   # Adds "X" at index 1
# Move button
seg.move(3, "A")     # Move "A" to index 3
# Delete button
seg.delete("C")      # Remove "C"
seg.set("X")         # Select "X"
app.mainloop()


"""
    usage notes:
        -> Use `.set("Value")` to programmatically select a segment.
        -> Use `.get()` to retrieve the currently selected segment.
        -> Always ensure that `values` list is **not empty**.
        -> You can bind a `StringVar` to sync value changes across widgets.
        -> Customize colors for selected/unselected states to match theme.
        -> Disable interaction with `state="disabled"` when needed.
"""