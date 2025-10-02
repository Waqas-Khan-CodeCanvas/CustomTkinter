"""
Widget: CTkEntry

    definition:
        - A customizable text input widget in CustomTkinter.
        - Used to collect a single line of user input.
        - Supports placeholder text, custom colors, borders, corner radius, fonts, states, and dynamic value management.
        - You can use it with or without a tkinter.StringVar variable.

    arguments:
        master                      → parent widget (CTk, CTkFrame, Frame)
        width                       → width of the entry (px)
        height                      → height of the entry (px)
        corner_radius               → corner radius (px)
        fg_color                    → foreground (background) color (single or tuple)
        text_color                  → color of input text
        placeholder_text            → hint text shown when empty (disappears when user types)
        placeholder_text_color      → color of placeholder text (single or tuple)
        font                        → text font (tuple: ("font_name", size))
        textvariable                → tkinter.StringVar for dynamic value management
        state                       → "normal" (editable) | "disabled" (read-only)
        
        # additional standard tkinter.Entry options:
        exportselection             → export selection to clipboard (bool)
        insertborderwidth           → width of insertion cursor border
        insertofftime               → blinking off time (ms)
        insertontime                → blinking on time (ms)
        insertwidth                 → width of the insert cursor
        justify                     → "left" | "center" | "right" (text alignment)
        selectborderwidth           → selection border width
        show                        → masking character (e.g. "*")
        takefocus                   → widget focus behavior
        validate                    → validation type (e.g. "key")
        validatecommand              → function to validate input
        xscrollcommand               → scrollbar callback

    methods:
        entry.configure(attribute=value, ...)     # configure attributes dynamically
        entry.cget(attribute_name)                # get current value of any attribute

        entry.get()                               # get current text
        entry.insert(index, string)               # insert text at index
        entry.delete(first_index, last_index=None)# delete character(s)
        
        entry.focus()                             # focus the widget
        entry.focus_force()                       # force focus
        
        # selection & cursor control
        entry.index(index)
        entry.icursor(index)
        entry.select_adjust(index)
        entry.select_from(index)
        entry.select_clear()
        entry.select_present()
        entry.select_range(start_index, end_index)
        entry.select_to(index)
        
        # x-view control
        entry.xview(index)
        entry.xview_moveto(f)
        entry.xview_scroll(number, what)
        
        # event binding
        entry.bind(sequence, command)

"""

# Example 1: Simple CTkEntry with placeholder
from customtkinter import *
app = CTk()
entry = CTkEntry(app,placeholder_text="Enter your name")
entry.pack(padx=20, pady=20)
# app.mainloop()


# Example 2: CTkEntry with variable and custom style
def on_text_change(*args):
    print("Current text:", entry_var.get())

entry_var = StringVar(value="")
entry_var.trace("w", on_text_change)
styled_entry = CTkEntry(app,width=250,height=35,corner_radius=8,fg_color=("white", "#2B2B2B"),text_color=("black", "white"),placeholder_text="Type something...",placeholder_text_color=("gray", "#888"),font=("Helvetica", 14),textvariable=entry_var)
styled_entry.pack(padx=20, pady=20)

# Example 3: Disabled Entry
disabled_entry = CTkEntry(app,placeholder_text="Disabled entry",state="disabled")
disabled_entry.pack(padx=20, pady=20)
app.mainloop()
"""

usage notes:
    ->  Use `textvariable` (tkinter.StringVar) to sync text dynamically.
    ->  Use `get()` to retrieve current value for processing.
    ->  Use `insert()` and `delete()` for programmatic text changes.
    ->  Use `state="disabled"` for non-editable entries.
    ->  Use `placeholder_text` for user-friendly hints (not available when using `textvariable`).
    ->  Combine with validation commands for input filtering.
"""
