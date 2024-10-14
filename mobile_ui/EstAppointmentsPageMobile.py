import flet as ft
import flet.canvas as cv
import math
import platform
from .flet_map import FletMap

from fletroute import Params, Basket

class EstAppointmentsPage():
    dev_scale = 1
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

        ### FOR EASE OF DEVELOPMENT ONLY
        if platform.system() == "Windows":
            self.dev_scale = 0.5
        ###

        title_container = ft.Container(
            ft.Column([
                ft.Row([
                    ft.Text("Welcome, Name"),
                    ft.Image("./resources/logo.png", width=64 * self.dev_scale, height=64 * self.dev_scale, fit=ft.ImageFit.CONTAIN)
                ], alignment=ft.MainAxisAlignment.CENTER),
                ft.Text("Check and have your appointment right now.")
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            bgcolor="#dad9d6"
        )

        half_circle = cv.Canvas(
            [
                cv.Arc(
                    x = -540,
                    y = -50,
                    width=1080,
                    height=100,
                    start_angle=math.pi,
                    sweep_angle=-math.pi,
                    paint=ft.Paint(
                        style=ft.PaintingStyle.FILL,
                        color="#dad9d6"
                    )
                )
            ]
        )

        self.table = ft.Column([
            ft.Container(
                ft.Row([
                    ft.Container(
                        ft.Text("Mr. Soberano's Appointment"),
                        bgcolor="#dbefe1"
                    ),
                    ft.Container(
                        ft.Text("Status"),
                        bgcolor="#dbefe1"
                    )
                ]),
                bgcolor="f4f0ec"
            ),
            ft.Container(
                ft.Row([
                    ft.Container(
                        ft.Text("Mr. Soberano's Appointment"),
                        bgcolor="#dbefe1"
                    ),
                    ft.Container(
                        ft.Text("Status"),
                        bgcolor="#dbefe1"
                    )
                ]),
                bgcolor="f4f0ec"
            )
        ], spacing=20)

        self.navbottom = ft.Container(
            ft.Row([
                ft.IconButton(ft.icons.SCHEDULE_OUTLINED, on_click=self.tobook),
                ft.IconButton(ft.icons.HISTORY_OUTLINED),
                ft.IconButton(ft.icons.SETTINGS_OUTLINED)
            ]),
            bgcolor="#5b8485"
        )

        self.view = ft.View(
            route="/estappoints",
            controls=[
                ft.Container(
                    ft.Column([
                        title_container,
                    ]),
                    expand=True,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.bottom_center,
                        end=ft.Alignment(0.8, 1),
                        colors=[
                            "0xffcdffd8",
                            "0xff94b9ff",
                        ],
                        tile_mode=ft.GradientTileMode.MIRROR,
                    ),
                    expand_loose=True
                ),
                half_circle,
                self.table,
                self.navbottom

            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            padding=0,
            spacing=0,
            scroll=ft.ScrollMode.ADAPTIVE
        )
    
    def get_view(self, page: ft.Page, params: Params, basket: Basket):
        self.page = page
        return self.view
    
    def tobook(self, control: ft.ControlEvent):
        self.page.go("/clibook")
        self.page.update()