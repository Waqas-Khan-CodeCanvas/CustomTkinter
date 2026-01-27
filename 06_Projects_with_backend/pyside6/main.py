# ===============================
# FILE: main.py
# ===============================
from app.core.app import Application
import sys

if __name__ == "__main__":
    app = Application()
    sys.exit(app.exec())   # ✅ Qt event loop
