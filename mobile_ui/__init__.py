import flet as ft
from fletroute import Routing, path

from .LoginPageMobile import LoginPage
from .ChoicePageMobile import ChoicePage
from .ClientRegisterPageMobile import ClientRegisterPage
from .EstablishmentRegisterPageMobile import EstablishmentRegisterPage
from .ClientBookPageMobile import ClientBookPage
from .ClientHistoryPageMobile import ClientHistoryPage
from .EstAppointmentsPageMobile import EstAppointmentsPage

async def start(page: ft.Page):
    page.window.width = 1080
    page.window.height = 960
    page.window.title_bar_hidden = True
    page.theme_mode = ft.ThemeMode.LIGHT

    login_page = LoginPage(page)
    choice_page = ChoicePage(page)
    client_register_page = ClientRegisterPage(page)
    establishment_register_page = EstablishmentRegisterPage(page)
    client_book_page = ClientBookPage(page)
    client_history_page = ClientHistoryPage(page)
    establishment_appointments_page = EstAppointmentsPage(page)

    app_routes = [
        path(url="/", clear=True, view=login_page.get_view),
        path(url="/choice", clear=True, view=choice_page.get_view),
        path(url="/clireg", clear=True, view=client_register_page.get_view),
        path(url="/estreg", clear=True, view=establishment_register_page.get_view),
        path(url="/clibook", clear=True, view=client_book_page.get_view),
        path(url="/clihist", clear=True, view=client_history_page.get_view),
        path(url="/estappoints", clear=True, view=establishment_appointments_page.get_view)
    ]

    Routing(page=page, app_routes=app_routes)
    page.go(page.route)