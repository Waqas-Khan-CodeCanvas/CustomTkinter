from PySide6.QtWidgets import QWidget, QHBoxLayout, QStackedWidget
from app.components.sidebar import Sidebar
from app.views.create_view import CreateView
from app.views.read_view import ReadView
from app.views.update_view import UpdateView
from app.views.delete_view import DeleteView


class MainView(QWidget):
    def __init__(self, router):
        super().__init__()
        self.router = router

        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # Sidebar
        self.sidebar = Sidebar(router=self.router)
        self.layout.addWidget(self.sidebar)

        # Stacked widget for dynamic content
        self.stack = QStackedWidget()
        self.layout.addWidget(self.stack)

        # Initialize all views
        self.views = {
            "main": QWidget(),  # Placeholder dashboard
            "create": CreateView(router=self.router),
            "read": ReadView(router=self.router),
            "update": UpdateView(router=self.router),
            "delete": DeleteView(router=self.router),
        }

        # Add views to stacked widget
        for view in self.views.values():
            self.stack.addWidget(view)

        # Show default view
        self.navigate("main")

    def navigate(self, route):
        if route not in self.views:
            print(f"[MainView] Unknown route: {route}")
            return

        # Set stacked widget to the correct view
        widget = self.views[route]
        self.stack.setCurrentWidget(widget)

        # Update sidebar active button
        self.sidebar.set_active(route)
