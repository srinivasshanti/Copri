import tkinter as tk
from tkinter import ttk
import pyperclip


class PopupUI:
    def __init__(self, storage):
        self.storage = storage

        self.root = tk.Tk()
        self.root.title("Clipboard Keeper")
        self.root.geometry("400x350")
        self.root.withdraw()

        self.notebook = ttk.Notebook(self.root)
        self.tab_recent = ttk.Frame(self.notebook)
        self.tab_favorites = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_recent, text="Recent")
        self.notebook.add(self.tab_favorites, text="Favorites")
        self.notebook.pack(expand=True, fill="both")

    # Thread-safe wrappers
    def toggle_safe(self):
        self.root.after(0, self.toggle_visibility)

    def show_safe(self):
        self.root.after(0, self.show)

    def quit_safe(self):
        self.root.after(0, self.root.quit)

    # UI interaction
    def toggle_visibility(self):
        if self.root.state() == "withdrawn":
            self.show()
        else:
            self.hide()

    def show(self):
        self.populate_recent()
        self.populate_favorites()
        self.root.deiconify()
        self.root.lift()
        self.root.focus_force()

    def hide(self):
        self.root.withdraw()

    def populate_recent(self):
        for w in self.tab_recent.winfo_children():
            w.destroy()

        for item in self.storage.get_history():
            text = item["text"]
            frame = ttk.Frame(self.tab_recent)
            frame.pack(fill="x", pady=3)

            ttk.Label(frame, text=text[:40]).pack(side="left", padx=5)
            ttk.Button(frame, text="Copy",
                       command=lambda t=text: self.copy_and_close(t)).pack(side="right")

    def populate_favorites(self):
        for w in self.tab_favorites.winfo_children():
            w.destroy()

        for fav in self.storage.get_favorites():
            frame = ttk.Frame(self.tab_favorites)
            frame.pack(fill="x", pady=3)

            ttk.Label(frame, text=fav[:40]).pack(side="left", padx=5)
            ttk.Button(frame, text="Copy",
                       command=lambda t=fav: self.copy_and_close(t)).pack(side="right")
            ttk.Button(frame, text="X",
                       command=lambda t=fav: self.remove_favorite(t)).pack(side="right")

    def copy_and_close(self, text):
        pyperclip.copy(text)
        self.hide()

    def remove_favorite(self, text):
        self.storage.remove_favorite(text)
        self.populate_favorites()

    def run(self):
        self.root.mainloop()
