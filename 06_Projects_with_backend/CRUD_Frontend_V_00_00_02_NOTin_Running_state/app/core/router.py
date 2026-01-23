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
    from app.views.items_view import ItemsView
    from app.views.form_view import FormView
    self.routes = {
        "main": MainView,
        "items": ItemsView,
        "create": FormView,
        "update": FormView,
    }


def navigate(self, route, **kwargs):
    if self.current_view:
        self.current_view.destroy()
    view_class = self.routes[route]
    self.current_view = view_class(self.root, self, **kwargs)
    self.current_view.pack(fill="both", expand=True)

