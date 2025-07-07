import pyautogui
import time

# Step 1: Wait and switch to Chrome
print("Switch to WhatsApp Web in Chrome. Waiting for 10 seconds...")
time.sleep(10)

# Step 2: Click on search bar (Update your coordinates!)
pyautogui.click(x=157, y=177)
time.sleep(1)

# Step 3: Type group name and press Enter
pyautogui.write("SE - AI-B1 - 1", interval=0.05)
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)

# Step 4: Type your message
message = "Hi all, I am texting here through pyAutoGUI testing process. Thank you for your understanding."
pyautogui.write(message, interval=0.05)
time.sleep(1)

# Step 5: Send it
pyautogui.press('enter')

print("✅ Message sent using coordinate-based method.")
