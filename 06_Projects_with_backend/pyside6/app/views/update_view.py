# ===============================
# FILE: frontend/app/views/update_view.py
# ===============================
import customtkinter as ctk
from app.controllers.items_controller import ItemsController
from app.components.modals import ConfirmModal, AlertModal

class UpdateView(ctk.CTkFrame):
    def __init__(self, root, router):
        super().__init__(root)
        self.router = router

        ctk.CTkLabel(self, text="Update Item", font=("Arial", 24)).pack(pady=20)

        # Entry for selecting Item ID
        self.id_entry = ctk.CTkEntry(self, placeholder_text="Item ID to update")
        self.id_entry.pack(pady=5)

        self.name_entry = ctk.CTkEntry(self, placeholder_text="New Name")
        self.name_entry.pack(pady=5)

        self.price_entry = ctk.CTkEntry(self, placeholder_text="New Price")
        self.price_entry.pack(pady=5)

        ctk.CTkButton(self, text="Update", command=self.update_item).pack(pady=10)
        ctk.CTkButton(self, text="Back", command=lambda: router.navigate("main")).pack()

    def update_item(self):
        try:
            item_id = int(self.id_entry.get())
            payload = {
                "name": self.name_entry.get(),
                "price": float(self.price_entry.get())
            }
            if ConfirmModal.show(message=f"Update item {item_id}?"):
                response = ItemsController.update_item(item_id, payload,callback=lambda: self.router.navigate("main"))
                if response["success"]:
                    AlertModal.show(message="Item updated successfully!")
                    self.router.navigate("main")
                else:
                    AlertModal.show(message=f"Failed: {response['message']}")
        except ValueError:
            AlertModal.show(message="Invalid ID or Price")
