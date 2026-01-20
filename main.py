import flet as ft

class HomeView(ft.Column):
    '''Home tab design'''
    def __init__(self):
        super().__init__()
        self.controls = [
            ft.Text('Home Dashboard', size=28, weight=ft.FontWeight.BOLD),
            ft.Text('Your Progress'),
            ft.Container(height=100, bgcolor=ft.Colors.ON_SURFACE_VARIANT, border_radius=10)
        ]

class ExerciseTile(ft.Container):
    '''A custom component for a single exercise row'''
    def __init__(self, name, set_reps, icon=ft.Icons.CHECK_CIRCLE_OUTLINE):
        super().__init__()
        self.padding = 10
        self.bgcolor = ft.Colors.WHITE10
        self.border_radius = 10
        self.content = ft.ListTile(
            leading=ft.Icon(icon, color=ft.Colors.BLUE_400),
            title=ft.Text(name, weight=ft.FontWeight.BOLD),
            subtitle=ft.Text(set_reps),
            trailing=ft.IconButton(ft.Icons.INFO_OUTLINE, icon_size=20)
        )
        
class WorkoutTab(ft.Column):
    '''Workout Tab Design'''
    def __init__(self):
        super().__init__()
        self.scroll = ft.ScrollMode.ADAPTIVE
        self.expand = True
        
        #1. Header section
        self.header = ft.Text('Choose your Routine', size=24, weight=ft.FontWeight.BOLD)
        
        # 2. Filter Bubbles (Horizontal Scroll)
        self.filters = ft.Row(
            scroll=ft.ScrollMode.HIDDEN,
            controls=[
                ft.Chip(label=ft.Text('All'), selected=True),
                ft.Chip(label=ft.Text('Strength')),
                ft.Chip(label=ft.Text('Cardio')),
                ft.Chip(label=ft.Text('Flexibility'))
            ]
        )
        
        # 3. Predesigned workout card
        self.workout_card = ft.Container(
            content=ft.Column([
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.FITNESS_CENTER, color=ft.Colors.AMBER),
                    title=ft.Text('Full Body Blast', weight=ft.FontWeight.BOLD),
                    subtitle=ft.Text('Intermediate (45 mins)')
                ),
                ft.Text("A high-intensity routine focusing on compound movements.", size=12, color=ft.Colors.GREY_400)
            ]),
            bgcolor=ft.Colors.RED_900,
            border_radius=15,
            padding=10,
            on_click= lambda _: print('Workout Selected!')
        )

        self.controls = [
            self.header,
            self.filters,
            ft.Text('Featured Workout', size=16, color=ft.Colors.BLUE_400),
            self.workout_card
        ]
        
class WorkoutManager(ft.Column):
    '''Main Class for App Management'''
    def __init__(self):
        super().__init__()
        self.expand = True # Fill the screen
        self.title = ft.Container(
            content=ft.Text('FITNESS PRO', weight=ft.FontWeight.BOLD, size=32), alignment=ft.alignment.top_center
            )
        
        # 1. Define the dynamic content area
        self.content_area = ft.Container(
            content=ft.Text('Select a Page'), expand=True, alignment=ft.alignment.center
        )
        
        # 2. Define the navigation bar
        self.nav_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.HOME, label='Home'),
                ft.NavigationBarDestination(icon=ft.Icons.FITNESS_CENTER, label='Workouts'),
                ft.NavigationBarDestination(icon=ft.Icons.SETTINGS, label='Settings')
            ],
            on_change=self.handle_route_change,
        )
        
        self.controls = [
            self.title,
            self.content_area,
            self.nav_bar
        ]
    
    def handle_route_change(self, e):
        idx = e.control.selected_index
        if idx == 0:
            self.content_area.content = HomeView()
        elif idx == 1:
            self.content_area.content = WorkoutTab()
        elif idx == 2:
            self.content_area.content = ft.Text('Settings')
        self.update()
        
def main(page:ft.Page):
    page.title = 'Fitness Pro'
    page.bgcolor = '#121212'
    page.theme_mode = ft.ThemeMode.DARK
    #page.theme = ft.Theme(font_family="Verdana")
    
    work_ui = WorkoutManager()
    page.add(work_ui)
ft.app(target=main)
