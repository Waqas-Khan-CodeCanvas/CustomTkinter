import customtkinter as ctk
import tkinter as tk
import re
import os
import sys

# --- Window Setup ---
ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.geometry("380x560")
root.title("ClearMath")
root.overrideredirect(True)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

root.iconbitmap(resource_path("icon.ico"))

# --- Colors (match your website theme) ---
BG_COLOR = "#0a0a0a"
ACCENT = "#1f93ff"
TEXT_COLOR = "#e6e6e6"
BTN_BG = "#1a1a1a"
BTN_HOVER = "#1f93ff"
ERROR_COLOR = "#ff4d4d"

# --- Outer Frame with Gradient Border ---
outer = ctk.CTkFrame(root, corner_radius=20, fg_color=BG_COLOR, border_width=2, border_color=ACCENT)
outer.pack(fill="both", expand=True, padx=2, pady=2)

# --- Custom Title Bar ---
title_bar = ctk.CTkFrame(outer, height=40, corner_radius=20, fg_color=BG_COLOR)
title_bar.pack(fill="x", padx=10, pady=5)

title_label = ctk.CTkLabel(title_bar, text="ClearMath", font=("Segoe UI", 14, "bold"), text_color=ACCENT)
title_label.pack(side="left", padx=10)

# --- Close and Minimize Buttons ---
def minimize_window():
    root.overrideredirect(False)
    root.iconify()

ctk.CTkButton(title_bar, text="—", width=35, height=30, corner_radius=8,
              fg_color=BTN_BG, hover_color="#333333", text_color="white",
              command=minimize_window).pack(side="right", padx=5, pady=5)

ctk.CTkButton(title_bar, text="✕", width=35, height=30, corner_radius=8,
              fg_color="#ff1a1a", hover_color=ERROR_COLOR, text_color="white",
              command=root.destroy).pack(side="right", padx=5, pady=5)

# --- Make window draggable ---
def start_move(e): root.x, root.y = e.x, e.y
def stop_move(e): root.x = root.y = None
def on_move(e):
    deltax, deltay = e.x - root.x, e.y - root.y
    root.geometry(f"+{root.winfo_x() + deltax}+{root.winfo_y() + deltay}")
for w in [title_bar, title_label]:
    w.bind("<ButtonPress-1>", start_move)
    w.bind("<ButtonRelease-1>", stop_move)
    w.bind("<B1-Motion>", on_move)

# --- Entry Field (Display) ---
main_frame = ctk.CTkFrame(outer, fg_color=BG_COLOR)
main_frame.pack(fill="both", expand=True, padx=5, pady=5)

entry = ctk.CTkEntry(main_frame, font=("Consolas", 28, "bold"), justify="right",
                     width=360, height=70, border_width=1.5,
                     fg_color=BTN_BG, border_color=ACCENT, text_color=TEXT_COLOR)
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=(0, 20))

# --- Safe Expression Evaluator ---
def evaluate_expression(expr: str) -> str:
    try:
        expr = expr.replace("×", "*").replace("÷", "/")
        expr = re.sub(r'(\d+)%', r'(\1/100)', expr)
        while expr and expr[-1] in "+-*/.": expr = expr[:-1]
        result = eval(expr, {"__builtins__": None}, {})
        return str(round(result, 6))
    except Exception:
        return "Error"

# --- Button Logic ---
def on_click(char):
    text = entry.get()
    if char == "C": entry.delete(0, "end")
    elif char == "←": entry.delete(len(text)-1)
    elif char == "=":
        result = evaluate_expression(text)
        entry.delete(0, "end")
        entry.insert("end", result)
        if result == "Error":
            entry.configure(border_color=ERROR_COLOR)
        else:
            entry.configure(border_color=ACCENT)
    else:
        entry.insert("end", char)

# --- Button Layout ---
buttons = [
    ["C", "←", "÷", "×"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "."],
    ["0", "="]
]

# Generate buttons with Glow Hover effect 
for r, row in enumerate(buttons, start=1):
    for c, char in enumerate(row):
        if r == 5 and c == len(row) - 1:
            ctk.CTkButton(main_frame, text=char, width=70, height=60,
                          corner_radius=12, font=("Segoe UI", 22, "bold"),
                          fg_color=ACCENT, hover_color="#2aa3ff",
                          text_color="white",
                          command=lambda ch=char: on_click(ch)).grid(
                              row=r, column=c, columnspan=3, padx=8, pady=8, sticky="nsew"
                          )
            break
        ctk.CTkButton(main_frame, text=char, width=70, height=60,
                      corner_radius=12, font=("Segoe UI", 20),
                      fg_color=BTN_BG, hover_color=BTN_HOVER,
                      text_color=TEXT_COLOR,
                      command=lambda ch=char: on_click(ch)).grid(
                          row=r, column=c, padx=8, pady=8, sticky="nsew"
                      )

# --- Responsive Grid ---
for i in range(5): main_frame.rowconfigure(i, weight=1)
for i in range(4): main_frame.columnconfigure(i, weight=1)

# --- Reapply border after minimize ---
def watch_state():
    if root.state() == "normal":
        try: root.overrideredirect(True)
        except: pass
    root.after(300, watch_state)

root.after(300, watch_state)
root.mainloop()
