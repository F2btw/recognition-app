#библиотеки
import flet as ft
from flet import *
import webbrowser
import pyperclip
import base64
from PIL import Image, ImageFilter
import pytesseract
import multiprocessing as mp

#градиент
bg_gradient = LinearGradient(
begin=alignment.top_center,
end=alignment.bottom_center,
colors=[colors.BLUE_600, colors.PURPLE_600],
stops=[0.0, 1.0],)  # Blue at 0% and Purple at 100%

#градиент
gradient = LinearGradient(
begin=alignment.top_left,
end=alignment.bottom_right,
colors=["blue700", "purple700"])

#градиент
Dgradient = LinearGradient(
begin=alignment.top_center,
end=alignment.bottom_center,
colors=[colors.BLUE_GREY_800, colors.PURPLE_800],
stops=[0.0, 1.0],
)

#градиент
BGDgradient = LinearGradient(
begin=alignment.top_center,
end=alignment.bottom_center,
colors=[colors.BLUE_GREY_900, colors.PURPLE_900],
stops=[0.0, 1.0],
)

#открытие ссылки
def open_link(e):
    webbrowser.open("https://github.com/F2btw/recognition-app")

#изменение темы
is_initial_gradient = True
def toggle_all_gradient(e):
 
    global is_initial_gradient
    # Toggle the gradient
    if is_initial_gradient:
        background.gradient = BGDgradient
        settings.gradient = Dgradient
        ImagePage.gradient = Dgradient
    
    else:
        background.gradient = bg_gradient 
        settings.gradient = gradient 
        ImagePage.gradient = gradient
        
    # Update the flag
    is_initial_gradient = not is_initial_gradient
    # Update the container to reflect the change
    background.update()
    settings.update()
    ImagePage.update()
    
#закрытие приложения
def close_app(e):
    e.page.window.close()

#строка с кнопками
row_of_buttons_1 = Row(
        controls=[
            IconButton(icons.WB_SUNNY,icon_size=60, on_click= toggle_all_gradient,tooltip="Сменить тему"),
             IconButton(icons.CLOSE,icon_size=60,on_click=close_app,tooltip="Закрыть" )
              #чтобы добавить новую кнопку просто поставь запятую и сделаю любую кнопку: IconButton(icons.WB_CLOUDY,icon_size=60),
        ],spacing=100
    )

#строка с кнопками
row_of_buttons_2 = Row(
        controls=[
            TextButton(content=Text(value='github',weight=FontWeight.BOLD,size=22,),on_click= open_link,tooltip="ссылка: https://github.com/F2btw/recognition-app" )
        ],spacing=20
    )

#основная страница
def main(page: ft.Page):
    # название приложения
    page.title = "Recognition-app"
    page.theme_mode = 'dark'
    page.horizontal_alignment='center'
    page.vertical_alignment = 'center'

    #получение пути до изображения
    image = ft.Image(visible=False,fit= ImageFit.FILL)
    def get_file_path(e: FilePickerResultEvent):
     global file_path

     print(e.files)
     if e.files and len(e.files):
            file_path = e.files[0].path
            
            with open(e.files[0].path, 'rb')as r:
             image.src_base64 = base64.b64encode(r.read()).decode('utf-8')
             image.visible = True
             page.update()
     #распознование текста       
     global text
     
     # Укажите путь к исполняемому файлу tesseract, если он не добавлен в PATH
     pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
     imageR = Image.open(file_path)
     imageR = imageR.convert('L')  # Grayscale
     imageR = imageR.filter(ImageFilter.SHARPEN)  # Sharpen image
     #imageR = imageR.filter(ImageFilter.GaussianBlur(radius=0.5))
     imageR = imageR.point(lambda x: 0 if x < 128 else 255, '1')
     
     cfg = r'--oem 3 --psm 6 '
     text = pytesseract.image_to_string(imageR,lang='rus',config=cfg  )
     print(text)
     if __name__ == '__main__':
      with mp.Pool(mp.cpu_count()) as pool:
        results = pool.map(file_path)
      for i, text in enumerate(results):
        print(f"Text from image {i+1}:\n{text}\n")   
    File_Picker = FilePicker(on_result=get_file_path)
    page.overlay.append(File_Picker)
    
    #функция для копирования текста
    def copy_text(e):
       pyperclip.copy(text)
       
    #строка с кнопками
    row_of_buttons_3 = Row(
        controls=[ 
            ElevatedButton('ВЫБЕРИТЕ ИЗОБРАЖЕНИЕ',width=300,height=30,on_click=lambda _:File_Picker.pick_files(allow_multiple=False,
            allowed_extensions=['jpg','jpeg','png'])),
            IconButton(icons.COPY_ALL,icon_size=60,on_click=copy_text,tooltip="Скопировать")
              #чтобы добавить новую кнопку просто поставь запятую и сделаю любую кнопку: IconButton(icons.WB_CLOUDY,icon_size=60),
        ],spacing=630
    )

    #анимация settings_page
    def expand(e):
        if e.data == "true":
           background.content.controls[0].width = 300
           background.content.controls[0].update()
        else:
           background.content.controls[0].width = 400 / 4
           background.content.controls[0].update()
        
        pass

   # страница с настройками
    def settings_page():
     global settings
     settings = Container(width= 400 / 4, height=1000,
     gradient=gradient,border_radius=10,
     animate=animation.Animation(duration=650,curve="easeInOut"),
     on_hover=lambda e: expand(e), padding=15,
     content=Column(alignment='start',spacing=10,
     controls=[Row(alignment='center',
     controls=[Text('SETTINGS',size=16,weight="w500")]),
     Container(padding=padding.only(bottom=10)),
     Row(controls=[Container(content=row_of_buttons_1)]),
     Container(padding=padding.only(bottom=730)),
     Row(controls=[Container(content=row_of_buttons_2)])
     
     ]))

     return settings

    #старница с изображением
    def Image_page():
     global ImagePage
     ImagePage = Container(width= 1000, height=880,gradient=gradient,border_radius=10,animate=animation.Animation(duration=650,curve="easeInOut"),
     content=Column(controls=[
     Row(controls=[Container(width= 1000, height=800,content=image)]),
    
     Row(controls=[Container(content=row_of_buttons_3)])

     ]))

     return ImagePage
    
    #анимация задний фон
    global background
    background = Container(
        width= main, height=main, border_radius=10,gradient= bg_gradient,
        padding=10,animate=Animation(650, AnimationCurve.EASE_IN_OUT),
        content=Row(controls=[settings_page(),Image_page(),],spacing=300),
    ) 
    
    page.add(background)
   
app(target=main)
