import asyncio
import flet as ft


class Countdown(ft.Text):
    def __init__(self, seconds):
        super().__init__()
        self.running = None
        self.seconds = seconds

    def did_mount(self):
        self.running = True
        self.page.run_task(self.update_timer)

    def will_unmount(self):
        self.running = False

    async def update_timer(self):
        while self.seconds and self.running:
            mins, secs = divmod(self.seconds, 60)
            self.value = "{:02d}:{:02d}".format(mins, secs)
            self.update()
            await asyncio.sleep(1)
            self.seconds -= 1


def main(page: ft.Page):
    page.add(Countdown(120), Countdown(60))


ft.app(main)
