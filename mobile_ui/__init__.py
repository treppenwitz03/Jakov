import flet as ft
from fletroute import Routing, path

from .LoginPageMobile import LoginPage

async def start(page: ft.Page):
    page.window.width = 1080
    page.window.height = 960
    page.window.title_bar_hidden = True
    page.theme_mode = ft.ThemeMode.LIGHT

    login_page = LoginPage(page)

    app_routes = [
        path(url="/", clear=True, view=login_page.get_view),
    ]

    Routing(page=page, app_routes=app_routes)
    page.go(page.route)