import customtkinter as ctk
from tkinter import messagebox

class ConfirmModal:
    @staticmethod
    def show(title="Confirm", message="Are you sure?"):
        return messagebox.askyesno(title, message)

class AlertModal:
    @staticmethod
    def show(title="Alert", message="Something happened"):
        messagebox.showinfo(title, message)


# use like this 
# if ConfirmModal.show(message="Delete this item?"):
#     ItemsController.delete_item(item_id, self.load)
