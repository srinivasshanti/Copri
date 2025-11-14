# 📋 Copri  
ClipboadKeeper is a lightweight, fast, and cross-platform clipboard manager designed for developers and productivity-focused users. It runs silently in the background, tracks the latest clipboard entries, allows users to save custom snippets, and opens instantly using a global hotkey.

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

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/Copri.git
cd Copri
2. Install dependencies
Copri uses Python 3.10+.

bash
Copy code
pip3 install -r requirements.txt
3. Run the application
bash
Copy code
python3 main.py
🔧 System Requirements
Python 3.10 or newer

Tkinter (bundled with Python on macOS & Windows)

Accessibility permission on macOS for global keyboard listening

Pillow and other libraries installed through requirements.txt

🔐 macOS Setup Notes
Global Hotkeys Require Permission
On macOS, the hotkey listener requires Accessibility permissions. Go to:

System Settings → Privacy & Security → Accessibility

Add Terminal, iTerm, or your IDE (VSCode, PyCharm, etc.)

Enable permission

Without this step, hotkeys will not work.

Tray Icon on macOS
macOS requires GUI elements—like tray icons and windows—to be created only on the main thread. Copri is implemented to follow these requirements and avoid crashes.

📁 Project Structure
bash
Copy code
Copri/
│
├── main.py                # Application entry point
├── clipboard_watcher.py   # Monitors system clipboard in a background thread
├── hotkey.py              # Global hotkey handling
├── ui.py                  # Tkinter UI for popup window (Recent/Favorites)
├── storage.py             # JSON-based storage for history and favorites
├── tray.py                # Tray icon and menu integration
├── requirements.txt       # Project dependencies
└── assets/
    └── icon.png
🚀 Usage Guide
Start the application
bash
Copy code
python3 main.py
Using the popup
Press ⌘ + Shift + V to toggle the popup window. The popup shows:

Recent Clipboard Items
View and copy recent entries.

Favorite Snippets
View, copy, or delete saved snippets.

Clicking Copy automatically copies the text to your clipboard and closes the popup.

From the tray icon:
Open the popup

Quit the application

🧠 How It Works (Architecture Overview)
Copri consists of three major components working together:

1. Clipboard Watcher (Background Thread)
Polls clipboard at a safe interval

Detects new text

Stores up to 10 most recent entries

Saves to persistent storage

2. Global Hotkey Listener (Background Thread)
Listens for keyboard events globally

On hotkey press, instructs UI to toggle the popup

Ensures all UI actions are dispatched safely to the Tkinter main thread

3. Tkinter UI + Tray (Main Thread)
The main Tkinter thread runs the UI event loop

All UI updates are performed on the main thread

The tray icon is also initialized in the main thread (critical for macOS stability)

Thread safety is achieved using root.after(), ensuring Tkinter never receives a direct cross-thread call.

🔮 Roadmap
v0.2 (Upcoming)
Customizable hotkey from settings

Search bar inside Recent & Favorites

Dark mode optimized UI

Auto-start on login

UI redesign with rounded edges and cleaner layout

v0.3
Snippet folders / categories

Export and import snippet collections

Encrypted sync via GitHub Gist

v1.0 Stable Release
Full SwiftUI macOS native version

Full settings page

Plugin system for code expansions

Image clipboard support

🤝 Contributing
We welcome contributions from the community!

Contribution Steps
Fork the repository

Create a branch

bash
Copy code
git checkout -b feature-name
Make your changes

Commit with clear messages

Push and create a pull request

Guidelines
Maintain Python readability and PEP-8 compliance

Ensure UI changes remain thread-safe

Test functionality on macOS (preferred primary environment)

Avoid heavy dependencies — keep app lightweight

🧪 Development Commands
Install dependencies
bash
Copy code
pip3 install -r requirements.txt
Run the project
bash
Copy code
python3 main.py
Build standalone macOS app
bash
Copy code
pyinstaller --onefile --windowed main.py
Packaging scripts for macOS DMG and Linux AppImage are coming soon.

📄 License
Copri is released under the MIT License, giving you full freedom to:

Use

Modify

Distribute

Integrate

Sell

as long as the original license is included.

👨‍💻 Author
Srinivas Shanti
Developer | Engineer | Builder
Focused on creating practical, efficient tools that improve everyday workflows.

If you found this useful, please ⭐ the repository!