from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from app.controllers.items_controller import ItemsController


class CreateView(QWidget):
    def __init__(self, router):
        super().__init__()
        self.router = router

        layout = QVBoxLayout(self)

        title = QLabel("Create Item")
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(title)

        self.name_entry = QLineEdit()
        self.name_entry.setPlaceholderText("Item Name")
        layout.addWidget(self.name_entry)

        self.price_entry = QLineEdit()
        self.price_entry.setPlaceholderText("Price")
        layout.addWidget(self.price_entry)

        save_btn = QPushButton("Save")
        save_btn.clicked.connect(self.save)
        layout.addWidget(save_btn)

        back_btn = QPushButton("Back")
        back_btn.clicked.connect(lambda: self.router.navigate("main"))
        layout.addWidget(back_btn)

        layout.addStretch(1)

    def save(self):
        name = self.name_entry.text().strip()
        price = self.price_entry.text().strip()

        if not name or not price:
            QMessageBox.warning(self, "Validation Error", "Name and price cannot be empty.")
            return

        try:
            price = float(price)
        except ValueError:
            QMessageBox.warning(self, "Validation Error", "Price must be a number.")
            return

        payload = {"name": name, "price": price}

        # Call controller async
        ItemsController.create_item(payload, callback=lambda: self.router.navigate("main"))
