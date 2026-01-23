# ===============================
# FILE: frontend/app/views/read_view.py
# ===============================
import customtkinter as ctk
from app.controllers.items_controller import ItemsController
from app.state.store import store

class ReadView(ctk.CTkFrame):
    def __init__(self, root, router):
        super().__init__(root)
        self.router = router

        ctk.CTkLabel(self, text="All Items", font=("Arial", 24)).pack(pady=20)

        self.textbox = ctk.CTkTextbox(self, width=600, height=300)
        self.textbox.pack()

        ctk.CTkButton(self, text="Refresh", command=self.load).pack(pady=10)
        ctk.CTkButton(self, text="Back", command=lambda: router.navigate("main")).pack()

        self.load()

    def load(self):
        self.textbox.delete("1.0", "end")

        def render():
            for item in store.items:
                self.textbox.insert("end", f"{item}\n")

        ItemsController.fetch_items(render)

