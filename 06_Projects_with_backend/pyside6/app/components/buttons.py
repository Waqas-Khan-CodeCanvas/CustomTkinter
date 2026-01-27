import customtkinter as ctk

class PrimaryButton(ctk.CTkButton):
    def __init__(self, master, text, command=None, width=200, **kwargs):
        super().__init__(master, text=text, width=width, command=command, corner_radius=8, **kwargs)
        self.configure(font=("Arial", 14))

class DangerButton(ctk.CTkButton):
    def __init__(self, master, text, command=None, width=200, **kwargs):
        super().__init__(master, text=text, width=width, command=command, fg_color="#e74c3c",
                         hover_color="#c0392b", corner_radius=8, **kwargs)
        self.configure(font=("Arial", 14))


# use like this 
# btn = PrimaryButton(self, text="Create", command=self.create_item)
# btn.pack(pady=10)
