import flet as ft

import platform
import os

def main(page: ft.Page):
    if platform.system() == "Windows" or platform.system() == "Linux" or platform.system() == "Darwin":
        if "iPhone" in platform.platform():
            import mobile_ui as ui
            ui.start(page)
            return

        import desktop_ui as ui
        ui.start(page)

    else:
        if "android" in platform.system().lower() or os.path.isfile('/system/build.prop'):
            import mobile_ui as ui
            ui.start(page)
            return
        
        print("Your Operating system is not currently supported by Yakov :<.")

ft.app(target=main)