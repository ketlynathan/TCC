from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

def on_press(btn):
    btn.text = 'Apertado'

def on_release(btn):
    btn.text = 'Solto!'

class MyApp(App):
    def build(self):
        # Criando um layout BoxLayout vertical
        box = BoxLayout(orientation='vertical')
        label = Label(text='Olá, Mundo!')
        label.font_size = 50

        text_input = TextInput()


        box = BoxLayout(orientation='vertical')
        btn = Button(
            text='Clique aqui', 
            on_press=on_press,
            on_release= on_release
            )
        btn.font_size = 50
        # Adicionando os widgets ao layout BoxLayout
        box.add_widget(label)
        box.add_widget(text_input)
        box.add_widget(btn)

        return box

if __name__ == '__main__':
    MyApp().run()
