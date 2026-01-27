from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableView, QLabel
from app.components.table_model import CommentsTableModel
from app.services.api_client import APIClient


class ReadView(QWidget):
    def __init__(self, router=None):
        super().__init__()
        self.router = router  # store router for future use (optional)

        layout = QVBoxLayout(self)

        title = QLabel("Comments")
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(title)

        self.table = QTableView()
        layout.addWidget(self.table)

        # Load data (for now synchronous)
        data = APIClient.get_items()  # returns 500 items
        model = CommentsTableModel(data)
        self.table.setModel(model)
        self.table.resizeColumnsToContents()
