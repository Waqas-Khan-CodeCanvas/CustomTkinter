# ===============================
# FILE: frontend/app/views/main_view.py
# ===============================
import customtkinter as ctk


class MainView(ctk.CTkFrame):
    def __init__(self, root, router):
        super().__init__(root)
        self.router = router
        ctk.CTkLabel(self, text="CRUD Dashboard", font=("Arial", 28)).pack(pady=40)
        ctk.CTkButton(self, text="Manage Items", width=250, command=lambda: router.navigate("items")).pack(pady=10)
        ctk.CTkButton(self, text="Exit", width=250, command=root.destroy).pack(pady=10)

