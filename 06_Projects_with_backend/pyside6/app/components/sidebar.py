from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton


class Sidebar(QWidget):
    def __init__(self, router):
        super().__init__()
        self.router = router

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)

        self.buttons = {}

        # Define all available routes
        routes = ["main", "create", "read", "update", "delete"]

        for name in routes:
            btn = QPushButton(name.capitalize())
            btn.clicked.connect(lambda _, r=name: self.router.navigate(r))
            layout.addWidget(btn)
            self.buttons[name] = btn

        layout.addStretch(1)  # Push buttons to the top

    def set_active(self, route_name):
        """Highlight the active button"""
        for name, btn in self.buttons.items():
            if name == route_name:
                btn.setStyleSheet("font-weight: bold; background-color: lightblue;")
            else:
                btn.setStyleSheet("")
