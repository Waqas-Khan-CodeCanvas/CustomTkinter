# ===============================
# FILE: frontend/app/core/router.py
# ===============================
class Router:
    def __init__(self, root):
        self.root = root
        self.current_view = None
        self.routes = {}

        self._register_routes()

    def _register_routes(self):
        from app.views.main_view import MainView
        from app.views.create_view import CreateView
        from app.views.read_view import ReadView
        from app.views.update_view import UpdateView
        from app.views.delete_view import DeleteView

        self.routes = {
            "main": MainView,
            "create": CreateView,
            "read": ReadView,
            "update": UpdateView,
            "delete": DeleteView,
        }

    def navigate(self, route_name):
        if self.current_view:
            self.current_view.destroy()

        view_class = self.routes.get(route_name)
        if not view_class:
            raise ValueError(f"Route '{route_name}' not found")

        self.current_view = view_class(self.root, self)
        self.current_view.pack(fill="both", expand=True)

