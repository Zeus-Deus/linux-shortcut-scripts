# Brave Window Switcher

A simple Python script for Linux (tested on Arch Linux with KDE Plasma, Wayland session) that cycles through all open Brave browser windows (across all profiles) each time it is run. If no Brave window is open, it will launch Brave. This is especially useful for users who want to quickly switch between multiple Brave windows using a keyboard shortcut.

## Features

- Focuses the next open Brave browser window (cycles through all open Brave windows)
- If no Brave window is open, launches Brave
- Designed to be bound to a custom keyboard shortcut in KDE Plasma (or any Linux desktop environment)
- Works on Wayland using [kdotool](https://github.com/htrefil/kdotool)
- Filters windows by title, only including those ending with `- Brave` (the standard for Brave browser windows)

## Requirements

- Python 3 (no third-party packages required)
- [kdotool](https://github.com/htrefil/kdotool) (must be installed from the AUR or built from source)
- Brave browser

Install the required system package (on Arch Linux, from the AUR):

```bash
yay -S kdotool
# or
paru -S kdotool
```

## Setup

1. Clone this repository or copy the script to your system.
2. (Optional) Test the script from the terminal:
   ```bash
   python brave_window_switcher_kdotool.py
   # or
   python3 brave_window_switcher_kdotool.py
   ```

## Usage

### Bind to a Keyboard Shortcut (KDE Plasma)

1. Open **System Settings** → **Shortcuts** → **Custom Shortcuts**.
2. Add a new global shortcut:
   - Action: `python /full/path/to/brave_window_switcher_kdotool.py`
   - Or: `python3 /full/path/to/brave_window_switcher_kdotool.py`
3. Assign your desired key combination.

Now, pressing your shortcut will cycle through open Brave windows, or launch Brave if none are open.

## Troubleshooting

- The script filters windows by checking if the window title ends with `- Brave`. If you have other windows with `Brave` in the title (such as editors or terminals with files named `brave`), they will not be included in the cycle.
- If you rename your Brave browser window or use a non-standard window title, update the filtering logic in the script accordingly.
- If you encounter issues, run the script in a terminal to see debug output of window IDs and names.
