import json
import os
from collections import deque
from datetime import datetime


class Storage:
    def __init__(self):
        self.path = os.path.expanduser("~/.clipboardkeeper.json")
        self.data = {
            "favorites": [],
            "history": [],
            "max_history": 10,
            "hotkey": "cmd+shift+v"
        }
        self.load()

        # Internal fast-access structure
        self.history = deque(self.data.get("history", []), maxlen=self.data["max_history"])

    def load(self):
        if os.path.exists(self.path):
            try:
                with open(self.path, "r") as f:
                    self.data = json.load(f)
            except:
                pass

    def save(self):
        self.data["history"] = list(self.history)
        with open(self.path + ".tmp", "w") as f:
            json.dump(self.data, f, indent=2)
        os.replace(self.path + ".tmp", self.path)

    # -------------------------
    # HISTORY HANDLING
    # -------------------------
    def add_history(self, text):
        self.history.appendleft({"text": text, "timestamp": datetime.now().isoformat()})
        self.save()

    def get_history(self):
        return list(self.history)

    # -------------------------
    # FAVORITES HANDLING
    # -------------------------
    def add_favorite(self, text):
        if text not in self.data["favorites"]:
            self.data["favorites"].append(text)
            self.save()

    def remove_favorite(self, text):
        if text in self.data["favorites"]:
            self.data["favorites"].remove(text)
            self.save()

    def get_favorites(self):
        return self.data["favorites"]
