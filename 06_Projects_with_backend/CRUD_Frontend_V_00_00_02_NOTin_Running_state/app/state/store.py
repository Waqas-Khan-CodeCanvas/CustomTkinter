# ===============================
# FILE: frontend/app/state/store.py
# ===============================
class Store:
    def __init__(self):
        self.items = []
        self.selected_item = None
        self.loading = False
        self.error = None


store = Store()