import flet as ft

def main(page: ft.Page):
    def mostrar_login():
        # Lógica del login
        # Si el login es exitoso, llamar a mostrar_portafolio
        pass

    def mostrar_portafolio():
        page.controls.clear()
        
        # Pestañas de navegación
        tabs = ft.Tabs(
            selected_index=0,
            tabs=[
                ft.Tab(text="Inicio", content=mostrar_inicio()),
                ft.Tab(text="Skills", content=mostrar_skills()),
                ft.Tab(text="Experiencia Laboral", content=mostrar_experiencia_laboral()),
                ft.Tab(text="Contacto", content=mostrar_contacto()),
            ],
            expand=1,
        )

        # Botón de Cerrar Sesión
        logout_button = ft.IconButton(
            icon=ft.icons.EXIT_TO_APP,
            on_click=lambda _: mostrar_login()
        )
        
        page.add(tabs, logout_button)
        page.update()

    def mostrar_inicio():
        # Lógica y contenido de la pestaña "Inicio"
        return ft.Text("Contenido de Inicio")

    def mostrar_skills():
        # Lógica y contenido de la pestaña "Skills"
        return ft.Text("Contenido de Skills")

    def mostrar_experiencia_laboral():
        # Lógica y contenido de la pestaña "Experiencia Laboral"
        return ft.Text("Contenido de Experiencia Laboral")

    def mostrar_contacto():
        # Lógica y contenido de la pestaña "Contacto"
        return ft.Text("Contenido de Contacto")

    mostrar_login()  # Mostrar la pantalla de login al iniciar

if __name__ == '__main__':
    ft.app(target=main)
