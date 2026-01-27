from app.views.main_view import MainView


class Router:
    def __init__(self, window):
        self.window = window
        self.main_view = MainView(router=self)
        self.window.setCentralWidget(self.main_view)

    def navigate(self, route):
        """Delegate navigation to MainView's stacked widget"""
        self.main_view.navigate(route)
