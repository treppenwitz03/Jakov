import flet as ft
import flet.canvas as cv
import math

from fletroute import Params, Basket

class LoginPage():
    dev_scale = 1
    def __init__(self, page: ft.Page):
        super().__init__()

        ### FOR EASE OF DEVELOPMENT ONLY
        import platform
        if platform.system() == "Windows":
            self.dev_scale = 0.7
        ###

        self.page = page

        self.login_cont = ft.Container(
            bgcolor="#dad9d6",
            expand=True,
            content=ft.Column(
                [
                    ft.Row([
                            ft.Text("Welcome to ", weight=ft.FontWeight.W_900, size=36 * self.dev_scale),
                            ft.Image(f"./resources/logo.png", width=150 * self.dev_scale, height=150 * self.dev_scale, fit=ft.ImageFit.CONTAIN)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    ft.Text("Sign in to Continue", weight=ft.FontWeight.W_800, size=20 * self.dev_scale),
                    ft.Text("Username", weight=ft.FontWeight.W_400, size=16 * self.dev_scale, width=350 * self.dev_scale),
                    ft.Row([
                            ft.Icon(ft.icons.CONTACT_MAIL_ROUNDED, size=32 * self.dev_scale),
                            ft.TextField(hint_text="Enter your username...")
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    ft.Text("Password", weight=ft.FontWeight.W_400, size=16 * self.dev_scale, width=350 * self.dev_scale),
                    ft.Row([
                            ft.Icon(ft.icons.PASSWORD_ROUNDED, size=32 * self.dev_scale),
                            ft.TextField(hint_text="Enter your password...", password=True, can_reveal_password=True)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    ft.Checkbox("I agree to the terms and conditions of JAKOV.", width=300 * self.dev_scale),
                    ft.FilledButton("Sign in", icon_color="#abcbfb", width=300 * self.dev_scale, height=64 * self.dev_scale),
                    ft.TextButton("Don't have an Account? Create One")
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=30
            )
        )

        self.cont = ft.Container(
            alignment=ft.alignment.center,
            expand=True,
            gradient=ft.LinearGradient(
                begin=ft.alignment.bottom_center,
                end=ft.Alignment(0.8, 1),
                colors=[
                    "0xffcdffd8",
                    "0xff94b9ff",
                ],
                tile_mode=ft.GradientTileMode.MIRROR,
            )
        )

        self.half_circle = cv.Canvas(
            [
                cv.Arc(
                    x = 0,
                    y = 400,
                    width=1080,
                    height=100,
                    start_angle=0,
                    sweep_angle=-math.pi,
                    paint=ft.Paint(
                        style=ft.PaintingStyle.FILL,
                        color="#dad9d6"
                    )
                )
            ]
        )

        self.view = ft.View(
            route="/",
            controls=[
                ft.Stack([
                    self.cont,
                    self.half_circle], 
                    height=300*self.dev_scale
                ),
                self.login_cont
            ],
            padding=0,
            spacing=0
        )
    
    def get_view(self, page: ft.Page, params: Params, basket: Basket):
        self.page = page
        return self.view