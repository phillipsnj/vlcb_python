import flet as ft


def main(page: ft.Page) -> None:
    page.title = 'Increment Counter'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = 'light'

    text_number = ft.TextField(value='0', text_align=ft.TextAlign.RIGHT, width=100, data=0)

    def decrement(e) -> None:
        text_number.data -= 1
        text_number.value = str(text_number.data)
        page.update()

    def increment(e) -> None:
        text_number.data += 1
        text_number.value = str(text_number.data)
        page.update()

    page.add(
        ft.Row(
            controls=[
                ft.IconButton(ft.Icons.REMOVE, on_click=decrement),
                text_number,
                ft.IconButton(ft.Icons.ADD, on_click=increment)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


if __name__ == '__main__':
    ft.app(target=main)