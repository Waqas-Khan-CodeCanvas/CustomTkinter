# ===============================
# FILE: frontend/app/views/delete_view.py
# ===============================
import customtkinter as ctk

class DeleteView(ctk.CTkFrame):
    def __init__(self, root, router):
        super().__init__(root)
        self.router = router

        ctk.CTkLabel(self, text="Delete Item", font=("Arial", 24)).pack(pady=20)
        ctk.CTkLabel(self, text="(Implement selection + delete logic)").pack(pady=10)

        ctk.CTkButton(self, text="Back", command=lambda: router.navigate("main")).pack()
