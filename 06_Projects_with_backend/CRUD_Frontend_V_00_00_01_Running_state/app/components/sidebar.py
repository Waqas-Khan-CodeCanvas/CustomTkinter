# ===============================
# FILE: frontend/app/components/sidebar.py
# ===============================
import customtkinter as ctk

class Sidebar(ctk.CTkFrame):
    """
    Reusable sidebar navigation component.

    Example usage:
        self.sidebar = Sidebar(self, router)
        self.sidebar.pack(side="left", fill="y")
    """

    def __init__(self, master, router, width=200, **kwargs):
        super().__init__(master, width=width, **kwargs)
        self.router = router
        self.configure(corner_radius=0)

        # Title
        self.title_label = ctk.CTkLabel(self, text="CRUD App", font=("Arial", 20, "bold"))
        self.title_label.pack(pady=(20, 40))

        # Buttons
        self.buttons = {}

        self.add_button("Main", "main")
        self.add_button("Create Item", "create")
        self.add_button("Update Item", "update")
        self.add_button("Delete Item", "delete")

        # Fill empty space to push buttons to top
        self.empty_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.empty_frame.pack(expand=True, fill="both")

    def add_button(self, text, route_name):
        """
        Adds a button to the sidebar
        """
        btn = ctk.CTkButton(
            self,
            text=text,
            width=160,
            height=40,
            command=lambda: self.router.navigate(route_name),
            corner_radius=8,
            fg_color="#3498db",
            hover_color="#2980b9",
            font=("Arial", 14)
        )
        btn.pack(pady=5)
        self.buttons[route_name] = btn

    def set_active(self, route_name):
        """
        Highlight the active button
        """
        for name, btn in self.buttons.items():
            if name == route_name:
                btn.configure(fg_color="#2ecc71")  # Active green
            else:
                btn.configure(fg_color="#3498db")  # Default blue
