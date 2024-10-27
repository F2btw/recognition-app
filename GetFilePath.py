import base64
from flet import *
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

#кнопка 
ElevatedButton('ВЫБЕРИТЕ ИЗОБРАЖЕНИЕ',width=300,height=30,on_click=lambda _:File_Picker.pick_files(allow_multiple=False,
            allowed_extensions=['jpg','jpeg','png']))
