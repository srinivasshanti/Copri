# 📋 Copri  
Copri is a lightweight, fast, and cross-platform clipboard manager designed for developers and productivity-focused users. It runs silently in the background, tracks the latest clipboard entries, allows users to save custom snippets, and opens instantly using a global hotkey.
Built with Python using Tkinter, pystray, and pynput, Copri offers a minimal and clean UI with essential functionality baked in, making it a perfect small utility tool for your workflow.

---

## ✨ Features

### 🔹 Automatic Clipboard History  
Copri constantly monitors your clipboard in the background and stores the **10 most recent text entries**. It detects changes instantly and updates the history without requiring any manual action.

### 🔹 Saved Snippets (Favorites)  
You can store your frequently used text snippets such as code snippets (`cout << "";`), TODO comments, or any text you use repeatedly. These favorites remain permanent until you remove them.

### 🔹 Global Hotkey  
A quick global hotkey brings the popup window to the front instantly from anywhere on your system.

**Default:** `⌘ + Shift + V` (macOS)  
This shortcut is ideal for developers and is close to regular paste (`⌘ + V`), making it intuitive and fast to use.

### 🔹 Clean and Minimal UI  
The application provides a simple two-tab interface:
- **Recent** — Shows the latest clipboard history  
- **Favorites** — Lists your saved snippets  

Each entry includes buttons to quickly copy or remove items.

### 🔹 System Tray Integration  
The app runs from the system tray (menu bar on macOS). You can open the popup or quit the app directly from the tray icon.

### 🔹 Cross-Platform Support  
Copri runs on:
- **macOS** (primary platform; requires Accessibility permissions)
- **Windows**
- **Linux**

All platforms receive the same minimal and efficient experience.
---

## 🧠 How It Works (Architecture Overview)
Copri consists of three major components working together:

1. Clipboard Watcher (Background Thread)
- Polls clipboard at a safe interval
- Detects new text
- Stores up to 10 most recent entries
- Saves to persistent storage

2. Global Hotkey Listener (Background Thread)
- Listens for keyboard events globally
- On hotkey press, instructs UI to toggle the popup
- Ensures all UI actions are dispatched safely to the Tkinter main thread

3. Tkinter UI + Tray (Main Thread)
- The main Tkinter thread runs the UI event loop
- All UI updates are performed on the main thread
- The tray icon is also initialized in the main thread (critical for macOS stability)
- Thread safety is achieved using root.after(), ensuring Tkinter never receives a direct cross-thread call.
---

## 🚀 Usage Guide
Start the application
- python3 main.py
Using the popup
- Press ⌘ + Shift + V to toggle the popup window. 
The popup shows:
- Recent Clipboard Items
- View and copy recent entries.
- Favorite Snippets
- View, copy, or delete saved snippets.
- Clicking Copy automatically copies the text to your clipboard and closes the popup.
From the tray icon:
- Open the popup
- Quit the application
---

### 🔐 macOS Setup Notes
Global Hotkeys Require Permission
On macOS, the hotkey listener requires Accessibility permissions. 
Go to:
- System Settings → Privacy & Security → Accessibility
- Add Terminal, iTerm, or your IDE (VSCode, PyCharm, etc.)
- Enable permission
- Without this step, hotkeys will not work.
- Tray Icon on macOS
- macOS requires GUI elements—like tray icons and windows—to be created only on the main thread. Copri is implemented to follow these requirements and avoid crashes.
---
