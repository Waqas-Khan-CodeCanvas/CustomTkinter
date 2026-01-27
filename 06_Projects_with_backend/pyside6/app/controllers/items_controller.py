# # ===============================
# # FILE: frontend/app/controllers/items_controller.py
# # ===============================
# import threading
# from app.services.api_client import APIClient
# from app.state.store import store

# class ItemsController:
#     @staticmethod
#     def fetch_items(callback):
#         def task():
#             store.loading = True
#             response = APIClient.get_items()
#             store.items = response.get("data", [])
#             store.loading = False
#             callback()

#         threading.Thread(target=task, daemon=True).start()

#     @staticmethod
#     def create_item(payload, callback):
#         def task():
#             APIClient.create_item(payload)
#             callback()

#         threading.Thread(target=task, daemon=True).start()

#     @staticmethod
#     def update_item(item_id, payload, callback):
#         def task():
#             APIClient.update_item(item_id, payload)
#             callback()

#         threading.Thread(target=task, daemon=True).start()

#     @staticmethod
#     def delete_item(item_id, callback):
#         def task():
#             APIClient.delete_item(item_id)
#             callback()

#         threading.Thread(target=task, daemon=True).start()





# ===============================
# FILE: frontend/app/controllers/items_controller.py
# ===============================
import threading
from app.services.api_client import APIClient
from app.state.store import store

class ItemsController:

    @staticmethod
    def fetch_items(on_success=None, on_error=None):
        def task():
            try:
                store.loading = True
                data = APIClient.get_items()  # JSONPlaceholder returns LIST

                store.items = data
                store.error = None

                if on_success:
                    on_success()

            except Exception as e:
                store.error = str(e)
                if on_error:
                    on_error(str(e))

            finally:
                store.loading = False

        threading.Thread(target=task, daemon=True).start()

    @staticmethod
    def create_item(payload, callback=None):
        def task():
            try:
                APIClient.create_item(payload)
                if callback:
                    callback()
            except Exception as e:
                store.error = str(e)

        threading.Thread(target=task, daemon=True).start()

    @staticmethod
    def update_item(item_id, payload, callback=None):
        def task():
            try:
                APIClient.update_item(item_id, payload)
                if callback:
                    callback()
            except Exception as e:
                store.error = str(e)

        threading.Thread(target=task, daemon=True).start()

    @staticmethod
    def delete_item(item_id, callback=None):
        def task():
            try:
                APIClient.delete_item(item_id)
                if callback:
                    callback()
            except Exception as e:
                store.error = str(e)

        threading.Thread(target=task, daemon=True).start()
