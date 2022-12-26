import pyautogui

# Get the color of the pixel at position (100, 200)
r, g, b = pyautogui.pixel(1297, 620)

# Print the color values
print(f"Red: {r}, Green: {g}, Blue: {b}")