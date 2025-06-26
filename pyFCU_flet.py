import flet as ft


class FletFCU(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page.title = 'Flet Experimental FCU'
        self.page.appbar = ft.AppBar(
            title = ft.Text('Flet FCU'),
            center_title=False,
            color=ft.Colors.WHITE,
            bgcolor=ft.Colors.PRIMARY,
            actions = [
                ft.IconButton(ft.Icons.WB_SHADE_OUTLINED),
                ft.IconButton(ft.Icons.FILTER_3)
            ]
        )
        self.page.bottom_appbar = ft.BottomAppBar(
            bgcolor=ft.Colors.WHITE,
            content=ft.Row(
                controls=[
                    ft.Text('Flet FCU'),
                ]
            )
        )
        menubar = ft.MenuBar(
            expand=True,
            style=ft.MenuStyle(
                alignment=ft.alignment.top_left,
                bgcolor=ft.Colors.GREY_100,
                mouse_cursor={
                    ft.ControlState.HOVERED: ft.MouseCursor.WAIT,
                    ft.ControlState.DEFAULT: ft.MouseCursor.ZOOM_OUT
                },
            ),
            controls=[
                ft.SubmenuButton(
                content=ft.Text("File"),
                    # on_open=handle_submenu_open,
                    # on_close=handle_submenu_close,
                    # on_hover=handle_submenu_hover,
                    controls=[
                        ft.MenuItemButton(
                            content=ft.Text("About"),
                            leading=ft.Icon(ft.Icons.INFO),
                            style=ft.ButtonStyle(
                                bgcolor={ft.ControlState.HOVERED: ft.Colors.GREEN_100}
                            ),
                        ),
                        ft.MenuItemButton(
                            content=ft.Text("Save"),
                            leading=ft.Icon(ft.Icons.SAVE),
                            style=ft.ButtonStyle(
                                bgcolor={ft.ControlState.HOVERED: ft.Colors.GREEN_100}
                            ),
                        ),
                        ft.MenuItemButton(
                            content=ft.Text("Quit"),
                            leading=ft.Icon(ft.Icons.CLOSE),
                            style=ft.ButtonStyle(
                                bgcolor={ft.ControlState.HOVERED: ft.Colors.GREEN_100}
                            ),
                        ),
                    ],
                ),
                ft.SubmenuButton(
                    content=ft.Text("View"),
                    controls=[
                        ft.MenuItemButton(
                            content=ft.Text("Nodes"),
                            leading=ft.Icon(ft.Icons.CLOSE),
                            style=ft.ButtonStyle(
                                bgcolor={ft.ControlState.HOVERED: ft.Colors.GREEN_100}
                            ),
                        ),
                        ft.MenuItemButton(
                            content=ft.Text("Events"),
                            leading=ft.Icon(ft.Icons.CLOSE),
                            style=ft.ButtonStyle(
                                bgcolor={ft.ControlState.HOVERED: ft.Colors.GREEN_100}
                            ),
                        ),
                    ],
                ),
            ],

        )
        self.page.add(ft.Row([menubar]))
        self.page.add(ft.Text("Body!"))


if __name__ == "__main__":
    def main(page: ft.Page):
        page.title = "Experimantal Fcu"
        page.padding = 0
        page.window_width = 850  # window's width is 200 px
        page.window_height = 850
        page.horizontal_alignment = ft.CrossAxisAlignment.START
        page.vertical_alignment = ft.MainAxisAlignment.START
        page.bgcolor = ft.Colors.BLUE_GREY_200
        app = FletFCU(page)
        page.add(app)
        page.update()


    ft.app(target=main)