import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Row(
            controls=[
                ft.Image(
                    src='img/inicio.jpg',
                    width=150,
                    height=150
                ),
                ft.Image(
                    src='img/ubi.jpg',
                    width=150,
                    height=150
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    page.update()
    

if __name__ == '__main__':
    ft.app(target=main)


