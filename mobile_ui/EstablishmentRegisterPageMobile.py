import flet as ft
import flet.canvas as cv
import math
import platform

from fletroute import Params, Basket

class EstablishmentRegisterPage():
    dev_scale = 1
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

        ### FOR EASE OF DEVELOPMENT ONLY
        if platform.system() == "Windows":
            self.dev_scale = 0.5
        ###

        title_container = ft.Container(
            ft.Row([
                ft.Image("./resources/logo.png", width=64 * self.dev_scale, height=64 * self.dev_scale, fit=ft.ImageFit.CONTAIN),
                ft.Image("./resources/establishment.png", width=64 * self.dev_scale, height=64 * self.dev_scale, fit=ft.ImageFit.CONTAIN)
            ], alignment=ft.MainAxisAlignment.CENTER),
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

        self.view = ft.View(
            route="/estreg",
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
                ft.Text("Create your Account"),
                ft.Row([
                    ft.Icon(ft.icons.STOREFRONT_OUTLINED, size=48),
                    ft.TextField(hint_text="Company/Building Name", width=250)
                ]),
                ft.Row([
                    ft.Icon(ft.icons.MAPS_HOME_WORK_OUTLINED, size=48),
                    ft.TextField(hint_text="Address", width=250)
                ]),
                ft.Row([
                    ft.Icon(ft.icons.EMAIL_OUTLINED, size=48),
                    ft.TextField(hint_text="Email", width=250)
                ]),
                ft.Row([
                    ft.Icon(ft.icons.PASSWORD_OUTLINED, size=48),
                    ft.TextField(hint_text="Password", width=250)
                ]),
                ft.Row([
                    ft.Icon(ft.icons.PASSWORD_OUTLINED, size=48),
                    ft.TextField(hint_text="Confirm Password", width=250)
                ]),
                ft.ElevatedButton("Register", width=250, height=64)
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            padding=0,
            spacing=0,
            scroll=ft.ScrollMode.ADAPTIVE
        )
    
    def get_view(self, page: ft.Page, params: Params, basket: Basket):
        self.page = page
        return self.view