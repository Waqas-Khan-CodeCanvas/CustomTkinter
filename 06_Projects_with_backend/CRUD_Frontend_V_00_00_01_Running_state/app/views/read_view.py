# # ===============================
# # FILE: frontend/app/views/read_view.py
# # ===============================
# import customtkinter as ctk
# from app.controllers.items_controller import ItemsController
# from app.state.store import store

# class ReadView(ctk.CTkFrame):
#     def __init__(self, root, router):
#         super().__init__(root)
#         self.router = router

#         ctk.CTkLabel(self, text="All Items", font=("Arial", 24)).pack(pady=20)

#         self.textbox = ctk.CTkTextbox(self, width=600, height=300)
#         self.textbox.pack()

#         ctk.CTkButton(self, text="Refresh", command=self.load).pack(pady=10)
#         ctk.CTkButton(self, text="Back", command=lambda: router.navigate("main")).pack()

#         self.load()

#     def load(self):
#         self.textbox.delete("1.0", "end")

#         def render():
#             for item in store.items:
#                 self.textbox.insert("end", f"{item}\n")

#         ItemsController.fetch_items(render)
















# ===============================
# FILE: frontend/app/views/read_view.py
# ===============================
import customtkinter as ctk
import threading
from app.services.api_client import APIClient

class ReadView(ctk.CTkFrame):
    def __init__(self, root, router):
        super().__init__(root)
        self.router = router

        # ---- Title ----
        ctk.CTkLabel(self, text="Items List", font=("Arial", 24, "bold")).pack(pady=(10, 20))

        # ---- Status Label (loading / error) ----
        self.status_label = ctk.CTkLabel(self, text="Loading...", font=("Arial", 14))
        self.status_label.pack(pady=10)

        # ---- Table Container ----
        self.table_frame = ctk.CTkFrame(self)
        self.table_frame.pack(expand=True, fill="both")

        # ---- Header ----
        headers = ["ID", "Name", "Email", "Body"]
        header_frame = ctk.CTkFrame(self.table_frame)
        header_frame.pack(fill="x", pady=(0, 5))

        for h in headers:
            ctk.CTkLabel(
                header_frame,
                text=h,
                width=200,
                font=("Arial", 14, "bold")
            ).pack(side="left", padx=5)

        # ---- Scrollable Body ----
        self.body_frame = ctk.CTkScrollableFrame(self.table_frame, height=400)
        self.body_frame.pack(expand=True, fill="both")

        # ---- Load data async ----
        self.load_data()

    def load_data(self):
        """
        Fetch data in background to avoid UI freeze
        """
        self.status_label.configure(text="Loading data...")
        threading.Thread(target=self._fetch_data, daemon=True).start()

    def _fetch_data(self):
        try:
            data = APIClient.get_items()[:500]  # limit rows for UI

            self.after(0, lambda: self.render_table(data))

        except Exception as e:
            self.after(0, lambda: self.show_error(str(e)))

    def render_table(self, items):
        self.status_label.configure(text=f"Loaded {len(items)} items")

        # Clear old rows
        for widget in self.body_frame.winfo_children():
            widget.destroy()

        for item in items:
            row = ctk.CTkFrame(self.body_frame)
            row.pack(fill="x", pady=2)

            ctk.CTkLabel(row, text=item["id"], width=200).pack(side="left", padx=5)
            ctk.CTkLabel(row, text=item["name"], width=200).pack(side="left", padx=5)
            ctk.CTkLabel(row, text=item["email"], width=200).pack(side="left", padx=5)

            body_text = item["body"][:50] + "..." if len(item["body"]) > 50 else item["body"]
            ctk.CTkLabel(row, text=body_text, width=300, anchor="w").pack(side="left", padx=5)

    def show_error(self, message):
        self.status_label.configure(text="❌ Failed to load data")
        error_label = ctk.CTkLabel(
            self.body_frame,
            text=message,
            text_color="red",
            wraplength=600,
        )
        error_label.pack(pady=20)
