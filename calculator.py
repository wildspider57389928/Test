from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

class CalculatorApp(App):
    def build(self):
        self.expression = ""

        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # نمایشگر
        self.display = TextInput(text="", multiline=False, font_size=40, size_hint=(1, 0.2))
        main_layout.add_widget(self.display)

        # دکمه‌ها با تغییر جای C و =
        buttons = [
            ['7','8','9','/'],
            ['4','5','6','*'],
            ['1','2','3','-'],
            ['0','.','C','+'],  # C به جای قبلی و + سمت چپ
            ['=']               # = به ردیف جداگانه
        ]

        for row in buttons:
            row_layout = GridLayout(cols=len(row), spacing=5, size_hint=(1, 0.16))
            for label in row:
                button = Button(text=label, font_size=32)
                button.bind(on_press=self.on_button_press)
                row_layout.add_widget(button)
            main_layout.add_widget(row_layout)

        return main_layout

    def on_button_press(self, instance):
        text = instance.text
        if text == "=":
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"
        elif text == "C":
            self.expression = ""
        else:
            self.expression += text
        self.display.text = self.expression

if __name__ == "__main__":
    CalculatorApp().run()