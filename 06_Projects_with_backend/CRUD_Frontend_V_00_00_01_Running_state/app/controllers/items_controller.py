# ===============================
# FILE: frontend/app/controllers/items_controller.py
# ===============================
import threading
from app.services.api_client import APIClient
from app.state.store import store

class ItemsController:
    @staticmethod
    def fetch_items(callback):
        def task():
            store.loading = True
            response = APIClient.get_items()
            store.items = response.get("data", [])
            store.loading = False
            callback()

        threading.Thread(target=task, daemon=True).start()

    @staticmethod
    def create_item(payload, callback):
        def task():
            APIClient.create_item(payload)
            callback()

        threading.Thread(target=task, daemon=True).start()

    @staticmethod
    def update_item(item_id, payload, callback):
        def task():
            APIClient.update_item(item_id, payload)
            callback()

        threading.Thread(target=task, daemon=True).start()

    @staticmethod
    def delete_item(item_id, callback):
        def task():
            APIClient.delete_item(item_id)
            callback()

        threading.Thread(target=task, daemon=True).start()

