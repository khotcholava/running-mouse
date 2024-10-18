import pyautogui
import time
import random

def move_mouse_randomly():
    # Get the screen width and height
    screen_width, screen_height = pyautogui.size()
    
    # Generate random coordinates
    random_x = random.randint(0, screen_width - 1)
    random_y = random.randint(0, screen_height - 1)
    
    # Move the mouse to the random coordinates
    pyautogui.moveTo(random_x, random_y)

def detect_mouse_inactivity(duration):
    # Get the current mouse position
    last_position = pyautogui.position()
    
    while True:
        # Wait for the specified duration
        time.sleep(duration)
        
        # Get the new mouse position
        new_position = pyautogui.position()
        
        # Check if the mouse has moved
        if new_position == last_position:
            # If the mouse hasn't moved, move it randomly
            move_mouse_randomly()
        else:
            # Update the last position
            last_position = new_position

if __name__ == "__main__":
    # Set the duration to 2 minutes (240 seconds)
    inactivity_duration = 120
    detect_mouse_inactivity(inactivity_duration)
