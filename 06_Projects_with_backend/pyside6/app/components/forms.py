import customtkinter as ctk

class LabeledEntry(ctk.CTkFrame):
    """Reusable entry with label"""
    def __init__(self, master, label_text, placeholder="", **kwargs):
        super().__init__(master, **kwargs)
        self.label = ctk.CTkLabel(self, text=label_text, anchor="w")
        self.label.pack(fill="x", pady=(0, 5))
        self.entry = ctk.CTkEntry(self, placeholder_text=placeholder)
        self.entry.pack(fill="x")
    
    def get_value(self):
        return self.entry.get()
    
    def set_value(self, value):
        self.entry.delete(0, "end")
        self.entry.insert(0, value)



# use like this 
# name_input = LabeledEntry(self, "Item Name")
# name_input.pack(pady=5)
