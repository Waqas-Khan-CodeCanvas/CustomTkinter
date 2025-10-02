"""
Widget: CTkTabview

    definition:
        - A **tabbed view widget** in CustomTkinter, similar to a Notebook in tkinter.
        - It organizes the interface into **multiple tabs**, each acting like a **CTkFrame**.
        - You can add widgets inside each tab just like a normal frame.
        - Commonly used for **settings panels**, **multi-section forms**, or **dashboards**.

    arguments:
        master                              → parent widget (CTk, CTkFrame, Frame, TopLevel)
        width                               → total width of the tabview (px)
        height                              → total height of the tabview (px)
        corner_radius                       → corner radius for the tabview container (px)
        border_width                        → thickness of the border (px)
        fg_color                            → background color of tabview and tabs, tuple: (light, dark) or single color
        border_color                        → color of the border, tuple: (light, dark) or single color
        segmented_button_fg_color           → background color of the segmented button (tab selector)
        segmented_button_selected_color     → color of selected tab
        segmented_button_selected_hover_color → hover color of selected tab
        segmented_button_unselected_color   → color of unselected tabs
        segmented_button_unselected_hover_color → hover color of unselected tabs
        text_color                          → text color for tab labels
        text_color_disabled                 → text color when state="disabled"
        command                             → callback function executed when tab is switched (receives tab name)
        anchor                              → position of the tab selector ("n", "s", "nw", "ne", "sw", "se")
        state                               → "normal" (default) or "disabled"

    methods:
        tabview.add(name)                   → create a new tab with the given name (unique)
        tabview.tab(name)                   → returns reference to the tab’s frame (for placing widgets)
        tabview.set(name)                   → switch to the tab with the given name
        tabview.get()                       → get the currently visible tab’s name
        tabview.index(name)                 → get index (position) of tab by name
        tabview.insert(index, name)         → insert tab at a specific index
        tabview.move(new_index, name)       → reorder tabs
        tabview.rename(old_name, new_name)  → rename a tab
        tabview.delete(name)                → remove a tab
        tabview.configure(option=value, ...)→ dynamically update attributes
        tabview.cget(option)                → retrieve current attribute value

"""

# Example 1: Basic CTkTabview
from customtkinter import *

app = CTk()
app.title("CTkTabview Example")

tabview = CTkTabview(master=app)
tabview.pack(padx=20, pady=20, fill="both", expand=True)

# Add tabs
tabview.add("Home")
tabview.add("Settings")

# Set visible tab
tabview.set("Home")

# Add widgets to tabs
CTkLabel(tabview.tab("Home"), text="Welcome to Home Tab").pack(padx=10, pady=10)
CTkButton(tabview.tab("Settings"), text="Save Settings").pack(padx=10, pady=10)

app.mainloop()


# Example 2: Access Tabs via Variables
from customtkinter import *

app = CTk()
tabview = CTkTabview(app)
tabview.pack(padx=20, pady=20)

tab1 = tabview.add("Profile")
tab2 = tabview.add("About")

CTkLabel(tab1, text="User Profile Info").pack(pady=10)
CTkLabel(tab2, text="About This App").pack(pady=10)

app.mainloop()


# Example 3: Styled Tabview
from customtkinter import *

def on_tab_switch(name):
    print("Switched to:", name)

app = CTk()
styled_tabview = CTkTabview(
    app,
    width=400,
    height=250,
    fg_color=("white", "#1E1E1E"),
    border_color=("gray70", "gray25"),
    border_width=2,
    corner_radius=10,
    segmented_button_fg_color=("gray90", "gray20"),
    segmented_button_selected_color=("#3B82F6", "#2563EB"),
    segmented_button_selected_hover_color=("#60A5FA", "#1D4ED8"),
    segmented_button_unselected_color=("gray80", "gray30"),
    segmented_button_unselected_hover_color=("gray70", "gray40"),
    text_color=("black", "white"),
    command=on_tab_switch
)
styled_tabview.pack(padx=20, pady=20, fill="both", expand=True)

styled_tabview.add("Dashboard")
styled_tabview.add("Settings")
styled_tabview.set("Dashboard")

CTkLabel(styled_tabview.tab("Dashboard"), text="📊 Dashboard Content").pack(pady=20)
CTkLabel(styled_tabview.tab("Settings"), text="⚙️ Settings Content").pack(pady=20)

app.mainloop()


# Example 4: Using Classes
from customtkinter import *

class MyTabView(CTkTabview):
    def __init__(self, master):
        super().__init__(master)
        self.add("Tab 1")
        self.add("Tab 2")
        CTkLabel(self.tab("Tab 1"), text="Inside Tab 1").pack(padx=10, pady=10)
        CTkButton(self.tab("Tab 2"), text="Click Tab 2").pack(padx=10, pady=10)

class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.tabview = MyTabView(self)
        self.tabview.pack(padx=20, pady=20, fill="both", expand=True)

app = App()
app.mainloop()


"""
    usage notes:
        -> Each tab behaves like a CTkFrame — place widgets using .tab("name").
        -> Tab names must be unique.
        -> Use    .set("Tab Name")    to programmatically switch tabs.
        -> Use    .get()    to get the active tab name.
        -> Use    command=lambda name: ...    to trigger actions when switching tabs.
        -> Customize colors with    segmented_button_*    options for modern designs.
        -> Great for dashboards, settings panels, or multi-step forms.
"""
