import flet as ft

def main(page: ft.Page) -> None:
    page.fonts = {
        "Cascadia Mono": "fonts/CascadiaMono.ttf",
        "Cascadia Mono Italic": "fonts/CascadiaMonoItalic.ttf",
    }
    page.title = 'Garma'
    page.window_width = 400
    page.window_height = 800
    
    # Stores the views (pages)
    def route_change(e: ft.RouteChangeEvent) -> None:
        page.views.clear()
        
        # Home Page 
        page.views.append(
            ft.View(
                route='/',
                bgcolor='#0C2D48',
                controls=[
                    ft.SafeArea( 
                        ft.Container(
                            padding=10,  # Padding for better spacing
                            content=ft.Column(  # Main Column Container
                                controls=[
                                    ft.Row(  # The original Row
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        controls=[
                                            ft.Text('Welcome to Garma', color='#145DA0', font_family='Cascadia Mono', size=30),
                                            ft.IconButton(
                                                icon=ft.icons.SETTINGS_ROUNDED,
                                                icon_color='#B1D4E0',
                                                icon_size=30,
                                                on_click=lambda _: page.go('/settings')
                                            )
                                        ]
                                    ),
                                    ft.Divider(color='#B1D4E0'),  # Optional Separator
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Text('Available Sets:', color='#B1D4E0', font_family='Cascadia Mono', size=30)
                                        ]
                                    ),
                                    ft.Column(  # New Column Content
                                        controls=[
                                            # This is what shows the available sets 
                                            ft.Card(
                                                content=
                                                ft.Container(
                                                    bgcolor='#2E8BC0',
                                                    margin = ft.margin.all(10),
                                                    padding = ft.padding.all(10),
                                                    border_radius= ft.border_radius.all(10),
                                                    content=ft.Row(
                                                        controls=[
                                                            # Displays the set number
                                                            ft.Text('01', size=40, color='#B1D4E0', font_family='Cascadia Mono'),
                                                            ft.VerticalDivider(color='#B1D4E0'),
                                                            # Displays the name of the set
                                                            ft.Text('Filipino', size=30, color='#0C2D48', font_family='Cascadia Mono Italic'),
                                                            ft.IconButton(
                                                                icon=ft.icons.PLAY_ARROW_ROUNDED,
                                                                icon_color='#B1D4E0',
                                                                icon_size=40,
                                                                
                                                                on_click=lambda _: page.go('/quiz')
                                                            )
                                                        ],
                                                        
                                                    )
                                                ),
                                                color='#145DA0',
                                                width=400,
                                                height=100,
                                            )
                                        ],
                                        width=400,
                                        scroll=ft.ScrollMode.HIDDEN,
                                    ),
                                ],
                            ),               
                        ),
                    )
                ],
            )               
        )

        # Quiz Page
        if page.route == '/quiz':
            page.views.append(
                ft.View(
                    route='/',
                    bgcolor='#0C2D48',
                    controls=[
                        ft.SafeArea( 
                            ft.Container(
                                padding=10,  # Padding for better spacing
                                content=ft.Column(  # Main Column Container
                                    controls=[
                                        ft.Row(  # The original Row
                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                            controls=[
                                                ft.Text('Quiz', color='#145DA0', font_family='Cascadia Mono', size=30),
                                                ft.IconButton(
                                                    icon=ft.icons.ARROW_BACK_IOS_NEW_ROUNDED,
                                                    icon_color='#B1D4E0',
                                                    icon_size=30,
                                                    on_click=lambda _: page.go('/')
                                                )
                                            ]
                                        ),
                                        ft.Divider(color='#B1D4E0'),  # Optional Separator
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Text('[Question]', color='#B1D4E0', font_family='Cascadia Mono', size=30)
                                            ]
                                        ),
                                        ft.Column(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                # This is what shows the card
                                                ft.Card(
                                                    content=
                                                    ft.Container(
                                                        bgcolor='#2E8BC0',
                                                        margin = ft.margin.all(10),
                                                        padding = ft.padding.all(10),
                                                        border_radius= ft.border_radius.all(10),
                                                        content=ft.Row(
                                                            controls=[],
                                                        )
                                                    ),
                                                    color='#145DA0',
                                                    width=300,
                                                    height=300,
                                                )
                                            ],
                                        ),
                                    ],
                                ),               
                            ),
                        )
                    ],
                )               
            )
        
        # Learn Cards Page
        if page.route == '/learn':
            page.views.append(
                ft.View(
                    route='/',
                    bgcolor='#0C2D48',
                    controls=[
                        ft.SafeArea( 
                            ft.Container(
                                padding=10,  # Padding for better spacing
                                content=ft.Column(  # Main Column Container
                                    controls=[
                                        ft.Row(  # The original Row
                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                            controls=[
                                                ft.Text('Learn Cards', color='#145DA0', font_family='Cascadia Mono', size=30),
                                                ft.IconButton(
                                                    icon=ft.icons.ARROW_BACK_IOS_NEW_ROUNDED,
                                                    icon_color='#B1D4E0',
                                                    icon_size=30,
                                                    on_click=lambda _: page.go('/')
                                                )
                                            ]
                                        ),
                                        ft.Divider(color='#B1D4E0'),  # Optional Separator
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Text('[Question]', color='#B1D4E0', font_family='Cascadia Mono', size=30)
                                            ]
                                        ),
                                        ft.Column(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                # This is what shows the card
                                                ft.Card(
                                                    content=
                                                    ft.Container(
                                                        bgcolor='#2E8BC0',
                                                        margin = ft.margin.all(10),
                                                        padding = ft.padding.all(10),
                                                        border_radius= ft.border_radius.all(10),
                                                        content=ft.Row(
                                                            controls=[],
                                                        )
                                                    ),
                                                    color='#145DA0',
                                                    width=300,
                                                    height=300,
                                                )
                                            ],
                                        ),
                                    ],
                                ),               
                            ),
                        )
                    ],
                )               
            )

        # Settings Page
        if page.route == '/settings':
            page.views.append(
                ft.View(
                    route='/settings',
                    bgcolor='#0C2D48',
                    controls=[
                        ft.SafeArea( 
                            ft.Container(
                                padding=10,  # Padding for better spacing
                                # alignment=ft.alignment.center, 
                                content=ft.Column(  # Main Column Container
                                    controls=[
                                        ft.Row(  # The original Row
                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                            controls=[
                                                ft.Text('Settings', color='#145DA0', font_family='Cascadia Mono', size=30),
                                                ft.IconButton(
                                                    icon=ft.icons.ARROW_BACK_IOS_NEW_ROUNDED,
                                                    icon_color='#B1D4E0',
                                                    icon_size=30,
                                                    on_click=lambda _: page.go('/')
                                                )
                                            ],
                                        ),
                                        ft.Divider(color='#B1D4E0'),  # Optional Separator
                                        ft.Column(  # New Column Content
                                            controls=[
                                                ft.Card(
                                                    content=ft.Text("Content For the Card"),
                                                )
                                            ]
                                        )
                                    ],
                                ),               
                            ),
                        )
                    ],
                )               
            )
        
        page.update()
        
    def view_pop(e: ft.ViewPopEvent) -> None:
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
        
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go('/')
    
if __name__ == "__main__":
    ft.app(main)