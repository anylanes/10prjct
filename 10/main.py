from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.button import Button
import parser
import geo

# Глобальные настройки
Window.size = (300, 200)
Window.clearcolor = (255 / 255, 186 / 255, 3 / 255, 1)
Window.title = "Для владельцев домашних любимцев"
api_key = "8f76020291852cb116ac3b8c3ff5bed7"
name="Введите геопозицию"
class MyApp(App):

    # Создание всех виджетов (объектов)
    def __init__(self):
        super().__init__()
        self.label = Label(text='Для владельцев домашних любимцев')
        self.davl = Label(text='Давление:')
        self.temp = Label(text='Температура:')
        self.vlaz = Label(text='Влажность:')
        self.day = Label(text='Cостояние погоды:')
        self.input_data = TextInput(hint_text='Введите геопозицию', multiline=False)
        self.input_data.bind(on_text_validate=self.on_text)
        self.checkbox = Button(text="Текущая геопозиция",background_color=(255/255,255/255,255/255,1))
        self.checkbox.bind(on_press=lambda x:self.on_chekbox())
    # Получаем данные и производит их конвертацию
    def on_text(self, *args):
        data = self.input_data.text
        a,b= geo.get_location_coordinates(data)
        c= parser.params(api_key, a, b)
        self.davl.text = 'Давление: ' + str(round(int(c[2]) / (1.333224),1))+"мм. рт. ст."
        self.temp.text = 'Температура: ' + str(round(int(c[0]) -273.15,1))+"С"
        self.vlaz.text = 'Влажность: ' + str(int(c[1]))+"%"
        self.day.text = 'Сочтояние погоды: ' + str((c[3]))

    def on_chekbox(self):
        a, b = geo.get_location()
        name= geo.get_location_name(a, b)
        c = parser.params(api_key, a, b)
        self.davl.text = 'Давление: ' + str(round(int(c[2]) / (1.333224), 1)) + "мм. рт. ст."
        self.temp.text = 'Температура: ' + str(round(int(c[0]) - 273.15, 1)) + "С"
        self.vlaz.text = 'Влажность: ' + str(int(c[1])) + "%"
        self.day.text = 'Сочтояние погоды: ' + str((c[3]))
        self.input_data = TextInput(hint_text=name, multiline=False)

    # Основной метод для построения программы
    def build(self):
        # Все объекты будем помещать в один общий слой
        box = BoxLayout(orientation='vertical')
        box.add_widget(self.label)
        box.add_widget(self.checkbox)
        box.add_widget(self.input_data)
        box.add_widget(self.davl)
        box.add_widget(self.temp)
        box.add_widget(self.vlaz)
        box.add_widget(self.day)

        return box


# Запуск проекта
if __name__ == "__main__":
    MyApp().run()