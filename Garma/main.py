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
        
        # Answer field for Quiz
        def answer_field():
            return ft.TextField(
                border_color=ft.colors.TRANSPARENT,
                border_width=0,
                color='#0C2D48',
                cursor_color='#B1D4E0',
                hint_text=None,
                label='Answer here...',
                label_style=ft.TextStyle(color='#B1D4E0', font_family='Cascadia Mono'),
                text_size=20,
                width=230,
                text_style=ft.TextStyle(font_family='Cascadia Mono Italic'),
            )
               
        # Home Page 
        page.views.append(
            ft.View(
                route='/',
                bgcolor='#0C2D48',
                controls=[
                    ft.SafeArea( 
                        ft.Container(
                            padding=10,
                            content=ft.Column(
                                controls=[
                                    ft.Row(
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
                                    ft.Divider(color='#B1D4E0'),
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Text('Available Sets:', color='#B1D4E0', font_family='Cascadia Mono', size=30)
                                        ]
                                    ),
                                    ft.Column(
                                        alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            # This is what shows the available sets 
                                            ft.Card(
                                                content=
                                                ft.Container(
                                                    alignment=ft.alignment.center,
                                                    bgcolor='#2E8BC0',
                                                    margin = ft.margin.all(10),
                                                    padding = ft.padding.all(10),
                                                    border_radius= ft.border_radius.all(10),
                                                    content=ft.Row(
                                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
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
                                                                
                                                                on_click=lambda _: page.go('/choosemode')
                                                            )
                                                        ],
                                                        
                                                    )
                                                ),
                                                color='#145DA0',
                                                # width=400,
                                                height=100,
                                            )
                                        ],
                                        # width=400,
                                        scroll=ft.ScrollMode.HIDDEN,
                                    ),
                                ],
                            ),            
                        ),
                    )
                ],
            )               
        )

        # Choose Mode Page
        if page.route == '/choosemode':
            page.views.append(
                ft.View(
                    route='/choosemode',
                    bgcolor='#0C2D48',
                    controls=[
                        ft.SafeArea(
                            ft.Container(
                                padding=10,
                                content=ft.Column(
                                    controls=[
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                            controls=[
                                                ft.Text('Choose Mode', color='#145DA0', font_family='Cascadia Mono', size=30),
                                                ft.IconButton(
                                                    icon=ft.icons.ARROW_BACK_IOS_NEW_ROUNDED,
                                                    icon_color='#B1D4E0',
                                                    icon_size=30,
                                                    on_click=lambda _: page.go('/')
                                                )
                                            ]
                                        ),
                                        ft.Divider(color='#B1D4E0'),
                                        ft.Column(
                                            controls=[
                                                ft.Row(
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.Card(
                                                            ft.ElevatedButton(
                                                                'Learn Cards',
                                                                bgcolor=('#B1D4E0'),
                                                                on_click=lambda _: page.go('/learn'),
                                                                elevation=0,
                                                                color=('#0C2D48'),
                                                                ),
                                                            color=('#B1D4E0'),
                                                            # width=190,
                                                            height=60,
                                                        ),
                                                        ft.Card(
                                                            ft.ElevatedButton(
                                                                'Quiz Mode',
                                                                bgcolor=('#B1D4E0'),
                                                                on_click=lambda _: page.go('/quiz'),
                                                                elevation=0,
                                                                color=('#0C2D48'),
                                                                ),
                                                            color=('#B1D4E0'),
                                                            # width=190,
                                                            height=60,
                                                        ),
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        )
                    ],
                    vertical_alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.MainAxisAlignment.CENTER
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
                                alignment = ft.alignment.center,
                                padding=10,
                                content=ft.Column(
                                    controls=[
                                        ft.Row(
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
                                        ft.Divider(color='#B1D4E0'),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Text('[Question]', color='#B1D4E0', font_family='Cascadia Mono', size=30)
                                            ]
                                        ),
                                        ft.Column(
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                # This is what shows the card
                                                ft.Card(
                                                    content=
                                                    ft.Container(
                                                        padding=10,
                                                        content=ft.Image(
                                                            src='https://placekitten.com/400/400',
                                                            border_radius=ft.border_radius.all(10)
                                                        )
                                                    ),
                                                    color='#145DA0',
                                                    width=400,
                                                    height=300,
                                                )
                                            ],
                                        ),
                                        ft.Column(
                                            
                                            controls=[
                                                ft.Card(
                                                    content=
                                                    ft.Container(
                                                        bgcolor='#2E8BC0',
                                                        margin = ft.margin.all(10),
                                                        padding = ft.padding.all(10),
                                                        border_radius= ft.border_radius.all(10),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                            controls=[
                                                                # Answer field
                                                                answer_field(),
                                                                ft.VerticalDivider(color='#B1D4E0'),
                                                                # Submit answer Button
                                                                ft.IconButton(
                                                                    icon=ft.icons.CHECK_CIRCLE_ROUNDED,
                                                                    icon_color='#B1D4E0',
                                                                    icon_size=30,
                                                                    on_click=None
                                                                )
                                                            ],
                                                            
                                                        )
                                                    ),
                                                    color='#145DA0',
                                                    # width=400,
                                                    height=100,
                                                )
                                            ],
                                            # width=400,
                                            scroll=ft.ScrollMode.HIDDEN,
                                        ),
                                    ],
                                ),               
                            ),
                        )
                    ],
                    vertical_alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.MainAxisAlignment.CENTER
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
                                padding=10,
                                content=ft.Column(
                                    controls=[
                                        ft.Row(
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
                                        ft.Divider(color='#B1D4E0'),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Text('[Question]', color='#B1D4E0', font_family='Cascadia Mono', size=30)
                                            ]
                                        ),
                                        ft.Column(
                                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                            controls=[
                                                ft.Card(
                                                    content=
                                                    ft.Container(
                                                        padding=10,
                                                        content=ft.Image(
                                                            src='https://placekitten.com/300/300',
                                                            border_radius=ft.border_radius.all(10),
                                                        )
                                                    ),
                                                    color='#145DA0',
                                                    # width=300,
                                                    # height=300,
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

        # Create Sets Page

        # Settings Page
        if page.route == '/settings':
            page.views.append(
                ft.View(
                    route='/settings',
                    bgcolor='#0C2D48',
                    controls=[
                        ft.SafeArea( 
                            ft.Container(
                                padding=10,
                                content=ft.Column(
                                    controls=[
                                        ft.Row(
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
                                        ft.Divider(color='#B1D4E0'),
                                        ft.Column(
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
                    vertical_alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.MainAxisAlignment.CENTER
                )               
            )
        
        page.update()
        
    def view_pop(e: ft.ViewPopEvent) -> None:
        page.views.pop()
        top_view: ft.View = page.views[-1]
        page.go(top_view.route)
        
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    
if __name__ == "__main__":
    ft.app(main)
