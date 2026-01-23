# ===============================
# FILE: frontend/app/views/main_view.py
# ===============================
import customtkinter as ctk

class MainView(ctk.CTkFrame):
    def __init__(self, root, router):
        super().__init__(root)
        self.router = router

        ctk.CTkLabel(self, text="CRUD Dashboard", font=("Arial", 28)).pack(pady=20)

        buttons = [
            ("Create", "create"),
            ("Read", "read"),
            ("Update", "update"),
            ("Delete", "delete"),
        ]

        for text, route in buttons:
            ctk.CTkButton(
                self,
                text=text,
                width=200,
                command=lambda r=route: self.router.navigate(r),
            ).pack(pady=10)
            
        
