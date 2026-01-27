# # ===============================
# # FILE: frontend/app/services/api_client.py
# # ===============================
# import requests

# BASE_URL = "http://127.0.0.1:5000/api/v1"

# class APIClient:
#     @staticmethod
#     def get_items():
#         return requests.get(f"{BASE_URL}/items", timeout=5).json()

#     @staticmethod
#     def create_item(payload):
#         return requests.post(f"{BASE_URL}/items", json=payload, timeout=5).json()

#     @staticmethod
#     def update_item(item_id, payload):
#         return requests.put(f"{BASE_URL}/items/{item_id}", json=payload, timeout=5).json()

#     @staticmethod
#     def delete_item(item_id):
#         return requests.delete(f"{BASE_URL}/items/{item_id}", timeout=5).json()






 # ========================================xxxxxxxxxxxxx===================================
# FIXME:  don't use this in production mode this is not the real data
# import requests
# import random

# BASE_URL = "http://127.0.0.1:5000/api/v1"

# # Set this True to use dummy data instead of real API
# USE_DUMMY_DATA = True

# # Dummy dataset
# DUMMY_ITEMS = [
#     {"id": 1, "name": "Apple", "price": 1.25},
#     {"id": 2, "name": "Banana", "price": 0.75},
#     {"id": 3, "name": "Orange", "price": 1.10},
# ]

# class APIClient:
#     @staticmethod
#     def get_items():
#         if USE_DUMMY_DATA:
#             # Return a copy to avoid modifying original dummy data
#             return {"success": True, "message": "Items retrieved", "data": DUMMY_ITEMS.copy()}
#         return requests.get(f"{BASE_URL}/items", timeout=5).json()

#     @staticmethod
#     def create_item(payload):
#         if USE_DUMMY_DATA:
#             new_id = max(item["id"] for item in DUMMY_ITEMS) + 1
#             new_item = {"id": new_id, **payload}
#             DUMMY_ITEMS.append(new_item)
#             return {"success": True, "message": "Item created", "data": new_item}
#         return requests.post(f"{BASE_URL}/items", json=payload, timeout=5).json()

#     @staticmethod
#     def update_item(item_id, payload):
#         if USE_DUMMY_DATA:
#             for item in DUMMY_ITEMS:
#                 if item["id"] == item_id:
#                     item.update(payload)
#                     return {"success": True, "message": "Item updated", "data": item}
#             return {"success": False, "message": "Item not found", "data": None}
#         return requests.put(f"{BASE_URL}/items/{item_id}", json=payload, timeout=5).json()

#     @staticmethod
#     def delete_item(item_id):
#         if USE_DUMMY_DATA:
#             global DUMMY_ITEMS
#             DUMMY_ITEMS = [item for item in DUMMY_ITEMS if item["id"] != item_id]
#             return {"success": True, "message": "Item deleted", "data": None}
#         return requests.delete(f"{BASE_URL}/items/{item_id}", timeout=5).json()




# Now all CRUD operations work fully with dummy data, and your CustomTkinter frontend can operate without the backend.



# Testing Dummy API


# client = APIClient()

# # Get items
# print(client.get_items())

# # Create item
# print(client.create_item({"name": "Mango", "price": 1.50}))

# # Update item
# print(client.update_item(1, {"name": "Green Apple", "price": 1.35}))

# # Delete item
# print(client.delete_item(2))



















# ===============================
# FILE: frontend/app/services/api_client.py
# ===============================
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

class APIClient:

    @staticmethod
    def get_items():
        """
        Fetch comments as items
        """
        response = requests.get(f"{BASE_URL}/comments", timeout=5)
        response.raise_for_status()
        print(response.json())
        return response.json()

    @staticmethod
    def create_item(payload):
        """
        Fake create (JSONPlaceholder returns success but doesn't save)
        """
        response = requests.post(
            f"{BASE_URL}/comments",
            json={
                "name": payload.get("name"),
                "email": "test@example.com",
                "body": payload.get("price"),
            },
            timeout=5,
        )
        response.raise_for_status()
        return response.json()

    @staticmethod
    def update_item(item_id, payload):
        """
        Fake update
        """
        response = requests.put(
            f"{BASE_URL}/comments/{item_id}",
            json={
                "id": item_id,
                "name": payload.get("name"),
                "email": "updated@example.com",
                "body": payload.get("price"),
            },
            timeout=5,
        )
        response.raise_for_status()
        return response.json()

    @staticmethod
    def delete_item(item_id):
        """
        Fake delete
        """
        response = requests.delete(
            f"{BASE_URL}/comments/{item_id}",
            timeout=5,
        )
        response.raise_for_status()
        return {"success": True, "deleted_id": item_id}
