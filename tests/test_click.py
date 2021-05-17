from pynput.mouse import Button, Controller

mouse = Controller()
mouse.position = (1795, 611)
# Click the left button
mouse.click(Button.left, 1)