# ===============================
import customtkinter as ctk
from app.core.app import Application


if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    app = Application()
    app.mainloop()