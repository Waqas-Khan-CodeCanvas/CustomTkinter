# ===============================
# FILE: frontend/app/core/app.py
# ===============================
import customtkinter as ctk
from app.core.router import Router
from app.core.theme import apply_theme

class Application(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("CRUD Desktop App")
        self.geometry("1000x600")
        self.minsize(900, 550)

        apply_theme()

        self.router = Router(self)
        self.router.navigate("main")

