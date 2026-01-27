# ===============================
# FILE: frontend/app/views/delete_view.py
# ===============================
import customtkinter as ctk
from app.controllers.items_controller import ItemsController
from app.components.modals import ConfirmModal, AlertModal

class DeleteView(ctk.CTkFrame):
    def __init__(self, root, router):
        super().__init__(root)
        self.router = router

        ctk.CTkLabel(self, text="Delete Item", font=("Arial", 24)).pack(pady=20)

        # Entry for selecting Item ID to delete
        self.id_entry = ctk.CTkEntry(self, placeholder_text="Item ID to delete")
        self.id_entry.pack(pady=5)

        ctk.CTkButton(self, text="Delete", command=self.delete_item).pack(pady=10)
        ctk.CTkButton(self, text="Back", command=lambda: router.navigate("main")).pack()

    def delete_item(self):
        try:
            item_id = int(self.id_entry.get())
            if ConfirmModal.show(message=f"Delete item {item_id}?"):
                response = ItemsController.delete_item(item_id,callback=lambda: self.router.navigate("main"))
                if response["success"]:
                    AlertModal.show(message="Item deleted successfully!")
                    self.router.navigate("main")
                else:
                    AlertModal.show(message=f"Failed: {response['message']}")
        except ValueError:
            AlertModal.show(message="Invalid ID")
