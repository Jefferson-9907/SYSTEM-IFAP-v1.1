from kivy.lan import Builder
from kivymd.app import MDApp

from kinymd.uix.picker import MDTimePicket

class reloj:
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file("time.kv")


    def get_time(self, instance, time):
        self.root.ids.time_label.text = str(time)


    def on_cancel(self, instance, time):
        self.root.ids.time_label = "CANCELAR"


    def show_time_picker(self):
        from datetime import datetime

        defaul_time = datetime.strptime("08:00:00", "%H:%M:%S").time()

        time_dialog = MDTimePicker()

        time_dialog.set_time(default_time)
        time_dialog.bind(on_cancel=self.on_cancel, time=self.get_time)
        time_dialog.open()
