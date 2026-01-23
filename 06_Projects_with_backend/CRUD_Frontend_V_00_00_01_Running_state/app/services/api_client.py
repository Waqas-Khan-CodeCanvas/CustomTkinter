# ===============================
# FILE: frontend/app/services/api_client.py
# ===============================
import requests

BASE_URL = "http://127.0.0.1:5000/api/v1"

class APIClient:
    @staticmethod
    def get_items():
        return requests.get(f"{BASE_URL}/items", timeout=5).json()

    @staticmethod
    def create_item(payload):
        return requests.post(f"{BASE_URL}/items", json=payload, timeout=5).json()

    @staticmethod
    def update_item(item_id, payload):
        return requests.put(f"{BASE_URL}/items/{item_id}", json=payload, timeout=5).json()

    @staticmethod
    def delete_item(item_id):
        return requests.delete(f"{BASE_URL}/items/{item_id}", timeout=5).json()

