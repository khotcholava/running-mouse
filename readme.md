# Mouse Mover

This Python script moves the mouse cursor randomly if it detects inactivity for a specified duration. It can be useful to prevent the computer from going to sleep or to keep a session active.

## Requirements

- Python 3.x
- `pyautogui` library

## Installation

1. Install Python 3.x from the [official website](https://www.python.org/).
2. Install the `pyautogui` library using pip:

    ```sh
    pip install pyautogui
    ```

## Usage

1. Save the script to a file, e.g., `main.py`.
2. Run the script:

    ```sh
    python main.py
    ```

By default, the script checks for mouse inactivity every 2 minutes (120 seconds). If the mouse hasn't moved, it will move the mouse cursor to a random position on the screen.

## Configuration

You can change the inactivity duration by modifying the `inactivity_duration` variable in the script. The duration is specified in seconds.

