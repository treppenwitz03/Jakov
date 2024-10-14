import flet as ft
import flet.canvas as cv
import math
import platform

from fletroute import Params, Basket

class ChoicePage():
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
                ft.Column(
                    [
                        ft.Text("A Special Help Appointment System", size=24 * self.dev_scale),
                        ft.Text("Connecting Clients to the Establishments for Accessible Assistance", size=16 * self.dev_scale)
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ], alignment=ft.MainAxisAlignment.CENTER),
            bgcolor="#dad9d6"
        )

        self.client_button = ft.Container(
            ft.Column([
                ft.Image("./resources/client.png", width=100 * self.dev_scale, height=100 * self.dev_scale, fit=ft.ImageFit.CONTAIN),
                ft.Text("Create an account as a Client", text_align=ft.TextAlign.CENTER)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            width=300 * self.dev_scale,
            height=300 * self.dev_scale
        )

        self.establishment_button = ft.Container(
            ft.Column([
                ft.Image("./resources/establishment.png", width=100 * self.dev_scale, height=100 * self.dev_scale, fit=ft.ImageFit.CONTAIN),
                ft.Text("Create an account as an Establishment", text_align=ft.TextAlign.CENTER)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            width=300 * self.dev_scale,
            height=300 * self.dev_scale
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
            route="/choice",
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
                self.client_button,
                self.establishment_button
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            padding=0,
            spacing=0,
            scroll=ft.ScrollMode.ADAPTIVE
        )
    
    def get_view(self, page: ft.Page, params: Params, basket: Basket):
        self.page = page
        return self.view