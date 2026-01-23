# ===============================
# FILE: frontend/app/views/update_view.py
# ===============================
import customtkinter as ctk

class UpdateView(ctk.CTkFrame):
    def __init__(self, root, router):
        super().__init__(root)
        self.router = router

        ctk.CTkLabel(self, text="Update Item", font=("Arial", 24)).pack(pady=20)
        ctk.CTkLabel(self, text="(Implement selection + update logic)").pack(pady=10)

        ctk.CTkButton(self, text="Back", command=lambda: router.navigate("main")).pack()

