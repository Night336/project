from menu import Button, Menu
from base_views import BaseView


class Setting(BaseView):
    def __init__(self, stack, player):
        super().__init__(stack, player)
        
        print('Загружаем настроки')

    def __call__(self):
        self.loop()

    def loop(self):
        running = [True]
        while running:
            first_dialog = Menu(
                Button("Настройка Звука"),
                Button("Настройки разрешение"),
                Button("Насройка Еще чего-то"),
                Button("Выход", lambda: running.pop())
            )
            first_dialog.draw()
            first_dialog.select(input())