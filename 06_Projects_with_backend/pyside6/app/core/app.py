# ===============================
# FILE: app/core/app.py
# ===============================
from PySide6.QtWidgets import QApplication, QMainWindow
from app.core.router import Router
import sys

class Application(QApplication):
    def __init__(self):
        super().__init__(sys.argv)

        self.window = QMainWindow()
        self.window.setWindowTitle("CRUD Dashboard")
        self.window.resize(1200, 700)

        self.router = Router(self.window)
        self.router.navigate("main")

        self.window.show()
