import flet as ft
from flet import *

bg_gradient = LinearGradient(
begin=alignment.top_center,
end=alignment.bottom_center,
colors=[colors.BLUE_600, colors.PURPLE_600],
stops=[0.0, 1.0],)  # Blue at 0% and Purple at 100%

gradient = LinearGradient(
begin=alignment.top_left,
end=alignment.bottom_right,
colors=["blue700", "purple700"])


def main(page: ft.Page):
    page.theme_mode = 'dark'
    page.horizontal_alignment='center'
    page.vertical_alignment = 'center'

    def expand(e):
        if e.data == "true":
           background.content.controls[0].width = 300
           background.content.controls[0].update()
        else:
           background.content.controls[0].width = 400 / 4
           background.content.controls[0].update()
        
        pass

    #SBG = '#041955'

   # страница с настройками
    def settings_page():
     settings = Container(width= 400 / 4, height=1000,
     gradient=gradient,border_radius=10,
     animate=animation.Animation(duration=650,curve="easeInOut"),
     on_hover=lambda e: expand(e), padding=15,
     content=Column(alignment='start',spacing=10,
     controls=[Row(alignment='center',
     controls=[Text('SETTINGS',size=16,weight="w500")]),
     Container(padding=padding.only(bottom=5)),
     Row(alignment= 'center',spacing=30,
         controls=[Column(controls=[Container(width=90,height=90,)])]
         )]))

     return settings

    



    background = Container(
        width= 2000, height=1000, border_radius=10,gradient= bg_gradient,
        padding=10,
        content=Stack(width= 1800, height=900,controls=[settings_page()]),
    )
    
    page.add(background)

 
  

app(target=main)

