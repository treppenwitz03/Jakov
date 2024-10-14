import flet as ft

import platform
import os
from os import environ
import sys

async def main(page: ft.Page):
    if 'ANDROID_ARGUMENT' in environ or 'ANDROID_BOOTLOGO' in environ:
        import mobile_ui as ui
        await ui.start(page)
        return

    elif platform.system() == "Windows" or platform.system() == "Linux" or platform.system() == "Darwin":
        if "iPhone" in platform.platform():
            import mobile_ui as ui
            await ui.start(page)
            return
        
        if len(sys.argv) > 1 and sys.argv[1] == "-m": # TO EASE ANDROID DEVELOPMENT
            print("MOBILE MODE")
            import mobile_ui as ui
            await ui.start(page)
            return

        import desktop_ui as ui
        await ui.start(page)

    else:
        print("Your Operating system is not currently supported by Yakov :<.")

ft.app(target=main)