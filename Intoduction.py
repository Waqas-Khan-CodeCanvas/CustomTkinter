"""
    Introduction of CustomTkinter :
        CustomTkinter is a python desktop UI-library based on Tkinter, which provides modern looking and fully customizable widgets. consistent look across all desktop platforms (Windows, macOS, Linux).

    installation of CustomTkinter:
        just open the cmd or teminal and run (pip install customtkinter)  


    Colors and Themes in CustomTkinter:
        - fg_color -> attribute used for forground color
        - bg_color -> attribute used for background color
        
        Colors can be:
            - simple string -> "red"
            - Hex string → "#FF0000"
            - Tuple →("light_mode_color""dark_mode_color")

        Built-in Themes:
            - Available: blue, green,dark-blue
            - ctk.set_default_color_theme("dark-blue")

        Custom Themes:
            ctk.set_default_color_theme("path/custom_theme.json")
            Use single colors for quick styling, themes for consistent design, and custom themes if you want full control.


        Appearance Mode in CustomTkinter:
            - Decides which color from a tuple will be used.
            - Example: fg_color = ("red", "darkred")
                * In light mode → "red"
                * In dark mode  → "darkred"
            - by using ctk.set_appearance_mode(arg) method (arg can be system , dark, light)
        Notes:
            - system → follows OS setting automatically.
            - If OS changes appearance (light/dark), app adapts too.
            - On Linux → "system" = always light mode (for now).



        Scaling & HighDPI:
        intro:
            - DPI = Dots Per Inch (how many pixels per inch of screen)
            - HighDPI = high-resolution displays (4K, Retina, etc.)
            - Problem: without scaling, apps look tiny or blurry
            - Solution: CustomTkinter auto-scales widgets & windows

        default:
            - On macOS → works automatically
            - On Windows → CustomTkinter makes the app DPI aware

        deactivate:
            customtkinter.deactivate_automatic_dpi_awareness()
            # disables scaling (not recommended, app may look blurry)

        custom scaling:
            - customtkinter.set_widget_scaling(1.2)   # scale widgets/text
            - customtkinter.set_window_scaling(1.5)   # scale window size


    Packaging (Windows .exe with PyInstaller / Auto Py to Exe):

        problem:
            - customtkinter has extra files (.json, .otf) besides .py
            - pyinstaller --onefile will not work
            - must use --onedir 
            - must manually include customtkinter folder (--add-data)

        steps:
            1. Find install path of customtkinter:
            pip show customtkinter
            # look at "Location", e.g.
            # C:/Users/<user>/AppData/Local/Programs/Python/Python310/Lib/site-packages

            2. Run pyinstaller with --add-data:
            pyinstaller --noconfirm --onedir --windowed ^
            --add-data "<path_to_site_packages>/customtkinter;customtkinter/" ^
            "<your_script>.py"

            3. Folder "dist" will contain the app + all dependencies.

        auto-py-to-exe:
            - GUI tool for pyinstaller
            - Add "customtkinter" folder manually in "Additional Files"
            - Same effect as --add-data option

        example:
            pyinstaller --noconfirm --onedir --windowed ^
            --add-data "C:/Users/Waqas/AppData/Local/Programs/Python/Python310/Lib/site-packages/customtkinter;customtkinter/" ^
            main.py
"""
