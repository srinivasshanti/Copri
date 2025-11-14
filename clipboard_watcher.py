import pyperclip
import time


class ClipboardWatcher:
    def __init__(self, callback, interval=0.3):
        self.callback = callback
        self.interval = interval
        self.last = ""

    def start(self):
        while True:
            try:
                text = pyperclip.paste()
                if text and text != self.last:
                    self.last = text
                    self.callback(text)
                time.sleep(self.interval)
            except Exception:
                pass
