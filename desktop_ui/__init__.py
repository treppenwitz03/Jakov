import flet as ft
from fletroute import Routing, path

from .LoginPage import LoginPage

async def start(page: ft.Page):
    page.window.maximized = True
    page.window.title_bar_hidden = True

    login_page = LoginPage(page)

    app_routes = [
        path(url="/", clear=True, view=login_page.get_view),
    ]

    Routing(page=page, app_routes=app_routes)
    page.go(page.route)