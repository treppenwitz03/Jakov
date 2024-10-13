import flet as ft

def start(page: ft.Page):
    page.window_width = 960
    page.window_height = 640

    page.controls = [ft.Text("Hello World")]
    page.update()