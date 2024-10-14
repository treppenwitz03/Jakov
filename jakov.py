import flet as ft

import platform
import os
import sys

async def main(page: ft.Page):
    if platform.system() == "Windows" or platform.system() == "Linux" or platform.system() == "Darwin":
        if "iPhone" in platform.platform():
            import mobile_ui as ui
            await ui.start(page)
            return
        
        if sys.argv[1] == "-m": # TO EASE ANDROID DEVELOPMENT
            print("MOBILE MODE")
            import mobile_ui as ui
            await ui.start(page)

        import desktop_ui as ui
        await ui.start(page)

    else:
        if "android" in platform.system().lower() or os.path.isfile('/system/build.prop'):
            import mobile_ui as ui
            await ui.start(page)
            return
        
        print("Your Operating system is not currently supported by Yakov :<.")

ft.app(target=main)