import flet as ft
import flet.canvas as cv
import math

from fletroute import Params, Basket

class LoginPage():
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page

        self.close_button = ft.IconButton(
            "close_outlined",
            "black",
            32,
            right=10,
            top=10,
            expand=True,
            on_click= lambda x: self.page.window.close()
        )

        self.login_cont = ft.Container(
            bgcolor="#dad9d6",
            expand=True,
            content=ft.Column(
                [
                    ft.Row([
                            ft.Text("Welcome to ", weight=ft.FontWeight.W_900, size=36),
                            ft.Image(f"./resources/logo.png", width=150, height=150, fit=ft.ImageFit.CONTAIN)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    ft.Text("Sign in to Continue", weight=ft.FontWeight.W_800, size=20),
                    ft.Text("Username", weight=ft.FontWeight.W_400, size=16, width=350),
                    ft.Row([
                            ft.Icon(ft.icons.CONTACT_MAIL_ROUNDED, size=32),
                            ft.TextField(hint_text="Enter your username...")
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    ft.Text("Password", weight=ft.FontWeight.W_400, size=16, width=350),
                    ft.Row([
                            ft.Icon(ft.icons.PASSWORD_ROUNDED, size=32),
                            ft.TextField(hint_text="Enter your password...", password=True, can_reveal_password=True)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    ft.Checkbox("I agree to the terms and conditions of JAKOV.", width=300),
                    ft.FilledButton("Sign in", icon_color="#abcbfb", width=300, height=64),
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
                begin=ft.alignment.top_left,
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
                    x = -200,
                    y = -20,
                    width=400,
                    height=900,
                    start_angle=1.57,
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
                ft.Row(
                    [
                        self.login_cont,
                        ft.Stack([
                            self.cont,
                            self.close_button,
                            self.half_circle], 
                            expand=True
                        )
                    ],
                    expand=True,
                    spacing=0
                )],
            padding=0
        )
    
    def get_view(self, page: ft.Page, params: Params, basket: Basket):
        self.page = page
        return self.view