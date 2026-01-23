# ===============================
# FILE: frontend/app/views/form_view.py
# ===============================
import customtkinter as ctk
from app.controllers.items_controller import ItemsController
from app.state.store import store


class FormView(ctk.CTkFrame):
    def __init__(self, root, router, item_id=None):
        super().__init__(root)
        self.router = router
        self.item_id = item_id


        title = "Update Item" if item_id else "Create Item"
        ctk.CTkLabel(self, text=title, font=("Arial", 24)).pack(pady=20)


        self.name_entry = ctk.CTkEntry(self, placeholder_text="Item Name")
        self.name_entry.pack(pady=10)


        self.price_entry = ctk.CTkEntry(self, placeholder_text="Price")
        self.price_entry.pack(pady=10)


        if item_id:
            item = next((i for i in store.items if str(i['id']) == str(item_id)), None)
            if item:
                self.name_entry.insert(0, item['name'])
                self.price_entry.insert(0, item['price'])


        ctk.CTkButton(self, text="Save", command=self.save).pack(pady=10)
        ctk.CTkButton(self, text="Cancel", command=lambda: router.navigate("items")).pack()


    def save(self):
        data = {
            "name": self.name_entry.get(),
            "price": self.price_entry.get(),
        }
        if self.item_id:
            ItemsController.update_item(self.item_id, data, lambda: self.router.navigate("items"))
        else:
            ItemsController.create_item(data, lambda: self.router.navigate("items"))

