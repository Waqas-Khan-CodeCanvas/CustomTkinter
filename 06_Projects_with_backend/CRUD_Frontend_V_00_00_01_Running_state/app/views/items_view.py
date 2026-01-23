# ===============================
# FILE: frontend/app/views/items_view.py
# ===============================
import customtkinter as ctk
from app.controllers.items_controller import ItemsController
from app.state.store import store


class ItemsView(ctk.CTkFrame):
    def __init__(self, root, router):
        super().__init__(root)
        self.router = router
        ctk.CTkLabel(self, text="Items", font=("Arial", 24)).pack(pady=10)


        self.listbox = ctk.CTkTextbox(self, height=350)
        self.listbox.pack(fill="x", padx=20)


        btn_frame = ctk.CTkFrame(self)
        btn_frame.pack(pady=10)


        ctk.CTkButton(btn_frame, text="Create", command=lambda: router.navigate("create")).grid(row=0, column=0, padx=5)
        ctk.CTkButton(btn_frame, text="Update", command=self.update_item).grid(row=0, column=1, padx=5)
        ctk.CTkButton(btn_frame, text="Delete", command=self.delete_item).grid(row=0, column=2, padx=5)
        ctk.CTkButton(btn_frame, text="Back", command=lambda: router.navigate("main")).grid(row=0, column=3, padx=5)


        self.load()


    def load(self):
        self.listbox.delete("1.0", "end")
        def render():
            for item in store.items:
                self.listbox.insert("end", f"{item['id']} | {item['name']} | {item['price']}\n")
        ItemsController.load_items(render)


    def update_item(self):
        content = self.listbox.get("insert linestart", "insert lineend").strip()
        if content:
            item_id = content.split("|")[0].strip()
            self.router.navigate("update", item_id=item_id)


    def delete_item(self):
        content = self.listbox.get("insert linestart", "insert lineend").strip()
        if content:
            item_id = content.split("|")[0].strip()
            ItemsController.delete_item(item_id, self.load)

