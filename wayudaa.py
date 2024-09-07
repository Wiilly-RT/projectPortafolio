import flet as ft

def main(page: ft.Page):
    def mostrar_login():
        page.controls.clear()

        user_input = ft.TextField(
            width=280,
            height=40,
            hint_text='username or mail address',
            border='underline',
            color='black',
            prefix_icon=ft.icons.EMAIL
        )

        password_input = ft.TextField(
            width=280,
            height=40,
            hint_text='Password',
            border='underline',
            color='black',
            prefix_icon=ft.icons.LOCK,
            password=True
        )

        def login_clicked(e):
            if user_input.value == "admin" and password_input.value == "123":
                mostrar_portafolio() 
            else:
                page.snack_bar = ft.SnackBar(ft.Text("Login incorrecto"))
                page.snack_bar.open = True
                page.update()
        
        login_button = ft.ElevatedButton(
            text='Sign in',
            width=280,
            on_click=login_clicked
        )
        
        # Contenedor del diseño de login
        conteiner = ft.Container(
            ft.Column([
                ft.Container(
                    ft.Text('Iniciar Sesión',
                            width=320,
                            size=30,
                            text_align='center', 
                            weight='w900'
                            ),
                    padding=ft.padding.only(20, 20)
                ),
                ft.Container(user_input, padding=ft.padding.only(20, 20)),
                ft.Container(password_input, padding=ft.padding.only(20, 20)),
                ft.Container(
                    ft.Checkbox(
                        label='Recordar contraseña',
                        check_color='black'
                    ),
                    padding=ft.padding.only(80)
                ),
                ft.Container(login_button, padding=ft.padding.only(20, 20))
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY),
            border_radius=20,
            width=320,
            height=500,
            gradient=ft.LinearGradient([
                ft.colors.DEEP_PURPLE,
                ft.colors.INDIGO,
                ft.colors.INDIGO,
                ft.colors.INDIGO,
                ft.colors.INDIGO,
                ft.colors.DEEP_PURPLE
            ])
        )
        
        page.add(conteiner)
        page.bgcolor = ft.colors.BLACK
        page.vertical_alignment= 'center'
        page.horizontal_alignment= 'center'
        page.update()  
    def mostrar_portafolio():
        page.controls.clear()
        # Tabs/Pestañas para navegación
        tabs = ft.Tabs(
            selected_index=1,
            animation_duration=300,
            tabs=[
                ft.Tab(
                    text="Inicio",
                    content=ft.Container(
                        content=ft.Text("This is 1"), alignment=ft.alignment.center
                    ),
                ),
                ft.Tab(
                    text="Skills",
                    content=ft.Container(
                        content=ft.Text("This is Tab 2"), alignment=ft.alignment.center
                    ),
                ),
                ft.Tab(
                    text="Experencia Laboral",
                    content=ft.Container(
                        content=ft.Text("This is Tab 3"), alignment=ft.alignment.center
                     ),
                ),
                ft.Tab(
                    text="Contacto",
                    content=ft.Container(
                        content=ft.Text("This is Tab 4"), alignment=ft.alignment.center
                    ),
                ),
            ],
            expand=1,
        )
        page.add(tabs)

    mostrar_login()  
if __name__ == '__main__':
    ft.app(target=main)