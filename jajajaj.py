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

        img_container = ft.Container(
            content=ft.Image(src="img/araña.png", fit=ft.ImageFit.COVER),
            width=100,
            height=100,
            border_radius=50,
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS
        )

        name_text = ft.Text("Wilfredo Rojas", size=24, weight=ft.FontWeight.BOLD)
        description_text = ft.Text("Estudiante", size=18)

        def cerrar_sesion(e):
            mostrar_login()  # Vuelve a mostrar la vista de inicio de sesión
        
        logout_button = ft.IconButton(
            icon=ft.icons.LOGOUT,
            tooltip="Cerrar sesión",
            on_click=cerrar_sesion  # Llama a la función de cerrar sesión
        )

        tabs = ft.Tabs(
            selected_index=0,
            tabs=[
                ft.Tab(text="Inicio", content=ft.Text("Esta es la sección de inicio")),
                ft.Tab(text="Skills", content=ft.Text("Esta es la sección de Skills")),
                ft.Tab(text="Experiencia Laboral", content=ft.Text("Esta es la sección de Experiencia Laboral")),
                ft.Tab(text="Contacto", content=ft.Text("Esta es la sección de Contacto")),
            ]
        )

        portafolio_container = ft.Container(
            ft.Column([
                ft.Row([logout_button], alignment=ft.MainAxisAlignment.END),
                ft.Container(
                    img_container,
                    alignment=ft.alignment.center
                ),
                ft.Container(
                    name_text,
                    alignment=ft.alignment.center
                ),
                ft.Container(
                    description_text,
                    alignment=ft.alignment.center
                ),
                tabs
            ],
            spacing=20),
            padding=20
        )

        page.add(portafolio_container)
        page.bgcolor = ft.colors.BLACK
        page.update()
    
    mostrar_login()  
    
if __name__ == '__main__':
    ft.app(target=main)
