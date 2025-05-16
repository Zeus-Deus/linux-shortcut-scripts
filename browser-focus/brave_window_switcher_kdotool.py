#!/usr/bin/env python3
import subprocess

INDEX_FILE = '/tmp/brave_window_switcher_index'
COUNT_FILE = '/tmp/brave_window_switcher_count'

# Function to list all Brave windows using kdotool, strictly filtering by window name
def list_brave_windows():
    result = subprocess.run(["kdotool", "search", "--name", "Brave"], capture_output=True, text=True)
    window_ids = result.stdout.strip().splitlines()
    brave_windows = []
    print("Brave window IDs and names:")
    for wid in window_ids:
        if wid:
            name = subprocess.run(["kdotool", "getwindowname", wid], capture_output=True, text=True).stdout.strip()
            print(f"{wid}: {name}")
            # Only include windows that end with "- Brave" (typical for Brave browser windows)
            if name.endswith("- Brave"):
                brave_windows.append(wid)
    return brave_windows

# Function to focus a window by ID
def focus_window(window_id):
    subprocess.run(["kdotool", "windowactivate", window_id])

# Functions to get/set the last focused window index in a file
def get_last_index():
    try:
        with open(INDEX_FILE, 'r') as f:
            return int(f.read())
    except Exception:
        return -1

def set_last_index(idx):
    with open(INDEX_FILE, 'w') as f:
        f.write(str(idx))

def get_last_count():
    try:
        with open(COUNT_FILE, 'r') as f:
            return int(f.read())
    except Exception:
        return -1

def set_last_count(count):
    with open(COUNT_FILE, 'w') as f:
        f.write(str(count))

# Main logic to cycle through Brave windows
def focus_next_brave_window():
    brave_windows = list_brave_windows()
    if not brave_windows:
        subprocess.Popen(["brave-browser"])
        return
    last_index = get_last_index()
    last_count = get_last_count()
    # Reset index if window count changed
    if last_count != len(brave_windows):
        last_index = -1
    # Clamp the index to a valid range
    if last_index >= len(brave_windows) or last_index < -1:
        last_index = -1
    next_index = (last_index + 1) % len(brave_windows)
    set_last_index(next_index)
    set_last_count(len(brave_windows))
    next_window_id = brave_windows[next_index]
    focus_window(next_window_id)

if __name__ == "__main__":
    focus_next_brave_window() 