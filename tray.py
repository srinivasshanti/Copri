import pystray
from PIL import Image


class Tray:
    def __init__(self, ui):
        self.ui = ui

    def start_in_main_thread(self):
        # Create simple tray icon (must run on main thread in macOS)
        image = Image.new("RGB", (64, 64), "black")

        icon = pystray.Icon(
            "ClipboardKeeper",
            image,
            "Clipboard Keeper",
            menu=pystray.Menu(
                pystray.MenuItem("Open", lambda: self.ui.show_safe()),
                pystray.MenuItem("Quit", lambda: self.ui.quit_safe())
            )
        )

        # This runs tray without blocking Tkinter, safe on macOS
        icon.run_detached()
