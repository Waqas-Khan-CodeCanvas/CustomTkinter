# ===============================
# FILE: frontend/app/views/main_view.py
# ===============================
import customtkinter as ctk
from app.components.sidebar import Sidebar
from app.views.create_view import CreateView
from app.views.read_view import ReadView
from app.views.update_view import UpdateView
from app.views.delete_view import DeleteView

class MainView(ctk.CTkFrame):
    def __init__(self, root, router):
        super().__init__(root)
        self.router = router

        # ---- Layout frames ----
        self.sidebar_frame = ctk.CTkFrame(self, width=220, fg_color="#2c3e50")
        self.sidebar_frame.pack(side="left", fill="y")

        self.content_frame = ctk.CTkFrame(self, fg_color="#ecf0f1")
        self.content_frame.pack(side="right", expand=True, fill="both", padx=20, pady=20)

        # ---- Sidebar ----
        self.sidebar = Sidebar(self.sidebar_frame, router=None)  # We'll handle routing ourselves
        self.sidebar.pack(fill="y")
        self.sidebar.set_active("main")

        # ---- Content views ----
        self.views = {
            "main": ctk.CTkLabel(self.content_frame, text="Welcome to the CRUD Dashboard", font=("Arial", 28 ), bg_color="#2B2B2B"),
            "create": CreateView(self.content_frame, self),
            "read": ReadView(self.content_frame, self),
            "update": UpdateView(self.content_frame, self),
            "delete": DeleteView(self.content_frame, self),
        }

        # Pack default view
        self.active_content = None
        self.show_content("main")

        # ---- Connect sidebar buttons to content switching ----
        for route_name, btn in self.sidebar.buttons.items():
            btn.configure(command=lambda r=route_name: self.show_content(r))

    def show_content(self, route_name):
        """
        Show the content view inside content_frame without destroying MainView
        """
        # Destroy previous content
        if self.active_content:
            self.active_content.pack_forget()

        # Set new content
        self.active_content = self.views[route_name]
        self.active_content.pack(expand=True, fill="both")

        # Highlight active sidebar button
        self.sidebar.set_active(route_name)
