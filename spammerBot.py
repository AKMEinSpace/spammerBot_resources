import pyautogui, time

f = open("bee.txt", "r")
content = f.readlines()

def start(content):
    for line in content:
        pyautogui.typewrite(line.strip())
        pyautogui.press("enter")

        time.sleep(0.2)


input("Press enter to start the program!")
start(content)
