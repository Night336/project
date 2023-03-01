from menu import Menu, Button
from base_views import BaseView


class Score(BaseView):
    def __call__(self):
        print('обновляем информацию о рекордах')
        self.loop()

    def loop(self):
        running = [True]
        first_dialog = Menu(
            Button("выход", lambda: running.pop())
        )
        while running:
            print("Рекордов еще нет")
            first_dialog.draw()
            first_dialog.select(input())