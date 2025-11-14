from pynput import keyboard

class HotkeyManager:
    def __init__(self, ui):
        self.ui = ui
        self.combo = {keyboard.Key.cmd, keyboard.Key.shift, keyboard.KeyCode(char='v')}
        self.current = set()

    def listen(self):

        def on_press(key):
            if key in self.combo:
                self.current.add(key)

            if all(k in self.current for k in self.combo):
                self.ui.toggle_safe()

        def on_release(key):
            if key in self.current:
                self.current.remove(key)

        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
