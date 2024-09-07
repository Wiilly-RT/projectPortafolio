import flet as ft

def main(page: ft.Page):
    # Crea un contenedor para la imagen
    img_container = ft.Container(
        content=ft.Image(src="img/araña.png", fit=ft.ImageFit.COVER),  # Carga la imagen directamente
        width=100,  # Ajusta el tamaño según necesites
        height=100,  # Ajusta el tamaño según necesites
        border_radius=50,  # Esto hace que la imagen sea circular si el width y height son iguales
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS
    )

    # Agrega el contenedor a la página
    page.add(img_container)

# Llama a la función main para ejecutar la aplicación
ft.app(target=main)



# Opciones de Alineación en Flet
# Flet utiliza diferentes valores para la alineación, y estos valores son generalmente más explícitos. Los valores comunes son:

# ft.Alignment.top_left
# ft.Alignment.top_center
# ft.Alignment.top_right
# ft.Alignment.center_left
# ft.Alignment.center
# ft.Alignment.center_right
# ft.Alignment.bottom_left
# ft.Alignment.bottom_center
# ft.Alignment.bottom_right