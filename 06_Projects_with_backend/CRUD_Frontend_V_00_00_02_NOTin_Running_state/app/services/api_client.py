# ===============================
# FILE: frontend/app/services/api_client.py
# ===============================
import requests


BASE_URL = "http://127.0.0.1:5000/api/v1/items"


class APIClient:
    @staticmethod
    def get_items():
        return requests.get(BASE_URL, timeout=5).json()


    @staticmethod
    def create_item(data):
        return requests.post(BASE_URL, json=data, timeout=5).json()


    @staticmethod
    def update_item(item_id, data):
        return requests.put(f"{BASE_URL}/{item_id}", json=data, timeout=5).json()


    @staticmethod
    def delete_item(item_id):
        return requests.delete(f"{BASE_URL}/{item_id}", timeout=5).json()

