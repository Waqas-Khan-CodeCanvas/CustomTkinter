import customtkinter as ctk

app = ctk.CTk()
app.geometry("1000x600")
app._set_appearance_mode("dark")

# app level configurations
app.grid_rowconfigure(0 , weight=1)
app.grid_columnconfigure(1 , weight=1)

# sidebar
sidebar = ctk.CTkFrame(app , width=200 , border_width=1)
sidebar.grid(row=0 , column=0 , sticky="nsew")
sidebar.grid_columnconfigure(0, weight=0)

#  main app window
main = ctk.CTkFrame(app , border_width=1)
main.grid(row=0 , column=1 , sticky="nsew")
main.grid_rowconfigure(1 , weight=1)
main.grid_columnconfigure(0 , weight=1)

#  header (navbar)
topbar = ctk.CTkFrame(main, height=60 , border_width=1)
topbar.grid(row=0 , column=0 , sticky="nsew")

# content container
content = ctk.CTkFrame(main, border_width=1  , fg_color="#312626")
content.grid(row=1 , column=0 , sticky="nsew")

# content container configurations
content.grid_rowconfigure(1, weight=1)
content.grid_columnconfigure((0,1,2), weight=1)

# orders
card1 = ctk.CTkFrame(content)
card1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# pinding
card2 = ctk.CTkFrame(content)
card2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# deliverd 
card3 = ctk.CTkFrame(content)
card3.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

# bar chat
chart_frame = ctk.CTkFrame(content , height=200)
chart_frame.grid(row=1, column=0, columnspan=2, sticky="new", padx=10, pady=10)

# pie chart 
chart_frame1 = ctk.CTkFrame(content , height=200)
chart_frame1.grid(row=1, column=2, sticky="new", padx=10, pady=10)

app.mainloop()