
from utils.logger import log_info

class ConsoleRenderer:
    def __init__(self):
        self.menu_visible = False

    def toggle_menu(self):
        self.menu_visible = not self.menu_visible
        if self.menu_visible:
            self.show_menu()
        else:
            log_info("Menu hidden")

    def show_menu(self):
        print("╔══════════════════════════════════════╗")
        print("║   PARALIVES TRAINER v1.0            ║")
        print("║   F2 - Infinite Money               ║")
        print("║   F3 - Max All Needs                ║")
        print("║   F4 - Complete Wants               ║")
        print("║   F5 - Max All Skills               ║")
        print("║   F6 - Freeze Aging (toggle)        ║")
        print("║   F7 - Unlock All Items             ║")
        print("║   F8 - Unstuck Character            ║")
        print("║   F9 - Exit                         ║")
        print("╚══════════════════════════════════════╝")
