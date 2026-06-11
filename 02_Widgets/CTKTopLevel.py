import customtkinter as ctk


# Correct Basic Structure
# Core Idea (Most Important Concept)

# In CustomTkinter:

# CTk() = your main application window
# CTkToplevel() = secondary windows (dialogs, forms, popups)
# Golden rule:

# 👉 You should have ONE main CTk() instance only
# 👉 All other windows should be CTkToplevel attached to it

# Never create multiple CTk() windows — that causes bugs and crashes.
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Main Window")
        self.geometry("600x400")

        btn = ctk.CTkButton(self, text="Open Toplevel", command=self.open_window)
        btn.pack(pady=20)

    def open_window(self):
        popup = ctk.CTkToplevel(self)
        popup.title("Child Window")
        popup.geometry("300x200")

        label = ctk.CTkLabel(popup, text="I am a Toplevel window")
        label.pack(pady=20)


app = App()
app.mainloop()

