from clipboard_watcher import ClipboardWatcher
from hotkey import HotkeyManager
from storage import Storage
from ui import PopupUI
from tray import Tray
import threading


def main():
    storage = Storage()
    ui = PopupUI(storage)

    watcher = ClipboardWatcher(storage.add_history)

    # Run clipboard watcher in thread
    threading.Thread(target=watcher.start, daemon=True).start()

    # Hotkey listener runs in background thread
    threading.Thread(target=lambda: HotkeyManager(ui).listen(), daemon=True).start()

    # Tray icon MUST run on main thread BEFORE Tkinter mainloop
    tray = Tray(ui)
    tray.start_in_main_thread()

    # Start Tkinter loop last
    ui.run()


if __name__ == "__main__":
    main()
