import customtkinter as ctk

class SimpleTable(ctk.CTkTextbox):
    """Basic table to display rows"""
    def __init__(self, master, height=300, **kwargs):
        super().__init__(master, height=height, state="normal", **kwargs)
        self.configure(font=("Arial", 12))
    
    def set_data(self, rows):
        self.delete("1.0", "end")
        for row in rows:
            line = " | ".join(str(v) for v in row.values())
            self.insert("end", line + "\n")


# use like this 
# table = SimpleTable(self)
# table.pack(padx=20, pady=20)
# table.set_data(store.items)
