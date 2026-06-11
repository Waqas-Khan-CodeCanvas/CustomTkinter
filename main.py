import customtkinter as ctk
from matplotlib.widgets import ToolLineHandles

app = ctk.CTk()
app.title("CTKTopLevel demo")
app.geometry("800x400")

toplevel = ctk.CTkToplevel(app)
toplevel.geometry("800x400")
# lb = ctk.CTkLabel(toplevel , text="hello TopLevel")
# lb.pack()


app.mainloop()