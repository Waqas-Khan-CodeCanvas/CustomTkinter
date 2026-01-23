# ===============================
# FILE: frontend/app/views/create_view.py
# ===============================
import customtkinter as ctk
from app.controllers.items_controller import ItemsController

class CreateView(ctk.CTkFrame):
    def __init__(self, root, router):
        super().__init__(root)
        self.router = router

        ctk.CTkLabel(self, text="Create Item", font=("Arial", 24)).pack(pady=20)

        self.name_entry = ctk.CTkEntry(self, placeholder_text="Item Name")
        self.name_entry.pack(pady=10)

        self.price_entry = ctk.CTkEntry(self, placeholder_text="Price")
        self.price_entry.pack(pady=10)

        ctk.CTkButton(self, text="Save", command=self.save).pack(pady=10)
        ctk.CTkButton(self, text="Back", command=lambda: router.navigate("main")).pack()

    def save(self):
        payload = {
            "name": self.name_entry.get(),
            "price": self.price_entry.get(),
        }
        ItemsController.create_item(payload, callback=lambda: self.router.navigate("main"))
