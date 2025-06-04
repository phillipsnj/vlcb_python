import flet as ft


class FletFCU(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page


        self.page.appbar = ft.AppBar(
            title=ft.Text("Concept FCU Layout"),
            center_title=False,
            bgcolor=ft.Colors.SURFACE,
            actions=[
                ft.IconButton(ft.Icons.REFRESH),
                ft.IconButton(ft.Icons.FILTER_3),
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text="Item 1"),
                        ft.PopupMenuItem(),  # divider
                        ft.PopupMenuItem(
                            text="Checked item", checked=False
                        ),
                    ]
                ),
            ],
        )

        self.raw_tab = ft.Column(
            controls=[ft.Text("Raw Data")]
        )

        self.summary_tab = ft.Column(
            controls=[ft.Text("Summary Data")]
        )

        self.variables_tab = ft.Column(
            controls=[ft.Text("Variables")]
        )

        self.events_tab = ft.Column(
            controls=[ft.Text("Events")]
        )

        self.services_tab = ft.Column(
            controls=[ft.Text("services")]
        )

        self.node_details_tabs = ft.Tabs(
            selected_index=0,
            animation_duration=300,

            tabs=[
                ft.Tab(
                    text="Raw",
                    # content=ft.Container(
                    #     content=ft.Text("Raw Data"), alignment=ft.alignment.center
                    content=self.raw_tab
                ),
                ft.Tab(
                    text="Summary",
                    content=self.summary_tab
                ),
                ft.Tab(
                    text="Variables",
                    content=self.variables_tab
                ),
                ft.Tab(
                    text="Events",
                    content=self.events_tab
                ),
                ft.Tab(
                    text="Services",
                    content=self.services_tab,
                ),
            ],
            expand=1,
        )
        self.node_list_container = ft.Container(
            content=ft.Text('Node List'),
            width=500,
            height=300,
            margin=10,
            padding=10,
            bgcolor=ft.Colors.WHITE,
            border_radius=10,
            visible=True,
        )
        self.node_detail_container = ft.Container(
            content=self.node_details_tabs,
            width=500,
            height=300,
            margin=10,
            padding=10,
            bgcolor=ft.Colors.WHITE,
            border_radius=10,
            visible=True,
        )

        self.messages = ft.Container(
            content=ft.Text('Messages'),
            width=400,
            height=650,
            margin=10,
            padding=10,
            bgcolor=ft.Colors.WHITE,
            border_radius=10,
            visible=True,
        )

        self.main_row = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            controls=[
                ft.Column(
                    wrap=True,
                    scroll=ft.ScrollMode.AUTO,
                    controls=[
                        ft.Row(
                            controls=[
                                self.node_list_container
                            ],
                            scroll=ft.ScrollMode.AUTO
                        ),
                        ft.Row(
                            controls=[
                                self.node_detail_container
                            ],
                            scroll=ft.ScrollMode.AUTO
                        )
                    ]
                ),
                ft.Column(
                    wrap=True,
                    scroll=ft.ScrollMode.AUTO,
                    controls=[self.messages]

                )
            ]
        )

        self.page.add(self.main_row)


if __name__ == "__main__":
    def main(page: ft.Page):
        page.title = "Experimantal Fcu"
        page.padding = 0
        page.window.width = 1000  # window's width is 200 px
        page.window.height = 850
        page.horizontal_alignment = ft.CrossAxisAlignment.START
        page.vertical_alignment = ft.MainAxisAlignment.START
        page.bgcolor = ft.Colors.BLUE_GREY_200
        app = FletFCU(page)
        page.add(app)
        page.update()


    ft.app(target=main)
