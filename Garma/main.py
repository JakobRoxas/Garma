import flet as ft
from assets import sets

current_set = None
current_card_index = 0
question_value = ft.Text(value='This should be a question...', color='#B1D4E0', font_family='Cascadia Mono', size=20, width=300, text_align=ft.TextAlign.CENTER, no_wrap=False)
front_image_source = ft.Image(src=f'/images/garma.jpg', fit=ft.ImageFit.SCALE_DOWN, border_radius=ft.border_radius.all(10))
score_image = ft.Image(src=f'/images/garma.jpg', fit=ft.ImageFit.SCALE_DOWN, border_radius=ft.border_radius.all(10))
current_set_name = None
correctly_answered = []
incorrectly_answered = []
leitner_system_state = False
switch_value = False

def main(page: ft.Page) -> None: 
    page.fonts = {
        "Cascadia Mono": "fonts/CascadiaMono.ttf",
        "Cascadia Mono Italic": "fonts/CascadiaMonoItalic.ttf",
    }
    page.title = 'Garma'
    page.window_width = 400
    page.window_height = 800
    
    
    # Retrieves and stores the set names from the sets.py file
    set_names = [name for name, value in sets.__dict__.items() if isinstance(value, list)]
   
    # Creates cards that display the set name
    def provide_set_cards(): 
        controls = []
        for set_name in set_names:
             controls.append(ft.Card(
                content=ft.Container(
                    alignment=ft.alignment.center,
                    bgcolor='#2E8BC0',
                    margin=ft.margin.all(10),
                    padding=ft.padding.all(10),
                    border_radius=ft.border_radius.all(10),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.START,
                        controls=[

                            ft.IconButton(icon=ft.icons.PLAY_ARROW_ROUNDED, icon_color='#B1D4E0', icon_size=40, on_click=lambda _, set_name=set_name: [assign_current_set(set_name), page.go('/choosemode')]),
                            ft.VerticalDivider(color='#B1D4E0'),
                            ft.Text(set_name, size=30, color='#0C2D48', font_family='Cascadia Mono Italic'),
                        ],
                    )
                ),
                color='#145DA0',
                height=100,
            )
        )
        return controls
   
    # Creates TextFields
    def create_text_field(label, hint_text=None):
        return ft.TextField(
            border_color=ft.colors.TRANSPARENT,
            border_width=0,
            color='#0C2D48',
            cursor_color='#B1D4E0',
            hint_text=hint_text,
            label=label,
            label_style=ft.TextStyle(color='#B1D4E0', font_family='Cascadia Mono'),
            text_size=20,
            width=230,
            text_style=ft.TextStyle(font_family='Cascadia Mono Italic')
        )
   
   # Assigns the current set and card index
    def assign_current_set(set_name):
        global current_set, current_card_index, current_set_name
        current_set_name = set_name
        current_set = sets.__dict__[set_name]
        current_card_index = 0  # Reset index when changing set
        provide_question()  # Show the first card's question 
        provide_front_image() 
        print(f'Current set: {current_set}')
    
    # Provides the question of the current card
    def provide_question():
        global current_set, current_card_index
        if current_set and current_card_index < len(current_set):
            question = current_set[current_card_index]['question']
        else:
            question = 'There are no more questions in this set...and you should not be seeing this...'
        question_value.value = question

    # Provides the front image of the current card
    def provide_front_image():
        global current_set, current_card_index, front_image_source
        if current_set and current_card_index < len(current_set):
            front_image = current_set[current_card_index]['front_image']
        else:
            print('Something went wrong, and we don\'t know why...')
        front_image_source.src = front_image
    
    # Submits the quiz answer, checks if it's correct then updates the controls
    def submit_quiz_answer():
        global current_set, current_card_index, score_image, leitner_system_state
        answer = quiz_answer_field.value
        if current_set and current_card_index < len(current_set):  # Check for index within bounds
            if answer == current_set[current_card_index]['answer'].lower():
                print('Correct')
                correctly_answered.append(current_set[current_card_index])
            else:
                print('Incorrect')
                incorrectly_answered.append(current_set[current_card_index])
                if leitner_system_state and len(incorrectly_answered) >= len(current_set) / 3:  # Check if Leitner system is enabled and a third of the set is answered incorrectly
                    current_set.append(current_set[current_card_index])  # Add incorrectly answered question back to the set
        else:
            print("End of set!")  # Notify when the set is finished

        if len(correctly_answered) / len(current_set) * 100 >= 50:
            score_image.src = f'/images/good_score.jpg'
        else:
            score_image.src = f'/images/bad_score.jpg' 

        quiz_answer_field.value = ''
        current_card_index += 1  # Increment index (if we haven't reached the end)
        if current_card_index >= len(current_set):
            if leitner_system_state:
                page.go('/')
            else:
                page.go('/scorepage')
        else:
            provide_question()
            provide_front_image()
        page.update()

    # Redo the quiz
    def redo_quiz():
        global current_set, current_card_index, correctly_answered, incorrectly_answered
        current_card_index = 0
        correctly_answered = []
        incorrectly_answered = []
        provide_question()
        provide_front_image()
        page.go('/quiz')
        page.update()

    # Redo the learn mode
    def redo_learn():
        global current_set, current_card_index
        current_card_index = 0
        provide_question()
        provide_front_image()
        page.go('/learn')
        page.update()

    # Submits the set name
    def submit_set_name():
        set_name = set_name_field.value
        print(f'A set named {set_name} has been created.')

        set_name_field.disabled = True
        page.update()
     
    # Saves the set       
    def done_clicked():
        page.go('/')
        print('Done clicked')
    
    # adds a card to the set        
    def add_card():
        question = card_question_field.value
        answer = card_answer_field.value
        front_image = front_image_field.value
        back_image = back_image_field.value
            
        # Input Validation
        if not all([question, answer, front_image, back_image]):
            # Display an error message or indication to the user
            print('Please fill in all fields.')
            return
            
        # Clear text fields
        for field in [card_question_field, card_answer_field, front_image_field, back_image_field]:
            field.value = ''
            
        # log the card to the console
        print(f'Card added: {question}, {answer}, {front_image}, {back_image}')
        page.update()
        
    # Flip card (learn)
    def flip_card():
        global front_image_source, current_set, current_card_index, question_value

        if current_set and current_card_index < len(current_set):
            card = current_set[current_card_index]

            # Image Toggle
            if front_image_source.src == card['front_image']:
                front_image_source.src = card['back_image']
            else:
                front_image_source.src = card['front_image']

            # Question/Answer Toggle
            if question_value.value == card['question']:
                question_value.value = card['answer']
            else:
                question_value.value = card['question']

            page.update()     
       
    # Change Leitner System State
    def change_leitner_system_state():
        global leitner_system_state
        leitner_system_state = not leitner_system_state
        print (f'Leitner system state: {leitner_system_state}')
    
    # Next card (learn)
    def next_card():
        global current_set, current_card_index
        if current_set and current_card_index < len(current_set):
            current_card_index += 1
            if current_card_index >= len(current_set):
                page.go('/setcomplete')
            else:
                provide_question()
                provide_front_image() 
                page.update() 
        else:
            print("There are no more cards in the set.")

    # Previous card (learn)
    def previous_card():
        global current_set, current_card_index
        if current_set and current_card_index < len(current_set):
            current_card_index -= 1
            if current_card_index < 0:
                current_card_index = 0
            else:
                provide_question()
                provide_front_image() 
                page.update() 
        else:
            print("There are no more cards in the set.")

    # TextFields
    card_question_field = create_text_field('Question...')
    card_answer_field = create_text_field('Answer...')
    front_image_field = create_text_field('Front image...')
    back_image_field = create_text_field('Back image...')
    set_name_field = create_text_field('Set name...')
    quiz_answer_field = create_text_field('Answer...')

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
                            padding=10,
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        controls=[
                                            ft.IconButton(
                                                icon=ft.icons.SETTINGS_ROUNDED,
                                                icon_color='#B1D4E0',
                                                icon_size=30,
                                                on_click=lambda _: page.go('/settings')
                                            ),
                                            ft.Text('Welcome to Garma', color='#145DA0', font_family='Cascadia Mono', size=30),
                                            ft.IconButton(
                                                icon=ft.icons.ADD_CIRCLE_ROUNDED,
                                                icon_color='#B1D4E0',
                                                icon_size=30,
                                                on_click=lambda _: page.go('/createset')
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
                                        *[provide_set_cards()],
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
                                                ft.Text(current_set_name, color='#145DA0', font_family='Cascadia Mono', size=30),
                                                ft.IconButton(
                                                    icon=ft.icons.ARROW_CIRCLE_LEFT_ROUNDED,
                                                    icon_color='#B1D4E0',
                                                    icon_size=30,
                                                    on_click=lambda _: page.go('/')
                                                )
                                            ]
                                        ),
                                        ft.Divider(color='#B1D4E0'),
                                        ft.Column(
                                            controls=[
                                                ft.Column(
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.Card(
                                                            content=ft.Container(
                                                                alignment=ft.alignment.center,
                                                                bgcolor='#2E8BC0',
                                                                margin=ft.margin.all(10),
                                                                padding=ft.padding.all(10),
                                                                border_radius=ft.border_radius.all(10),
                                                                content=ft.Row(
                                                                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                        controls=[
                                                                        ft.Text('quiz ', size=30, color='#0C2D48', font_family='Cascadia Mono Italic'),
                                                                        ft.VerticalDivider(color='#B1D4E0'),
                                                                        ft.IconButton(icon=ft.icons.PLAY_ARROW_ROUNDED, icon_color='#B1D4E0', icon_size=40, on_click=lambda _: page.go('/quiz')),
                                                                        ],
                                                                    )
                                                                ),
                                                                color='#145DA0',
                                                                height=100,
                                                            ),
                                                        ft.Card(
                                                        content=ft.Container(
                                                            alignment=ft.alignment.center,
                                                            bgcolor='#2E8BC0',
                                                            margin=ft.margin.all(10),
                                                            padding=ft.padding.all(10),
                                                            border_radius=ft.border_radius.all(10),
                                                            content=ft.Row(
                                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                    controls=[
                                                                        ft.Text('learn', size=30, color='#0C2D48', font_family='Cascadia Mono Italic'),
                                                                        ft.VerticalDivider(color='#B1D4E0'),
                                                                        ft.IconButton(icon=ft.icons.PLAY_ARROW_ROUNDED, icon_color='#B1D4E0', icon_size=40, on_click=lambda _: page.go('/learn')),
                                                                    ],
                                                                )
                                                            ),
                                                            color='#145DA0',
                                                            height=100,
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
                ),
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
                                                ft.Text(f'Quiz on {current_set_name}', color='#145DA0', font_family='Cascadia Mono', size=30),
                                                ft.IconButton(
                                                    icon=ft.icons.ARROW_CIRCLE_LEFT_ROUNDED,
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
                                                question_value
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
                                                        content=front_image_source,
                                                    ),
                                                    color='#145DA0',
                                                    width=370,
                                                    height=370,
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
                                                                quiz_answer_field,
                                                                ft.VerticalDivider(color='#B1D4E0'),
                                                                # Submit answer Button
                                                                ft.IconButton(
                                                                    icon=ft.icons.CHECK_CIRCLE_ROUNDED,
                                                                    icon_color='#B1D4E0',
                                                                    icon_size=30,
                                                                    on_click=lambda _: submit_quiz_answer()
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
                    route='/learn',
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
                                                ft.Text(f'Learn {current_set_name}', color='#145DA0', font_family='Cascadia Mono', size=30),
                                                ft.IconButton(
                                                    icon=ft.icons.ARROW_CIRCLE_LEFT_ROUNDED,
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
                                                question_value
                                            ]
                                        ),
                                        ft.Column(
                                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                            controls=[
                                                ft.Card(
                                                    content=
                                                    ft.Container(
                                                        padding=10,
                                                        content=front_image_source,
                                                    ),
                                                    color='#145DA0',
                                                    width=370,
                                                    height=370,
                                                )
                                            ],
                                        ),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                            controls=[
                                                 ft.IconButton(
                                                    icon=ft.icons.ARROW_LEFT_ROUNDED,
                                                    icon_color='#B1D4E0',
                                                    icon_size=50,
                                                    on_click=lambda _: previous_card()
                                                ),
                                                ft.IconButton(
                                                    icon=ft.icons.COMPARE_ARROWS_ROUNDED,
                                                    icon_color='#B1D4E0',
                                                    icon_size=50,
                                                    on_click=lambda _: flip_card()
                                                ),
                                                ft.IconButton(
                                                    icon=ft.icons.ARROW_RIGHT_ROUNDED,
                                                    icon_color='#B1D4E0',
                                                    icon_size=50,
                                                    on_click=lambda _: next_card()
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
        
        # Create Sets Page
        if page.route == '/createset':
            page.views.append(
                ft.View(
                    route='/createset',
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
                                                ft.Text('Create Set', color='#145DA0', font_family='Cascadia Mono', size=30),
                                                ft.IconButton(
                                                    icon=ft.icons.ARROW_CIRCLE_LEFT_ROUNDED,
                                                    icon_color='#B1D4E0',
                                                    icon_size=30,
                                                    on_click=lambda _: page.go('/')
                                                )
                                            ]
                                        ),
                                        ft.Divider(color='#B1D4E0'),
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
                                                                # Set name field
                                                                set_name_field,
                                                                ft.VerticalDivider(color='#B1D4E0'),
                                                                # Submit set name button
                                                                ft.IconButton(
                                                                    icon=ft.icons.CHECK_CIRCLE_ROUNDED,
                                                                    icon_color='#B1D4E0',
                                                                    icon_size=30,
                                                                    on_click=lambda _: submit_set_name(),
                                                                )
                                                            ],
                                                            
                                                        )
                                                    ),
                                                    color='#145DA0',
                                                    # width=400,
                                                    height=100,
                                                ),
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
                                                                # Question field
                                                                card_question_field,
                                                            ],
                                                            
                                                        )
                                                    ),
                                                    color='#145DA0',
                                                    # width=400,
                                                    height=100,
                                                ),
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
                                                                card_answer_field,
                                                            ],
                                                            
                                                        )
                                                    ),
                                                    color='#145DA0',
                                                    # width=400,
                                                    height=100,
                                                ),
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
                                                                # Front image field
                                                                front_image_field,
                                                            ],
                                                            
                                                        )
                                                    ),
                                                    color='#145DA0',
                                                    # width=400,
                                                    height=100,
                                                ),
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
                                                                # Back image field
                                                                back_image_field,
                                                            ],
                                                            
                                                        )
                                                    ),
                                                    color='#145DA0',
                                                    height=100,
                                                ),
                                                ft.Row(
                                                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                    controls=[
                                                        ft.ElevatedButton(
                                                            'Add Card',
                                                            bgcolor=('#B1D4E0'),
                                                            color=('#0C2D48'),
                                                            width=115,
                                                            on_click=lambda _: add_card()
                                                        ),
                                                        ft.ElevatedButton(
                                                            'Done',
                                                            bgcolor=('#B1D4E0'),
                                                            color=('#0C2D48'),
                                                            width=115,
                                                            on_click=lambda _: done_clicked()
                                                        )
                                                    ]
                                                )
                                            ],
                                            scroll=ft.ScrollMode.HIDDEN,
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
                                padding=10,
                                content=ft.Column(
                                    controls=[
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                            controls=[
                                                ft.Text('Settings', color='#145DA0', font_family='Cascadia Mono', size=30),
                                                ft.IconButton(
                                                    icon=ft.icons.ARROW_CIRCLE_LEFT_ROUNDED,
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
                                                                ft.Icon(ft.icons.CREDIT_CARD_ROUNDED, color='#B1D4E0', size=50),
                                                                ft.VerticalDivider(color='#B1D4E0'),
                                                                ft.Text('Leitner system', size=20, color='#0C2D48', font_family='Cascadia Mono Italic', text_align=ft.TextAlign.LEFT, no_wrap=False),
                                                                ft.Switch(on_change=lambda _: change_leitner_system_state(), value=leitner_system_state),
                                                            ],
                                                            
                                                        )
                                                    ),
                                                    color='#145DA0',
                                                    height=100,
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
        
        # Score Page
        if page.route == '/scorepage':
            page.views.append(
                ft.View(
                    route='/scorepage', #! Change route back later
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
                                                ft.Text('Score', color='#145DA0', font_family='Cascadia Mono', size=30),
                                                ft.IconButton(
                                                    icon=ft.icons.ARROW_CIRCLE_LEFT_ROUNDED,
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
                                                ft.Text(f'You got {len(correctly_answered)} out of {len(current_set)} correct!', color='#B1D4E0', font_family='Cascadia Mono', size=20)
                                            ]
                                        ),
                                        score_image,
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                            controls=[
                                                ft.IconButton(
                                                    icon=ft.icons.REPLAY_ROUNDED,
                                                    icon_color='#B1D4E0',
                                                    icon_size=30,
                                                    on_click=lambda _: redo_quiz()
                                                ),
                                                ft.IconButton(
                                                    icon=ft.icons.ARROW_CIRCLE_LEFT_ROUNDED,
                                                    icon_color='#B1D4E0',
                                                    icon_size=30,
                                                    on_click=lambda _: page.go('/')
                                                )
                                            ]
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
        
        # Set Complete Page
        if page.route == '/setcomplete':
            page.views.append(
                ft.View(
                    route='/setcomplete',
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
                                                ft.Text('You have completed {current_set}!', color='#145DA0', font_family='Cascadia Mono', size=30),
                                                ft.IconButton(
                                                    icon=ft.icons.ARROW_CIRCLE_LEFT_ROUNDED,
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
                                                ft.Text('Try a quiz next!', color='#B1D4E0', font_family='Cascadia Mono', size=20)
                                            ]
                                        ),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                            controls=[
                                                ft.IconButton(
                                                    icon=ft.icons.REPLAY_ROUNDED,
                                                    icon_color='#B1D4E0',
                                                    icon_size=30,
                                                    on_click=lambda _: redo_learn()
                                                ),
                                                ft.IconButton(
                                                    icon=ft.icons.ARROW_CIRCLE_LEFT_ROUNDED,
                                                    icon_color='#B1D4E0',
                                                    icon_size=30,
                                                    on_click=lambda _: page.go('/')
                                                )
                                            ]
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