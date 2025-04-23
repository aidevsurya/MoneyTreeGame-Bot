import pyautogui
import time
import sys

location = None
# Optional: Give some time to switch to the target window
print("You have 5 seconds to open the target screen...")
time.sleep(5)

# Try to locate the image on screen
image_path = 'target.png'  # Replace with your image file
while 1:
    try:
        location = pyautogui.locateCenterOnScreen(image_path, confidence=0.6)
    except KeyboardInterrupt:
        sys.exit(0)

    if location is not None:
        print(f"Image found at: {location}")
        pyautogui.moveTo(location, duration=0.01)
        pyautogui.click()
        print("Clicked on the image.")
    else:
        print("Image not found on screen.")
        
