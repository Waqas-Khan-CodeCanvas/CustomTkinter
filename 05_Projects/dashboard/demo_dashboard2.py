# ============================================================
# MODERN SIDEBAR + MODERN TOP NAVBAR
# Production Grade UI
# Python + CustomTkinter
# ============================================================

import customtkinter as ctk

ctk.set_appearance_mode("light")


# ============================================================
# THEME
# ============================================================

THEME = {

    # MAIN
    "bg": "#F5F7FB",
    "surface": "#FFFFFF",
    "surface_2": "#F8FAFC",

    # SIDEBAR
    "sidebar_bg": "#0F172A",
    "sidebar_surface": "#111827",
    "sidebar_hover": "#1E293B",

    # PRIMARY
    "primary": "#2563EB",
    "primary_hover": "#1D4ED8",
    "primary_light": "#DBEAFE",

    # STATUS
    "success": "#22C55E",
    "warning": "#F59E0B",
    "danger": "#EF4444",
    "info": "#0EA5E9",

    # TEXT
    "text": "#0F172A",
    "text_secondary": "#475569",
    "text_muted": "#94A3B8",
    "text_white": "#FFFFFF",

    # BORDER
    "border": "#E2E8F0",
}


# ============================================================
# MODERN SIDEBAR
# ============================================================

class ModernSidebar(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(

            parent,

            width=290,

            fg_color=THEME["sidebar_bg"],

            corner_radius=0
        )

        self.pack_propagate(False)

        self.create_logo()
        self.create_navigation()
        self.create_workspace_card()
        self.create_profile()


    # ========================================================
    # LOGO SECTION
    # ========================================================

    def create_logo(self):

        top = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        top.pack(fill="x", padx=22, pady=(24, 18))

        # LOGO ROW

        row = ctk.CTkFrame(
            top,
            fg_color="transparent"
        )

        row.pack(fill="x")

        # ICON

        icon = ctk.CTkFrame(

            row,

            width=50,
            height=50,

            fg_color=THEME["primary"],

            corner_radius=16
        )

        icon.pack(side="left")

        icon.pack_propagate(False)

        ctk.CTkLabel(
            icon,
            text="N",
            text_color="white",
            font=("Segoe UI", 24, "bold")
        ).place(relx=0.5, rely=0.5, anchor="center")

        # TITLE

        text_frame = ctk.CTkFrame(
            row,
            fg_color="transparent"
        )

        text_frame.pack(side="left", padx=14)

        ctk.CTkLabel(
            text_frame,
            text="NotifyHub",
            text_color="white",
            font=("Segoe UI", 21, "bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            text_frame,
            text="Notification Platform",
            text_color=THEME["text_muted"],
            font=("Segoe UI", 11)
        ).pack(anchor="w")


    # ========================================================
    # NAVIGATION
    # ========================================================

    def create_navigation(self):

        nav = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        nav.pack(fill="both", expand=True, padx=16)

        ctk.CTkLabel(
            nav,
            text="MAIN MENU",
            text_color=THEME["text_muted"],
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w", padx=10, pady=(8, 12))

        items = [

            ("⌂", "Dashboard", True),
            ("✉", "Notifications", False),
            ("⚡", "Campaigns", False),
            ("👥", "Customers", False),
            ("📊", "Analytics", False),
            ("🔔", "Alerts", False),
            ("🧾", "Logs", False),
            ("⚙", "Settings", False),
        ]

        for icon, text, active in items:
            self.nav_item(nav, icon, text, active)


    # ========================================================
    # NAV ITEM
    # ========================================================

    def nav_item(self, parent, icon, text, active=False):

        if active:

            bg = THEME["primary"]
            hover = THEME["primary_hover"]
            color = "white"

        else:

            bg = "transparent"
            hover = THEME["sidebar_hover"]
            color = "#E2E8F0"

        btn = ctk.CTkButton(

            parent,

            text=f"  {icon}    {text}",

            anchor="w",

            height=52,

            fg_color=bg,
            hover_color=hover,

            text_color=color,

            corner_radius=14,

            font=("Segoe UI", 13, "bold")
        )

        btn.pack(fill="x", pady=4)


    # ========================================================
    # WORKSPACE CARD
    # ========================================================

    def create_workspace_card(self):

        card = ctk.CTkFrame(

            self,

            fg_color=THEME["sidebar_surface"],

            corner_radius=18,

            border_width=1,

            border_color="#1F2937",

            height=145
        )

        card.pack(fill="x", padx=18, pady=10)

        card.pack_propagate(False)

        ctk.CTkLabel(
            card,
            text="Workspace Health",
            text_color="white",
            font=("Segoe UI", 14, "bold")
        ).pack(anchor="w", padx=18, pady=(18, 4))

        ctk.CTkLabel(
            card,
            text="98.2% delivery success rate",
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

        progress_bg.pack(fill="x", padx=18, pady=(18, 0))

        fill = ctk.CTkFrame(
            progress_bg,
            width=190,
            height=10,
            fg_color=THEME["success"],
            corner_radius=100
        )

        fill.place(x=0, y=0)

        # BUTTON

        btn = ctk.CTkButton(

            card,

            text="View Analytics",

            height=38,

            fg_color=THEME["primary"],
            hover_color=THEME["primary_hover"],

            corner_radius=10,

            text_color="white",

            font=("Segoe UI", 12, "bold")
        )

        btn.pack(fill="x", padx=18, pady=(18, 0))


    # ========================================================
    # PROFILE
    # ========================================================

    def create_profile(self):

        profile = ctk.CTkFrame(

            self,

            fg_color=THEME["sidebar_surface"],

            height=80,

            corner_radius=18,

            border_width=1,

            border_color="#1F2937"
        )

        profile.pack(fill="x", padx=18, pady=(8, 20))

        profile.pack_propagate(False)

        # AVATAR

        avatar = ctk.CTkFrame(

            profile,

            width=48,
            height=48,

            fg_color=THEME["primary"],

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
        ).place(x=78, y=18)

        ctk.CTkLabel(
            profile,
            text="System Administrator",
            text_color=THEME["text_muted"],
            font=("Segoe UI", 11)
        ).place(x=78, y=42)


# ============================================================
# MODERN NAVBAR
# ============================================================

class ModernNavbar(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(

            parent,

            height=88,

            fg_color=THEME["surface"],

            corner_radius=18,

            border_width=1,

            border_color=THEME["border"]
        )

        self.pack_propagate(False)

        self.create_left()
        self.create_right()


    # ========================================================
    # LEFT SECTION
    # ========================================================

    def create_left(self):

        left = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        left.place(x=24, rely=0.5, anchor="w")

        ctk.CTkLabel(
            left,
            text="Customer Notifications",
            text_color=THEME["text"],
            font=("Segoe UI", 26, "bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            left,
            text="Manage campaigns, notifications and analytics",
            text_color=THEME["text_secondary"],
            font=("Segoe UI", 12)
        ).pack(anchor="w", pady=(2, 0))


    # ========================================================
    # RIGHT SECTION
    # ========================================================

    def create_right(self):

        right = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        right.place(relx=0.98, rely=0.5, anchor="e")

        # SEARCH

        search = ctk.CTkEntry(

            right,

            width=260,
            height=42,

            corner_radius=12,

            fg_color=THEME["surface_2"],

            border_color=THEME["border"],

            placeholder_text="Search notifications...",

            font=("Segoe UI", 12)
        )

        search.pack(side="left", padx=8)

        # NOTIFICATION BUTTON

        notify = ctk.CTkButton(

            right,

            text="🔔",

            width=42,
            height=42,

            fg_color=THEME["surface_2"],
            hover_color="#E2E8F0",

            text_color=THEME["text"],

            corner_radius=12,

            border_width=1,
            border_color=THEME["border"]
        )

        notify.pack(side="left", padx=8)

        # CREATE BUTTON

        create = ctk.CTkButton(

            right,

            text="+ Create Notification",

            height=42,

            fg_color=THEME["primary"],
            hover_color=THEME["primary_hover"],

            text_color="white",

            corner_radius=12,

            font=("Segoe UI", 12, "bold")
        )

        create.pack(side="left", padx=8)


# ============================================================
# DEMO APP
# ============================================================

class App(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.geometry("1550x920")

        self.title("Customer Notifications Management")

        self.configure(fg_color=THEME["bg"])

        # GRID

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # SIDEBAR

        sidebar = ModernSidebar(self)
        sidebar.grid(row=0, column=0, sticky="ns")

        # MAIN AREA

        main = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        main.grid(row=0, column=1, sticky="nsew")

        # NAVBAR

        navbar = ModernNavbar(main)

        navbar.pack(
            fill="x",
            padx=24,
            pady=24
        )

        # SAMPLE CONTENT

        content = ctk.CTkFrame(

            main,

            fg_color=THEME["surface"],

            corner_radius=20,

            border_width=1,

            border_color=THEME["border"]
        )

        content.pack(
            fill="both",
            expand=True,
            padx=24,
            pady=(0, 24)
        )

        ctk.CTkLabel(
            content,
            text="Main Dashboard Content",
            text_color=THEME["text"],
            font=("Segoe UI", 28, "bold")
        ).place(relx=0.5, rely=0.5, anchor="center")


# ============================================================
# RUN
# ============================================================

app = App()
app.mainloop()