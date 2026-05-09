# # ============================================================
# # PRODUCTION GRADE LIGHT THEME
# # Customer Notifications Management System
# # Tech Stack: Python + CustomTkinter
# # ============================================================

# import customtkinter as ctk

# # ------------------------------------------------------------
# # GLOBAL APPEARANCE
# # ------------------------------------------------------------

# ctk.set_appearance_mode("light")
# ctk.set_default_color_theme("blue")


# # ============================================================
# # DESIGN TOKENS
# # ============================================================

# THEME = {

#     # --------------------------------------------------------
#     # PRIMARY BRAND COLORS
#     # --------------------------------------------------------
#     "primary": "#2563EB",          # Professional blue
#     "primary_hover": "#1D4ED8",
#     "primary_light": "#DBEAFE",

#     # --------------------------------------------------------
#     # SUCCESS / WARNING / ERROR
#     # --------------------------------------------------------
#     "success": "#16A34A",
#     "warning": "#F59E0B",
#     "danger": "#DC2626",
#     "info": "#0EA5E9",

#     # --------------------------------------------------------
#     # BACKGROUND SYSTEM
#     # --------------------------------------------------------
#     "bg": "#F5F7FB",               # Main app background
#     "surface": "#FFFFFF",          # Cards / panels
#     "surface_2": "#F8FAFC",        # Secondary panels
#     "sidebar": "#111827",          # Dark sidebar for contrast

#     # --------------------------------------------------------
#     # TEXT COLORS
#     # --------------------------------------------------------
#     "text": "#0F172A",
#     "text_secondary": "#475569",
#     "text_muted": "#94A3B8",
#     "text_white": "#FFFFFF",

#     # --------------------------------------------------------
#     # BORDER / DIVIDER
#     # --------------------------------------------------------
#     "border": "#E2E8F0",
#     "divider": "#CBD5E1",

#     # --------------------------------------------------------
#     # INPUTS
#     # --------------------------------------------------------
#     "input_bg": "#FFFFFF",
#     "input_border": "#D1D5DB",
#     "input_focus": "#2563EB",

#     # --------------------------------------------------------
#     # TABLES
#     # --------------------------------------------------------
#     "table_header": "#F1F5F9",
#     "table_row_hover": "#EFF6FF",

#     # --------------------------------------------------------
#     # SHADOW EFFECT COLORS
#     # --------------------------------------------------------
#     "shadow_light": "#00000010",
# }


# # ============================================================
# # TYPOGRAPHY SYSTEM
# # ============================================================

# FONTS = {
#     "display": ("Segoe UI", 28, "bold"),
#     "title": ("Segoe UI", 22, "bold"),
#     "heading": ("Segoe UI", 18, "bold"),
#     "subheading": ("Segoe UI", 15, "bold"),
#     "body": ("Segoe UI", 13),
#     "body_bold": ("Segoe UI", 13, "bold"),
#     "small": ("Segoe UI", 11),
#     "button": ("Segoe UI Semibold", 13),
# }


# # ============================================================
# # SPACING SYSTEM
# # ============================================================

# SPACE = {
#     "xs": 4,
#     "sm": 8,
#     "md": 12,
#     "lg": 16,
#     "xl": 24,
#     "xxl": 32,
# }


# # ============================================================
# # COMPONENT FACTORIES
# # ============================================================

# class UITheme:

#     # --------------------------------------------------------
#     # MAIN WINDOW
#     # --------------------------------------------------------
#     @staticmethod
#     def app_window(app):
#         app.configure(fg_color=THEME["bg"])


#     # --------------------------------------------------------
#     # SIDEBAR
#     # --------------------------------------------------------
#     @staticmethod
#     def sidebar(parent):
#         return ctk.CTkFrame(
#             parent,
#             fg_color=THEME["sidebar"],
#             corner_radius=0,
#             width=260
#         )


#     # --------------------------------------------------------
#     # MAIN CONTENT AREA
#     # --------------------------------------------------------
#     @staticmethod
#     def content(parent):
#         return ctk.CTkFrame(
#             parent,
#             fg_color=THEME["bg"],
#             corner_radius=0
#         )


#     # --------------------------------------------------------
#     # CARDS
#     # --------------------------------------------------------
#     @staticmethod
#     def card(parent):
#         return ctk.CTkFrame(
#             parent,
#             fg_color=THEME["surface"],
#             border_width=1,
#             border_color=THEME["border"],
#             corner_radius=14
#         )


#     # --------------------------------------------------------
#     # PRIMARY BUTTON
#     # --------------------------------------------------------
#     @staticmethod
#     def primary_button(parent, text, command=None):

#         return ctk.CTkButton(
#             parent,
#             text=text,
#             command=command,

#             height=42,
#             corner_radius=10,

#             fg_color=THEME["primary"],
#             hover_color=THEME["primary_hover"],
#             text_color=THEME["text_white"],

#             border_width=0,

#             font=FONTS["button"],

#             cursor="hand2"
#         )


#     # --------------------------------------------------------
#     # SECONDARY BUTTON
#     # --------------------------------------------------------
#     @staticmethod
#     def secondary_button(parent, text, command=None):

#         return ctk.CTkButton(
#             parent,
#             text=text,
#             command=command,

#             height=42,
#             corner_radius=10,

#             fg_color=THEME["surface"],
#             hover_color="#F1F5F9",

#             text_color=THEME["text"],

#             border_width=1,
#             border_color=THEME["border"],

#             font=FONTS["button"],

#             cursor="hand2"
#         )


#     # --------------------------------------------------------
#     # INPUT FIELD
#     # --------------------------------------------------------
#     @staticmethod
#     def entry(parent, placeholder=""):

#         return ctk.CTkEntry(
#             parent,

#             height=42,
#             corner_radius=10,

#             fg_color=THEME["input_bg"],
#             border_color=THEME["input_border"],
#             text_color=THEME["text"],

#             placeholder_text=placeholder,
#             placeholder_text_color=THEME["text_muted"],

#             font=FONTS["body"]
#         )


#     # --------------------------------------------------------
#     # SEARCH INPUT
#     # --------------------------------------------------------
#     @staticmethod
#     def search_entry(parent):

#         return ctk.CTkEntry(
#             parent,

#             height=44,
#             corner_radius=12,

#             fg_color=THEME["surface"],
#             border_color=THEME["border"],

#             placeholder_text="Search notifications...",
#             placeholder_text_color=THEME["text_muted"],

#             text_color=THEME["text"],

#             font=FONTS["body"]
#         )


#     # --------------------------------------------------------
#     # LABELS
#     # --------------------------------------------------------
#     @staticmethod
#     def title(parent, text):

#         return ctk.CTkLabel(
#             parent,
#             text=text,
#             text_color=THEME["text"],
#             font=FONTS["title"]
#         )


#     @staticmethod
#     def heading(parent, text):

#         return ctk.CTkLabel(
#             parent,
#             text=text,
#             text_color=THEME["text"],
#             font=FONTS["heading"]
#         )


#     @staticmethod
#     def body(parent, text):

#         return ctk.CTkLabel(
#             parent,
#             text=text,
#             text_color=THEME["text_secondary"],
#             font=FONTS["body"]
#         )


#     # --------------------------------------------------------
#     # SIDEBAR NAV BUTTON
#     # --------------------------------------------------------
#     @staticmethod
#     def nav_button(parent, text, command=None):

#         return ctk.CTkButton(
#             parent,

#             text=text,
#             command=command,

#             height=46,
#             anchor="w",

#             fg_color="transparent",
#             hover_color="#1F2937",

#             text_color="#E5E7EB",

#             corner_radius=10,

#             font=FONTS["body_bold"]
#         )


#     # --------------------------------------------------------
#     # STATUS BADGES
#     # --------------------------------------------------------
#     @staticmethod
#     def success_badge(parent, text="Active"):

#         return ctk.CTkLabel(
#             parent,
#             text=f"  {text}  ",
#             fg_color="#DCFCE7",
#             text_color="#166534",
#             corner_radius=8,
#             font=FONTS["small"],
#             height=28
#         )


#     @staticmethod
#     def warning_badge(parent, text="Pending"):

#         return ctk.CTkLabel(
#             parent,
#             text=f"  {text}  ",
#             fg_color="#FEF3C7",
#             text_color="#92400E",
#             corner_radius=8,
#             font=FONTS["small"],
#             height=28
#         )


#     @staticmethod
#     def danger_badge(parent, text="Failed"):

#         return ctk.CTkLabel(
#             parent,
#             text=f"  {text}  ",
#             fg_color="#FEE2E2",
#             text_color="#991B1B",
#             corner_radius=8,
#             font=FONTS["small"],
#             height=28
#         )


# # ============================================================
# # PRODUCTION LAYOUT EXAMPLE
# # ============================================================

# class DemoApp(ctk.CTk):

#     def __init__(self):
#         super().__init__()

#         self.geometry("1440x900")
#         self.title("Customer Notifications Management System")

#         UITheme.app_window(self)

#         # ----------------------------------------------------
#         # GRID
#         # ----------------------------------------------------
#         self.grid_columnconfigure(1, weight=1)
#         self.grid_rowconfigure(0, weight=1)

#         # ----------------------------------------------------
#         # SIDEBAR
#         # ----------------------------------------------------
#         sidebar = UITheme.sidebar(self)
#         sidebar.grid(row=0, column=0, sticky="nsw")

#         logo = ctk.CTkLabel(
#             sidebar,
#             text="NotifyHub",
#             text_color="white",
#             font=("Segoe UI", 24, "bold")
#         )
#         logo.pack(padx=24, pady=(30, 24), anchor="w")

#         nav_items = [
#             "Dashboard",
#             "Notifications",
#             "Campaigns",
#             "Customers",
#             "Analytics",
#             "Settings"
#         ]

#         for item in nav_items:
#             btn = UITheme.nav_button(sidebar, item)
#             btn.pack(fill="x", padx=16, pady=4)

#         # ----------------------------------------------------
#         # CONTENT AREA
#         # ----------------------------------------------------
#         content = UITheme.content(self)
#         content.grid(row=0, column=1, sticky="nsew")

#         content.grid_columnconfigure(0, weight=1)

#         # ----------------------------------------------------
#         # TOPBAR
#         # ----------------------------------------------------
#         topbar = ctk.CTkFrame(
#             content,
#             fg_color="transparent",
#             height=80
#         )
#         topbar.grid(row=0, column=0, sticky="ew", padx=24, pady=20)

#         title = UITheme.title(
#             topbar,
#             "Customer Notifications"
#         )
#         title.pack(side="left")

#         search = UITheme.search_entry(topbar)
#         search.pack(side="right", padx=(0, 12))

#         create_btn = UITheme.primary_button(
#             topbar,
#             "Create Notification"
#         )
#         create_btn.pack(side="right", padx=12)

#         # ----------------------------------------------------
#         # STATS CARDS
#         # ----------------------------------------------------
#         cards_frame = ctk.CTkFrame(
#             content,
#             fg_color="transparent"
#         )
#         cards_frame.grid(
#             row=1,
#             column=0,
#             sticky="ew",
#             padx=24,
#             pady=(0, 20)
#         )

#         for i in range(4):
#             cards_frame.grid_columnconfigure(i, weight=1)

#         stats = [
#             ("Total Sent", "124,892"),
#             ("Delivered", "121,341"),
#             ("Pending", "1,284"),
#             ("Failed", "267"),
#         ]

#         for index, (label, value) in enumerate(stats):

#             card = UITheme.card(cards_frame)
#             card.grid(
#                 row=0,
#                 column=index,
#                 padx=10,
#                 sticky="nsew"
#             )

#             inner = ctk.CTkFrame(
#                 card,
#                 fg_color="transparent"
#             )
#             inner.pack(
#                 fill="both",
#                 expand=True,
#                 padx=20,
#                 pady=20
#             )

#             ctk.CTkLabel(
#                 inner,
#                 text=label,
#                 text_color=THEME["text_secondary"],
#                 font=FONTS["body"]
#             ).pack(anchor="w")

#             ctk.CTkLabel(
#                 inner,
#                 text=value,
#                 text_color=THEME["text"],
#                 font=("Segoe UI", 28, "bold")
#             ).pack(anchor="w", pady=(10, 0))

#         # ----------------------------------------------------
#         # TABLE CONTAINER
#         # ----------------------------------------------------
#         table_card = UITheme.card(content)
#         table_card.grid(
#             row=2,
#             column=0,
#             sticky="nsew",
#             padx=24,
#             pady=(0, 24)
#         )

#         table_title = UITheme.heading(
#             table_card,
#             "Recent Notifications"
#         )
#         table_title.pack(anchor="w", padx=20, pady=(20, 16))

#         # HEADER
#         header = ctk.CTkFrame(
#             table_card,
#             fg_color=THEME["table_header"],
#             corner_radius=8,
#             height=46
#         )
#         header.pack(fill="x", padx=20)

#         headers = [
#             "Customer",
#             "Channel",
#             "Message",
#             "Status",
#             "Date"
#         ]

#         for h in headers:
#             lbl = ctk.CTkLabel(
#                 header,
#                 text=h,
#                 text_color=THEME["text_secondary"],
#                 font=FONTS["body_bold"]
#             )
#             lbl.pack(side="left", padx=30)

#         # SAMPLE ROWS
#         for _ in range(5):

#             row = ctk.CTkFrame(
#                 table_card,
#                 fg_color="transparent",
#                 height=60
#             )
#             row.pack(fill="x", padx=20, pady=6)

#             ctk.CTkLabel(
#                 row,
#                 text="John Doe",
#                 width=160,
#                 anchor="w",
#                 text_color=THEME["text"],
#                 font=FONTS["body"]
#             ).pack(side="left")

#             ctk.CTkLabel(
#                 row,
#                 text="Email",
#                 width=120,
#                 anchor="w",
#                 text_color=THEME["text_secondary"]
#             ).pack(side="left")

#             ctk.CTkLabel(
#                 row,
#                 text="Your invoice has been generated.",
#                 width=360,
#                 anchor="w",
#                 text_color=THEME["text_secondary"]
#             ).pack(side="left")

#             badge = UITheme.success_badge(
#                 row,
#                 "Delivered"
#             )
#             badge.pack(side="left", padx=30)

#             ctk.CTkLabel(
#                 row,
#                 text="09 May 2026",
#                 text_color=THEME["text_muted"]
#             ).pack(side="right", padx=20)


# # ============================================================
# # START APP
# # ============================================================

# if __name__ == "__main__":

#     app = DemoApp()
#     app.mainloop()




































# ============================================================
# WHY MANY COLORS EXIST IN A PRODUCTION THEME
# ============================================================

# """
# A professional production-grade system NEVER uses only 1 or 2 colors.

# Every color has a responsibility.

# ---------------------------------------------------------------
# COLOR PURPOSES
# ---------------------------------------------------------------

# PRIMARY
# - Main actions
# - CTA buttons
# - Active navigation
# - Important highlights

# SUCCESS
# - Delivered notifications
# - Success alerts
# - Connected status
# - Completed operations

# WARNING
# - Pending notifications
# - Retry required
# - Expiring data
# - Draft campaigns

# DANGER
# - Failed notifications
# - Delete buttons
# - Errors
# - Critical alerts

# INFO
# - Information banners
# - Analytics highlights
# - Neutral system states

# BACKGROUND COLORS
# - App structure
# - Layout separation
# - Better readability

# TEXT COLORS
# - Typography hierarchy
# - Accessibility
# - Professional readability

# BORDER COLORS
# - Component separation
# - Cleaner UI structure

# ---------------------------------------------------------------
# GOOD UI PRINCIPLE
# ---------------------------------------------------------------

# A modern enterprise application should:
# ✔ Use semantic colors
# ✔ Have clear visual hierarchy
# ✔ Separate content visually
# ✔ Reduce eye fatigue
# ✔ Improve scanning speed
# ✔ Increase readability
# ✔ Make statuses instantly understandable

# ===============================================================
# UPDATED DEMO APP USING ALL COLORS
# ===============================================================
# """

# import customtkinter as ctk

# ctk.set_appearance_mode("light")


# # ============================================================
# # FULL PROFESSIONAL COLOR SYSTEM
# # ============================================================

# THEME = {

#     # BRAND
#     "primary": "#2563EB",
#     "primary_hover": "#1D4ED8",
#     "primary_light": "#DBEAFE",

#     # STATUS COLORS
#     "success": "#16A34A",
#     "success_bg": "#DCFCE7",

#     "warning": "#F59E0B",
#     "warning_bg": "#FEF3C7",

#     "danger": "#DC2626",
#     "danger_bg": "#FEE2E2",

#     "info": "#0EA5E9",
#     "info_bg": "#E0F2FE",

#     # SURFACES
#     "bg": "#F5F7FB",
#     "surface": "#FFFFFF",
#     "surface_2": "#F8FAFC",

#     # SIDEBAR
#     "sidebar": "#0F172A",
#     "sidebar_hover": "#1E293B",

#     # TEXT
#     "text": "#0F172A",
#     "text_secondary": "#475569",
#     "text_muted": "#94A3B8",
#     "text_white": "#FFFFFF",

#     # BORDER
#     "border": "#E2E8F0",

#     # TABLE
#     "table_header": "#F1F5F9",
#     "table_hover": "#EFF6FF",
# }


# # ============================================================
# # APP
# # ============================================================

# class App(ctk.CTk):

#     def __init__(self):
#         super().__init__()

#         self.geometry("1500x900")
#         self.title("Customer Notifications Management")

#         self.configure(fg_color=THEME["bg"])

#         # ----------------------------------------------------
#         # LAYOUT
#         # ----------------------------------------------------
#         self.grid_columnconfigure(1, weight=1)
#         self.grid_rowconfigure(0, weight=1)

#         self.create_sidebar()
#         self.create_main()


#     # ========================================================
#     # SIDEBAR
#     # ========================================================

#     def create_sidebar(self):

#         sidebar = ctk.CTkFrame(
#             self,
#             width=260,
#             fg_color=THEME["sidebar"],
#             corner_radius=0
#         )
#         sidebar.grid(row=0, column=0, sticky="ns")

#         logo = ctk.CTkLabel(
#             sidebar,
#             text="NotifyHub",
#             text_color="white",
#             font=("Segoe UI", 26, "bold")
#         )
#         logo.pack(anchor="w", padx=24, pady=(30, 30))

#         menus = [
#             "Dashboard",
#             "Notifications",
#             "Campaigns",
#             "Analytics",
#             "Customers",
#             "Settings"
#         ]

#         for menu in menus:

#             btn = ctk.CTkButton(
#                 sidebar,
#                 text=menu,
#                 height=46,
#                 anchor="w",

#                 fg_color="transparent",
#                 hover_color=THEME["sidebar_hover"],

#                 text_color="#E2E8F0",

#                 corner_radius=10,

#                 font=("Segoe UI", 13, "bold")
#             )

#             btn.pack(fill="x", padx=16, pady=4)


#     # ========================================================
#     # MAIN CONTENT
#     # ========================================================

#     def create_main(self):

#         main = ctk.CTkFrame(
#             self,
#             fg_color="transparent"
#         )
#         main.grid(row=0, column=1, sticky="nsew")

#         main.grid_columnconfigure(0, weight=1)

#         # ----------------------------------------------------
#         # TOPBAR
#         # ----------------------------------------------------

#         topbar = ctk.CTkFrame(
#             main,
#             height=80,
#             fg_color="transparent"
#         )
#         topbar.grid(row=0, column=0, sticky="ew", padx=24, pady=20)

#         title = ctk.CTkLabel(
#             topbar,
#             text="Customer Notifications",
#             text_color=THEME["text"],
#             font=("Segoe UI", 28, "bold")
#         )
#         title.pack(side="left")

#         create_btn = ctk.CTkButton(
#             topbar,
#             text="Create Notification",

#             fg_color=THEME["primary"],
#             hover_color=THEME["primary_hover"],

#             text_color="white",

#             height=42,
#             corner_radius=10,

#             font=("Segoe UI", 13, "bold")
#         )
#         create_btn.pack(side="right")


#         # ====================================================
#         # STATUS CARDS
#         # ====================================================

#         cards = ctk.CTkFrame(
#             main,
#             fg_color="transparent"
#         )
#         cards.grid(row=1, column=0, sticky="ew", padx=24)

#         for i in range(4):
#             cards.grid_columnconfigure(i, weight=1)

#         # ----------------------------------------------------
#         # PRIMARY CARD
#         # ----------------------------------------------------

#         primary_card = self.card(
#             cards,
#             "Total Sent",
#             "124,892",
#             THEME["primary"],
#             THEME["primary_light"]
#         )
#         primary_card.grid(row=0, column=0, padx=8, sticky="nsew")

#         # ----------------------------------------------------
#         # SUCCESS CARD
#         # ----------------------------------------------------

#         success_card = self.card(
#             cards,
#             "Delivered",
#             "121,341",
#             THEME["success"],
#             THEME["success_bg"]
#         )
#         success_card.grid(row=0, column=1, padx=8, sticky="nsew")

#         # ----------------------------------------------------
#         # WARNING CARD
#         # ----------------------------------------------------

#         warning_card = self.card(
#             cards,
#             "Pending",
#             "1,284",
#             THEME["warning"],
#             THEME["warning_bg"]
#         )
#         warning_card.grid(row=0, column=2, padx=8, sticky="nsew")

#         # ----------------------------------------------------
#         # DANGER CARD
#         # ----------------------------------------------------

#         danger_card = self.card(
#             cards,
#             "Failed",
#             "267",
#             THEME["danger"],
#             THEME["danger_bg"]
#         )
#         danger_card.grid(row=0, column=3, padx=8, sticky="nsew")


#         # ====================================================
#         # INFO BANNER
#         # ====================================================

#         info_banner = ctk.CTkFrame(
#             main,
#             fg_color=THEME["info_bg"],
#             corner_radius=12,
#             height=60,
#             border_width=1,
#             border_color="#BAE6FD"
#         )

#         info_banner.grid(
#             row=2,
#             column=0,
#             sticky="ew",
#             padx=24,
#             pady=20
#         )

#         info_label = ctk.CTkLabel(
#             info_banner,
#             text="System health is stable. Notification queue processing normally.",
#             text_color=THEME["info"],
#             font=("Segoe UI", 13, "bold")
#         )
#         info_label.pack(anchor="w", padx=20, pady=18)


#         # ====================================================
#         # TABLE SECTION
#         # ====================================================

#         table = ctk.CTkFrame(
#             main,
#             fg_color=THEME["surface"],
#             corner_radius=14,
#             border_width=1,
#             border_color=THEME["border"]
#         )

#         table.grid(
#             row=3,
#             column=0,
#             sticky="nsew",
#             padx=24,
#             pady=(0, 24)
#         )

#         # ----------------------------------------------------
#         # TABLE HEADER
#         # ----------------------------------------------------

#         header = ctk.CTkFrame(
#             table,
#             fg_color=THEME["table_header"],
#             height=50,
#             corner_radius=10
#         )

#         header.pack(fill="x", padx=20, pady=20)

#         headers = [
#             "Customer",
#             "Channel",
#             "Message",
#             "Status",
#             "Priority"
#         ]

#         for h in headers:

#             lbl = ctk.CTkLabel(
#                 header,
#                 text=h,
#                 text_color=THEME["text_secondary"],
#                 font=("Segoe UI", 13, "bold")
#             )

#             lbl.pack(side="left", padx=28)


#         # ----------------------------------------------------
#         # ROWS
#         # ----------------------------------------------------

#         self.row(table, "John Doe", "Email", "Delivered", "High")
#         self.row(table, "Sarah Smith", "SMS", "Pending", "Medium")
#         self.row(table, "Michael", "Push", "Failed", "Critical")
#         self.row(table, "Alex", "Email", "Delivered", "Low")


#     # ========================================================
#     # CARD COMPONENT
#     # ========================================================

#     def card(self, parent, title, value, color, bg):

#         card = ctk.CTkFrame(
#             parent,
#             fg_color=THEME["surface"],
#             corner_radius=14,
#             border_width=1,
#             border_color=THEME["border"],
#             height=140
#         )

#         top = ctk.CTkFrame(
#             card,
#             fg_color=bg,
#             height=8,
#             corner_radius=10
#         )
#         top.pack(fill="x", padx=0, pady=0)

#         body = ctk.CTkFrame(
#             card,
#             fg_color="transparent"
#         )
#         body.pack(fill="both", expand=True, padx=20, pady=20)

#         ctk.CTkLabel(
#             body,
#             text=title,
#             text_color=THEME["text_secondary"],
#             font=("Segoe UI", 13)
#         ).pack(anchor="w")

#         ctk.CTkLabel(
#             body,
#             text=value,
#             text_color=color,
#             font=("Segoe UI", 30, "bold")
#         ).pack(anchor="w", pady=(10, 0))

#         return card


#     # ========================================================
#     # TABLE ROW
#     # ========================================================

#     def row(self, parent, customer, channel, status, priority):

#         row = ctk.CTkFrame(
#             parent,
#             fg_color=THEME["surface"],
#             height=60
#         )

#         row.pack(fill="x", padx=20, pady=6)

#         ctk.CTkLabel(
#             row,
#             text=customer,
#             width=160,
#             anchor="w",
#             text_color=THEME["text"],
#             font=("Segoe UI", 13, "bold")
#         ).pack(side="left")

#         ctk.CTkLabel(
#             row,
#             text=channel,
#             width=120,
#             anchor="w",
#             text_color=THEME["text_secondary"]
#         ).pack(side="left")

#         # STATUS COLORS

#         if status == "Delivered":
#             status_bg = THEME["success_bg"]
#             status_text = THEME["success"]

#         elif status == "Pending":
#             status_bg = THEME["warning_bg"]
#             status_text = THEME["warning"]

#         else:
#             status_bg = THEME["danger_bg"]
#             status_text = THEME["danger"]

#         badge = ctk.CTkLabel(
#             row,
#             text=f"  {status}  ",
#             fg_color=status_bg,
#             text_color=status_text,
#             corner_radius=8,
#             height=28,
#             font=("Segoe UI", 11, "bold")
#         )

#         badge.pack(side="left", padx=20)

#         # PRIORITY COLORS

#         if priority == "Critical":
#             p_color = THEME["danger"]

#         elif priority == "High":
#             p_color = THEME["warning"]

#         elif priority == "Medium":
#             p_color = THEME["info"]

#         else:
#             p_color = THEME["success"]

#         priority_label = ctk.CTkLabel(
#             row,
#             text=priority,
#             text_color=p_color,
#             font=("Segoe UI", 12, "bold")
#         )

#         priority_label.pack(side="right", padx=20)


# # ============================================================
# # RUN APP
# # ============================================================

# app = App()
# app.mainloop()







































# ============================================================
# MODERN PRODUCTION SIDEBAR
# Customer Notifications Management System
# ONLY SIDEBAR
# ============================================================

import customtkinter as ctk

ctk.set_appearance_mode("light")


# ============================================================
# COLORS
# ============================================================

THEME = {

    # SIDEBAR
    "sidebar_bg": "#0F172A",
    "sidebar_surface": "#111827",

    # ACTIVE
    "active_bg": "#2563EB",
    "active_hover": "#1D4ED8",

    # HOVER
    "hover": "#1E293B",

    # TEXT
    "text": "#E5E7EB",
    "text_muted": "#94A3B8",
    "text_active": "#FFFFFF",

    # STATUS
    "success": "#22C55E",

    # BORDER
    "border": "#1F2937",
}


# ============================================================
# SIDEBAR COMPONENT
# ============================================================

class ModernSidebar(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(

            parent,

            width=290,

            fg_color=THEME["sidebar_bg"],

            corner_radius=0,

            border_width=0
        )

        self.pack_propagate(False)

        # ----------------------------------------------------
        # TOP SECTION
        # ----------------------------------------------------

        self.top_section()

        # ----------------------------------------------------
        # NAVIGATION
        # ----------------------------------------------------

        self.navigation()

        # ----------------------------------------------------
        # STORAGE / SYSTEM CARD
        # ----------------------------------------------------

        self.system_card()

        # ----------------------------------------------------
        # USER PROFILE
        # ----------------------------------------------------

        self.user_profile()


    # ========================================================
    # TOP SECTION
    # ========================================================

    def top_section(self):

        top = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        top.pack(fill="x", padx=22, pady=(24, 20))

        # ----------------------------------------------------
        # LOGO ROW
        # ----------------------------------------------------

        logo_row = ctk.CTkFrame(
            top,
            fg_color="transparent"
        )

        logo_row.pack(fill="x")

        # LOGO ICON

        logo_icon = ctk.CTkFrame(
            logo_row,

            width=48,
            height=48,

            fg_color="#2563EB",

            corner_radius=14
        )

        logo_icon.pack(side="left")

        logo_icon.pack_propagate(False)

        ctk.CTkLabel(
            logo_icon,
            text="N",
            text_color="white",
            font=("Segoe UI", 22, "bold")
        ).place(relx=0.5, rely=0.5, anchor="center")

        # APP NAME

        text_frame = ctk.CTkFrame(
            logo_row,
            fg_color="transparent"
        )

        text_frame.pack(side="left", padx=14)

        ctk.CTkLabel(
            text_frame,
            text="NotifyHub",
            text_color="white",
            font=("Segoe UI", 20, "bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            text_frame,
            text="Notification Platform",
            text_color=THEME["text_muted"],
            font=("Segoe UI", 11)
        ).pack(anchor="w")

        # ----------------------------------------------------
        # ONLINE STATUS
        # ----------------------------------------------------

        status = ctk.CTkFrame(
            top,
            fg_color=THEME["sidebar_surface"],
            corner_radius=12,
            height=52
        )

        status.pack(fill="x", pady=(22, 0))

        status.pack_propagate(False)

        dot = ctk.CTkFrame(
            status,
            width=10,
            height=10,
            fg_color=THEME["success"],
            corner_radius=100
        )

        dot.place(x=18, rely=0.5, anchor="w")

        ctk.CTkLabel(
            status,
            text="System Online",
            text_color=THEME["text"],
            font=("Segoe UI", 12, "bold")
        ).place(x=38, rely=0.38)

        ctk.CTkLabel(
            status,
            text="All services operational",
            text_color=THEME["text_muted"],
            font=("Segoe UI", 10)
        ).place(x=38, rely=0.62)


    # ========================================================
    # NAVIGATION
    # ========================================================

    def navigation(self):

        nav = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        nav.pack(fill="both", expand=True, padx=16, pady=(10, 10))

        # SECTION TITLE

        ctk.CTkLabel(
            nav,
            text="MAIN MENU",
            text_color=THEME["text_muted"],
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w", padx=10, pady=(0, 12))

        # NAV ITEMS

        menus = [

            ("◉", "Dashboard", True),
            ("✉", "Notifications", False),
            ("⚡", "Campaigns", False),
            ("👥", "Customers", False),
            ("📊", "Analytics", False),
            ("🔔", "Alerts", False),
            ("🧾", "Logs", False),
            ("⚙", "Settings", False),
        ]

        for icon, text, active in menus:

            self.nav_item(nav, icon, text, active)


    # ========================================================
    # SINGLE NAV ITEM
    # ========================================================

    def nav_item(self, parent, icon, text, active=False):

        if active:

            bg = THEME["active_bg"]
            hover = THEME["active_hover"]
            text_color = THEME["text_active"]

        else:

            bg = "transparent"
            hover = THEME["hover"]
            text_color = THEME["text"]

        btn = ctk.CTkButton(

            parent,

            text=f"  {icon}    {text}",

            height=52,

            anchor="w",

            fg_color=bg,
            hover_color=hover,

            text_color=text_color,

            corner_radius=14,

            font=("Segoe UI", 13, "bold"),

            border_width=0
        )

        btn.pack(fill="x", pady=4)

        # ACTIVE INDICATOR

        if active:

            indicator = ctk.CTkFrame(
                btn,
                width=4,
                fg_color="white",
                corner_radius=10
            )

            indicator.place(x=0, y=12, relheight=0.55)


    # ========================================================
    # SYSTEM CARD
    # ========================================================

    def system_card(self):

        card = ctk.CTkFrame(
            self,

            fg_color=THEME["sidebar_surface"],

            corner_radius=18,

            border_width=1,

            border_color=THEME["border"],

            height=140
        )

        card.pack(fill="x", padx=18, pady=10)

        card.pack_propagate(False)

        # TITLE

        ctk.CTkLabel(
            card,
            text="Storage Usage",
            text_color="white",
            font=("Segoe UI", 14, "bold")
        ).pack(anchor="w", padx=18, pady=(18, 4))

        # DESCRIPTION

        ctk.CTkLabel(
            card,
            text="2.4 GB of 10 GB used",
            text_color=THEME["text_muted"],
            font=("Segoe UI", 11)
        ).pack(anchor="w", padx=18)

        # PROGRESS BAR

        progress_bg = ctk.CTkFrame(
            card,
            height=10,
            fg_color="#1F2937",
            corner_radius=100
        )

        progress_bg.pack(fill="x", padx=18, pady=(16, 0))

        progress_fill = ctk.CTkFrame(
            progress_bg,
            height=10,
            width=120,
            fg_color="#2563EB",
            corner_radius=100
        )

        progress_fill.place(x=0, y=0)

        # BUTTON

        upgrade = ctk.CTkButton(

            card,

            text="Upgrade Storage",

            height=36,

            fg_color="#2563EB",
            hover_color="#1D4ED8",

            text_color="white",

            corner_radius=10,

            font=("Segoe UI", 12, "bold")
        )

        upgrade.pack(fill="x", padx=18, pady=(18, 0))


    # ========================================================
    # USER PROFILE
    # ========================================================

    def user_profile(self):

        profile = ctk.CTkFrame(

            self,

            fg_color=THEME["sidebar_surface"],

            height=78,

            corner_radius=18,

            border_width=1,

            border_color=THEME["border"]
        )

        profile.pack(fill="x", padx=18, pady=(6, 20))

        profile.pack_propagate(False)

        # AVATAR

        avatar = ctk.CTkFrame(
            profile,

            width=46,
            height=46,

            fg_color="#2563EB",

            corner_radius=14
        )

        avatar.place(x=16, rely=0.5, anchor="w")

        ctk.CTkLabel(
            avatar,
            text="A",
            text_color="white",
            font=("Segoe UI", 18, "bold")
        ).place(relx=0.5, rely=0.5, anchor="center")

        # USER INFO

        ctk.CTkLabel(
            profile,
            text="Admin User",
            text_color="white",
            font=("Segoe UI", 13, "bold")
        ).place(x=76, y=18)

        ctk.CTkLabel(
            profile,
            text="System Administrator",
            text_color=THEME["text_muted"],
            font=("Segoe UI", 11)
        ).place(x=76, y=40)

        # SETTINGS BUTTON

        settings_btn = ctk.CTkButton(

            profile,

            text="⋮",

            width=36,
            height=36,

            fg_color="transparent",

            hover_color=THEME["hover"],

            text_color=THEME["text_muted"],

            corner_radius=10,

            font=("Segoe UI", 18, "bold")
        )

        settings_btn.place(relx=0.93, rely=0.5, anchor="center")


# ============================================================
# DEMO APP
# ============================================================

class App(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.geometry("1500x900")

        self.configure(fg_color="#F5F7FB")

        sidebar = ModernSidebar(self)
        sidebar.pack(side="left", fill="y")


# ============================================================
# RUN
# ============================================================

app = App()
app.mainloop()