# ===============================
# FILE: frontend/app/components/table_model.py
# ===============================
from PySide6.QtCore import QAbstractTableModel, Qt

class CommentsTableModel(QAbstractTableModel):
    HEADERS = ["ID", "Name", "Email", "Body"]

    def __init__(self, data=None):
        super().__init__()
        self._data = data or []

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self.HEADERS)

    def data(self, index, role):
        if not index.isValid():
            return None

        if role == Qt.DisplayRole:
            item = self._data[index.row()]
            return [
                item["id"],
                item["name"],
                item["email"],
                item["body"],
            ][index.column()]

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.HEADERS[section]
